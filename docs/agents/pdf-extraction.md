# PDF extraction

PDF intake has one epistemic baseline: a **high-quality machine extraction** checked into the repository.
Two methods are valid. Use MinerU Flash first:

```bash
mineru-open-api flash-extract myfile.pdf --language en
```

When MinerU Flash fails on a source (timeouts, parse failures, or garbled output at an
identified location), extract it with the Mistral OCR API, which writes the extraction and its
provenance file:

```bash
just ocr-pdf assets/attachments/myfile.pdf assets/attachments/myfile_extracted.md
```

Do not use `pdftotext`, Tesseract, PyMuPDF/`fitz`, or any other text extractor in place of
these two. A transient MinerU failure (upload timeout, `-60007`, `-60010`) is retried, with
page ranges when a whole-file upload times out, before it counts as a failure.

Rendering a page to PNG and reading it is the method for an identified defect the extraction
cannot carry: a figure, a garbled matrix or glyph, a cropped choice. Transcribe that location
from the render and record on the card and provenance file that it was read from the page
image. Rendered output is also how authored cards and pages are spot-checked.

Every problem-bearing PDF consumed by intake must therefore have a checked-in MinerU Flash or
Mistral OCR Markdown extraction. The extraction is the auditable transcription baseline from which cards
are produced. An existing `*_extracted.md` or `assets/attachments/extracted/*.md` file may be
reused only when repository evidence establishes that it came from one of these two paths.
**Unknown extraction provenance is not acceptable evidence:** regenerate the extraction before
using it for intake.

Model work begins only *after* the machine extraction exists. Its role
is limited to transcription cleanup and resolving concrete extractor errors or ambiguities. If a
specific extraction defect must be resolved against the original PDF, inspect only that disputed
location and record the correction as such; do not turn source inspection into an independent
second transcription pass or a claim that the rest of the extraction has been verified. If
neither extractor can run, intake of that PDF is blocked rather than falling back to another
extraction path.

A genuine source that exists only as a retained raster image is not a separate extraction case.
Preserve the original image as provenance, wrap it losslessly and deterministically into a PDF
container, record the image hash and derived-PDF hash, and run the same extraction on
that PDF. The conversion step must not OCR, resample, enhance, redraw, or otherwise interpret the
image. If the image itself is missing (for example the lost Anki
`collection.media` figures), there is nothing to convert or extract; that remains missing-source
recovery work.

Never extract PDFs to `/tmp`, `.tmp`, or any other temp directory. Temp
files are not tracked by git and vanish between sessions. Always extract
into the repository so the output is versioned and persistent.

Source PDFs live under `assets/attachments/`. Their checked-in extractions live
under `assets/attachments/` as `<stem>_extracted.md` beside the PDF or as
`assets/attachments/extracted/<stem>.md`. Example:

```bash
mineru-open-api flash-extract assets/attachments/exam.pdf > assets/attachments/exam_extracted.md
```

Commit the final extraction with the intake work. If you need intermediate files while resolving
a specific extraction defect, stage them in the repo — for example
`assets/attachments/intermediate/` — and delete them when the final extraction/correction is
committed.

## Extraction output is an input, not a card

What comes out of an extractor is a transcription source. It becomes a card when its
mathematics has been written as LaTeX and reads as the source reads — not when it has been
pasted between `::: {.problem}` fences. A statement carrying unicode mathematics outside any
`$`-delimiter has not been transcribed: `∂u ∂x (0, 0)` is a lost derivative, a bare `Z` where
an integral belongs is a lost integral, and a nested radical flattened to `v u s r Z 9u √ q t`
is a lost problem. The card looks finished, `just unsolved` offers it, and a worker writes a
proof of something nobody asked.

Never run a whitespace or line normalizer over unconverted extraction output. The column
layout in a raw extraction is the last surviving record of the fraction bar, the integral
bound, and the superscript; joining the lines is not a cleanup, it is the step that makes the
card unrecoverable without going back to the PDF. On 2026-09-13 a normalization pass did
exactly this to three freshly ingested collections, one commit after ingesting them.

Two consequences for a turn. An ingest that needs a follow-up normalization commit did not
land cards, it landed extraction residue — fix the pipeline rather than paying it by hand on
every source. And where the source cannot settle what a statement said, mark the card as
unrecovered and say so; an invented plausible problem is the one outcome worse than a gap,
because nothing downstream can tell it from the real thing.
