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

### ag-notes migration omits substantive source content

**Assessment:** incomplete.
The [ag-notes migration queue](queues/H-ag-notes-migration.md) owns the direct source-to-target comparison and remaining work.
It identifies missing questions, proofs, hypotheses, examples and diagrams, with separate source-repair, reference and private-material dispositions.

**Source boundary:** the deployed `/var/www/ag_notes/` tree was compared with authored corpus and wiki content.
The later `/var/www/Notes/Class_Notes/2022/Fall/Orals/` vault remains a separate, unreviewed revision.
The queue records the source inventory and target revision.

**Owner and expected repair:** algebraic-geometry corpus curation.
Complete the named mathematical items and resolve damaged source fragments before retiring their source.
The queue records work; it does not perform the migration.

## Workflow and rendering papercuts

### Direct `.venv` authoring commands can see an unsupported host Pandoc

- **Object and evidence:** during the final read-only sweep of the assigned range, `.venv/bin/python -m qualc.authoring unsolved <collection>` failed inside `qualc.pandoc_batch` because the process found host Pandoc 3.1.3 while the repository requires Pandoc 3.10 or newer.
  The same authoring command succeeds through the repository's normal login-shell `uv run` route.

- **Impact:** invoking the repository interpreter directly is insufficient for authoring commands that depend on the repository's Pandoc toolchain; a seemingly valid local environment therefore fails before reading any card content.
  No corpus file was changed by the failed sweep.

- **Rechecked 2026-09-16:** `/usr/bin/pandoc` is still 3.1.3 and `~/.local/bin/pandoc` is 3.10.2; `qualc.pandoc_batch` resolves `pandoc` from `PATH`, so a direct invocation whose `PATH` lacks `~/.local/bin` still reaches the unsupported executable.

- **Repair:** use the repository's documented `just`/`uv run` authoring entry points for Pandoc-dependent commands, or make the supported Pandoc executable available inside direct `.venv` invocations if that route is meant to be supported.

