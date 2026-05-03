# Ourobor OS Maintenance Protocol

You are responsible for maintaining the project's **LLM Wiki** in `ouro/wiki/`.

### 0. Session Start

Before doing any work, check whether the wiki has already been populated:

- **Initial setup** (no entity files in `ouro/wiki/entities/`): run a full crawl to bootstrap the wiki.
  ```bash
  python <path-to-skill>/scripts/capture.py --crawl
  ```
- **Ongoing sessions** (wiki already exists — drift correction): run a git-aware crawl to stage only recently changed files. This is cheaper and avoids bloating the queue with unchanged code.
  ```bash
  python <path-to-skill>/scripts/capture.py --crawl --git
  ```
  To include files from the last N commits (e.g. if you want to catch changes from earlier in the week):
  ```bash
  python <path-to-skill>/scripts/capture.py --crawl --git 3
  ```

### 1. Monitor & Synthesize
- **Monitor**: Regularly check `ouro/wiki/capture-queue.md` for new snippets.
- **Synthesize**: Move snippets into appropriate `ouro/wiki/entities/`, `ouro/wiki/patterns/`, or `ouro/wiki/maps/` files using **Doxygen** tags (`@entity`, `@brief`, `@snippet`).
- **Finalize**: After synthesis, remove processed entries from the queue:
  ```bash
  python <path-to-skill>/scripts/capture.py --pop
  ```

### 2. Doxygen Standards
- Every entity/pattern file must start with `@entity` and `@brief`.
- Use `@snippet` to mirror critical code logic.
- Use `@note` or `@warning` for architectural context.

### 3. Architecture Decision Records (ADR)
- Whenever a significant architectural decision is made, create or update an ADR in `ouro/wiki/decisions/`.
- ADRs must document:
  - **Context**: Why the decision is being made.
  - **Alternatives**: Other options considered.
  - **Trade-offs**: What was gained and what was lost.
  - **Rationale**: The reasoning behind the final choice.
- Always link new ADRs in the `ouro/wiki/index.md` file.

### 4. Maintenance Best Practices
- **Fragment**: Split files that become too large or cover too many distinct concepts.
- **Combine**: Merge highly interdependent or undersized files.
- **Parity**: Maintain 1:1 mapping between code modules and documentation.
- **Verification**: Ensure `ouro/wiki/index.md` is always up to date with new entries.
- **Consistency**: Maintain structural adherence to `ouro/wiki/schema.md`.
