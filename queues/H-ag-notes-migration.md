# ag-notes migration queue

Substantive migration is incomplete.
The open rows identify omitted statements, prompts, proof steps, examples, diagrams and source errors needing correction.

This queue owns the remaining migration work.
[Source file inventory](ag-notes-source-files.tsv) records every file in the deployed tree, including aliases, detached images, reference PDFs and renderer files.
It records bytes, paths and SHA-256 only; it makes no mathematical dispositions.

## Source and comparison boundary

- Source: `/var/www/ag_notes/` on `zack@159.223.102.204`, copied on 2026-09-12. Paths in the queue are relative to that root unless stated otherwise.
  Preserve this source while any content or source-repair row remains open.

- Target: authored `corpus/` and `wiki/` in this repository.
  The comparison used their actual bodies, not collection completion fields or previous migration reports.
  Target reference revision: `a82fbded3bb880564fd041eff5b93f37fdfd0248`. The comparison concerns source transfer, not unrelated assertions added to target cards.

- HTML comparison includes displayed mathematics, footnotes, hints, worked solutions stored in HTML `title` attributes, and both case-sensitive Definitions revisions.
  Image comparison includes local PNGs, detached figures and the externally hosted Mathpix crops.
  Linked quiver data can preserve a diagram whose SVG file is absent.

- A search-based omission means no counterpart was found in the named targets and the corpus/wiki searches.
  It is not a proof that no equivalent theorem exists anywhere.
  A general theorem can preserve an asserted consequence, but an unrelated example or an unsolved exercise does not preserve a source proof.

- The later Markdown vault `/var/www/Notes/Class_Notes/2022/Fall/Orals/` is a distinct source revision.
  Its later additions are listed separately below; the deployed-site comparison does not certify that vault.

## Statuses

| Status | Meaning | Next action |
| --- | --- | --- |
| `missing` | A readable source unit has no located substantive target. | Write or integrate the named content after checking related targets. |
| `partial` | Some content survives; the row names omitted content, source errors, target errors or missing source annotations. | Complete or correct the named parts. Retain sound existing work. |
| `source-repair` | Source content is missing, illegible, truncated or too incomplete to interpret safely. | Recover the source or resolve its exact ambiguity before authorship. |
| `migrated` | The stated source unit has a substantive target, and this comparison identified no remaining transfer work in it. | Use the cited source and target if the disposition is challenged. This is not a certification of unrelated target assertions. |
| `reference-only` | The file is retained reference material, a syllabus, navigation or build infrastructure. | Preserve the useful reference or historical source role specified in the row. It does not count as authored mathematics. |
| `private` | Personal schedules, progress records or local application data. | Keep in private source history; do not publish as study content. |
| `unreviewed` | A separately named source revision has not received this comparison. | Read it before assigning a transfer disposition. |

## Order of work

Work through the source sections below in order, one named item at a time.
Within a partial page, its explicit remaining statements and proof steps are the checklist.
Source-repair entries can proceed independently when recovery does not depend on another item.
Move a row to migrated only with the actual source-to-target correspondence, including hypotheses, subparts, arguments and mathematical diagrams.
Keep unfinished source arguments visibly unfinished until corrected; copying them is not a finished solution.

Mixed pages have separate content dispositions: private planning does not hide a mathematical question, and a reference list does not hide an exercise.
The image and diagram sections identify the same page's supporting source material, not additional copies of the mathematical work.

## Source sections

| Queue section | Content |
| --- | --- |
| [Study guides and Definitions](ag-notes/guides.md) | Questions, definition lists, proof sketches, resources, and external diagram content. |
| [Reading notes and Hartshorne III–IV](ag-notes/reading.md) | McKernan, Hartshorne reading notes, Fulton notes/figures, and chapter III–IV exercises. |
| [Worked problems and Hartshorne I–II](ag-notes/exercises.md) | Gathmann, Vakil, homework, native TeX, and chapter I–II exercises. |
| [Images and Hartshorne V](ag-notes/images-and-surfaces.md) | Image-only theorems, syllabi, reference PDFs, and chapter V exercises/figures. |
| [Navigation, private records and infrastructure](ag-notes/infrastructure.md) | Generated pages, personal tracking, application state, and source build files. |

## Source recovery and retained source files

