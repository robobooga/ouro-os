# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ouro OS is a portable, compounding knowledge system designed as an "External Brain" for LLM agents. It transforms project documentation into a structured, machine-readable wiki using Doxygen tags. The entire system lives in the `ouro/` directory and is designed to be dropped into any project.

## Core Philosophy

- **Persistence**: If it's not in the wiki, it doesn't exist for the LLM
- **Compounding**: Every development session adds to the collective intelligence
- **Portability**: All paths must be relative and self-contained within `ouro/`
- **1:1 Parity**: Maintain direct mapping between source modules and wiki documentation

## Directory Structure

```
ouro-os/
├── docs/              # Internal working documentation for Ouro OS development
├── ouro/              # The portable system (drop into any project)
│   ├── AGENT.md       # Agent maintenance protocol instructions
│   ├── scripts/
│   │   └── capture.py # Doxygen tag extraction and staging
│   └── wiki/          # The "Brain"
│       ├── index.md   # Central hub and catalog
│       ├── schema.md  # Operating manual and Doxygen standards
│       ├── entities/  # 1:1 mirrored codebase documentation
│       ├── decisions/ # Architecture Decision Records (ADRs)
│       ├── patterns/  # Reusable architectural abstractions
│       ├── maps/      # High-level mental models
│       └── log/
│           └── capture-queue.md  # Staged snippets awaiting synthesis
```

**Important**: `docs/` is for Ouro OS project development planning. `ouro/wiki/` is the portable wiki system that gets deployed to other projects.

## Development Commands

### Capture System
```bash
# Crawl entire project for Doxygen tags
python ./ouro/scripts/capture.py --crawl

# Crawl specific directory
python ./ouro/scripts/capture.py --crawl <directory>

# Stage a specific file
python ./ouro/scripts/capture.py <file_path>

# Stage raw snippet
python ./ouro/scripts/capture.py "snippet content"
```

### Integration
To integrate Ouro OS into a project, append `ouro/AGENT.md` to the project's agent instructions (e.g., `GEMINI.md` or `CLAUDE.md`).

## Doxygen Protocol

The wiki uses structured Doxygen tags within Markdown for machine-readability:

- `@entity <name>` — Defines the module/entity being documented (required)
- `@brief <text>` — One-sentence summary (required)
- `@snippet <id>` — Critical code block identifier
- `@note <text>` — Important developer information
- `@warning <text>` — Critical alerts about side effects/risks
- `@param <name> <desc>` — Parameter documentation (for functions)
- `@return <desc>` — Return value documentation

## Capture → Synthesis Workflow

1. **Capture**: The `capture.py` script scans files for Doxygen tags and stages them in `wiki/log/capture-queue.md`
2. **Synthesis**: Process the capture queue and transform entries into structured documentation in `wiki/entities/` or `wiki/patterns/`
3. **Indexing**: Update `wiki/index.md` to reflect new entities
4. **Cleanup**: Remove synthesized entries from the capture queue

## Key Implementation Details

### capture.py Architecture
- Ignores binary files and common directories (`.git`, `node_modules`, `__pycache__`, `.venv`, `dist`, `build`, `.next`)
- Filters files containing `@entity` or `@brief` tags
- Appends captures to the queue with timestamp and source metadata
- Supports both file paths and raw snippet input
- Queue path: `ouro/wiki/log/capture-queue.md`

### Portability Requirements
- All scripts must use relative paths from `ouro/` root
- The system should function identically regardless of parent project structure
- No dependencies on project-specific configuration outside `ouro/`

## Wiki Maintenance Protocol

When working on this project:

1. **Monitor** `ouro/wiki/log/capture-queue.md` for new captures
2. **Synthesize** captures into appropriate `wiki/entities/` or `wiki/patterns/` files
3. **Structure** all entity files with `@entity` and `@brief` tags at minimum
4. **Mirror** critical code logic using `@snippet` blocks
5. **Update** `wiki/index.md` when adding new entities
6. **Maintain** 1:1 parity between code modules and documentation
7. **Verify** that the foundation structure remains consistent with `schema.md`

## Documentation Standards

- Always include `@entity` and `@brief` at the top of entity files
- Use `@snippet` blocks to mirror critical code logic
- Apply `@note` for important architectural context
- Apply `@warning` for side effects, risks, or gotchas
- Keep documentation synchronized with code changes
- Remove outdated captures from the queue after synthesis

## Development Context

The project is currently in early development. Reference `docs/PLAN.md` for the current implementation roadmap and migration strategy. This is a meta-project: we're building the foundation that will help LLMs understand other projects.
