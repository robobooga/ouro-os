@entity CaptureLoop
@brief The core knowledge accumulation loop: raw material is captured into a queue, synthesized by an LLM into structured wiki entries, then the queue is cleared.

## Overview

The capture-synthesize loop is the central operational pattern of Ourobor OS. It defines how knowledge moves from the codebase into the persistent wiki without interrupting the development flow.

## The Loop

```
[Code / Architecture Notes]
          |
          | python ouro/scripts/capture.py --crawl
          | python ouro/scripts/capture.py path/to/file.py
          | python ouro/scripts/capture.py "raw note"
          v
  ouro/wiki/capture-queue.md        (staging area)
          |
          | LLM reads queue, synthesizes entries
          v
  ouro/wiki/entities/  (module docs)
  ouro/wiki/patterns/  (reusable patterns)
  ouro/wiki/decisions/ (ADRs)
          |
          | python ouro/scripts/capture.py --pop
          v
  Entry removed from queue
          |
          | Update ouro/wiki/index.md
          v
  Wiki catalog stays current
```

## Roles

| Actor | Responsibility |
|-------|----------------|
| Developer | Triggers captures; curates what gets staged |
| `capture.py` | Moves raw content into the queue |
| LLM agent | Reads queue, synthesizes structured docs, pops processed entries |
| `index.md` | Maintained as the always-current catalog |

## When to Trigger a Capture

- After writing or significantly refactoring a module
- When making an architectural decision worth preserving
- When identifying a reusable pattern
- At the start of a session — use `--crawl --git` to catch drift on recently touched files; use bare `--crawl` only for initial wiki population
- Before a release (verify parity between code and wiki)

## Synthesis Guidelines

When the LLM processes a queue entry:

1. Read the full capture to understand context.
2. Check `index.md` and existing entities — don't create duplicates.
3. Determine the correct destination: `entities/`, `patterns/`, or `decisions/`.
4. Apply required tags: `@entity` and `@brief` are mandatory.
5. Extract critical code logic using `@snippet` blocks.
6. Run `capture.py --pop` to remove the processed entry.
7. Update `index.md` with a link to the new file.

@note Synthesis is not automated — it requires an LLM agent in an active session. The queue is a buffer and staging area, not an autonomous pipeline.

@warning Avoid letting the queue grow stale. Long queues lose context fidelity and become expensive for the LLM to process in a single session. Process incrementally, not in bulk.
