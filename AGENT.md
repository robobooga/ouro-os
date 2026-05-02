# AGENT.md

Project documentation for Ourobor OS.

## Overview
Ourobor OS is a portable, compounding knowledge system ("External Brain"). It maps project documentation to a machine-readable wiki contained in the `ouro/` directory.

> **CRITICAL**: The `ouro/` directory is a **portable skill package** (the "system"). Keep it distinct from your **target project codebase**. When running commands, be aware of whether you are operating on the Ourobor OS system or your project files.

## Wiki Protocol
- **Persistence**: If it's not in the wiki, it doesn't exist.
- **Compounding**: Every session grows the collective intelligence.
- **1:1 Parity**: Maintain direct mapping between source modules and documentation.

### Doxygen Standards
- `@entity <name>`: Module/entity defined.
- `@brief <text>`: One-sentence summary.
- `@snippet <id>`: Critical code block.
- `@note`/`@warning`: Dev context/alerts.
- `@param`/`@return`: Function documentation.

## Workflow For Skill Package
1. **Monitor**: Check `ouro/wiki/capture-queue.md`.
2. **Synthesize**: Use `python ouro/scripts/capture.py --pop` to process captures.
3. **Document**: Transform entries into `ouro/wiki/entities/` or `patterns/`.
4. **Index**: Update `ouro/wiki/index.md`.
5. **Clean**: Remove synthesized entries from queue.

## Development Commands
```bash
# Package distribution
python scripts/package.py
```

## Skill Distribution
The `ouro/` directory is a universal, platform-agnostic skill meant to be dropped into target projects.
- **Install Paths**: `~/.agents/skills/ouro/` or project-local `.llm/skills/ouro/`.
- **Initialization**: Run `python ouro/scripts/bootstrap.py` in the **project root**.
- **Source of Truth**: All Ourobor OS system development happens in `ouro/`.

## Key Directories
- `ouro/`: Core portable system (the "Skill").
- `ouro/scripts/`: `bootstrap.py` (init), `capture.py` (tag extraction).
- `ouro/wiki/`: The "Brain" (entities, decisions, patterns, maps).
- `docs/`: Ourobor OS project-specific planning.
- `dist/`: Generated archives.
