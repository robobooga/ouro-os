# Gemini Agent Instructions: Portable Ourobor OS & LLM Wiki Foundation

## 1. Core Mandate: Portability
Everything within the `ouro/` directory is designed to be **portable**. The Ourobor OS is a "drop-in" system that users can integrate into any project. Ensure all paths, scripts, and documentation within the `ouro/` folder are relative and self-contained.

## 2. Core Mandate: Building the LLM Wiki Foundation
You are responsible for building and refining the **LLM Wiki Foundation** in the `ouro/wiki/` directory. This is not about content maintenance, but about establishing the architectural standards, schemas, and automation scripts (the "Brain") that make the wiki functional and portable.

## 3. Directory Structure & Taxonomy (within `ouro/wiki/`)
- `index.md`: The central hub and foundation catalog.
- `schema.md`: The operating manual (Rules of the Brain).
- `log/`: Chronological context shifts and foundation development logs.
- `maps/`: High-level mental models of the foundation's architecture.
- `entities/`: Structural templates and foundational entity documentation.
- `decisions/`: Architecture Decision Records (ADRs) for the Ourobor OS.
- `patterns/`: Abstracted architectural patterns for the foundation.

## 4. Foundational Protocols
### Capture & Synthesis Infrastructure
- Develop and refine scripts (e.g., `ouro/scripts/capture.py`) to monitor `ouro/wiki/log/capture-queue.md`.
- Establish **Doxygen**-style tagging standards (`@entity`, `@brief`, `@snippet`, `@note`, `@warning`) for the foundation.
- Ensure the synthesis logic correctly populates `ouro/wiki/entities/` or `ouro/wiki/patterns/`.

### Verification & Integrity
- Validate that the foundation structure remains consistent with `schema.md`.
- Ensure `ouro/wiki/index.md` accurately reflects the current state of the foundation.
- Verify that all scripts and paths remain portable.

## 5. Doxygen Standards
- Always include an `@entity` and `@brief` tag at the top of entity files.
- Mirror critical code logic using `@snippet` blocks.
- Highlight architectural notes with `@note` or `@warning`.

## 6. Active Plan: Build Ourobor OS Foundation
Follow the steps to establish the portable Ourobor OS core:
1. **Foundational Infrastructure**: Finalize `ouro/wiki/schema.md` and `ouro/wiki/index.md` as standard templates.
2. **Automation**: Refine `ouro/scripts/capture.py` to handle the synthesis of snippets into the wiki foundation.
3. **Portability Validation**: Ensure the entire `ouro/` directory can be moved and function independently in any workspace.
