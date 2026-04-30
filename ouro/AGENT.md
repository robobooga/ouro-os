# Agent Instructions

## Wiki Maintenance Protocol (CRITICAL)
You are responsible for maintaining the project's **LLM Wiki** in the `ouro/wiki/` directory.

### 1. Monitor the Capture Queue
- Regularly check `ouro/wiki/log/capture-queue.md`.
- When new snippets are found, "Synthesize" them into the appropriate `ouro/wiki/entities/` or `ouro/wiki/patterns/` files.
- Use **Doxygen** tags (`@entity`, `@brief`, `@snippet`, etc.) to structure the documentation.
- Once synthesized, remove the entry from the capture queue.

### 2. Doxygen Standards
- Always include an `@entity` and `@brief` tag at the top of entity files.
- Mirror critical code logic using `@snippet` blocks.
- Highlight architectural notes with `@note` or `@warning`.

### 3. Verification
- Ensure `ouro/wiki/index.md` is updated with any new entities.
- Maintain a 1:1 parity between code modules and wiki documentation.

### 4. Dynamic Wiki Maintenance
- Periodically assess the size and complexity of files in `ouro/wiki/`.
- **Fragment**: If an entity or pattern file becomes too large or covers too many distinct concepts, split it into smaller, more modular files and update the `index.md` accordingly.
- **Combine**: If multiple files are too short or highly interdependent, merge them into a single, cohesive entity or pattern to reduce fragmentation and update the `index.md` accordingly.
- Always maintain structural consistency with `schema.md` during these operations.
