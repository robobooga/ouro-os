@entity builder
@brief Static site generator that converts a wiki directory into a browsable HTML dashboard with navigation sidebar.

## Overview

`ouro-webui/builder.py` walks a wiki directory (default: `ouro/wiki/`), processes Doxygen tags via regex, renders Markdown to HTML using `mistune`, and writes output to `ouro-webui/dist/`, preserving the wiki's subdirectory structure. Each page includes a sidebar with links to all wiki pages grouped by section (Entities, Decisions, Patterns, Maps).

@note The web UI is a separate concern from the core skill and is not included in the distributed `ouro/` package. See [ADR-004](../decisions/ADR-004-webui-as-separate-concern.md).

## Functions

### `parse_doxygen_tags(text)`

Applies regex substitutions to convert Ourobor Doxygen tags into HTML elements before Markdown rendering.

| Tag | Output Element |
|-----|----------------|
| `@entity <name>` | `<div class="entity-header">Entity: name</div>` |
| `@brief <text>` | `<p class="brief"><strong>Brief:</strong> text</p>` |
| `@note <text>` | `<div class="note"><strong>Note:</strong> text</div>` |
| `@warning <text>` | `<div class="warning"><strong>Warning:</strong> text</div>` |

### `build_nav_tree(wiki_dir)`

Pre-collects all wiki `.md` files (excluding skip list) and returns a list of section dicts `{title, pages}` ordered by `SECTION_ORDER`. Each page entry is `{label, href}` where `href` is the relative path from `dist/` root.

### `process_file(wiki_path, nav_tree, root_prefix)`

Reads a `.md` file, runs `parse_doxygen_tags()`, renders with `mistune`, and returns the final HTML string rendered through a Jinja2 template. Accepts `nav_tree` and `root_prefix` (e.g. `../` for subpages) so sidebar links resolve correctly from any depth. Runs inside a `ProcessPoolExecutor` worker.

### `build(wiki_dir=None)`

Accepts an optional `wiki_dir` path (defaults to `ouro/wiki/`). Skips `capture-queue.md` and `schema.md`, pre-builds the nav tree, then processes all other `.md` files with `root_prefix` set per file depth. Writes `.html` output to `ouro-webui/dist/` mirroring the source subdirectory structure.

## Known Issues

All previously documented issues have been resolved.

## Dependencies

```
mistune
jinja2
```

Install via `pip install -r ouro-webui/requirements.txt`.

## CLI Usage

```bash
cd ouro-webui

# Default: builds from ../ouro/wiki
python builder.py

# Custom wiki directory (e.g. this project's own wiki)
python builder.py --wiki-dir ../wiki

# Output: ouro-webui/dist/
```
