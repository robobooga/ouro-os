import os
import re
import concurrent.futures
from pathlib import Path
import mistune
from jinja2 import Environment, FileSystemLoader

# Paths
BASE_DIR = Path(__file__).resolve().parent
WIKI_DIR = BASE_DIR.parent / 'ouro' / 'wiki'
DIST_DIR = BASE_DIR / 'dist'
TEMPLATES_DIR = BASE_DIR / 'templates'

def parse_doxygen_tags(text):
    # Mapping tags to HTML
    text = re.sub(r'@entity\s+(.*)', r'<div class="entity-header">Entity: \1</div>', text)
    text = re.sub(r'@brief\s+(.*)', r'<p class="brief"><strong>Brief:</strong> \1</p>', text)
    text = re.sub(r'@note\s+(.*)', r'<div class="note"><strong>Note:</strong> \1</div>', text)
    text = re.sub(r'@warning\s+(.*)', r'<div class="warning"><strong>Warning:</strong> \1</div>', text)
    return text

def process_file(wiki_path):
    # Initialize objects locally in child process
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template('page.html')
    markdown = mistune.create_markdown(plugins=['table', 'strikethrough'])

    with open(wiki_path, 'r', encoding='utf-8') as f:
        content = f.read()

    processed_content = parse_doxygen_tags(content)
    html_content = markdown(processed_content)
    
    return template.render(content=html_content)

def build():
    print(f"Building Ouro Wiki Web UI from {WIKI_DIR} to {DIST_DIR}...")
    
    if not WIKI_DIR.exists():
        print(f"Error: Wiki directory not found at {WIKI_DIR}")
        return

    # Ensure dist exists
    DIST_DIR.mkdir(exist_ok=True)
    
    # Use a single persistent executor
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        for root, dirs, files in os.walk(WIKI_DIR):
            if 'dist' in dirs: dirs.remove('dist')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file.endswith('.md'):
                    wiki_path = Path(root) / file
                    print(f"Processing: {wiki_path.relative_to(WIKI_DIR)}")
                    
                    try:
                        future = executor.submit(process_file, wiki_path)
                        final_html = future.result(timeout=5)
                        
                        relative_path = wiki_path.relative_to(WIKI_DIR)
                        output_path = DIST_DIR / relative_path.with_suffix('.html')
                        output_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(final_html)
                    except concurrent.futures.TimeoutError:
                        print(f"Timeout: Skipping {wiki_path}")
                    except Exception as e:
                        print(f"Error processing {wiki_path}: {e}")

    print("Build complete.")

if __name__ == '__main__':
    build()
