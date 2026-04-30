# Project Plan: Developer-Centric LLM Wiki

## Objective
Establish a compounding, product-agnostic "LLM Wiki" system inside the `ouro/wiki/` directory, supported by an offline-first dashboard in the `ouro-webui/` directory. This system serves as the persistent knowledge base for the project, maintained by the LLM and curated by the developer.

## Directory Structure
- `ouro/wiki/`
    - `index.md`: The central hub/catalog.
    - `schema.md`: The operating manual (Rules of the Brain).
    - `log/`: Chronological context shifts (Session logs).
    - `maps/`: High-level mental models and data flows.
    - `entities/`: Documentation mirrored from the source code (1:1 with modules).
    - `decisions/`: ADRs (Architecture Decision Records).
    - `patterns/`: Abstracted architectural patterns.
- `ouro-webui/`
    - `builder.py`: Static site generator.
    - `templates/`: Dashboard templates.
    - `dist/`: Generated dashboard output.

## Implementation Steps

### Phase 1: Ouro Core (COMPLETED)
1. Created `ouro/wiki/schema.md`: Defined philosophy, taxonomy, and maintenance protocols.
2. Created `ouro/wiki/index.md`: Initialized the hub with links to the new categories.
3. Updated `CLAUDE.md`/`GEMINI.md`: Added instructions for LLM agent to enforce wiki maintenance.
4. Populated `ouro/wiki/entities/Parser.md` and foundational ADRs.
5. Initialized logging and cleanup of project documentation.

### Phase 2: Ouro-WebUI (ACTIVE)
1. Scaffold `ouro-webui/` directory and basic structure.
2. Develop a Python-based SSG in `builder.py` using `mistune` (Markdown parsing & Doxygen tag processing) and `jinja2` (templating).
3. Create responsive, portable dashboard templates.
4. Integrate custom Mistune renderer for Ourobor protocol tags (`@entity`, `@brief`, `@note`, `@warning`).
5. Verify generation and portability of the dashboard.

## Verification
- LLM can successfully "look up" a decision or entity in the `ouro/wiki/`.
- `python ouro-webui/builder.py` generates a functional, linked dashboard.
- The wiki structure is portable and drop-in ready.

## Malleability Note
This structure is designed to be "Drop-in Ready." To use it in another project, simply copy the `ouro/` and `ouro-webui/` folders and reset the content while keeping the core schemas and scripts.
