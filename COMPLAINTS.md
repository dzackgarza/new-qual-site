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

### `P-27BNG` has no mathematical task after its hypothesis

- **Object and need:** `P-27BNG` must contain a posed mathematical question or conclusion after the hypothesis on a finite Galois extension $K/F$.
- **Observed evidence:** The complete card body is only `Suppose $K/F$ is a finite, normal, Galois extension.` Git history back through intake contains exactly the same text; the original title was just that sentence, and the card appears only in `SRC-UNSORTED-ALGEBRA`. Searches of the current corpus/wiki found no matching continuation.
- **Impact and owner:** There is no proposition to prove, so `corpus/problems/Algebra/P-27BNG.md` cannot receive a mathematically meaningful solution without fabricating missing source content.
- **Uncertainty:** The intended follow-up is unknown. `normal` and `Galois` are also redundant under standard finite-extension terminology, but that does not identify the missing task.
- **Repair:** This requires source recovery or an explicit editorial decision supplying the missing conclusion. Until then, leave the card unsolved and do not infer a theorem from the title alone.


\n\n\n


### `P-CVUQ3` reverses the semidirect-product factors

- **Object and need:** `P-CVUQ3` claims $\Gal(x^{15}+2/\QQ)\cong S_2\rtimes \ZZ/15\ZZ$ with $S_2$ a Sylow $2$-subgroup.
- **Observed evidence:** The repository macro `\semidirect` is `\rtimes`, so its first factor is the normal factor. For the splitting field $L=\QQ(\alpha,\zeta_{15})$ with $\alpha^{15}=-2$, the subgroup $\Gal(L/\QQ(\zeta_{15}))\cong C_{15}$ is normal, while a complement is $\Gal(\QQ(\zeta_{15})/\QQ)\cong(\ZZ/15\ZZ)^\times\cong C_4\times C_2$, of order $8$ and hence Sylow $2$. The Sylow-$2$ complement is not the normal factor in the natural affine/Kummer presentation.
- **Impact and owner:** The displayed semidirect product in `corpus/problems/Algebra/P-CVUQ3.md` has the factors in the wrong order.
- **Uncertainty:** None; the degree calculation gives $|G|=15\cdot8=120$ and the cyclotomic fixed-field subgroup identifies the normal $C_{15}$ canonically.
- **Repair:** State $\Gal(L/\QQ)\cong C_{15}\rtimes (\ZZ/15\ZZ)^\times$, equivalently $C_{15}\rtimes S_2$, and prove the splitting/complement structure.

### `P-CWZF3` omits nonzero from the prime-ideal PID criterion

- **Object and need:** `P-CWZF3` says $R/(p)$ is a field when $(p)$ is prime in a PID.
- **Observed evidence:** In the PID $\ZZ$, the ideal $(0)$ is prime but $\ZZ/(0)\cong\ZZ$ is not a field. The standard theorem is that every nonzero prime ideal in a PID is maximal.
- **Impact and owner:** `corpus/problems/Algebra/P-CWZF3.md` is false if $p=0$ is allowed.
- **Uncertainty:** None.
- **Repair:** Require $(p)\ne(0)$ (equivalently a nonzero prime element $p$) and prove maximality/field quotient.

### `P-D7DNH` and `P-DB3EP` are solution fragments stored as problems

- **Object and need:** Both cards are classified as problems but contain only attempted solution prose rather than posed tasks.
- **Observed evidence:** `P-D7DNH` begins with application of the structure theorem and a claimed Smith form; `P-DB3EP` begins with one implication of a proof. Their titles recover the intended tasks, and the displayed matrix in `P-D7DNH` is sufficient to state its quotient computation precisely.
- **Impact and owner:** The cards are parser-unsolved despite already containing proof-like text, and the public problem surface does not actually pose the exercise.
- **Uncertainty:** None about the intended theorem/computation from the titles and surviving data.
- **Repair:** Restore explicit problem statements, independently verify the Smith invariants / matrix-equation equivalence, and move the reasoning into structured solution blocks.

