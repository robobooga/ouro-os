# Ourobor OS: The Living Project Documentation Ecosystem

Ourobor OS is a holistic, AI-native "operating system" for project documentation. It creates a compounding knowledge base designed to be perfectly readable by humans and efficiently crawlable by LLMs. By embedding the knowledge capture directly into the development workflow, Ourobor OS ensures that your project documentation remains a living, evolving part of the codebase.

## ⚠️ The Documentation Problem
Documentation often falls into a "trap of obsolescence":
- **Context Friction**: Stopping the flow of coding to write documentation is mentally expensive and interrupts the development cycle.
- **The Staleness Cycle**: Documentation is frequently the first thing to become outdated as code changes, eventually leading to mistrust and abandonment of the wiki.

Ourobor OS aims to solve these by embedding documentation into the development flow, using automation to reduce manual overhead and ensuring the "Brain" stays synchronized with the evolving codebase.

## ♾️ About the Project
The name **Ourobor OS** is inspired by the *Ouroboros*—the ancient symbol of a snake eating its own tail. This represents the cyclical, self-renewing nature of our architecture: as you develop code, the system captures knowledge, which informs future development, which in turn updates and refines the documentation. It is a system that continuously feeds on its own evolution.

## 🌟 Project Plans
While Ourobor OS currently provides an **Agent Skill** for seamless IDE integration, our vision extends far beyond a simple plugin. We are building a comprehensive ecosystem for documentation, including but not limited to:
- **Web UI**: An intuitive interface for browsing, managing, and visualizing your project's knowledge graph.
- **Auxiliary Tooling**: Specialized utilities for documentation maintenance, validation, and analytics.
- **Holistic Integration**: A unified standard for AI-assisted project management where documentation is the primary interface for both developers and agents.

## 🧠 Core Philosophy
- **Persistence**: If it's not in the wiki, it doesn't exist for the LLM.
- **Compounding**: Every development session adds to the collective intelligence of the project.
- **Portability**: The entire Ouro Core system is designed to be lightweight, modular, and portable across any codebase.
- **Dual-Readability**: Documentation must be equally elegant for humans to read and structured for LLMs to crawl and synthesize.

## 🛠 Features
- **Doxygen Protocol**: Uses structured tags (`@entity`, `@brief`, `@snippet`) to make Markdown machine-readable and UI-ready.
- **Automated Capture**: Scripts to crawl your codebase and stage new knowledge for synthesis.
- **Architecture Mapping**: Dedicated tracks for ADRs (Decisions), Patterns, and Mental Models (Maps).
- **1:1 Parity**: Maintains a direct mapping between source modules and documentation entities.

## 📂 Structure
The project "Brain" resides in `ouro/wiki/`:
- **`index.md`**: The central hub and catalog.
- **`schema.md`**: The operating manual and Doxygen standards.
- **`entities/`**: 1:1 mirrored documentation of your codebase.
- **`decisions/`**: Architecture Decision Records (ADRs).
- **`patterns/`**: Abstracted, reusable architectural logic.
- **`capture-queue.md`**: The active capture staging area.

## 🚀 Quick Start

### 1. Installation

Using (`npx skills`)[https://github.com/vercel-labs/skills]
```bash
npx skills add robobooga/ourobor-os 
```

Clone this repository and copy the `ouro/` directory into your project's root:

```bash
# Clone the repository
git clone https://github.com/robobooga/ourobor-os.git

# Copy core functionality
cp -r ourobor-os/ouro ./
```

For developers working on Ourobor OS itself, you can package the skill for distribution:

```bash
python scripts/package.py
# Output: dist/ouro-skill.zip
```

### 2. Integration
Enable the agent by appending the maintenance protocols to your project's instructions (e.g., `GEMINI.md` or `CLAUDE.md`). See `ouro/AGENT_PROTOCOL.md` for the full protocol.

### 3. Usage
Run the capture script to scan your project for Doxygen tags:
```
python ./ouro/scripts/capture.py --crawl
```

Or, initialize the system in a new project:
```
python ./ouro/scripts/bootstrap.py
```

## 📖 Learn More
- Navigate to the [Wiki Index](./ouro/wiki/index.md) to explore the system's full capabilities.
- Inspired by [Andrej Karpathy’s "LLM Wiki"](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) concept.
