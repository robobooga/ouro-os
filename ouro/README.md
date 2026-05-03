# Ourobor OS - Universal LLM Skill

This is the complete, distributable Ourobor OS skill package - a platform-agnostic, portable compounding knowledge system for LLM agents.

## What is Ourobor OS?

Ourobor OS transforms project documentation into a structured, machine-readable wiki using Doxygen tags. It creates an "External Brain" that grows with every development session, providing persistent context for Claude, Gemini, Cursor, and other LLM agents.

**Platform-agnostic design**: Works with any LLM tool that can read files and execute shell commands.

## Installation

### Supported LLM Tools

- **Claude Code** (`~/.claude/skills/`)
- **Gemini CLI** (`~/.agents/skills/`)
- **Cursor** (`~/.cursor/skills/` or project-local)
- **Cline** (VS Code extension - project-local)
- **Aider** (project-local)
- **Continue** (`~/.continue/skills/`)
- **Any LLM**: Manual integration (see below)

### Installation by LLM Tool

#### Claude Code
```bash
# From packaged distribution
unzip ouro-skill.zip -d ~/.claude/skills/

# Or from source repository
cp -r ouro ~/.claude/skills/
```

#### Gemini CLI
```bash
# From packaged distribution (macOS/Linux)
unzip ouro-skill.zip -d ~/.gemini/skills/

# From source repository
cp -r ouro ~/.gemini/skills/

# Windows PowerShell (from source)
Copy-Item -Recurse -Path "ouro" -Destination "$HOME\.gemini\skills\"
```

#### Cursor / Cline / VS Code Extensions
```bash
# Option 1: Install to user skills directory (if supported)
unzip ouro-skill.zip -d ~/.cursor/skills/
# Or: cp -r ouro ~/.cursor/skills/

# Option 2: Project-local (recommended for team sharing)
unzip ouro-skill.zip -d <your-project>/.llm/skills/
# Or: cp -r ouro <your-project>/.llm/skills/
```

#### Aider / CLI-based LLMs
```bash
# Manual integration - copy to project
cp -r ouro <your-project>/
```

### Manual Integration (Any LLM)

If your LLM tool doesn't have a skills directory:

1. Copy the entire `ouro/` folder to your project
2. Run the bootstrap script to set up the wiki structure
3. Your LLM will automatically receive maintenance protocols via the updated instruction file

## Usage

### Bootstrap a New Project

**What to expect:**
The bootstrap script automates the setup of your Ourobor OS environment. It creates the necessary `ouro/wiki/` directory structure, initializes template files, and identifies your active LLM tools (e.g., Claude, Gemini, Cursor) to update your instruction files (`CLAUDE.md`, `GEMINI.md`, etc.) with the Ourobor OS maintenance protocols.

Run the bootstrap script from your project directory:

```bash
# If installed as a skill
python ~/.claude/skills/ouro/scripts/bootstrap.py  # Claude
python ~/.agents/skills/ouro/scripts/bootstrap.py  # Gemini

# If using manual integration
python <your-project>/ouro/scripts/bootstrap.py
```

### Capture Code & Documentation

**What to expect:**
The capture script acts as a staging bridge. When run, it identifies your target code or notes and automatically appends them to `ouro/wiki/capture-queue.md`. It uses a safe, append-only operation that prevents loss of previous captures. Once staged, your LLM agent will notice the new entries in the queue during its next maintenance pass, synthesize the raw information into formatted documentation, and move the finalized content into the appropriate `ouro/wiki/` subdirectories.

```bash
# Crawl only git-changed files (recommended after initial setup)
python <path-to-skill>/scripts/capture.py --crawl --git

# Include last N commits' worth of changes
python <path-to-skill>/scripts/capture.py --crawl --git 3

# Crawl entire project (use for initial wiki population)
python <path-to-skill>/scripts/capture.py --crawl

# Capture specific directory
python <path-to-skill>/scripts/capture.py src/

# Capture specific file
python <path-to-skill>/scripts/capture.py src/main.py

# Capture raw snippet or architectural note
python <path-to-skill>/scripts/capture.py "Architectural Note: Use composition over inheritance."

# Finalize/Pop the queue after synthesis
python <path-to-skill>/scripts/capture.py --pop
```

### Maintain the Wiki with Your LLM

Once initialized, your LLM agent will automatically:
- Monitor `ouro/wiki/capture-queue.md` for new captures
- Synthesize captures into structured documentation
- Maintain 1:1 parity between code and wiki
- Create Architecture Decision Records (ADRs)
- Use `python <path-to-skill>/scripts/capture.py --pop` to finalize and clear synthesized entries from the queue.

You can also:
- Use your LLM's scheduling features (if available) for recurring wiki maintenance
- Use task systems (if available) to track synthesis work
- Leverage your LLM's file reading/writing tools for manual wiki updates

## Platform-Agnostic Design

This unified distribution works across all LLM tools because:

### ✅ No Hard Dependencies
- Python 3.x only (standard library)
- No LLM-specific APIs or integrations
- Works with any file reading/writing tool

