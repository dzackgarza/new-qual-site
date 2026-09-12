# Corpus authorial stance audit

Scope: reader-facing authored corpus cards, wiki pages, publication introductions,
and shared site copy. Apply CONTRIBUTING.md's STANCE policies through full-text
reading. Original mathematical problem instructions are not study prescriptions.
External source documents retain their authored text; this audit concerns the
site's authored representations and commentary.

## Coverage owners

- [Wiki file coverage](tone-audit-wiki.md).
- [Theory and standalone problem file coverage](tone-audit-theory-problems.md).
- [Collection and contained problem file coverage](tone-audit-collections.md).

Unchecked file entries in those records remain required work. Newly added or
concurrently changed files require reading before whole-corpus completion can
be asserted. A phrase search cannot close a file's coverage entry.

## Publication and shared-copy coverage

- [x] `publications/algebra-guide.yaml`: read all titles and ledes; replaced exam
  rankings, memorization instructions, unsupported generalizations, and narrative
  metaphors with mathematical statements. Preserved problem memberships and links.
- [x] `publications/real-analysis-guide.yaml`: read all titles and ledes; removed
  universal exam claims and reader prescriptions, stated the relevant hypotheses.
- [x] `publications/complex-analysis-guide.yaml`: read all titles and ledes;
  replaced the prescribed reading path and exam rhetoric with mathematical content.
- [x] `publications/topology-guide.yaml`: read all titles and ledes; removed
  difficulty judgements, reading instructions, and claims about exam performance.
- [x] `publications/prelims-guide.yaml`: read all titles and ledes; removed
  claims about examiner intentions and diagnoses of candidates' understanding.
- [x] `publications/applied-algebra-guide.yaml`: read all titles and ledes;
  replaced sweeping computational promises and imposed sequence with results.
- [x] `publications/workshops-guide.yaml`: read all titles and ledes; described
  the worksheet subjects without prescribing how to traverse them.
- [x] `tools/qualc/emit.py`: read page-composition prose for home, source,
  problem, collection, guide, redirect, and error pages. Replaced home-page
  reading commands, internal reorganization commentary, and the unsubstantiated
  claim that every partial collection is a prefix of its source.
- [x] `tools/qualc/static_site.py`: read reader-facing shell, navigation,
  metadata, source-link, search, and footer text. No stance change required.
- [x] `site/app.js`: read complete source; displayed search results use authored
  titles and excerpts. No additional editorial prose requiring revision.
- [x] `assets/scripts/catalog-tables.js`: read complete source; action labels
  describe the interface operation. No stance change required.
- [x] `README.md`: read complete document; site navigation and contributor
  procedures do not assign readers a study programme. No stance change required.

Publication changes were checked by parsing both versions and comparing all
fields except their authored ledes. Membership, order, topics, and identifiers
are unchanged. Final render and link checks follow the remaining corpus edits.
