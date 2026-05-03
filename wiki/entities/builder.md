@entity builder
@brief Static site generator that converts ouro/wiki/ Markdown into a browsable HTML dashboard.

## Overview

`ouro-webui/builder.py` walks the `ouro/wiki/` directory, processes Doxygen tags via regex, renders Markdown to HTML using `mistune`, and writes output to `ouro-webui/dist/`, preserving the wiki's subdirectory structure.

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

### `process_file(wiki_path)`

Reads a `.md` file, runs `parse_doxygen_tags()`, renders with `mistune`, and returns the final HTML string rendered through a Jinja2 template. Runs inside a `ProcessPoolExecutor` worker.

### `build()`

Walks `ouro/wiki/`, skips `capture-queue.md` and `schema.md`, processes all other `.md` files, writes `.html` output to `ouro-webui/dist/` mirroring the source subdirectory structure.

## Known Issues

@warning **Template inheritance is broken.** `page.html` uses `{% extends "base.html" %}` and `{% block content %}`, but `base.html` has no `{% block %}` tags — it renders `{{ content }}` directly. Jinja2 template inheritance requires `{% block content %}{% endblock %}` in the parent. Running `build()` currently fails silently or throws a rendering error.

@warning **Dead code in `build()`.** Lines 53–55 compute a directory condition but the body is `pass` — it does nothing. A leftover from an abandoned refactor.

@warning **No inter-page navigation.** The sidebar in `base.html` contains only a static "Home" link. Generated pages have no links to each other. The output is a pile of disconnected HTML files.

## Dependencies

```
mistune
jinja2
```

Install via `pip install -r ouro-webui/requirements.txt`.

## CLI Usage

```bash
cd ouro-webui
python builder.py
# Output: ouro-webui/dist/
```
