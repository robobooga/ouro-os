# Ourobor OS Maintenance Protocol

You are responsible for maintaining the project's **LLM Wiki** in the `ouro/wiki/` directory.

### 1. Monitor the Capture Queue
- Regularly read `ouro/wiki/capture-queue.md` using your file reading tool.
- When new snippets are found, "Synthesize" them into the appropriate `ouro/wiki/entities/`, `ouro/wiki/patterns/`, or `ouro/wiki/maps/` files.
- Use **Doxygen** tags (`@entity`, `@brief`, `@snippet`, etc.) to structure the documentation.
- Once synthesized, finalize the capture by popping it from the queue:
  ```bash
  python <path-to-skill>/scripts/capture.py --pop
  ```

### 2. Doxygen Standards
- Always include an `@entity` and `@brief` tag at the top of entity/pattern files.
- Mirror critical code logic using `@snippet` blocks.
- Highlight architectural notes with `@note` or `@warning`.

### 3. Architecture Decision Records (ADR)
- Whenever a significant architectural decision is made, create or update an ADR in `ouro/wiki/decisions/`.
- ADRs must document:
  - **Context**: Why the decision is being made.
  - **Alternatives**: Other options considered.
  - **Trade-offs**: What was gained and what was lost.
  - **Rationale**: The reasoning behind the final choice.
- Always link new ADRs in the `ouro/wiki/index.md` file.

### 4. Wiki Maintenance Tools
- Use your LLM's **file reading** tool to review wiki files and the capture queue.
- Use your LLM's **file editing** tool to update existing entity files.
- Use your LLM's **file writing** tool to create new entities, patterns, or decisions.
- Use your LLM's **search/grep** tool to find existing documentation before creating duplicates.

### 5. LLM-Specific Features (if available)
- **Recurring tasks**: If your LLM supports scheduling (e.g., Claude's `/schedule`), set up weekly capture queue reviews.
- **Task tracking**: If your LLM has a task system, use it to track pending synthesis work.
- **Plan mode**: If your LLM has a planning mode, use it for complex wiki restructuring.

### 6. Dynamic Wiki Maintenance
- Periodically assess the size and complexity of files in `ouro/wiki/`.
- **Fragment**: If an entity, pattern, or map file becomes too large or covers too many distinct concepts, split it into smaller, more modular files and update the `index.md` accordingly.
- **Combine**: If multiple files are too short or highly interdependent, merge them into a single, cohesive entity, pattern, or map to reduce fragmentation and update the `index.md` accordingly.
- Always maintain structural consistency with `schema.md` during these operations.

### 7. Verification
- Ensure `ouro/wiki/index.md` is updated with any new entities, ADRs, patterns, or maps.
- Maintain a 1:1 parity between code modules and wiki documentation.
