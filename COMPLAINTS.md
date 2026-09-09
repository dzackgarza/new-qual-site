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

### `E-JRKXU` leaks a source tag and uses imprecise splitting-field wording

- **Object and need:** `E-JRKXU` should ask whether $\QQ(u)$ is the splitting field over $\QQ$ of the minimal polynomial of $u=\sqrt{3+\sqrt2}$. Public problem prose should contain the mathematics rather than an uncited source label.
- **Observed evidence:** The card currently asks `Is $\boldsymbol{Q}(u)$ a splitting field of $u$ over $\boldsymbol{Q}$ ? (MathSE)`. An element itself does not have a splitting field without reference to a polynomial; the exact Math StackExchange source asks the same shorthand question and identifies the minimal polynomial $x^4-6x^2+7$. The trailing `(MathSE)` is source/process metadata rendered in the public problem body.
- **Impact and owner:** The mathematical intent is recoverable, but the public statement is imprecise and leaks source metadata contrary to QUAL-08/citation policy. The owning file is `corpus/problems/Algebra/E-JRKXU.md`.
- **Uncertainty:** The matching Math StackExchange question is verified by the distinctive radical and wording. The repository collection itself has no external provenance entry for this card.
- **Repair:** Under TODO §7 / issue #2, state the minimal-polynomial splitting-field question precisely, remove the public `(MathSE)` tag, and solve the resulting field-membership problem.


## Workflow and rendering papercuts

### Local repository connector and batched authoring query failures

- **Object and need:** Algebra solution authoring needs reliable local repository access and the existing authoring-query commands so a worker can inspect the shared state and derive an unsolved worklist without touching `queues/C-unsolved-cards.md`.
- **Observed evidence:** On 2026-09-09, the first local terminal call failed before execution with `Tunnel-client has not been seen for 300 seconds`. After switching to the second connected terminal endpoint, a read-only batched command combining collection discovery with several `just unsolved-in` queries was blocked by the execution safety layer before running, while the same collection-discovery command succeeded when retried alone. The first `just unsolved-in SRC-UCSD-ALG-FALL-2008` invocation also exceeded the 30-second foreground-yield window and had to be left running with redirected output for later inspection.
- **Impact and owner:** This does not change corpus mathematics, but it interrupts the repository-prescribed workflow of reading current state and selecting work through project tooling. The affected boundary is the local connector/execution environment rather than `qualc` semantics.
- **Uncertainty:** The connector failure is verified from the returned error. The safety block is verified for that specific batched shell command only; the exact classifier trigger is unknown. The long `unsolved-in` latency may be normal Pandoc startup/parsing cost rather than a repository defect.
- **Repair:** No existing TODO task owns the external connector/runtime. A resolving result would be stable local terminal availability, predictable execution of read-only project commands, and foreground authoring queries that either complete or expose a supported continuation mechanism instead of losing their result after the yield limit.
