# Queue F: Wiki Doctor Findings

Current findings from `just doctor` (2026-08-31):

| Finding | Count | Status |
|---------|-------|--------|
| one-markdown-child-directories | 5 | Structural — each has real content |
| heading-or-wikilink-only-bodies | 0 | Resolved |
| obsidian-embed-syntax | 0 | Resolved |

## One-child directories (structural, not defects)

| Directory | Child page | Lines | Status |
|-----------|-----------|-------|--------|
| `wiki/topology/covering-spaces/` | `covering-spaces.md` | 377 | Well-organized, substantial |
| `wiki/topology/cw-complexes/` | `cw-complexes.md` | 200+ | Well-organized, substantial |
| `wiki/topology/degree/` | `fixed-points-and-degree.md` | 100+ | Prose added (Brouwer→Lefschetz→Borsuk-Ulam→Hairy Ball chain) |
| `wiki/topology/surfaces/` | `surfaces-and-manifolds.md` | 300+ | Well-organized, substantial |
| `wiki/topology/workshops/` | `topology-week-1-preliminaries.md` | 80+ | Tube lemma prose added, qual questions contextualized |

These are dedicated topic pages with real content. The one-child structure is a navigation choice — each topic gets its own directory with an index and a main page.

## Resolved this session

- **Algebra appendices** — content redistributed into `groups/characteristic-subgroups.md`, expanded `groups/series-and-solvability.md`, and added Gorenstein to `rings-and-ideals/which-kind-of-ring.md`. Directory deleted.
- **Heading-only bodies** — `gauss-lucas-theorem.md`, `riemann-integrability.md`, `useful-tricks.md` all written with prose.
- **Obsidian embeds** — 41 `![[...]]` converted to `![](...)` across 7 pages.
