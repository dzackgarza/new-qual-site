# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or
site use under [QUAL-05](CONTRIBUTING.md#named-policies). Include findings outside
the selected card. This file owns observations; [TODO.md](TODO.md) owns selected
repair tasks and dependencies. Keep existing GitHub issue links rather than
copying their live status. The [review policy index](REVIEW_POLICY.md) supplies
named candidate patterns, not proof that a candidate is a defect.

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

### `P-1P5M4` is a malformed quotient-module solution fragment

- **Object and need:** `P-1P5M4` should pose and prove the natural $R/I$-module structure on $A/IA$ for an $R$-module $A$ and ideal $I$.
- **Observed evidence:** The `problem` body is attempted solution prose; its displayed action is missing the module representative (`r+I \actson +IA`), and it verifies module axioms without first proving independence of the representatives $r+I$ and $a+IA$.
- **Impact and owner:** The public card `corpus/problems/Algebra/P-1P5M4.md` is not a posed problem and omits the essential well-definedness argument.
- **Uncertainty:** The original source wording is unavailable; the title and surviving calculations determine the standard quotient-module theorem.
- **Repair:** Under TODO §7 / issue #2, replace the fragment by the standard statement and give a complete proof of well-definedness and the module axioms.


## Workflow and rendering papercuts

### Local repository connector and batched authoring query failures

- **Object and need:** Algebra solution authoring needs reliable local repository access and the existing authoring-query commands so a worker can inspect the shared state and derive an unsolved worklist without touching `queues/C-unsolved-cards.md`.
- **Observed evidence:** On 2026-09-09, the first local terminal call failed before execution with `Tunnel-client has not been seen for 300 seconds`. After switching to the second connected terminal endpoint, a read-only batched command combining collection discovery with several `just unsolved-in` queries was blocked by the execution safety layer before running, while the same collection-discovery command succeeded when retried alone. The first `just unsolved-in SRC-UCSD-ALG-FALL-2008` invocation also exceeded the 30-second foreground-yield window and had to be left running with redirected output for later inspection. Later in the same Algebra stream, prose-only commits were mistakenly sent through the full pre-commit gate before the repository's documented prose-only exemption was re-read; Semgrep then spent several minutes in uninterruptible I/O (`folio_wait_bit_common`) and an optional `just check-card E-LUH54` likewise stalled in I/O.
- **Impact and owner:** This does not change corpus mathematics, but it interrupts the repository-prescribed workflow of reading current state and selecting work through project tooling. The affected boundary is the local connector/execution environment rather than `qualc` semantics.
- **Uncertainty:** The connector failure is verified from the returned error. The safety block is verified for that specific batched shell command only; the exact classifier trigger is unknown. The long `unsolved-in` latency may be normal Pandoc startup/parsing cost rather than a repository defect.
- **Repair:** No existing TODO task owns the external connector/runtime. A resolving result would be stable local terminal availability, predictable execution of read-only project commands, and foreground authoring queries that either complete or expose a supported continuation mechanism instead of losing their result after the yield limit.
