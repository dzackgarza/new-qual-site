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


\n\n\n


### `P-CEZOG` contains no posed problem

- **Object and need:** `P-CEZOG` is classified as a problem card but contains only a definition of the order of a cyclic module in terms of the annihilator of a generator.
- **Observed evidence:** The complete local history preserves the same declarative fragment from intake onward; no question, requested proof, or missing continuation survives in any revision.
- **Impact and owner:** `corpus/problems/Algebra/P-CEZOG.md` remains parser-unsolved, but there is no source-faithful task to solve.
- **Uncertainty:** The intended exercise is unrecoverable from local history and the unsorted collection provides no external source text.
- **Repair:** Recover the original source/question before converting the definition fragment into a posed problem; do not invent a task from the title alone.


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

### `P-CEZOG` is a definition fragment, not a posed problem

- **Object and need:** `P-CEZOG` is classified as a problem card but contains only the definition of the order ideal of a generator in a cyclic module and the consequence $ra=0$.
- **Observed evidence:** The body contains no imperative, question, or theorem to prove; it simply states `A has order r iff ... O_a=(r)` and `In particular, ra=0`.
- **Impact and owner:** There is no mathematically determined solution to attach without inventing a task. The owning file is `corpus/problems/Algebra/P-CEZOG.md`.
- **Uncertainty:** The intended source exercise is not recoverable from the surviving card text alone.
- **Repair:** Recover the original source prompt or reclassify the fragment as theory/definition material; do not fabricate a problem statement from the surviving definition.

### `P-FHDRZ` does not specify the base finite field

- **Object and need:** `P-FHDRZ` asks for “the smallest finite field” in which a quartic with integer coefficients necessarily has four roots.
- **Observed evidence:** A finite field has a fixed characteristic, while the card supplies only an integer polynomial and no prime $p$ or reduction modulo $p$. Local history shows the same wording from intake onward and contains no missing base-field clause.
- **Impact and owner:** There is no uniquely determined finite field answering the literal question. If the intended problem were “over $\FF_p$,” then the smallest uniform extension splitting every quartic would be $\FF_{p^{12}}$, but choosing that interpretation would add a hypothesis not present in the source. The owning file is `corpus/problems/Algebra/P-FHDRZ.md`.
- **Uncertainty:** The likely intended finite-field exercise is clear, but the prime/base field is not source-recoverable.
- **Repair:** Recover the original source context and specify the base field (for example $\FF_p$) before authoring a solution.


### `P-GSJ2A` omits the scalar field for the symmetric-matrix eigenvalue question

- **Object and need:** `P-GSJ2A` asks only “What are the eigenvalues of a symmetric matrix?”
- **Observed evidence:** For a real symmetric matrix, all eigenvalues are real and the matrix is orthogonally diagonalizable. For a complex matrix satisfying only $A^t=A$, eigenvalues need not be real; the corresponding spectral theorem uses Hermitian matrices instead.
- **Impact and owner:** The answer depends materially on the missing field/adjoint convention. The owning file is `corpus/problems/Algebra/P-GSJ2A.md`.
- **Uncertainty:** The surrounding topics suggest the standard real spectral theorem, but the surviving card contains no explicit field.
- **Repair:** Recover source context or state explicitly that $A$ is real symmetric before authoring the spectral-theorem answer.

### `P-HEOYS` does not specify what parts of the tetrahedron are colored

- **Object and need:** `P-HEOYS` asks for colorings of a tetrahedron with $C$ colors up to symmetry.
- **Observed evidence:** The card never says whether colors are assigned to vertices, faces, edges, or another set. These actions have different orbit counts. Git history shows the same wording from intake onward, so the missing object is not recoverable locally.
- **Impact and owner:** Burnside's lemma cannot produce a unique answer until the colored set is specified. The owning file is `corpus/problems/Algebra/P-HEOYS.md`.
- **Uncertainty:** Vertex- and face-coloring counts agree because both actions are the natural $S_4$ action on four objects, but edge-coloring gives a different answer; choosing among them would be speculation.
- **Repair:** Recover source context and specify the colored set before authoring the Burnside count.

### `P-HXTMK` incorrectly treats a minimal polynomial as determining a unique rational canonical form

