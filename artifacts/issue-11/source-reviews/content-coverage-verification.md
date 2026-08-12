# Direct source-to-target content checks

This is a migration record, not an M4 or M5 review record.
The session that produced it read the prior completion narratives first, so it cannot serve
as an independent review under invariants 11 and 15.
It supplies raw evidence for a later independent reviewer.

## What was checked, and what that is worth

The checks below compare **source statements with target card bodies**.
They do not compare a copied file with the file it was copied from: that measures the copy
operation, not the migration, and no such comparison appears here.

Pinned source revisions:

- `qual-wiki` `3fe1f58fdf800209c5ad243c91411bc0ee40cc7c`
- `qual-review-and-solutions` `590a8929b2326cc770a246e934ab36fb30b0c7ab`
- `make-me-a-qual` `beba581e5b32f54ff469ed603a0885d51591e5fc`
- `Analysis-Qual-Compendium` `15168d8df736c3bc99be57e8b48e0675e0cd4e2f`
- `math-flashcards` tracked baseline `69cecc401981fb2f897a6a3c29feb869d811013c`

Target revision: `9d698120`.

## make-me-a-qual: all 508 statements, verbatim

Every statement in the pinned `Combined_Questions.yaml` was matched to its occurrence card
body. 461 are identical after whitespace normalization. The other 47 differ only in pandoc
presentation encodings that preserve the mathematics: `\(x\)` to `$x$`, `\[x\]` to `$$x$$`,
the `<!-- -->` list separator, typographic quotes, `—` to `---`, and
`` `\begin{align*}…\end{align*}`{=tex} `` raw-TeX inline.

The last of those was checked against the build's own reader dialect rather than assumed:
pandoc emits it as `<span class="math display">`, which the site's MathJax typesets. It is
display math, not a code span.

No statement was missing, truncated, or altered.

## The 103 `ambiguous-exact` rows are not a semantic ambiguity

M5 recorded these as an unresolved ambiguity. They are not.

Every one of the 103 has exactly one distinct candidate card ID, and the chosen
`problem_id` is that ID. The ambiguity the importer recorded was over which *file path*
held the card — `corpus/canonical/` versus `corpus/qrs/` — not which statement or which
card. The statements matched exactly. The label is an importer artifact.

## The 8 occurrence rows naming a card with no file are already repointed

All eight are G3 collapse retirements with recorded survivors in
`sources/g3-collapse-map.jsonl`, and all eight occurrence files already point at the
surviving card, each of which exists. The retired identifier survives only in the
historical import record, which is where it belongs. There are no dangling references in
the corpus.

## Analysis-Qual-Compendium: 68 problems, 68 distinct cards

All 68 problems parse from the pinned `main.tex` and pair positionally with the 68
occurrence records, which name 68 distinct existing cards. Source content-word coverage of
the mapped card is at least 0.90 for 63 of them and at least 0.75 for all 68.

The two weakest were read directly rather than left at a score. `Spring 2017 #3` ->
`P-4RXD2` is the same problem; its residual is TeX macro spelling. The apparent second
weak case was an artifact of keying on exam term: `main.tex` numbers two Spring 2017
problems "#5", which the occurrence map records faithfully as two records.

## math-flashcards: 285 deck cards

285 source cards across the 17 transformed decks, all 285 present in the import ledger:
246 migrated and 39 dropped as duplicates. Every migrated card has an existing target whose
body carries the source back text. Four differ only in math spacing or a terminal period.

## make-me-a-qual authored Markdown: 522 statements

522 routing records cover all 18 source files, no file is unrouted, and every routed card
exists. Content-word coverage against the corpus is 1.00 for 16 files and 0.98/0.99 for
two; the only absent token in those two is `ish`, from the section title
"Spring 2016 (Neil-ish)".

## Where the authored source actually sits

Native retention under `assets/` is the plan's fallback for content that cannot be
represented completely by a card or page. It is not a stronger form of migration, and a row
holding a native copy is not better evidenced than a row holding a card.

Measuring the reverse direction — how much of each authored source file's text appears in
`corpus/` or `wiki/` — puts the transformed rows ahead of the retained ones:

| source held as | files | >=0.95 | >=0.80 | <0.80 |
| --- | ---: | ---: | ---: | ---: |
| cards only (make-me-a-qual, math-flashcards, compendium) | 47 | 45 | 2 | 0 |
| natively under `assets/` | 568 | 470 | 87 | 11 |

The 11 low files are `preamble.tex`, `macros_envs.tex`, `qual_progress.md`, two
math-flashcards repository documents, and six reading/orals decks outside the qual corpus.
None is a qual problem, solution, or theory statement.

## Result

No missing source content was found by any of these checks.

They do not certify complete migration. What they cover is statement-level presence for the
five transformed collections. Whether the qual-wiki and QRS authored material is
*organized into* the wiki is a separate question, and it is the project's stated unfinished
work rather than a migration gap.
