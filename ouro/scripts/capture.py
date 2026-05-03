import sys
import os
from datetime import datetime
from pathlib import Path

# Path to the capture queue
PROJECT_ROOT = Path.cwd()
QUEUE_PATH = PROJECT_ROOT / 'ouro' / 'wiki' / 'capture-queue.md'

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
        # Check if queue has *(Empty)* and remove it
        if QUEUE_PATH.exists():
            queue_content = QUEUE_PATH.read_text(encoding='utf-8')
            if "*(Empty)*" in queue_content:
                queue_content = queue_content.replace("*(Empty)*", "").strip() + "\n"
                QUEUE_PATH.write_text(queue_content, encoding='utf-8')

        with open(QUEUE_PATH, 'a', encoding='utf-8') as f:
            f.write(entry)
        print(f'Successfully staged capture from "{source}" to {QUEUE_PATH}')
    except Exception as e:
        print(f'Failed to write to capture queue: {e}')

IGNORED_DIRS = {
    # Version control
    '.git', '.svn', '.hg',
    # Python
    '__pycache__', '.venv', 'venv', 'env', '.tox', '.pytest_cache', '.mypy_cache', '.ruff_cache',
    # JavaScript / Node
    'node_modules', 'bower_components', '.yarn', '.pnp', '.npm',
    # Build outputs
    'dist', 'build', 'out', 'target', '_build', 'dist-skill', '.next', '.nuxt', '.svelte-kit', '.expo',
    # Caches
    '.cache', 'cache', '.parcel-cache',
    # Java / Kotlin / Scala
    '.gradle', '.m2',
    # Ruby
    '.bundle',
    # Haskell / Elm
    '.stack-work', 'elm-stuff',
    # Elixir / Erlang
    '_build', 'deps',
    # iOS / macOS
    'Pods', 'DerivedData',
    # Misc build / temp
    'tmp', 'temp', 'logs', 'coverage', '.coverage',
    # Infrastructure-as-code state (may contain secrets)
    '.terraform', '.vagrant',
    # Credential / secret directories
    '.aws', '.ssh', '.gnupg', '.gpg',
    'secrets', '.secrets', 'credentials', '.credentials',
    'certs', 'certificates', '.certs', 'keystore', 'keystores',
    'keys', '.keys', 'private', '.private', 'vault',
    # Project-specific
    'ouro',
}

# Individual filenames that are likely to contain secrets
SENSITIVE_NAMES = {
    '.env', '.env.local', '.env.development', '.env.production',
    '.env.staging', '.env.test', '.env.example',
    'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519',
    'id_rsa.pub', 'id_dsa.pub', 'id_ecdsa.pub', 'id_ed25519.pub',
    'known_hosts', 'authorized_keys',
    '.netrc', '.pgpass',
    'secrets.json', 'credentials.json', 'service-account.json',
}

# File extensions that are likely to contain secrets or are binary-adjacent
SENSITIVE_SUFFIXES = {
    '.pem', '.key', '.p12', '.pfx', '.cer', '.crt', '.der', '.ca-bundle',
    '.keystore', '.jks', '.p8',
    '.secret', '.secrets',
    '.token', '.tokens',
    '.asc',  # GPG armored
}

def is_sensitive(file_path: Path) -> bool:
    name = file_path.name.lower()
    if name in SENSITIVE_NAMES:
        return True
    if file_path.suffix.lower() in SENSITIVE_SUFFIXES:
        return True
    # Catch patterns like .env.local, *credentials*.json, *secret*.yml
    if name.startswith('.env'):
        return True
    if any(kw in name for kw in ('secret', 'credential', 'password', 'passwd', 'apikey', 'api_key', 'token', 'private_key')):
        return True
    return False


def crawl(directory):
    """Crawls a directory for files containing Doxygen tags."""
    dir_path = Path(directory).resolve()
    if not dir_path.exists() or not dir_path.is_dir():
        print(f'Error: Directory "{directory}" does not exist.')
        sys.exit(1)

    print(f'Crawling directory: {dir_path}...')
    count = 0
    skipped_sensitive = 0
    wiki_path = PROJECT_ROOT / 'ouro' / 'wiki'

    for file_path in dir_path.rglob('*'):
        if wiki_path in file_path.parents or file_path.parent == wiki_path:
            continue

        if any(part in IGNORED_DIRS for part in file_path.parts):
            continue

        if not file_path.is_file():
            continue

        if is_sensitive(file_path):
            print(f'Skipping sensitive file: {file_path}')
            skipped_sensitive += 1
            continue

        if is_binary(file_path):
            continue

        try:
            stage(str(file_path))
            count += 1
        except (UnicodeDecodeError, PermissionError):
            continue
        except Exception as e:
            print(f'Skipping file "{file_path}": {e}')

    print(f'Crawl complete. Staged {count} files. Skipped {skipped_sensitive} sensitive file(s).')

def pop():
    """Pops the first capture from the queue and prints it."""
    if not QUEUE_PATH.exists():
        print("Queue file not found.")
        return

    try:
        content = QUEUE_PATH.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading queue: {e}")
        return

    lines = content.splitlines()
    
    start_index = -1
    for i, line in enumerate(lines):
        if line.startswith('### Capture ['):
            start_index = i
            break
    
    if start_index == -1:
        print("No captures found in the queue.")
        return

    # Find the end of this capture (next ### Capture or end of file)
    end_index = len(lines)
    for i in range(start_index + 1, len(lines)):
        if lines[i].startswith('### Capture ['):
            end_index = i
            break
    
    capture_lines = lines[start_index:end_index]
    
    # The separator '---' might be at the end of the capture block or just after it
    if capture_lines and capture_lines[-1].strip() == '---':
        pass # Already included
    elif end_index < len(lines) and lines[end_index].strip() == '---':
        end_index += 1

    capture_text = '\n'.join(capture_lines).strip()
    
    # Remaining lines
    new_lines = lines[:start_index] + lines[end_index:]
    
    # Clean up and check if empty
    new_content = '\n'.join(new_lines).strip()
    if "### Capture [" not in new_content:
        # If no captures left, ensure *(Empty)* is there if the header exists
        if "## Pending Captures" in new_content:
            if "*(Empty)*" not in new_content:
                new_content = new_content.replace("## Pending Captures", "## Pending Captures\n*(Empty)*")
    
    try:
        QUEUE_PATH.write_text(new_content + '\n', encoding='utf-8')
        print(capture_text)
    except Exception as e:
        print(f"Failed to update queue: {e}")

def main():
    if len(sys.argv) < 2:
        print('Error: Please provide a file path, raw snippet, --crawl [dir], or --pop.')
        sys.exit(1)

    arg1 = sys.argv[1]

    if arg1 == '--crawl':
        directory = sys.argv[2] if len(sys.argv) > 2 else '.'
        crawl(directory)
    elif arg1 == '--pop':
        pop()
    else:
        stage(arg1)

if __name__ == '__main__':
    main()
