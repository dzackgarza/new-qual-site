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

- [x] wiki/algebra/appendices (index.md + appendix.md)
- [x] wiki/topology/covering-spaces (index.md + covering-spaces.md)
- [x] wiki/topology/cw-complexes (index.md + cw-complexes.md)
- [x] wiki/topology/degree (index.md + fixed-points-and-degree.md)
- [x] wiki/topology/surfaces (index.md + surfaces-and-manifolds.md)
- [x] wiki/topology/workshops (index.md + topology-week-1-preliminaries.md)

Not defects. Chapters not yet written. Per `AGENTS.md`: "Do not remove a thin or empty section."

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

### heading-or-wikilink-only-bodies (3)

Pages whose body is only headings or wikilinks, no prose.

- [x] wiki/complex-analysis/appendices/gauss-lucas-theorem.md
- [x] wiki/prelim/useful-tricks.md
- [x] wiki/real-analysis/undergraduate/riemann-integrability.md

Not defects. Chapters not yet written. Per `AGENTS.md`: "Do not remove a thin or empty section."

## Authoring signals

These are facts about the file, not defects.
A page with one section is a chapter not yet written, not a page in the wrong place.
