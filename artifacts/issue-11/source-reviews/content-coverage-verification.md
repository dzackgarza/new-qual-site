# Direct source-to-target content checks

Written by the session that ran the checks, so it is evidence for a reviewer rather than the review itself.
Every check here is re-runnable against the pinned sources.

## What was checked, and what that is worth

The checks below compare **source statements with target card bodies**. They do not compare a copied file with the file it was copied from: that measures the copy operation, not the migration, and no such comparison appears here.

Pinned source revisions:

- `qual-wiki` `3fe1f58fdf800209c5ad243c91411bc0ee40cc7c`

- `qual-review-and-solutions` `590a8929b2326cc770a246e934ab36fb30b0c7ab`

- `make-me-a-qual` `beba581e5b32f54ff469ed603a0885d51591e5fc`

- `Analysis-Qual-Compendium` `15168d8df736c3bc99be57e8b48e0675e0cd4e2f`

- `math-flashcards` tracked baseline `69cecc401981fb2f897a6a3c29feb869d811013c`

Target revision: `9d698120`.

## make-me-a-qual: all 508 statements, verbatim

Every statement in the pinned `Combined_Questions.yaml` was matched to its occurrence card body.
461 are identical after whitespace normalization.
The other 47 differ only in pandoc presentation encodings that preserve the mathematics: `\(x\)` to `$x$`, `\[x\]` to `$$x$$`, the `<!-- -->` list separator, typographic quotes, `—` to `---`, and `` `\begin{align*}…\end{align*}`{=tex} `` raw-TeX inline.

The last of those was checked against the build's own reader dialect rather than assumed: pandoc emits it as `<span class="math display">`, which the site's MathJax typesets.
It is display math, not a code span.

No statement was missing, truncated, or altered.

## The 103 `ambiguous-exact` rows are not a semantic ambiguity

M5 recorded these as an unresolved ambiguity.
They are not.

Every one of the 103 has exactly one distinct candidate card ID, and the chosen `problem_id` is that ID. The ambiguity the importer recorded was over which *file path* held the card — `corpus/canonical/` versus `corpus/qrs/` — not which statement or which card.
The statements matched exactly.
The label is an importer artifact.

## The 8 occurrence rows naming a card with no file are already repointed

All eight are G3 collapse retirements with recorded survivors in `sources/g3-collapse-map.jsonl`, and all eight occurrence files already point at the surviving card, each of which exists.
The retired identifier survives only in the historical import record, which is where it belongs.
There are no dangling references in the corpus.

## Analysis-Qual-Compendium: 68 problems, 68 distinct cards

All 68 problems parse from the pinned `main.tex` and pair positionally with the 68 occurrence records, which name 68 distinct existing cards.
Source content-word coverage of the mapped card is at least 0.90 for 63 of them and at least 0.75 for all 68.

The two weakest were read directly rather than left at a score.
`Spring 2017 #3` -> `P-4RXD2` is the same problem; its residual is TeX macro spelling.
The apparent second weak case was an artifact of keying on exam term: `main.tex` numbers two Spring 2017 problems "#5", which the occurrence map records faithfully as two records.

## math-flashcards: 285 deck cards

285 source cards across the 17 transformed decks, all 285 present in the import ledger: 246 migrated and 39 dropped as duplicates.
Every migrated card has an existing target whose body carries the source back text.
Four differ only in math spacing or a terminal period.

## make-me-a-qual authored Markdown: 522 statements

522 routing records cover all 18 source files, no file is unrouted, and every routed card exists.
Content-word coverage against the corpus is 1.00 for 16 files and 0.98/0.99 for two; the only absent token in those two is `ish`, from the section title "Spring 2016 (Neil-ish)".

## qual-wiki and qual-review-and-solutions: 398 authored files

These two repositories migrate authored Markdown by splitting each source file into a `wiki/` page plus extracted cards.
398 ledger rows carry the evidence "re-materialises to wiki/X.md + N cards, all in corpus", for 3,637 cards.
The wiki page keeps the source text and prepends `[[CARD]]` references, so the claim is directly testable.

Reassembling each page with the bodies of every card it references, and comparing with the pinned source, 230 of 398 reproduce every source token.
The 168 shortfalls are dominated by `\work`, `\todo`, `\done` and `$\work$` heading markers — authoring status macros the import discards by design — and by Obsidian pasted-image filenames.

The residue is not a migration question but a linking one.
Where a page no longer reaches a statement, deduplication moved that statement to a canonical card the page does not reference.
The Cauchy-Riemann statement missing from `Complex Analysis/UGA Question (no solutions)/sections/001_RealVariables.md` is present in five corpus files, `P-TH3WN` among them.

Asking the migration question instead — is each source token present **anywhere** in `corpus/` or `wiki/` — **377 of the 398 files are complete**. The other 21 lose between one and eight tokens each:

| absent token | source of it |
| --- | --- |
| `clean`, `sketchy`, `mess`, `finish`, `flesh`, `lost`, `work`, `someone`, `concepts` | authoring status notes |
| `definitions` (8) | heading status-macro residue |
| `projects` | the `Projects/Quals/Algebra/image/...` prefix of image paths |
| `7cconformal`, `20map`, `20exercises`, `onenote` | URL percent-encoding and link-scheme fragments |

Not one is a problem, solution, definition, or theorem.
No mathematics from either repository is absent from the target.

## Where the authored source actually sits

Native retention under `assets/` is the plan's fallback for content that cannot be represented completely by a card or page.
It is not a stronger form of migration, and a row holding a native copy is not better evidenced than a row holding a card.

Measuring the reverse direction — how much of each authored source file's text appears in `corpus/` or `wiki/` — puts the transformed rows ahead of the retained ones:

| source held as | files | >=0.95 | >=0.80 | <0.80 |
| --- | ---: | ---: | ---: | ---: |
| cards only (make-me-a-qual, math-flashcards, compendium) | 47 | 45 | 2 | 0 |
| natively under `assets/` | 568 | 470 | 87 | 11 |

The 11 low files are `preamble.tex`, `macros_envs.tex`, `qual_progress.md`, two math-flashcards repository documents, and six reading/orals decks outside the qual corpus.
None is a qual problem, solution, or theory statement.

## Result

No missing source content was found by any of these checks.

They now cover statement-level presence for all five source repositories: the five transformed collections above, and the 398 authored-Markdown files of qual-wiki and qual-review-and-solutions.

They do not certify complete migration, for two reasons that a fresh reviewer should test rather than inherit.
Presence of every content token is weaker than a reading of every statement; it can miss a reordering or a truncation that reuses the same vocabulary.
And whether the qual-wiki and QRS material is *organized into* the wiki is a separate question from whether it is present — that is the project's stated unfinished work, not a migration gap.
