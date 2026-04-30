Plan: Initialize Developer-Centric LLM Wiki

Objective
Establish a compounding, product-agnostic "LLM Wiki" system inside the ouro/wiki/ directory. This
system will serve as the persistent knowledge base for the project, maintained by the LLM
and curated by the developer.

Directory Structure
  - ouro/wiki/
      - index.md: The central hub/catalog.
      - schema.md: The operating manual (Rules of the Brain).
      - log/: Chronological context shifts (Session logs).
      - maps/: High-level mental models and data flows.
      - entities/: Documentation mirrored from the source code (1:1 with modules).
      - decisions/: ADRs (Architecture Decision Records).
      - patterns/: Abstracted architectural patterns.

Implementation Steps

Phase 1: Infrastructure
  1. Create ouro/wiki/schema.md: Define the philosophy, taxonomy, and maintenance protocols
    (Karpathy pattern).
  2. Create ouro/wiki/index.md: Initialize the hub with links to the new categories.
  3. Update CLAUDE.md: Add instructions to the LLM agent to enforce wiki maintenance as a
    core task.

Phase 2: Migration & Synthesis
  1. Migrate ouro/docs/PRD.md → ouro/wiki/entities/product.md.
  2. Migrate ouro/docs/ARCHITECTURE.md → ouro/wiki/entities/architecture.md (and link to Maps).
  3. Migrate ouro/docs/EXTRACTION.md → ouro/wiki/entities/extraction.md.
  4. Migrate ouro/docs/CHANGELOG.md → ouro/wiki/log/archive-changelog.md and start a new log format.
  5. Synthesize ouro/docs/DESIGN.md → ouro/wiki/entities/design-system.md and
    ouro/wiki/patterns/handy-notebook.md.
  6. Create ouro/wiki/decisions/ADR-001-async-job-strategy.md from ouro/docs/ASYNC_JOBS.md.

Phase 3: Cleanup
  1. Verify all "live" knowledge is in the ouro/wiki/ directory.
  2. Update the root INDEX.md or README.md to point to ouro/wiki/index.md.
  3. (Optional) Archive or delete the ouro/docs/ folder once synthesis is complete.

Verification
  - LLM can successfully "look up" a decision or entity in the ouro/wiki/.
  - The wiki reflects the latest code changes (e.g., Design System alignment).
  - The log/ contains today's work as the first entry.

Malleability Note
This structure is designed to be "Drop-in Ready." To use it in another project, simply copy
the ouro/ folder and reset the content while keeping schema.md.
