# Document queue F: Wiki doctor findings

Source: `just doctor`, against current wiki.

See `AGENTS.md`, "Two concerns, and the test that separates them".
A checker measures the file. What the file should say is a reading.

## Engineering defects

The build or the reader hits each of these. One checkbox each.

### unreadable-wiki-pages (0)

Pages the reader cannot parse.

ok

### empty-bodies (0)

Pages with no body.

ok

### order-at-least-100001 (0)

Pages with no position in their folder.

ok

### one-markdown-child-directories (6)

Directories with one child `.md` file besides `index.md`.

Not defects. Each directory has a content page with real prose (58–377 lines). The directory structure is a navigation choice, not a content gap.

### sibling-duplicate-titles (0)

Sibling pages sharing a title.

ok

### obsidian-embed-syntax (0)

Pages using Obsidian `![[...]]` embed syntax.

All 41 embeds across 7 pages converted to standard `![](...)` syntax (2026-08-31).

### notion-so-or-notion-site-urls (0)

ok

### hash-todo-markers (0)

ok

### tags-colon-lines (0)

ok

### hash-resources-only-lines (0)

ok

### task-list-item-lines (0)

ok

### heading-or-wikilink-only-bodies (0)

Pages whose body is only headings or wikilinks, no prose.

All three pages now have prose:
- `gauss-lucas-theorem.md`: theorem statement, proof, consequences
- `useful-tricks.md`: prose explaining the integration-by-parts and series images
- `riemann-integrability.md`: Lebesgue criterion, consequences, counterexample

## Authoring signals

These are facts about the file, not defects.
A page with one section is a chapter not yet written, not a page in the wrong place.
