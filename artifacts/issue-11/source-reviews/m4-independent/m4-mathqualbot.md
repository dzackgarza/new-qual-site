# M4 independent source review: MathQualBot scoped collection

Reviewer: `/root/m4_independent_review`, Mendel, this fresh review session.

Assignment: Review the scoped MathQualBot question-image collection.
Verify that every source image has its permanent native target.
This review does not claim migration of the wider MathQualBot application.

Source/input revision: non-Git vendored source.
The authoritative input is `sources/qualbot-question-images/PROVENANCE.md`, which records the MathQualBot droplet source and vendoring date 2026-07-23.

Target/output revision: `96380a3f1c6fc64ead25ec441dfdd939b92f872e` (current `main`).

Exact inventory boundary: the 51 PNG files under `sources/qualbot-question-images/`, excluding its provenance document, and the corresponding 51 PNG files under `assets/ws9/qualbot-question-images/`.

Direct evidence inspected:

- The source directory contains exactly 51 PNGs.
  The target directory contains exactly 51 matching relative paths.

- SHA-256 was compared for every source/target pair.
  All 51 pairs are byte-identical; there are zero missing, extra, or differing files.

- No transcription or semantic transformation is claimed for this scoped collection.
  The target is the complete native image collection.

Failures found: none within the stated 51-image boundary.
The absence of a Git commit is an input provenance fact, not a missing target; the provenance file identifies the vendored source and boundary.

Repairs excluded from this review: no image conversion, transcription, corpus, provenance, tooling, or test change was performed by this reviewer.

Final result: **PASS** for the scoped 51-image MathQualBot collection.
Every source PNG has an exact permanent native target.