| Source | Status | Evidence and next action |
| --- | --- | --- |
| `attachments/Pasted image 20220914124903.png` | migrated | Recovered byte source: `/var/www/notes_site/attachments/Pasted image 20220914124903.png` on the same host. It states that $\CC[X]$ is an integral domain iff $I(X)$ is prime iff $X$ is irreducible; `P-AGXVARCOORDDOMAIN` carries that statement as its solution. |
| `attachments/Pasted image 20220314125429.png`, `attachments/Pasted image 20220213162548.png`, `attachments/Pasted image 20220208145954.png` | migrated | Recovered from `/var/www/notes_site/attachments/` on the same host and read. `20220314125429` (Schemes guide) is the example of the regular function $5/6$ on $D(6) \subseteq \Spec \ZZ$ and its values at $(0)$, $(5)$ and $(11)$: the `D(6)` example on `FE-O12TX`. `20220213162548` (Cohomology guide, under the fine-sheaf prompt) defines flabby, soft, c-soft and fine sheaves: `D-COHFLQ` (flasque/flabby) and `D-SHFFINE`, which now defines c-soft sheaves. `20220208145954` (Cohomology guide, the unfinished "In general" slogan) is the lemma that $\operatorname{Ext}^0$, $\operatorname{Ext}^1$, $\operatorname{Ext}^2$ of $\Omega_{X/B}$ into $\OO_X$ give infinitesimal automorphisms, first-order deformations and obstructions to lifting $n$th-order deformations: `T-DEFEXT`, whose obstruction statement now covers lifting from order $n$ to order $n+1$ for every $n$. |
| `500_Extra Problems/Gathmann Exercises/figures/image_2020-09-01-10-43-00.png` | migrated | Original context recovered from `/var/www/Notes/Class_Notes/2020/Fall/Algebraic Geometry/sections/2020-09-01.md` (lines 180–193) on the same host: the lecture example of the $xy$-plane $V(z)$ and the parallel line $V(x, z-1)$ through $(0,0,1)$, with $I(X) = (z)(x, z-1) = (xz, z^2-z)$ and the product decomposition of $\CC[X]$. It illustrates no Gathmann exercise. Target: `FE-VARDISJUNION`, with the figure at `assets/algebraic-geometry/varieties/plane-and-disjoint-parallel-line.png` (labels as drawn: $X_1$ the line, $X_2$ the plane), the comaximality argument for intersection equals product, and the Chinese-remainder decomposition; transcluded on `wiki/algebraic-geometry/varieties/the-dictionary.md`. |
| `500_Extra Problems/Gathmann Exercises/problems.pdf` | partial | The full PDF contains the same dated problem sets and arguments as `problems.tex`; no PDF-only mathematical unit was found. Remaining mathematical work is named in the worked-source section. The PDF, editable TeX and extraction are preserved at commit `7eafedfc04579791477d2463cd35548ad398c9c9`, under `assets/attachments/intermediate/ag-notes-native/` and `assets/attachments/intermediate/ag-notes-gathmann.md`. Use the TeX for formulas: the extraction drops the Lagrange product exclusion, changes an index inequality, loses `dim` in 2.33 and loses words and arrows in Proposition 5.0.1. |
| `.nojekyll` | reference-only | Empty deployment-control file. No mathematical payload. |
| Later vault `/var/www/Notes/Class_Notes/2022/Fall/Orals/` | unreviewed | Separate, later source revision, with November/December additions absent from the deployed tree. It needs its own direct comparison before retirement. Former source pointers remain recoverable from Git history at `a82fbded3bb880564fd041eff5b93f37fdfd0248`; historical paths are `wiki/algebraic-geometry/PLAN.md`, `assets/algebraic-geometry/MANIFEST.md`, and `artifacts/algebraic-geometry/semantic-transcription-audit-ledger.md`. Their dispositions are not evidence. This queue adopts none of their completion claims. |

## File aliases and retention evidence

The source-file TSV is the complete physical inventory of the deployed snapshot.
Equal SHA-256 values identify byte-identical files only.
Read the content rows for mathematical equivalence and remaining work.

- The January theorem crops occur under `attachments/`, `0_Study Guides/attachments/` and `0_Study Guides/figures/`. Their content dispositions apply to each byte-identical alias.

- The March/May crops and reference PDFs occur under both attachment directories.
  The October syllabus crops occur under root `attachments/`.

- The September theorem crops also occur directly at the source root.
  The content rows name their attachment aliases.

- The original cone and quadric-ruling figures survive byte-identically as `assets/algebraic-geometry/varieties/affine-cone-over-curve-in-p2.png` and `quadric-surface-in-p3-two-rulings.png`. The plane/surface singularity figures survive as `assets/algebraic-geometry/curves-and-surfaces/plane-curve-singularities-node-cusp-tacnode.png` and `surface-singularities-conical-double-line-pinch.png`. Their missing use in the exercise cards remains in the Hartshorne rows.

- The resources PDFs are preserved byte-for-byte.
  The full document, rather than a preview image or a migration label, is the retained reference.

- [External Definitions images](ag-notes-external-images.tsv) gives the exact URLs and downloaded file hashes in source order.
  These readable diagrams and text fragments have mathematical dispositions in the Definitions section.

Source counts, previous task tags, title similarity and the existence of a target card do not close a row.
A source page can be retired only after its actual content has the stated target or an explicit reference/private disposition.
