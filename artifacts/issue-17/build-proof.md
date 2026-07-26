# Issue 17 full vertical slice proof

Proof target: merged implementation `d6aa9713a519aed5471fd58680a750de4f2ee4b3`
and Pages provisioning repair
`7d04adbfa48198e0d1a591b8a1d2497d84b532ac` on `main`.

## Published traversal

The bounded reading path is:

1. `guide/GUIDE-ALGEBRA.html`
2. `guide/GUIDE-ALGEBRA/finite-groups.html`
3. `guide/GUIDE-ALGEBRA/actions-and-counting.html`
4. `guide/GUIDE-ALGEBRA/sylow-theory.html`
5. `guide/GUIDE-ALGEBRA/applications-and-problems.html`

`tests/test_invariants.py::test_corpus_layout_is_semantically_inert` proves the
five stable routes, ordered subject navigation, breadcrumbs, previous/next
links, the named finite-groups spine, problem/hint/solution ordering, separated
relation groups, Page/Card/Problem search labels, and equality between the
generator problem IDs and the SQLite problem catalog.

Exact-command result:

```text
uv run pytest tests/test_invariants.py::test_corpus_layout_is_semantically_inert -q
1 passed in 88.99s
```

## Clean build boundary

The clean build was run with a temporary `pandoc` PATH wrapper and
`/usr/bin/time`:

```text
PATH="<pandoc-wrapper>:$PATH" /usr/bin/time \
  -f 'wall_seconds=%e\nmax_rss_kib=%M' just build

5218 cards OK
wall_seconds=51.59
max_rss_kib=480416
```

The wrapper recorded exactly two descendant Pandoc invocations:

```text
--print-default-data-file=abbreviations
server --port 55847 --timeout 30
```

The port is ephemeral. The process boundary is one abbreviations lookup and one
persistent Pandoc server for the whole corpus build.

## Generated-site integrity

The preserved validator can be rerun with:

```text
uv run --with html5lib python artifacts/issue-17/validate-site build/quarto/_site
```

Result against the exact instrumented build:

```text
html_pages: 3480
html_parse_errors: 0
local_references: 31077
missing_local_targets: 0
missing_fragments: 0
qmd_links: 0
```

## Browser and visual proof

The real static artifact was served from `build/quarto/_site` and exercised in
Chrome at `375x812`, `768x900`, `1024x768`, and `1440x1000`.

The replay traversed all five reading pages at desktop and mobile widths, opened
the problem hint and solution states, checked the three relation groups, opened
typed search results, and generated three problems from the shared catalog.
It produced 25 preserved screenshots under `screenshots/`, with zero console
errors and zero page errors.

Manual inspection covered every screenshot. The inspected states include:

- the complete reading traversal and active subject navigation;
- desktop, tablet, and mobile content wrapping without horizontal overflow;
- collapsed, hint-open, and hint-plus-solution-open problem states;
- authored dependencies, derived appearances, and backlinks as distinct groups;
- Page/Card/Problem search labels;
- semantic list markup and typeset mathematics in the generated practice set.

## Production deployment

The GitHub Pages workflow completed successfully after the provisioning repair:

- workflow run:
  <https://github.com/dzackgarza/new-qual-site/actions/runs/30201392802>
- deployed site: <https://dzackgarza.github.io/new-qual-site/>

The deployed artifact was replayed in Chrome at `375`, `768`, `1024`, and
`1440` CSS pixels. The replay covered the same 25 reading, disclosure,
relations, search, and generator states described above, with zero console
errors and zero page errors. Every deployed-state screenshot was manually
inspected.

The remaining operational follow-up is issue 21, which tracks migration away
from the Node 20 action runtime warning emitted by otherwise successful Pages
runs: <https://github.com/dzackgarza/new-qual-site/issues/21>.

## Nonclaims

This proof covers the finite-groups vertical slice in issue 17. It does not
claim bulk editorial completion for other subjects, a redesign of the corpus
generator, or completion of the Node action-runtime migration tracked in issue
21.