## Workflow and rendering papercuts

### Local repository connector and batched authoring query failures

- **Object and need:** Algebra solution authoring needs reliable local repository access and the existing authoring-query commands so a worker can inspect the shared state and derive an unsolved worklist without touching `queues/C-unsolved-cards.md`.
- **Observed evidence:** On 2026-09-09, the first local terminal call failed before execution with `Tunnel-client has not been seen for 300 seconds`. After switching to the second connected terminal endpoint, a read-only batched command combining collection discovery with several `just unsolved-in` queries was blocked by the execution safety layer before running, while the same collection-discovery command succeeded when retried alone. The first `just unsolved-in SRC-UCSD-ALG-FALL-2008` invocation also exceeded the 30-second foreground-yield window and had to be left running with redirected output for later inspection. Later in the same Algebra stream, prose-only commits were mistakenly sent through the full pre-commit gate before the repository's documented prose-only exemption was re-read; Semgrep then spent several minutes in uninterruptible I/O (`folio_wait_bit_common`) and an optional `just check-card E-LUH54` likewise stalled in I/O. The same stream later had a delayed batched shell command complete after its foreground result had already been lost; it staged `P-IVRLI` and then committed `P-IVRLI` together with `P-J3FBW`, crossing the intended one-card-per-commit boundary despite separate commit commands.
- **Impact and owner:** This does not change corpus mathematics, but it interrupts the repository-prescribed workflow of reading current state and selecting work through project tooling. The affected boundary is the local connector/execution environment rather than `qualc` semantics.
- **Uncertainty:** The connector failure is verified from the returned error. The safety block is verified for that specific batched shell command only; the exact classifier trigger is unknown. The long `unsolved-in` latency may be normal Pandoc startup/parsing cost rather than a repository defect.
- **Repair:** No existing TODO task owns the external connector/runtime. A resolving result would be stable local terminal availability, predictable execution of read-only project commands, and foreground authoring queries that either complete or expose a supported continuation mechanism instead of losing their result after the yield limit.

### Algebra P-O5YG6, P-OC42E, and P-ODNWF hypothesis defects

### Algebra P-OLLG3, P-OPR5T, and P-OQCJR presentation gaps

### Algebra P-OU7QZ, P-P4KA6, and P-PDRT9 statement/source defects

### Algebra P-SB67D: ambiguous meaning of `Z[w]`

`P-SB67D` asks whether `Z[t]/(t^p-1) -> Z[w]`, `t -> w`, is an isomorphism while stating only `w^p=1`. If `w` is a primitive complex p-th root, then `Z[w] ~= Z[t]/(Phi_p(t))` and the displayed map is not injective. If `Z[w]` is instead the universal ring generated by a formal element with only the relation `w^p=1`, then the map is an isomorphism by construction. The surviving card does not specify which meaning is intended, so the problem has no unique answer without source recovery.

### `P-S5JSR` is a compound Galois exercise card with a truncated item and a false dihedral subclaim

- **Object and need:** `corpus/problems/Algebra/P-S5JSR.md` contains a dozen separate Galois exercises in one card.
- **Observed evidence:** One bullet ends at “Show that $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$” with no conclusion. The first bullet also repeats the defective claim already identified on `P-KSSA7`: from the affine-group embedding for the splitting field of $x^n-2$, it asserts the group is dihedral of order $2n$ exactly for $n=3,4,6$ using an insufficient order-bound argument. The original missing conclusion of the truncated bullet is not recoverable from this card.
- **Impact and owner:** A complete solution cannot be authored without inventing at least one missing problem statement, and accepting the first bullet as written would preserve a known mathematical defect. The owning file is `corpus/problems/Algebra/P-S5JSR.md`.
- **Repair:** Recover the source statement for the truncated bullet and correct the $x^n-2$ Galois-group assertion before solving the compound card.
