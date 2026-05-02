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
├── ouro/                 # The core portable system (reference implementation)
│   ├── AGENT.md          # Agent maintenance protocol instructions
│   ├── scripts/
│   │   └── capture.py    # Doxygen tag extraction and staging
│   └── wiki/             # The "Brain"
│       ├── index.md      # Central hub and catalog
│       ├── schema.md     # Operating manual and Doxygen standards
│       ├── entities/     # 1:1 mirrored codebase documentation
│       ├── decisions/    # Architecture Decision Records (ADRs)
│       ├── patterns/     # Reusable architectural abstractions
│       ├── maps/         # High-level mental models
│       └── capture-queue.md  # Staged snippets awaiting synthesis
└── dist-skill/           # Universal LLM skill distribution
    └── ouro/
        ├── SKILL.md      # Platform-agnostic skill definition
        ├── README.md     # Installation guide for all LLMs
        ├── scripts/      # Bootstrap (with environment detection) & capture
        └── assets/       # Template files for new projects
```

**Important**: 
- `docs/` is for Ourobor OS project development planning
- `ouro/` is the reference implementation of the portable wiki system
- `dist-skill/` contains the universal skill package for distribution
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
```

### Integration

There are two ways to integrate Ourobor OS into a project:

1. **Via LLM Skill** (Recommended):
   - Claude Code: `cp -r dist-skill/ouro ~/.claude/skills/`
   - Gemini CLI: `cp -r dist-skill/ouro ~/.agents/skills/`
   - Cursor: `cp -r dist-skill/ouro ~/.cursor/skills/`
   - Other LLMs: See `dist-skill/README.md` for installation paths
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
- Ignores binary files and common directories (`.git`, `node_modules`, `__pycache__`, `.venv`, `dist`, `build`, `.next`)
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

1. **Monitor** `ouro/wiki/capture-queue.md` for new captures
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

## Skill Distribution System

Ourobor OS provides a **universal, platform-agnostic skill distribution** in `dist-skill/`:

### Universal Distribution (`dist-skill/`)
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

### Shared Components
All LLMs use the same:
- `capture.py` script (fully portable, Python standard library only)
- Template wiki files (index.md, schema.md, capture-queue.md)
- Doxygen protocol standards
- Core maintenance workflow

### When working on Ourobor OS development:
- Update the core `ouro/` reference implementation first
- Sync changes to `dist-skill/` as needed
- Test across multiple LLM tools to ensure portability
- Use environment detection features in bootstrap.py for LLM-specific behaviors

## Development Context

The project is currently in early development. Reference `docs/PLAN.md` for the current implementation roadmap and migration strategy. This is a meta-project: we're building the foundation that will help LLMs understand other projects.
