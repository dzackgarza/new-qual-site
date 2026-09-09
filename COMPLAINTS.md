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

### `E-ZCJZC` omits finiteness and uses a false conjugate-intersection count

- **Object and need:** `E-ZCJZC` states the same conjugate-cover theorem and already has a solution.
- **Observed evidence:** The card omits finiteness. Its solution also says distinct conjugates of $H$ `intersect only at the identity`, which is false in general; for example, distinct point stabilizers $S_{n-1}<S_n$ intersect in a subgroup $S_{n-2}$. The resulting formula $1+n(|H|-1)$ for the union size is therefore unjustified.
- **Impact and owner:** `corpus/problems/Algebra/E-ZCJZC.md` contains an invalid proof of a statement that is itself false for arbitrary infinite groups.
- **Uncertainty:** None about these defects.
- **Repair:** Add the finite-group hypothesis and replace the proof by a valid counting inequality or Burnside/orbit-counting argument.

### `P-5KZDX` contains only a definition fragment, not a problem

- **Object and need:** `P-5KZDX` is classified as a problem but should pose a complete separability/perfect-field task.
- **Observed evidence:** The body only defines a perfect field and then says `since $F$ is a finite field, $p$ must be a prime`, without introducing $p$ or asking anything. Git history shows the same fragment in the earliest retained version.
- **Impact and owner:** `corpus/problems/Algebra/P-5KZDX.md` has no recoverable mathematical obligation to solve.
- **Uncertainty:** The intended task may have been to prove finite fields are perfect, but that conclusion is not present in the source fragment.
- **Repair:** Recover the original source context before authoring a solution.

### `P-5KS4C` is a conclusion fragment with no recoverable hypothesis

- **Object and need:** `P-5KS4C` should pose a Galois/solvability problem, but its body begins `By a theorem in class, this would force...` and contains only the contradiction step.
- **Observed evidence:** Git history shows the same fragment in the earliest retained version; later commits changed only title/classification. No preceding hypothesis or construction of $E/K$ survives in the card.
- **Impact and owner:** The owning file `corpus/problems/Algebra/P-5KS4C.md` has no complete mathematical obligation to solve.
- **Uncertainty:** The fragment is compatible with several standard arguments involving nonsolvability of $S_n$ for $n\ge5$, so reconstructing a specific source question would be speculative.
- **Repair:** Recover the original source context before authoring a solution.

### `P-3VHPO` is truncated after naming two cubic fields

- **Object and need:** `P-3VHPO` should contain a complete question comparing $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$.
- **Observed evidence:** The current body is only `Show that $\QQ(2^{1\over 3})$ and $\QQ(\zeta_3 2^{1\over 3})$`. Git history shows the same truncation in the earliest retained version; only the title was later cleaned.
- **Impact and owner:** The owning file `corpus/problems/Algebra/P-3VHPO.md` has no recoverable conclusion to prove.
- **Uncertainty:** Several natural statements could have been intended (nonisomorphism over $\QQ$, distinct subfields of the splitting field, etc.), so guessing would not be source-faithful.
- **Repair:** Recover the original source text before authoring a solution.

### `P-3BNEC` is truncated before the mathematical question

- **Object and need:** `P-3BNEC` should contain a complete field-extension question, but its body ends after `is $F$`.
- **Observed evidence:** The current file literally stops at `6. If $F$ is over $K$, and $E$ is an intermediate extension of $F$ over $K$, is $F$`, and no exact duplicate of the lost continuation was found elsewhere in the corpus.
- **Impact and owner:** The owning file `corpus/problems/Algebra/P-3BNEC.md` has no recoverable mathematical obligation to solve.
- **Uncertainty:** The nearby solved card `E-N626Y` concerns algebraic/normal/separable properties over intermediate fields, so that may be related, but the missing text is not recoverable with enough confidence to replace it.
- **Repair:** Recover the original source text before authoring a solution.

### `P-35P7L` is false without additional hypotheses

