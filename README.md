# Ouro OS: Developer-Centric LLM Wiki

Ouro OS is a portable, compounding knowledge system designed to serve as an "External Brain" for LLM agents. It transforms project documentation into a structured, machine-readable wiki that grows alongside your codebase.

## 🧠 Core Philosophy
- **Persistence**: If it's not in the wiki, it doesn't exist for the LLM.
- **Compounding**: Every development session adds to the collective intelligence of the project.
- **Portability**: The entire system lives in the `ouro/` directory and can be dropped into any project.

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
