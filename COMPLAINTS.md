# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or site use under [QUAL-05](CONTRIBUTING.md#named-policies).
Include findings outside the selected card.
This file owns observations; [TODO.md](TODO.md) owns selected repair tasks and dependencies.
Keep existing GitHub issue links rather than copying their live status.
The [corpus review patterns](CONTRIBUTING.md#corpus-review-patterns) supply named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact mathematical statement and hypotheses, or user action and expected behavior.

- **Observed evidence:** source page and passage, counterexample or proof gap, or actual action and result with the relevant path/revision.

- **Impact and owner:** affected parts or consumers, existing partial result, and the mathematical or tool boundary that must change.

- **Uncertainty:** distinguish a verified error from a source ambiguity or review candidate.
  State inspected scope and remaining questions.
  For absence claims supply Searched, Found, Conclusion, Confidence and Gaps.

- **Repair:** link the existing TODO task or issue when available and state the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question.
An unsolved problem is ordinary authoring work, not by itself a defect.
A command that prevents reading the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card.
Preserve concurrent entries.
If the selected proof requires a repair, link that dependency and resolve it before relying on the statement; recording it does not make the proof valid.
Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the fixing commit; retain any unresolved portion.
Put durable mathematical errata on the owning card and durable policy in CONTRIBUTING. Keep process notes out of public mathematical remarks.

## Mathematical issues and source questions

### Duplicate finite-Galois card FD-4GFTY

- **Object and need:** `D-5JYEI` and `FD-4GFTY` in `corpus/theory/Algebra`. The canonical Galois card defines finite Galois extensions by normality and separability and proves the automorphism-count condition as an equivalent characterization; the flashcard restates that characterization as a second definition.

- **Observed evidence:** `D-5JYEI` item (5) states `$\size\Aut_F(K)=[K:F]_s=[K:F]$`; `FD-4GFTY` defines Galois by `$\abs{\Aut(K/F)}=[K:F]$`. The wiki and algebra guide displayed both.

- **Impact and owner:** the flashcard duplicates an equivalent condition already owned by the canonical card and creates a second defining surface.

- **Uncertainty:** none after reading both cards.

- **Repair:** a `CARD-04` repair moves the automorphism-count review prompt to `D-5JYEI`, removes duplicate reader-facing references, and deletes `FD-4GFTY`.

### Duplicate Eisenstein theorem cards FT-2P5VV and T-CF6S3

- **Object and need:** `FT-2P5VV` and `T-CF6S3` in `corpus/theory/Algebra`. Both state Eisenstein's criterion for `$f\in\ZZ[x]$` and prove it by Gauss's lemma and reduction modulo `$p$`.

- **Observed evidence:** the hypotheses and proof are the same.
  `T-CF6S3` additionally records the primitive-polynomial consequence giving irreducibility in `$\ZZ[x]$`; `FT-2P5VV` contributes only the review prompt.
  The Galois-theory wiki and algebra guide displayed both.

- **Impact and owner:** one standard irreducibility criterion had two theorem addresses, while the richer card strictly contains the other.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `T-CF6S3`, redirects the remaining theorem link, removes duplicate reader-facing references, and deletes `FT-2P5VV`.

### Gauss's lemma was split across two theorem cards

- **Object and need:** `FT-OXN3Y` and `T-JEZZY` in `corpus/theory/Algebra`. Both are standard forms of Gauss's lemma rather than genuinely separate theorems.

- **Observed evidence:** `FT-OXN3Y` states that a factorization in the fraction field descends to `$R[x]$` with the same factor degrees; `T-JEZZY` gives the primitive-polynomial irreducibility equivalence and the sharper scalar rescaling statement.
  The wiki and algebra guide displayed both together.

- **Impact and owner:** one theorem was split between two addresses, and a Hartshorne collection card linked specifically to the weaker half.

- **Uncertainty:** none after reading both cards; the two forms are standard parts of the same Gauss lemma.

- **Repair:** a `CARD-04` repair merges both forms and the polynomial-UFD consequence onto `T-JEZZY`, moves the review prompt there, redirects all live references, and deletes `FT-OXN3Y`.

### UCSD covering-spaces subgroup matching card holds no recoverable posed task

- **Object and need:** `P-O2J6S` in `SRC-UNSORTED-TOPOLOGY`.

- **Observed evidence:** the card body lists five subgroups of $\langle a,b\rangle$ and five images of covering diagrams, but no posed question.
  The card was intaken from the vendored compilation `assets/Topology/650_UCSD_Qual_Questions/Quals/Topology Problems (Solutions).pdf` (with its checked-in extraction), whose "Covering Spaces" section reads only "Generators of the subgroups:" followed by the same list and the same images: those bytes are the author's answer material, recorded without the question, because the compilation assumes the reader has the original course sheet.

- **Searched:** the vendored compilation and its extraction, `UCSD_290_F14_sheet*` extractions, `UCSD_Topology_Qual_Problems_2020-05-29`, `UCSD_290_Qualifying_Exams`, and the `qual-wiki` UCSD finals.
  **Found:** the subgroup list and images only.
  **Conclusion:** the posed task is not recoverable from any retained source.
  **Confidence:** high for absence from retained bytes.
  **Gaps:** the original UCSD 290 covering-spaces homework sheet that posed the question is not in this repository or the sibling clones; the vendored compilation is owner-authored notes and so is also not a valid `provenance:` oracle, which is why the collection's provenance list stays empty.

- **Impact and owner:** the card is not a self-contained problem; a solution cannot be authored without inventing the task.
  The five covering diagrams in `assets/Topology/650_UCSD_Qual_Questions/Quals/assets/` are the only record of the covers.

- **Uncertainty:** the intended task (presumably matching each subgroup with the corresponding cover of $S^1\vee S^1$) is a plausible reconstruction, not a reading of any source.

- **Repair:** blocked on recovering the original UCSD 290 covering-spaces sheet; until then the card stays unauthored rather than being given an invented statement.

## Workflow and rendering papercuts

### Shared QC installation lacks its PR workflow and branch protection

- **Object and need:** the shared QC installation declared in `justfile`.

- **Observed evidence:** `ai-review-ci doctor --target . --json` on 2026-10-25 accepted the local recipe delegation but reported missing `.github/workflows/review-pr.yml` and an unprotected `main` branch.

- **Impact and owner:** Pages CI runs the project suite and build; the shared required PR acceptance contexts are not installed.
  The installation belongs to ai-review-ci.

- **Uncertainty:** this is the doctor's current installation result, not a failure of the Pages tests or build.

- **Repair:** reconcile the shared PR installation with `QUAL-09`'s direct-to-main workflow before changing branch protection.

