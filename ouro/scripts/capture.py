import sys
import os
from datetime import datetime
from pathlib import Path

# Path to the capture queue
QUEUE_PATH = Path(__file__).resolve().parent.parent / 'wiki' / 'log' / 'capture-queue.md'

def stage(input_str):
    """Stages a file or raw snippet to the capture queue."""
    content = ""
    source = "Manual Capture"

    path_obj = Path(input_str)
    if path_obj.exists() and path_obj.is_file():
        try:
            content = path_obj.read_text(encoding='utf-8')
            source = input_str
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        content = input_str

    timestamp = datetime.now().isoformat()
    entry = f"""
### Capture [{timestamp}]
- **Source**: `{source}`
- **Content**:
```
{content}
```

---
"""
    try:
        with open(QUEUE_PATH, 'a', encoding='utf-8') as f:
            f.write(entry)
        print(f'Successfully staged capture from "{source}" to {QUEUE_PATH}')
    except Exception as e:
        print(f'Failed to write to capture queue: {e}')

def crawl(directory):
    """Crawls a directory for files containing Doxygen tags."""
    dir_path = Path(directory)
    if not dir_path.exists() or not dir_path.is_dir():
        print(f'Error: Directory "{directory}" does not exist.')
        sys.exit(1)

    print(f'Crawling directory: {directory}...')
    count = 0
    for file_path in dir_path.rglob('*'):
        if file_path.is_file() and file_path.name not in ['node_modules', '.git']:
            try:
                content = file_path.read_text(encoding='utf-8')
                if '@entity' in content or '@brief' in content:
                    stage(str(file_path))
                    count += 1
            except Exception as e:
                print(f'Skipping file "{file_path}": {e}')
    
    print(f'Crawl complete. Staged {count} files with Doxygen tags.')

def main():
    if len(sys.argv) < 2:
        print('Error: Please provide a file path, raw snippet, or --crawl [dir].')
        sys.exit(1)

    arg1 = sys.argv[1]

    if arg1 == '--crawl':
        directory = sys.argv[2] if len(sys.argv) > 2 else '.'
        crawl(directory)
    else:
        stage(arg1)

if __name__ == '__main__':
    main()
