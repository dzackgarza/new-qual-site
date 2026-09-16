# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or
site use under [QUAL-05](CONTRIBUTING.md#named-policies). Include findings outside
the selected card. This file owns observations; [TODO.md](TODO.md) owns selected
repair tasks and dependencies. Keep existing GitHub issue links rather than
copying their live status. The [corpus review patterns](CONTRIBUTING.md#corpus-review-patterns)
supply named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact
  mathematical statement and hypotheses, or user action and expected behavior.
- **Observed evidence:** source page and passage, counterexample or proof gap,
  or actual action and result with the relevant path/revision.
- **Impact and owner:** affected parts or consumers, existing partial result,
  and the mathematical or tool boundary that must change.
- **Uncertainty:** distinguish a verified error from a source ambiguity or
  review candidate. State inspected scope and remaining questions. For absence
  claims supply Searched, Found, Conclusion, Confidence and Gaps.
- **Repair:** link the existing TODO task or issue when available and state
  the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question. An unsolved problem is
ordinary authoring work, not by itself a defect. A command that prevents reading
the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card. Preserve
concurrent entries. If the selected proof requires a repair, link that dependency
and resolve it before relying on the statement; recording it does not make the
proof valid. Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the
fixing commit; retain any unresolved portion. Put durable mathematical errata
on the owning card and durable policy in CONTRIBUTING. Keep process notes out
of public mathematical remarks.

## Mathematical issues and source questions

### ag-notes migration omits substantive source content

**Assessment:** incomplete. The [ag-notes migration queue](queues/H-ag-notes-migration.md) owns the direct source-to-target comparison and remaining work. It identifies missing questions, proofs, hypotheses, examples and diagrams, with separate source-repair, reference and private-material dispositions.

**Source boundary:** the deployed `/var/www/ag_notes/` tree was compared with authored corpus and wiki content. The later `/var/www/Notes/Class_Notes/2022/Fall/Orals/` vault remains a separate, unreviewed revision. The queue records the source inventory and target revision.

**Owner and expected repair:** algebraic-geometry corpus curation. Complete the named mathematical items and resolve damaged source fragments before retiring their source. The queue records work; it does not perform the migration.

## Workflow and rendering papercuts

### Direct `.venv` authoring commands can see an unsupported host Pandoc

- **Object and evidence:** during the final read-only sweep of the assigned range, `.venv/bin/python -m qualc.authoring unsolved <collection>` failed inside `qualc.pandoc_batch` because the process found host Pandoc 3.1.3 while the repository requires Pandoc 3.10 or newer. The same authoring command succeeds through the repository's normal login-shell `uv run` route.
- **Impact:** invoking the repository interpreter directly is insufficient for authoring commands that depend on the repository's Pandoc toolchain; a seemingly valid local environment therefore fails before reading any card content. No corpus file was changed by the failed sweep.
- **Rechecked 2026-09-16:** `/usr/bin/pandoc` is still 3.1.3 and `~/.local/bin/pandoc` is 3.10.2; `qualc.pandoc_batch` resolves `pandoc` from `PATH`, so a direct invocation whose `PATH` lacks `~/.local/bin` still reaches the unsupported executable.
- **Repair:** use the repository's documented `just`/`uv run` authoring entry points for Pandoc-dependent commands, or make the supported Pandoc executable available inside direct `.venv` invocations if that route is meant to be supported.

### The worktree-per-stream instruction filled the host volume

- **Object and need:** this repository's own authoring instructions and commit gate. A stream reading `AGENTS.md` must not be told to open a second checkout, and a stream that opens one anyway must find out at its next commit rather than when the volume fills.
- **Observed evidence:** the `# Worktrees` chapter of `AGENTS.md` instructed each stream to open an isolated worktree, and streams followed it. Each worktree is a second checkout of the whole tracked corpus — roughly 420 MB, of which 353 MB is `assets/` — carrying a handful of edited Markdown files; the accumulated set held about a megabyte of authored prose between them. On 2026-09-10 the host volume reached 100% with 12 MB free. A full volume presents as killed processes and dying exec sessions rather than as a disk error, so builds and exec sessions died across every repository on the host for most of a day before anyone read `df`. The recorded counts differ by the moment each was taken: `AGENTS.md` says twenty-seven at the failure, holding forty-four changed files; [TODO.md](TODO.md) says twenty-five remained after nine were retired for 3.7 GB; the fleet-level report says twenty-seven to thirty-eight. The replacement rule — commit directly to `main`, no worktrees and no branches — had already been restated twice at fleet level and ignored twice, because it lived only in a fleet document that no worker in this repository reads.
- **Impact and owner:** repository-owned, in the surfaces workers actually read and the gate they actually pass through: `AGENTS.md` and `CONTRIBUTING.md` for the instruction, `just test-commit` and `just commit-card` for the gate. This is not a corpus defect and not an environment condition. The instruction produced the checkouts and no check in the repository refused them, so a third restatement would have changed nothing.
- **Uncertainty:** the peak worktree count is not settled by these sources, only bounded by them. Whether any authored prose went with the retired worktrees was not established here. Whether the volume had other contributors was not measured. `git worktree list` reports one entry, and the TODO retirement item was closed on 2026-09-13; whether each worktree was retired through the three `QUAL-09` readings rather than simply removed is not established here.
- **Repair:** `7757a6177` replaced the `# Worktrees` chapter with `# One checkout, one branch` in `AGENTS.md` and added `QUAL-09` to `CONTRIBUTING.md`, keeping the three readings that establish the state of a worktree this stream did not create and the retirement they permit. `a35065545` added the private `_no-worktrees` recipe and made `just test-commit` depend on it. `just commit-card` is not gated: on 2026-09-16 its recipe has no `_no-worktrees` dependency and `qualc.authoring commit` performs no worktree check before committing with `--no-verify` when the problem block is unchanged, so card authoring, the population that built the worktrees, bypasses the check. Two further pieces remain unowned. `git commit --no-verify` invoked directly under the prose-only exemption in `AGENTS.md` is ungateable by construction and is covered by documentation alone. Acceptance: `git worktree list` in this clone reports exactly one entry; `AGENTS.md`, `CONTRIBUTING.md` and `TODO.md` contain no instruction to create a worktree or a branch; and with a throwaway worktree added, `just test-commit` and `just commit-card` both refuse with the `QUAL-09` message and neither produces a commit. Remove this entry when all three hold.

### MinerU Flash extraction requests fail against the remote service

- **Fall 2007 and September 2005 page inspection:** `mutool draw` rendered PDF pages 36 and 43 successfully and again reported missing ICC support. Native image views showed the full monochrome pages legibly, including the polynomial signs, annular domain wording and the explicit right-half-plane inequalities. This was rendering only, not text extraction or OCR; color-profile fidelity was not tested.
- **September 2011 JHU visual review, 2026-09-10:** the main `.venv` has neither PDFium's Python wrapper nor Pillow. The installed `mutool draw` rendered retained PDF page 22 successfully without extraction, OCR or environment overrides. It emitted `warning: ICC support is not available`; the displayed monochrome mathematical page was legible. This does not establish color-profile fidelity or repair the separately unavailable extraction service.
- **Image-view boundary, 2026-09-10:** native `view_image` rejected `/tmp/newqual-july2013-fields-proof.png` because `/tmp` is outside the connector's approved roots, although terminal rendering there succeeded. Moving that rendered page to the ignored repository path `.tmp-july2013-fields-proof.png` allowed inspection of PDF page 8. Keep inspection images inside an approved root; this was an image-path restriction, not a rendering or source-file failure.
- **July 2013 Fields continuation, 2026-09-10:** opening the public raw PDF again returned `Internal Error`, without a PDF reference usable by the web screenshot tool. The already-rendered local `assets/attachments/intermediate/w13-source-review-hpowvjoz/page-8.png` displayed successfully and verified all four Fields questions; no new extraction or OCR was performed.
- **July 2013 symbol recovery:** the retained extraction drops the divisibility symbol in Groups 1(b). Visual inspection of PDF page 6 confirms `p` does not divide `q-1`, exactly as stated on `P-W13PQ`. The web reader returned an internal error for the public raw PDF and a non-retryable rejection for the CDN URL, so neither yielded a PDF that its screenshot tool could inspect. Rendering the retained PDF with the installed system PDFium and inspecting the resulting page image succeeded without OCR or a new text extraction. The card's hypothesis needed no correction.
- **July 2003 lattice recovery:** `P-ARTALG-JU03-6` replaced its essential diagram with the undefined phrase “a specific diamond shape.” Native inspection of PDF page 45 shows exactly four incomparable middle vertices, plus top and bottom. Commit `6b1b83169` restores that complete order relation and proves all five decisions, including realization over the specified base field. For this inspection, `UV_NO_SYNC=1 uv run python` lacked `pypdfium2`; `/usr/bin/python3` already had it and rendered the retained source successfully without installing packages or running OCR. PDF page 44 contains problem 5, not the required diagram.
- **Object and need:** source verification for `P-ARTALG-AL04-3` exposed an unavailable configured PDF extraction command and subsequent remote-service failures. The installed source-reading workflow should be usable without guessing numeric hypotheses from extracted text.
- **Observed evidence:** on 2026-09-10, `command -v mineru-open-api` returned no executable, and `UV_NO_SYNC=1 uv run mineru-open-api --help` failed with `No such file or directory`. `AGENTS.md` names this command as the sole permitted PDF extraction method.
- **Execution attempts:** the official Linux binary runs from `/tmp/qual-mineru.XhPQVW/mineru-open-api` and reports version `v0.5.9`. A page-29-only `flash-extract` request timed out uploading the PDF. Separate URL-input requests using the public GitHub copy and a jsDelivr copy both returned error `-60007`, reporting that the model service was temporarily unavailable. Both public copies were verified byte-identical to the repository PDF before submission. All three requests targeted page 29; none returned source content.
- **Source verification, 2026-09-10:** direct PDFium rasterization of the retained PDF and native image inspection succeeded. Page 29 contains only Groups 1; the actual Groups 3 statement is on PDF page 30 (printed page 2) and says the integer `72`, with no superscript and no abelian hypothesis. The PDF SHA-256 is `956dd5e3735e66d75eb0bed9af4f0c544015016fcf48fec8f10eeab98a06393b`. No new text extraction or OCR was used. Commit `83522c224` retains order 72 and proves the full fifty-class classification, including the executable exact action-orbit enumeration.
- **Additional tool friction:** web retrieval of the public raw PDF returned `DisabledError`, alternative PDF URLs were rejected, and a combined read-only repository request was rejected before execution. Native reads and local rendering restored source access. The installed PDFium wrapper also rejected the context-manager form with `TypeError`; constructing `PdfDocument` directly succeeded. A later combined request for `P-ARTALG-JU03-9` single-card parsing and diff review was also rejected before execution; the two separated operations succeeded, so the rejection was not a failed repository check.
- **Additional source defect repaired:** visual inspection of PDF page 32 (printed page 4), Rings 2, showed that `P-ARTALG-AL04-6` omitted part (a), the rational canonical form of the matrix with rows `(2,3)` and `(7,1)`. Commit `7db3ccc00` restores and proves both parts on that source item; the garbled matrix in the extraction was not evidence that the original paper omitted it.
- **Additional proof defect repaired:** the former `P-ARTALG-AL04-10` proof inferred that a group is abelian from a normal abelian subgroup and a cyclic quotient; that implication is false, as `S3` with its normal `C3` shows. The order-specific action argument needed there was absent. Commit `d79880a9b` replaces it with the index-three coset action. PDF page 37 also prints `[K:F]=105` with `F` undefined; the already-authored card explicitly states `[K:Q]=105`, and that is the hypothesis proved rather than an assertion about an unspecified field `F`.
- **Additional collection omission repaired:** PDF page 38 (printed page 10) contains 2004 Fields 4, asking for all subfield orders of a field of order `5^20` and uniqueness of its subfield of order 25. The 2004 section listed only ten items, ending with Fields 3 on `P-ARTALG-AL04-10`; its four Groups, three Rings, and three Fields cards omitted this final source problem. A corpus-wide literal search for `5^{20}`, `5^20`, and `more than one subfield of order` returned no matches. Commit `420c00019` restores the item as `P-ARTALG-AL04-11`, its ordered membership, and the complete existence-and-uniqueness proof. Zero unsolved listed cards had not established complete source coverage.
- **Rechecked 2026-09-16:** `mineru-open-api` is now installed at `~/.local/bin/mineru-open-api`, so the missing-command half of this entry no longer reproduces. The service half persists: [Queue E](queues/E-pdf-attachments.md) records eleven sources left open on 2026-09-14 because Flash uploads timed out awaiting response headers or required split page ranges.
- **Impact and owner:** the source ambiguity is resolved and no longer blocks this card. The missing configured command and remote-service failures remain setup/tooling issues; successful local rendering does not establish that those services were repaired.
- **Uncertainty:** the printed numeric hypothesis is now visually verified. The generic API errors do not establish a bad PDF, a credential failure, or a specific service-side cause.
- **Repair:** restore reliable service access for the installed extraction command. Source inspection of this card is complete; future page-specific requests must use the verified PDF page rather than the section's starting page.
