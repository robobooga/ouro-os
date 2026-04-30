import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
WIKI_DIR = BASE_DIR.parent / 'ouro' / 'wiki'
DIST_DIR = BASE_DIR / 'dist'

def build():
    print(f"Building Ouro Wiki Web UI from {WIKI_DIR} to {DIST_DIR}...")
    
    if not WIKI_DIR.exists():
        print(f"Error: Wiki directory not found at {WIKI_DIR}")
        return

    # Ensure dist exists
    DIST_DIR.mkdir(exist_ok=True)
    
    print("Scaffold complete. Ready for parser implementation.")

if __name__ == '__main__':
    build()
