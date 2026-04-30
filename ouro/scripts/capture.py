import sys
import os
from datetime import datetime
from pathlib import Path

# Path to the capture queue
QUEUE_PATH = Path(__file__).resolve().parent.parent / 'wiki' / 'capture-queue.md'

def is_binary(file_path):
    """Heuristic to check if a file is binary."""
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            return b'\x00' in chunk
    except Exception:
        return True

def stage(input_str):
    """Stages a file or raw snippet to the capture queue."""
    content = ""
    source = "Manual Capture"

    path_obj = Path(input_str)
    if path_obj.exists() and path_obj.is_file():
        if is_binary(path_obj):
            print(f"Skipping binary file: {input_str}")
            return
        try:
            content = path_obj.read_text(encoding='utf-8')
            # Use relative path from CWD for cleaner log entries
            try:
                source = str(path_obj.resolve().relative_to(Path.cwd().resolve()))
            except ValueError:
                source = input_str
        except Exception as e:
            print(f"Error reading file {input_str}: {e}")
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
    dir_path = Path(directory).resolve()
    if not dir_path.exists() or not dir_path.is_dir():
        print(f'Error: Directory "{directory}" does not exist.')
        sys.exit(1)

    print(f'Crawling directory: {dir_path}...')
    count = 0
    # Avoid crawling the wiki log directory itself
    wiki_path = Path(__file__).resolve().parent.parent / 'wiki'
    ignored_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'dist', 'build', '.next', 'ouro'}
    
    for file_path in dir_path.rglob('*'):
        # Check if file is inside the wiki directory to skip it
        if wiki_path in file_path.parents or file_path.parent == wiki_path:
            continue

        # Skip ignored directories
        if any(part in ignored_dirs for part in file_path.parts):
            continue
            
        if file_path.is_file():
            if is_binary(file_path):
                continue
                
            try:
                # Capture all non-binary files
                stage(str(file_path))
                count += 1
            except (UnicodeDecodeError, PermissionError):
                continue
            except Exception as e:
                print(f'Skipping file "{file_path}": {e}')
    
    print(f'Crawl complete. Staged {count} files.')

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
