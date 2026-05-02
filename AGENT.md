# AGENT.md

This file contains shared project documentation for all LLM agents working with Ourobor OS.

## Project Overview

Ourobor OS is a portable, compounding knowledge system designed as an "External Brain" for LLM agents. It transforms project documentation into a structured, machine-readable wiki using Doxygen tags. The entire system lives in the `ouro/` directory and is designed to be dropped into any project.

## Core Philosophy

- **Persistence**: If it's not in the wiki, it doesn't exist for the LLM
- **Compounding**: Every development session adds to the collective intelligence
- **Portability**: All paths must be relative and self-contained within `ouro/`
- **1:1 Parity**: Maintain direct mapping between source modules and wiki documentation

## Directory Structure

```
ourobor-os/
├── docs/                 # Internal working documentation for Ourobor OS development
├── ouro/                 # The core portable system (source of truth)
│   ├── AGENT.md          # Agent maintenance protocol instructions
│   ├── README.md         # Skill installation and usage guide
│   ├── SKILL.md          # Platform-agnostic skill definition
│   ├── scripts/
│   │   ├── bootstrap.py  # Project initialization with environment detection
│   │   └── capture.py    # Doxygen tag extraction and staging
│   └── wiki/             # The "Brain" (template structure)
│       ├── index.md      # Central hub and catalog
│       ├── schema.md     # Operating manual and Doxygen standards
│       ├── entities/     # 1:1 mirrored codebase documentation
│       ├── decisions/    # Architecture Decision Records (ADRs)
│       ├── patterns/     # Reusable architectural abstractions
│       ├── maps/         # High-level mental models
│       └── capture-queue.md  # Staged snippets awaiting synthesis
├── scripts/
│   └── package.py        # Packaging script for distribution
└── dist/                 # Generated distribution packages (gitignored)
    └── ouro-skill.zip    # Packaged skill ready for distribution
```

**Important**: 
- `docs/` is for Ourobor OS project development planning
- `ouro/` is the complete, distributable skill package
- `scripts/package.py` creates distribution archives from `ouro/`
- The distribution is platform-agnostic and works with Claude, Gemini, Cursor, and any LLM tool

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

# Pop the oldest capture for granular digestion
python ./ouro/scripts/capture.py --pop
```

### Integration

There are two ways to integrate Ourobor OS into a project:

1. **Via LLM Skill** (Recommended):
   - Obtain the packaged skill (from Claude Skills Marketplace or build from source)
   - Extract to your LLM's skills directory:
     - Claude Code: `~/.claude/skills/ouro/`
     - Gemini CLI: `~/.agents/skills/ouro/`
     - Cursor: `~/.cursor/skills/ouro/`
     - Other LLMs: See `ouro/README.md` for installation paths
   - Bootstrap in target project using the skill's bootstrap script
   - The bootstrap script auto-detects your LLM environment and adapts accordingly

2. **Manual Integration**:
   - Copy the entire `ouro/` directory to your target project
   - Append `ouro/AGENT.md` to the project's LLM instruction file (CLAUDE.md, GEMINI.md, etc.)
   - Run capture scripts directly from the project's `ouro/scripts/` directory

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

1. **Capture**: The `capture.py` script scans files for Doxygen tags and stages them in `wiki/capture-queue.md`
2. **Synthesis**: Process the capture queue and transform entries into structured documentation in `wiki/entities/` or `wiki/patterns/`
3. **Indexing**: Update `wiki/index.md` to reflect new entities
4. **Cleanup**: Remove synthesized entries from the capture queue

## Key Implementation Details

### capture.py Architecture
- Ignores binary files and common directories (`.git`, `node_modules`, `__pycache__`, `.venv`, `dist`, `build`, `.next`, `dist-skill`)
- Filters files containing `@entity` or `@brief` tags
- Appends captures to the queue with timestamp and source metadata
- Supports both file paths and raw snippet input
- Queue path: `ouro/wiki/capture-queue.md`

### Portability Requirements
- All scripts must use relative paths from `ouro/` root
- The system should function identically regardless of parent project structure
- No dependencies on project-specific configuration outside `ouro/`

## Wiki Maintenance Protocol

When working on this project:

1. **Monitor** `ouro/wiki/capture-queue.md` for new captures.
2. **Synthesize** captures granularly using `python ouro/scripts/capture.py --pop`. This ensures context is maintained by processing one entry at a time.
3. **Transform** popped entries into appropriate `wiki/entities/` or `wiki/patterns/` files.
4. **Structure** all entity files with `@entity` and `@brief` tags at minimum.
5. **Mirror** critical code logic using `@snippet` blocks.
6. **Update** `wiki/index.md` when adding new entities.
7. **Maintain** 1:1 parity between code modules and documentation.
8. **Verify** that the foundation structure remains consistent with `schema.md`.

## Documentation Standards

- Always include `@entity` and `@brief` at the top of entity files
- Use `@snippet` blocks to mirror critical code logic
- Apply `@note` for important architectural context
- Apply `@warning` for side effects, risks, or gotchas
- Keep documentation synchronized with code changes
- Remove outdated captures from the queue after synthesis

## Skill Distribution System

Ourobor OS provides a **universal, platform-agnostic skill distribution** via the `ouro/` directory:

### Universal Distribution
- Works with Claude Code, Gemini CLI, Cursor, Cline, Aider, Continue, and any LLM tool
- Smart bootstrap script detects LLM environment automatically
- Adapts instructions and tips based on detected environment
- Updates all common instruction files (CLAUDE.md, GEMINI.md, CURSOR.md, etc.)
- Provides LLM-specific tips when features are available (e.g., Claude's `/schedule`)

### Installation Paths by LLM
- Claude Code: `~/.claude/skills/ouro/`
- Gemini CLI: `~/.agents/skills/ouro/`
- Cursor: `~/.cursor/skills/ouro/`
- Continue: `~/.continue/skills/ouro/`
- Project-local: `<project>/.llm/skills/ouro/` or `<project>/ouro/`

### Core Components
The `ouro/` directory contains everything needed for distribution:
- `SKILL.md` — Platform-agnostic skill definition
- `README.md` — Installation guide for all LLMs
- `AGENT.md` — Agent maintenance protocol (this file)
- `scripts/bootstrap.py` — Smart initialization with environment detection
- `scripts/capture.py` — Portable capture script (Python standard library only)
- `wiki/` — Template structure with schema.md, index.md, capture-queue.md
- `wiki/entities/`, `wiki/decisions/`, `wiki/patterns/`, `wiki/maps/` — Documentation directories

### Packaging for Distribution

The `ouro/` directory is the source of truth and can be distributed as-is. A packaging script creates distribution archives:

```bash
python scripts/package.py
```

This script:
1. Validates the `ouro/` directory structure
2. Creates a clean distribution archive
3. Generates `dist/ouro-skill.zip` ready for distribution
4. Optionally creates platform-specific packages

**Development Workflow**:
1. Make all changes directly in the `ouro/` directory
2. Test changes by copying `ouro/` to a test project or LLM skills directory
3. Run `python scripts/package.py` to create distribution archive
4. Test the packaged skill in a fresh project using the bootstrap script

## Development Context

The project is currently in early development. Reference `docs/PLAN.md` for the current implementation roadmap and migration strategy. This is a meta-project: we're building the foundation that will help LLMs understand other projects.
