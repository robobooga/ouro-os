# Ourobor OS: Developer-Centric LLM Wiki

Ourobor OS is a portable, compounding knowledge system designed to serve as an "External Brain" for LLM agents. It transforms project documentation into a structured, machine-readable wiki that grows alongside your codebase.

## ♾️ About the Project
The name **Ourobor OS** is inspired by the *Ouroboros*—the ancient symbol of a snake eating its own tail. This represents the cyclical, self-renewing nature of our architecture: as you develop code, the system captures knowledge, which informs future development, which in turn updates and refines the documentation. It is a system that continuously feeds on its own evolution.

## 🧠 Core Philosophy
- **Persistence**: If it's not in the wiki, it doesn't exist for the LLM.
- **Compounding**: Every development session adds to the collective intelligence of the project.
- **Portability**: The entire system lives in the `ouro/` directory and can be dropped into any project.

## ⚠️ The Documentation Problem
Documentation often falls into a "trap of obsolescence":
- **Context Friction**: Stopping the flow of coding to write documentation is mentally expensive and interrupts the development cycle.
- **The Staleness Cycle**: Documentation is frequently the first thing to become outdated as code changes, eventually leading to mistrust and abandonment of the wiki.

Ourobor OS aims to solve these by embedding documentation into the development flow, using automation to reduce manual overhead and ensuring the "Brain" stays synchronized with the evolving codebase.

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
- **`log/`**: Chronological session history and the `capture-queue.md`.

## 🚀 Quick Start

### 1. Installation
Copy the `ouro/` directory into your project's root.

### 2. Integration
Enable the agent by appending the contents of `ouro/AGENT.md` to your project's instructions (e.g., `GEMINI.md` or `CLAUDE.md`).

### 3. Usage
Run the capture script to scan your project for Doxygen tags:
```powershell
python ./ouro/scripts/capture.py --crawl
```

## 📖 Learn More
Navigate to the [Wiki Index](./ouro/wiki/index.md) to explore the system's full capabilities.
