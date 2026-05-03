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

Walks all non-binary files and calls `stage()` on each, skipping ignored directories, sensitive files, and the `ouro/wiki/` directory itself to avoid recursive capture. Reports a count of staged files and separately a count of skipped sensitive files.

**Module-level constants** (edit in `capture.py` to customise for your project):

- **`IGNORED_DIRS`** — directory names that cause an entire subtree to be skipped. Covers version control, Python/JS/Go/Rust/JVM build and cache directories, infrastructure state (`.terraform`), and credential directories (`.aws`, `.ssh`, `secrets`, `certs`, `vault`, etc.).
- **`SENSITIVE_NAMES`** — exact filenames always skipped (`.env`, `id_rsa`, `credentials.json`, etc.).
- **`SENSITIVE_SUFFIXES`** — extensions always skipped (`.pem`, `.key`, `.p12`, `.pfx`, `.crt`, `.secret`, `.token`, etc.).

See [ADR-005](../decisions/ADR-005-crawl-sensitive-file-guard.md) for the rationale.

### `is_sensitive(file_path)`

Combines `SENSITIVE_NAMES`, `SENSITIVE_SUFFIXES`, and heuristic keyword matching (`secret`, `credential`, `password`, `passwd`, `apikey`, `api_key`, `token`, `private_key` in the filename) to decide whether a file should be skipped during crawl.

@warning `IGNORED_DIRS`, `SENSITIVE_NAMES`, `SENSITIVE_SUFFIXES`, and the keyword list in `is_sensitive()` are project-agnostic defaults. Projects with non-standard secret naming conventions should update these constants directly in `capture.py`.

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
- `IGNORED_DIRS` and `SENSITIVE_*` constants are not user-configurable via CLI flags — editing the source file is required.
- No deduplication — staging the same file twice creates duplicate entries.
