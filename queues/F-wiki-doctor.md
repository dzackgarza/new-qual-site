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

- [ ] wiki/algebra/appendices (index.md + appendix.md)
- [ ] wiki/topology/covering-spaces (index.md + covering-spaces.md)
- [ ] wiki/topology/cw-complexes (index.md + cw-complexes.md)
- [ ] wiki/topology/degree (index.md + fixed-points-and-degree.md)
- [ ] wiki/topology/surfaces (index.md + surfaces-and-manifolds.md)
- [ ] wiki/topology/workshops (index.md + topology-week-1-preliminaries.md)

### sibling-duplicate-titles (0)

Sibling pages sharing a title.

ok

### obsidian-embed-syntax (7)

Pages using Obsidian `![[...]]` embed syntax.

- [ ] wiki/algebra/workshops/algebra-week-2-finite-group-theory.md
- [ ] wiki/algebra/workshops/algebra-week-4-rings.md
- [ ] wiki/algebra/workshops/algebra-week-n-1-linear-algebra.md
- [ ] wiki/complex-analysis/workshops/complex-week-2-cauchy.md
- [ ] wiki/prelim/useful-tricks.md
- [ ] wiki/real-analysis/resources/problems.md
- [ ] wiki/real-analysis/resources/solutions.md

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

- [ ] wiki/complex-analysis/appendices/gauss-lucas-theorem.md
- [ ] wiki/prelim/useful-tricks.md
- [ ] wiki/real-analysis/undergraduate/riemann-integrability.md

## Authoring signals

These are facts about the file, not defects. A page with one section is a
chapter not yet written, not a page in the wrong place.
