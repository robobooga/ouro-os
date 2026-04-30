# Wiki Schema: Doxygen-Lite Protocol

This document defines the "Operating Manual" for the LLM Wiki. It uses **Doxygen** tags to ensure a "Gold Standard" of documentation while remaining lightweight and LLM-synthesizable.

## 1. Philosophy
- **Persistent Knowledge**: The wiki is the project's brain. If it's not in the wiki, it doesn't exist for the LLM.
- **Compounding**: Every session should add value to the wiki.
- **Doxygen-Lite**: Use structured tags within Markdown to allow for machine-readability and rich UI rendering.

## 2. Doxygen-Lite Tags
| Tag | Description |
| --- | --- |
| `@entity <name>` | Defines the module or entity this file documents. |
| `@brief <text>` | A one-sentence summary of the entity. |
| `@snippet <id>` | Identifies a code block that is critical for understanding. |
| `@note <text>` | Important information for developers. |
| `@warning <text>` | Critical alerts regarding side effects or risks. |
| `@param <name> <desc>` | Documents a parameter (for function-level entities). |
| `@return <desc>` | Documents the return value. |

## 3. Maintenance Protocols
- **Capture**: New code snippets are staged in `wiki/log/capture-queue.md`.
- **Synthesis**: The LLM must periodically process the queue and update `wiki/entities/`.
- **Parity**: Maintain a 1:1 mapping between `src/` modules and `wiki/entities/` files.

## 4. Directory Structure
- `index.md`: The central hub.
- `entities/`: Documentation for code modules.
- `decisions/`: Architecture Decision Records (ADRs).
- `patterns/`: Abstracted architectural patterns.
- `maps/`: Data flows and mental models.
- `log/`: Session logs and capture queue.