- **Object and need:** `P-35P7L` claims every group of order $12$ with a normal subgroup of order $4$ is isomorphic to $A_4$.
- **Observed evidence:** The cyclic group $C_{12}$ has its unique subgroup of order $4$, hence a normal subgroup of order $4$, but $C_{12}$ is abelian and therefore not isomorphic to $A_4$.
- **Impact and owner:** The owning file `corpus/problems/Algebra/P-35P7L.md` cannot be solved as stated.
- **Uncertainty:** The missing intended hypothesis is not recoverable from the current card; several plausible strengthenings would make different classification statements.
- **Repair:** Recover the source statement or identify the omitted hypothesis before authoring a solution.

### `P-2HERP` omits the scalar field for skew-symmetric eigenvalues

- **Object and need:** `P-2HERP` asks what can be said about eigenvalues of a skew-symmetric matrix, but the answer depends on the scalar field and on whether eigenvalues are taken in the base field or an algebraic closure.
- **Observed evidence:** The current card and every locally recoverable historical version contain only the same sentence and no field hypothesis. Over $\RR$, nonzero eigenvalues occur in purely imaginary conjugate pairs after complexification; over a general field the formulation is different.
- **Impact and owner:** The owning file `corpus/problems/Algebra/P-2HERP.md` is not precise enough to admit a unique source-faithful solution.
- **Uncertainty:** The intended real-matrix reading is plausible but not recoverable from local source/history.
- **Repair:** Recover the original source context or otherwise establish the intended scalar field before authoring the solution.

### `P-27BNG` has no mathematical task after its hypothesis

- **Object and need:** `P-27BNG` must contain a posed mathematical question or conclusion after the hypothesis on a finite Galois extension $K/F$.
- **Observed evidence:** The complete card body is only `Suppose $K/F$ is a finite, normal, Galois extension.` Git history back through intake contains exactly the same text; the original title was just that sentence, and the card appears only in `SRC-UNSORTED-ALGEBRA`. Searches of the current corpus/wiki found no matching continuation.
- **Impact and owner:** There is no proposition to prove, so `corpus/problems/Algebra/P-27BNG.md` cannot receive a mathematically meaningful solution without fabricating missing source content.
- **Uncertainty:** The intended follow-up is unknown. `normal` and `Galois` are also redundant under standard finite-extension terminology, but that does not identify the missing task.
- **Repair:** This requires source recovery or an explicit editorial decision supplying the missing conclusion. Until then, leave the card unsolved and do not infer a theorem from the title alone.


\n\n\n## Workflow and rendering papercuts

### Local repository connector and batched authoring query failures

- **Object and need:** Algebra solution authoring needs reliable local repository access and the existing authoring-query commands so a worker can inspect the shared state and derive an unsolved worklist without touching `queues/C-unsolved-cards.md`.
- **Observed evidence:** On 2026-09-09, the first local terminal call failed before execution with `Tunnel-client has not been seen for 300 seconds`. After switching to the second connected terminal endpoint, a read-only batched command combining collection discovery with several `just unsolved-in` queries was blocked by the execution safety layer before running, while the same collection-discovery command succeeded when retried alone. The first `just unsolved-in SRC-UCSD-ALG-FALL-2008` invocation also exceeded the 30-second foreground-yield window and had to be left running with redirected output for later inspection. Later in the same Algebra stream, prose-only commits were mistakenly sent through the full pre-commit gate before the repository's documented prose-only exemption was re-read; Semgrep then spent several minutes in uninterruptible I/O (`folio_wait_bit_common`) and an optional `just check-card E-LUH54` likewise stalled in I/O.
- **Impact and owner:** This does not change corpus mathematics, but it interrupts the repository-prescribed workflow of reading current state and selecting work through project tooling. The affected boundary is the local connector/execution environment rather than `qualc` semantics.
- **Uncertainty:** The connector failure is verified from the returned error. The safety block is verified for that specific batched shell command only; the exact classifier trigger is unknown. The long `unsolved-in` latency may be normal Pandoc startup/parsing cost rather than a repository defect.
- **Repair:** No existing TODO task owns the external connector/runtime. A resolving result would be stable local terminal availability, predictable execution of read-only project commands, and foreground authoring queries that either complete or expose a supported continuation mechanism instead of losing their result after the yield limit.