- **Object and need:** `P-HXTMK` attempts to determine rational canonical forms from specified minimal polynomials and ambient dimensions.
- **Observed evidence:** In the second case it assumes $m_A=(x^2+1)^2(x^3+1)$ and $\deg\chi_A=10$, then claims this forces $\chi_A=(x^2+1)^2(x^3+1)^2$. It does not. Over $\QQ$, $x^3+1=(x+1)(x^2-x+1)$, and the additional degree $3$ in the characteristic polynomial can be distributed among these irreducible factors in more than one way while keeping the same minimal polynomial. The body is also a worked solution fragment rather than a posed problem.
- **Impact and owner:** The claimed uniqueness of the second rational canonical form is false from the supplied data. The owning file is `corpus/problems/Algebra/P-HXTMK.md`.
- **Uncertainty:** The original exercise may have supplied characteristic polynomials or additional rank/nullity data that were lost in extraction, but no such hypotheses survive in the card.
- **Repair:** Recover the original source data. Without more information, restate the task as classifying all possible characteristic polynomials/invariant-factor lists rather than asserting a unique rational canonical form.

### `P-JH3EW` does not determine a Galois group without square-class hypotheses

- **Object and need:** `P-JH3EW` asks for $\mathrm{Gal}(\QQ(\sqrt{n_1},\ldots,\sqrt{n_m})/\QQ(\sqrt{n_1}+\cdots+\sqrt{n_m}))$ with no assumptions on the integers $n_i$.
- **Observed evidence:** The multiquadratic extension and the stabilizer of the displayed sum depend on relations among the square classes of the $n_i$; repeated or dependent radicals can change both the top field and the fixed subgroup.
- **Impact and owner:** There is no unique answer from the surviving statement. The owning file is `corpus/problems/Algebra/P-JH3EW.md`.
- **Repair:** Recover the source hypotheses (typically independent square classes, often distinct squarefree positive integers) before authoring a specific Galois group.

### `P-KSSA7` uses an invalid order argument for the dihedral criterion

- **Object and need:** `P-KSSA7` correctly embeds the Galois group of $x^n-2$ into $\ZZ/n\ZZ\rtimes(\ZZ/n\ZZ)^\times$, then claims it is dihedral of order $2n$ exactly when $\varphi(n)=2$ because the affine-group order bound $n\varphi(n)$ exceeds $2n$ when $\varphi(n)>2$.
- **Observed evidence:** An upper bound exceeding $2n$ says nothing about whether the actual subgroup has order $2n$. For $n=8$, the splitting field has degree $16=2n$ because $\QQ(2^{1/8})\cap\QQ(\zeta_8)=\QQ(\sqrt2)$, yet the Galois group is not dihedral: one obtains generators with relation $srs^{-1}=r^3$ rather than $r^{-1}$ (the semidihedral group of order $16$).
- **Impact and owner:** The stated conclusion may still be true with a correct proof, but the supplied deduction is invalid and the $\varphi(n)=4$ cases require separate analysis. The owning file is `corpus/problems/Algebra/P-KSSA7.md`.
- **Repair:** Keep the affine embedding, prove the $n=3,4,6$ dihedral cases directly, then rule out all $\varphi(n)>2$ cases by a valid group/field argument, treating $\varphi(n)=4$ ($n=5,8,10,12$) explicitly.

### `P-LZRAH` omits the characteristic needed for the trace-power criterion

- **Object and need:** `P-LZRAH` asks what follows from $\operatorname{tr}(A^k)=0$ for all $k$ but does not specify the scalar field.
- **Observed evidence:** In characteristic $p$, the identity matrix of size $p$ satisfies $\operatorname{tr}(I^k)=p=0$ for every $k$ but is not nilpotent. Over characteristic $0$, Newton identities imply that vanishing power sums force the characteristic polynomial to be $x^n$, hence $A$ is nilpotent.
- **Impact and owner:** The literal statement has different answers in different characteristics. The owning file is `corpus/problems/Algebra/P-LZRAH.md`.
- **Repair:** State that the matrix is over a field of characteristic $0$ (or impose the corresponding Newton-identity invertibility hypotheses) before concluding nilpotence.

