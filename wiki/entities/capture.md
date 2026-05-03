@entity capture
@brief Manages the capture queue — staging, crawling, and popping knowledge entries for LLM synthesis.

## Overview

`ouro/scripts/capture.py` is the primary knowledge ingestion tool. It reads code and notes into `ouro/wiki/capture-queue.md` for later synthesis by an LLM agent. It is the entry point to the [Capture-Synthesize Loop](../patterns/capture-synthesize-loop.md).

## Functions

### `stage(input_str)`
@param input_str A file path or raw text string.

Appends a timestamped entry to the capture queue. If a valid file path is given, reads its content; otherwise treats the input as a raw snippet. Handles binary file detection and encoding errors gracefully.

@snippet stage-entry-format
```
### Capture [2026-05-03T10:00:00]
- **Source**: `ouro/scripts/capture.py`
- **Content**:
```<content>```
---
```

If the queue contains `*(Empty)*`, it is removed before appending.

### `crawl(directory)`
@param directory Root directory to walk recursively. Defaults to `.` via CLI.

Walks all non-binary files and calls `stage()` on each, skipping ignored directories and the `ouro/wiki/` directory itself to avoid recursive capture.

**Hardcoded ignored directories**: `.git`, `node_modules`, `__pycache__`, `.venv`, `dist`, `build`, `.next`, `ouro`, `dist-skill`

@warning Currently stages every text file including config files, dotfiles, and lock files. No smart filtering exists — the LLM must triage noise from the queue manually. A configurable exclusion list and `--status` command are known missing features.

### `pop()`

Reads and prints the first `### Capture [...]` entry from the queue, removes it, and rewrites the file. If no entries remain, restores the `*(Empty)*` marker. Used by the LLM agent to process one entry at a time during synthesis.

### `is_binary(file_path)`

Heuristic check — reads the first 1024 bytes of a file and returns `True` if a null byte is found.

## CLI Usage

```bash
# Stage a specific file
python ouro/scripts/capture.py path/to/file.py

# Stage a raw architectural note
python ouro/scripts/capture.py "Decision: use composition over inheritance in the plugin loader."

# Crawl the whole project
python ouro/scripts/capture.py --crawl

# Crawl a specific directory
python ouro/scripts/capture.py --crawl src/

# Pop the first entry from the queue (used during synthesis)
python ouro/scripts/capture.py --pop
```

@note `QUEUE_PATH` is resolved relative to `Path.cwd()`, so the script must be run from the project root.

## Known Gaps

- No `--status` subcommand to show queue length or last capture timestamp.
- `--crawl` has no user-configurable exclusion list.
- No deduplication — staging the same file twice creates duplicate entries.
