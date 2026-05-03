import argparse
import os
import re
import shutil
import concurrent.futures
from pathlib import Path
import mistune
from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).resolve().parent
DIST_DIR = BASE_DIR / 'dist'
TEMPLATES_DIR = BASE_DIR / 'templates'

SKIP_FILES = {'capture-queue.md', 'schema.md'}

SECTION_ORDER = ['entities', 'decisions', 'patterns', 'maps']
SECTION_LABELS = {
    'entities': 'Entities',
    'decisions': 'Decisions',
    'patterns': 'Patterns',
    'maps': 'Maps',
}


def parse_doxygen_tags(text):
    _md = mistune.create_markdown(escape=False, plugins=['table', 'strikethrough'])

    def _inline(raw):
        rendered = _md(raw).strip()
        if rendered.startswith('<p>') and rendered.endswith('</p>'):
            rendered = rendered[3:-4]
        return rendered

    text = re.sub(r'^@entity\s+(.*)', lambda m: f'<div class="entity-header">Entity: {_inline(m.group(1))}</div>', text, flags=re.MULTILINE)
    text = re.sub(r'^@brief\s+(.*)', lambda m: f'<p class="brief"><strong>Brief:</strong> {_inline(m.group(1))}</p>', text, flags=re.MULTILINE)
    text = re.sub(r'^@note\s+(.*)', lambda m: f'<div class="note"><strong>Note:</strong> {_inline(m.group(1))}</div>', text, flags=re.MULTILINE)
    text = re.sub(r'^@warning\s+(.*)', lambda m: f'<div class="warning"><strong>Warning:</strong> {_inline(m.group(1))}</div>', text, flags=re.MULTILINE)
    return text


def build_nav_tree(wiki_dir):
    """Return nav sections grouped by subdirectory, ordered by SECTION_ORDER."""
    buckets = {s: [] for s in SECTION_ORDER}
    root_pages = []

    for root, dirs, files in os.walk(wiki_dir):
        dirs[:] = [d for d in dirs if d not in ('dist', '.git', 'scripts')]
        for file in sorted(files):
            if not file.endswith('.md') or file in SKIP_FILES:
                continue
            path = Path(root) / file
            rel = path.relative_to(wiki_dir)
            parts = rel.parts
            href = str(rel.with_suffix('.html')).replace('\\', '/')
            label = rel.stem.replace('-', ' ').replace('_', ' ')

            if len(parts) == 1:
                root_pages.append({'label': label, 'href': href})
            else:
                section = parts[0]
                if section in buckets:
                    buckets[section].append({'label': label, 'href': href})

    nav_tree = []
    if root_pages:
        nav_tree.append({'title': 'Wiki', 'pages': root_pages})
    for key in SECTION_ORDER:
        if buckets[key]:
            nav_tree.append({'title': SECTION_LABELS[key], 'pages': buckets[key]})
    return nav_tree


def process_file(wiki_path, nav_tree, root_prefix):
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template('page.html')
    markdown = mistune.create_markdown(escape=False, plugins=['table', 'strikethrough'])

    with open(wiki_path, 'r', encoding='utf-8') as f:
        content = f.read()

    processed = parse_doxygen_tags(content)
    html_content = markdown(processed)
    skip_pattern = '|'.join(re.escape(f) for f in SKIP_FILES)
    html_content = re.sub(
        rf'<a\b[^>]*href="[^"]*({skip_pattern})"[^>]*>.*?</a>',
        r'\1',
        html_content,
    )
    html_content = re.sub(
        r'href="([^"]*?)\.md(#[^"]*?)?"',
        lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"',
        html_content,
    )
    return template.render(content=html_content, nav_tree=nav_tree, root_prefix=root_prefix)


def build(wiki_dir=None):
    if wiki_dir is None:
        wiki_dir = BASE_DIR.parent / 'ouro' / 'wiki'
    wiki_dir = Path(wiki_dir).resolve()

    print(f"Building Ouro Wiki Web UI from {wiki_dir} to {DIST_DIR}...")

    if not wiki_dir.exists():
        print(f"Error: Wiki directory not found at {wiki_dir}")
        return

    DIST_DIR.mkdir(exist_ok=True)
    shutil.copy(BASE_DIR / 'static' / 'style.css', DIST_DIR / 'style.css')
    nav_tree = build_nav_tree(wiki_dir)

    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        for root, dirs, files in os.walk(wiki_dir):
            dirs[:] = [d for d in dirs if d not in ('dist', '.git', 'scripts')]

            for file in files:
                if not file.endswith('.md') or file in SKIP_FILES:
                    continue

                wiki_path = Path(root) / file
                relative_path = wiki_path.relative_to(wiki_dir)
                depth = len(relative_path.parts) - 1
                root_prefix = '../' * depth

                print(f"Processing: {relative_path}")

                try:
                    future = executor.submit(process_file, wiki_path, nav_tree, root_prefix)
                    final_html = future.result(timeout=10)

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
    parser = argparse.ArgumentParser(description='Build Ouro Wiki Web UI')
    parser.add_argument(
        '--wiki-dir',
        type=Path,
        default=BASE_DIR.parent / 'ouro' / 'wiki',
        help='Path to the wiki directory to build from (default: ../ouro/wiki)',
    )
    args = parser.parse_args()
    build(wiki_dir=args.wiki_dir)
