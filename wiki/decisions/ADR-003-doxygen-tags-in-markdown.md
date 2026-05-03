@entity ADR-003
@brief Custom Doxygen-style tags embedded in plain Markdown are the documentation protocol for all wiki files.

## Context

The wiki needs a documentation standard that satisfies two audiences simultaneously: human developers reading Markdown files directly in editors or on GitHub, and LLM agents parsing files for structured information. Additionally, `builder.py` needs a machine-readable hook to apply custom rendering beyond standard Markdown.

## Decision

Custom Doxygen-style tags (`@entity`, `@brief`, `@snippet`, `@note`, `@warning`, `@param`, `@return`) are embedded inline in standard Markdown files. These are not standard Doxygen — they are a lightweight convention unique to Ourobor OS.

`builder.py` uses regex substitution to convert tags into styled HTML before passing content to `mistune` for Markdown rendering.

## Alternatives Considered

- **Pure Markdown with headers only**: No structured signals for tooling. LLMs parse it fine, but the web UI would have no hook for semantic rendering without reinventing a tagging system.
- **Real Doxygen**: Requires a full Doxygen installation, produces XML or HTML rather than portable Markdown, and is far too heavy for a drop-in skill with zero tooling dependencies.
- **YAML frontmatter**: Well-supported and standard (Jekyll, Hugo, etc.), but frontmatter is per-file metadata — it can't tag individual sections like `@snippet` or `@warning` mid-document.
- **JSON sidecar files**: Maximum machine-readability, minimum human-readability. Violates the "dual-readability" principle directly.
- **HTML comments**: Invisible in rendered Markdown but readable by parsers. Too easy to accidentally break and provides no visual signal in raw file views.

## Trade-offs

- **Lost**: Standardization. These tags are not recognized by any existing tooling outside this project. A developer unfamiliar with the convention must read the schema to understand them.
- **Gained**: Zero dependencies for documentation itself. Files are readable in any Markdown viewer, on GitHub, and in any LLM context window. The system is extensible — new tags can be added to the schema without changing the file format.

## Rationale

The tags need to be readable by a human skimming a file on GitHub and by an LLM processing context. They also need to provide a rendering hook for the web UI. Inline Markdown with lightweight tags is the only approach that satisfies all three without introducing external tooling or breaking standard Markdown rendering.