### ✅ Smart Environment Detection
- Automatically detects Claude Code, Cursor, Aider, etc.
- Adapts instructions based on detected environment
- Provides relevant tips for each LLM tool

### ✅ Flexible Instruction File Updates
- Updates CLAUDE.md, GEMINI.md, CURSOR.md, CLINE.md, etc.
- Creates AI_INSTRUCTIONS.md if no instruction file exists
- Generic protocol works with any LLM's capabilities

### ✅ Portable Core
- `capture.py` uses only standard Python Path operations
- All paths are relative to `ouro/` directory
- Wiki structure is self-contained
- Automatically ignores common build/dependency directories and `dist-skill/` to prevent noise.

## Directory Structure

```
ouro/
├── SKILL.md                         # Platform-agnostic skill definition
├── README.md                        # This file
├── AGENT_PROTOCOL.md                # Agent maintenance protocol
├── scripts/
│   ├── bootstrap.py                 # Smart initialization with environment detection
│   └── capture.py                   # Portable capture script
└── wiki/                            # Template wiki structure
    ├── index.md                     # Wiki hub template
    ├── schema.md                    # Doxygen protocol template
    ├── capture-queue.md             # Empty capture queue
    ├── entities/                    # Code documentation directory
    ├── decisions/                   # ADR directory
    ├── patterns/                    # Patterns directory
    └── maps/                        # Mental models directory
```

## Key Features

### Universal Compatibility
Works with any LLM that can:
- Read files from disk
- Write/edit files
- Execute shell commands (for capture.py)

### Environment Detection
Automatically detects and adapts to:
- `.claude/` directory → Claude Code tips
- `.cursor/` directory → Cursor tips
- `.aider/` directory → Aider tips
- `.continue/` directory → Continue tips

### Flexible Protocols
- Generic maintenance protocol works everywhere
- Optional LLM-specific features (scheduling, tasks) when available
- Graceful degradation on simpler LLM tools

## Building from Source

This directory (`ouro/`) is the complete distributable package. To create distribution archives:

```bash
# From the parent ourobor-os repository
python scripts/package.py
```

This generates `dist/ouro-skill.zip` ready for distribution.

## Files Included

### SKILL.md
The main skill definition with:
- YAML frontmatter (`name: ouro`, `description: ...`)
- Platform-agnostic getting started guide
- LLM-specific tips for Claude, Gemini, Cursor, etc.
- Best practices for any LLM

### scripts/bootstrap.py
Smart initialization script that:
- Detects LLM environment automatically
- Creates `ouro/wiki/` directory structure
- Copies template files
- Updates all common instruction files
- Provides environment-specific tips

### scripts/capture.py
Portable capture script that:
- Crawls directories for code to document
- Stages files in the capture queue
- Works identically across all LLMs
- Uses `Path.cwd() / 'ouro'` for portability

> **Customize for your project**: `capture.py` ships with opinionated defaults for ignored directories and sensitive file detection. Review and adjust these near the top of the file to match your stack:
>
> - **`IGNORED_DIRS`** — directories skipped entirely during `--crawl` (build outputs, package managers, caches, credential folders, etc.). Add any project-specific directories that should never be crawled (e.g. `migrations`, `fixtures`, `android`, `ios`).
> - **`SENSITIVE_NAMES`** / **`SENSITIVE_SUFFIXES`** — exact filenames and extensions that are always skipped regardless of location (`.pem`, `.key`, `.env.*`, etc.). Extend these if your project uses non-standard secret file conventions.
> - **`is_sensitive()`** — the function that applies the above rules plus heuristic keyword matching (`secret`, `credential`, `token`, etc. in filenames). Edit the keyword list here if your project uses different naming patterns.
>
> The goal is to prevent secrets, credentials, or API keys from being written into the capture queue unintentionally.

### wiki/
Template files for a fresh wiki (copied to projects during bootstrap):
- `index.md`: Central catalog and hub
- `schema.md`: Doxygen protocol and operating manual
- `capture-queue.md`: Empty staging area
- Subdirectories: `entities/`, `decisions/`, `patterns/`, `maps/`

## Contributing

To improve this skill:

1. Test in real projects across different LLM tools
2. Report platform-specific issues
3. Suggest improvements to environment detection
4. Document common synthesis patterns

## License

Same as the main Ourobor OS project.

## Support

### General Issues
- Check `SKILL.md` for usage guidance
- Review the bootstrap script output for errors
- Ensure your LLM has permission to run Python scripts

### Platform-Specific Issues
- **Claude Code**: Ensure `.claude/` directory exists, use `!` prefix for commands
- **Gemini CLI**: Check file permissions, verify skill installation path
- **Cursor/VS Code**: Run bootstrap from integrated terminal
- **Aider**: Use project-local installation

### Wiki Protocol Issues
- See the main project documentation
- Review `ouro/wiki/schema.md` for Doxygen protocol
- Check `ouro/wiki/index.md` for examples

---

**Ready to build your External Brain?** Install the skill and run the bootstrap script!
