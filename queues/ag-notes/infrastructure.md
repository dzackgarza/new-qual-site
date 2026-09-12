# Navigation, private records and infrastructure

Source root: `/var/www/ag_notes/`. These rows cover source navigation, private records and renderer files.

| Physical source path or exact recursive family | Disposition | Content and destination |
| --- | --- | --- |
| `index.html` | reference-only | Links to definitions, the oral plan, practice questions, and generated completed/to-work problem lists. No independent mathematical text. The useful navigation belongs to `wiki/algebraic-geometry/index.md` and the current Hartshorne collection; the old tagged lists provide no migration evidence. |
| `900_Changelog.html` | reference-only | Dated linked-page edit history. No independent mathematics. Preserve only in source history; the current source collections provide reader navigation. |
| `0_Study Guides.html` | reference-only | Generated guide menu. The current algebraic-geometry wiki index provides the useful destination. |
| `Fulton.html` | reference-only | Generated menu to the Fulton chapter notes. The underlying pages are covered by the reading-source audit; keep their destinations, not a second menu. |
| `unresolved links output.html` | reference-only | Historical broken-wikilink diagnostic: target labels and originating Markdown paths, without mathematical statements. Preserve in source history. Its missing-image references require reconciliation with the asset audit, as specified below. |
| `IW-Queues.html` | reference-only | Generated child link to the study schedule. No mathematics. Source history is the destination. |
| `IW-Queues/queue.html` | private | Personal spaced-repetition priorities, intervals, next-review dates, and linked note names. No mathematical statements. Preserve privately with source history. |
| `progress.html` | private | Historical personal study progress table. No mathematical statements. Preserve privately; these counts cannot establish migration completeness. |
| `-/all.html`; `-/tags.html`; every `.html` recursively below `-/tags/` | reference-only | Generated title/link indexes and tag hierarchy. All bodies contain navigation only. Current wiki and collection navigation preserve the useful function. The physical generated-page family is enumerated below. |
| `-/export.json` | private | Generated graph of file paths, links, titles, URLs, parent notes, and metadata. File entries have no content-body field. Metadata keys are `afactor`, `aliases`, `date`, `interval`, `modification date`, `notoc`, `order`, `scheduler`, `sort`, `tags`, `title`; scheduling fields contain personal study metadata. Preserve privately with source history. |
| `progress_update.sh` | reference-only | Counts completed/work tags and appends personal progress data. No mathematical source. Preserve in historical source, not the new migration queue machinery. |
| `_emanote-bin/compile-css` | reference-only | Docker/Windi CSS build and HTML stylesheet rewriting. No mathematical source. Historical renderer dependency. |
| `preamble.sty` | reference-only | Entire file read: notation macros, operators, delimiters, formatting, category names, and theorem environments. No independent theorem, exercise, or proof. Preserve with the native TeX source in history so that source remains editable and renderable. |
| `500_Extra Problems/Rising Sea Exercises/Makefile` | reference-only | Assembles section includes and invokes LaTeX preview. No additional mathematics. Preserve with native source; also named in the worked-source section. |
| `1_Hartshorne/build.log` | private | LaTeX preview diagnostics and local paths, including a missing bibliography. No mathematical source. Preserve privately only if historical diagnostics are retained. |
| `attachments/149685.BAMS-review-Stein.pdf.xml`; `attachments/995861.Hartshorne - Solutions by Joe Cutrone and Nick Marshburn.pdf.xml`; `0_Study Guides/attachments/149685.BAMS-review-Stein.pdf.xml`; `0_Study Guides/attachments/995861.Hartshorne - Solutions by Joe Cutrone and Nick Marshburn.pdf.xml` | private | All four files read completely. Okular viewing history, page/view settings and local file paths; no annotations or extracted mathematical text. PDF content is a separate asset-audit obligation. |
| `_emanote-static/inverted-tree.css`; every `.ttf` in `_emanote-static/fonts/Nunito/`; `favicon.svg` | reference-only | Renderer stylesheet, font files and favicon, not authored mathematics. Preserve in source history if the historical renderer is retained. This row inventories renderer assets; it does not claim a visual mathematical comparison of the favicon. |

## Exact generated HTML family

Besides `-/all.html` and `-/tags.html`, the recursive tag family consists of:

- `-/tags/#.html`
- `-/tags/AG.html`, `-/tags/AG/basics.html`
- `-/tags/MMP.html`
- `-/tags/MOC.html`, `-/tags/MOC/resources.html`
- `-/tags/completed.html`
- `-/tags/examples.html`, `-/tags/examples/exercises.html`
- `-/tags/projects.html`, `-/tags/projects/active.html`, `-/tags/projects/exercises.html`, `-/tags/projects/notes.html`, `-/tags/projects/notes/reading.html`
- `-/tags/resources.html`, `-/tags/resources/full-courses.html`, `-/tags/resources/solutions.html`, `-/tags/resources/videos.html`
- `-/tags/study-guides.html`
- `-/tags/to_work.html`
- `-/tags/todo.html`, `-/tags/todo/add-references.html`, `-/tags/todo/create-links.html`, `-/tags/todo/learning.html`, `-/tags/todo/move-to-new-note.html`, `-/tags/todo/untagged.html`

## Physical HTML coverage

All deployed HTML is covered by the following physical-path partition. The infrastructure scope above contains no additional substantive source page.

- This section owns `index.html`, `900_Changelog.html`, `0_Study Guides.html`, `Fulton.html`, `unresolved links output.html`, `IW-Queues.html`, `progress.html`, all HTML below `IW-Queues/`, and all HTML below `-/`.
- The guides section owns root `Definitions.html`, `definitions.html`, `000 AG Oral Exam Plan.html`, `001 Practice Questions.html`, and the authored guide pages directly inside `0_Study Guides/`.
- The reading sections own `0_Study Guides/Notes/`, `0_Study Guides/Reading Notes/`, `Fulton/`, and Hartshorne III–IV, including their navigation pages. Any navigation rows for the top-level guide/Fulton menus overlap the explicit rows above and should be integrated once.
- The worked section owns `500_Extra Problems.html`, all HTML below `500_Extra Problems/`, `Hartshorne.html`, Hartshorne I–II, and the complete root `1_Hartshorne/1_1.html` through `1_Hartshorne/1_7.html` exercise aliases. The reading section retains the root `1_Hartshorne.html`, `2_Hartshorne.html`, and `2_Hartshorne/2_1.html` navigation/stub rows already communicated there.
- The images-and-surfaces section owns Hartshorne V. There is no HTML under root `attachments/`; the other top-level source directories are renderer directories inventoried above.

## Broken-image diagnostic references

`unresolved links output.html` names these historical image links. They are evidence of references, not evidence that image bytes survive. Reconcile them with the page-specific and image audits:

- `attachments/Pasted image 20220314125429.png`, from the Schemes guide.
- `attachments/Pasted image 20220213162548.png`, from the Cohomology guide.
- `attachments/Pasted image 20220208145954.png`, from the Cohomology guide.

The referenced guide pages, not this diagnostic, own any mathematical recovery obligation.
