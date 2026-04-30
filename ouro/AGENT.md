# Agent Instructions

## Wiki Maintenance Protocol (CRITICAL)
You are responsible for maintaining the project's **LLM Wiki** in the `wiki/` directory.

### 1. Monitor the Capture Queue
- Regularly check `wiki/log/capture-queue.md`.
- When new snippets are found, "Synthesize" them into the appropriate `wiki/entities/` or `wiki/patterns/` files.
- Use **Doxygen** tags (`@entity`, `@brief`, `@snippet`, etc.) to structure the documentation.
- Once synthesized, remove the entry from the capture queue.

### 2. Doxygen-Lite Standards
- Always include an `@entity` and `@brief` tag at the top of entity files.
- Mirror critical code logic using `@snippet` blocks.
- Highlight architectural notes with `@note` or `@warning`.

### 3. Verification
- Ensure `wiki/index.md` is updated with any new entities.
- Maintain a 1:1 parity between code modules and wiki documentation.
