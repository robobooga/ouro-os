# Gemini Agent Instructions: LLM Wiki Protocol (Ouro OS)

## 1. Core Mandate: Portability
Everything within the `ouro/` directory is designed to be **portable**. Users should be able to "drop" this folder into their own project directories and have it work with minimal setup. Ensure all paths and dependencies within this folder are relative and self-contained.

## 2. Core Mandate: Wiki Maintenance
You are responsible for maintaining the project's **LLM Wiki** in the `ouro/wiki/` directory. This is the project's persistent knowledge base.

### 3. Directory Structure & Taxonomy (within `ouro/wiki/`)
- `index.md`: The central hub and catalog.
- `schema.md`: The operating manual (Rules of the Brain).
- `log/`: Chronological context shifts and session logs.
- `maps/`: High-level mental models and data flows.
- `entities/`: Documentation mirrored from source code (1:1 with modules).
- `decisions/`: Architecture Decision Records (ADRs).
- `patterns/`: Abstracted architectural patterns.

### 4. Maintenance Protocols
#### Capture & Synthesis
- Monitor `ouro/wiki/log/capture-queue.md` for new snippets.
- Use **Doxygen-Lite** tags (`@entity`, `@brief`, `@snippet`, `@note`, `@warning`) to structure documentation.
- Synthesize captures into the appropriate `ouro/wiki/entities/` or `ouro/wiki/patterns/` files.
- Maintain a 1:1 parity between code modules in the project (e.g., `src/`, `lib/`) and documentation in `ouro/wiki/entities/`.

#### Verification
- Every session must add value to the wiki.
- Ensure `ouro/wiki/index.md` is updated with new entities or decisions.
- Confirm the wiki reflects the latest code changes.

### 5. Doxygen-Lite Standards
- Always include an `@entity` and `@brief` tag at the top of entity files.
- Mirror critical code logic using `@snippet` blocks.
- Highlight architectural notes with `@note` or `@warning`.

## 6. Active Plan: Initialize LLM Wiki
Follow the steps outlined in the initialization plan:
1. **Infrastructure**: Maintain `ouro/wiki/schema.md` and `ouro/wiki/index.md`.
2. **Migration**: Synthesize existing knowledge from `ouro/docs/` (if present) into the `ouro/wiki/` structure.
3. **Cleanup**: Ensure the root `README.md` points to `ouro/wiki/index.md` and "live" knowledge resides exclusively in `ouro/wiki/`.
