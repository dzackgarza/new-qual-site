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

### Berkeley Spring 1997 Problem 18 does not specify whether the direct product is finite

- **Object and need:** `P-BERK97S-18` / `SRC-BERKELEY-PRELIM-SPRING-1997`,
  Problem 18(2). The source asks whether an extension splits when the quotient
  is "a direct product of infinite cyclic groups" but does not say whether the
  product has finitely many factors.
- **Observed evidence:** the retained Spring 1997 extraction prints exactly
  that wording. For a finite product, the quotient is `\ZZ^r` and a basis can
  be lifted to split the quotient map. For an arbitrary infinite product the
  claim is false in general: the Baer--Specker group
  `\prod_{n\geq1}\ZZ` is not free, so a free presentation of it cannot split
  as the quotient times its kernel.
- **Impact and owner:** a proof that lifts the coordinate generators silently
  assumes the finite-product (equivalently here, finite-rank free-abelian)
  reading. The owning card must distinguish that case from a literal arbitrary
  infinite product.
- **Uncertainty:** the source's intended convention is unknown.
  **Searched:** current `assets/`, `sources/`, and Git history for
  `Spring97`, Spring 1997 solution variants, and the exact statement.
  **Found:** the exam PDF and its extraction, but no solution packet or prior
  authoritative solution. **Conclusion:** no authoritative retained solution
  resolving the convention was found. **Confidence:** high for the current
  repository. **Gaps:** external Berkeley archives were not searched.
- **Repair:** `P-BERK97S-18` now proves the finite-product reading and records
  the arbitrary-infinite-product counterexample. Keep this source-intent note
  until an authoritative Berkeley solution or convention resolves the wording.

### Azoff Möbius symmetry problem has a false fourth equivalent condition

- **Object and need:** \`P-AZOFF-C12\` / \`SRC-AZOFF-PROBLEMS-BY-TOPIC\`,
  Conformal mapping Problem 12. The source asks to prove four conditions on a
  Möbius transformation equivalent; condition (d) requires a real fixed point
  \(\alpha\) in addition to one nonreal conjugation-compatible point.
- **Observed evidence:** page 3 of the retained PDF prints
  \(T(\alpha)=\alpha\) with no overbar on either occurrence of \(\alpha\).
  The PDF vector data separately shows the overbars in
  \(T(\overline\beta)=\overline{T\beta}\), so the fixed-point clause is not an
  extraction loss. The Möbius transformation
  \(T(z)=-1/z\) has real coefficients and therefore satisfies (a)--(c), but
  its fixed-point equation is \(z^2=-1\), so it has no real fixed point and
  fails (d).
- **Impact and owner:** the printed four-way equivalence cannot be proved.
  The owning problem card must state the true implication pattern before its
  solution is authored.
- **Uncertainty:** verified against the rendered PDF, its text layer, and the
  vector rules carrying the overbars. The mathematical counterexample is
  exact; whether the source author intended a different condition (d) is
  unknown.
- **Repair:** correct \`P-AZOFF-C12\` to ask for the equivalence of (a)--(c),
  prove that printed (d) implies them, and record that the converse fails via
  \(T(z)=-1/z\). Preserve the printed source error as a durable erratum on
  the card.

### Zaidenberg Definition 4.3 makes the following finite-morphism exercises inconsistent

- **Object and need:** \`SRC-AGX-VARIETIES-PROBLEMS\`, Definition 4.3 and
  Exercises 4.4. The standard definition of a finite morphism does not require
  the comorphism to be injective.
- **Observed evidence:** page 6 of the recorded PDF says that a finite morphism
  has an "embedding" $f^*:O(Y)\to O(X)$, while the same exercise immediately
  asks for a non-surjective finite morphism. An injective module-finite
  comorphism is integral, so lying over makes the corresponding affine map
  surjective.
- **Impact and owner:** the source wording cannot govern cards about finite
  morphisms. \`P-AGXVARFINCLOSED\` records and uses the repository definition
  \`D-MORFIN\`, under which the exercise is coherent.
- **Uncertainty:** verified in the PDF with two independent text extractors;
  this may be a typo in the source rather than an intended nonstandard
  convention.
- **Repair:** retain the standard repository definition and treat the printed
  word "embedding" as source errata unless a corrected source edition is found.

### Berkeley Fall 2006 Problem 6A solution packet uses irreducibility circularly

- **Object and need:** `P-BKF06-6A` / `SRC-BERKELEY-PRELIM-FALL-2006`,
  Problem 6A. The retained solution packet proves that
  $x^p-x+1$ is irreducible over $\FF_p$ by analyzing subsets of its translated
  roots.
- **Observed evidence:** `assets/attachments/extracted/f06solution.md` says
  that $(\#I)\alpha\in\FF_p$ and then states “Since f is irreducible,
  $\alpha\notin\FF_p$,” using the desired conclusion to justify the key
  contradiction. The needed independent fact is immediate instead:
  $f(a)=a^p-a+1=1$ for every $a\in\FF_p$, so no root of $f$ lies in
  $\FF_p$.
- **Impact and owner:** the source solution has a circular proof at the
  decisive factor-exclusion step. The owning authored card must not inherit
  that circularity.
- **Uncertainty:** the circular sentence is present in the retained solution
  extraction, and the replacement argument is exact. No claim is made that a
  different edition of the source packet contains the same sentence.
- **Repair:** `P-BKF06-6A` now proves $\alpha\notin\FF_p$ directly from
  $f(a)=1$ before applying the root-sum argument. Retain this entry as source
  errata; the provenance packet itself is not rewritten.

### Berkeley Fall 2006 Problem 8A solution packet gives the wrong cokernel torsion

- **Object and need:** `P-BKF06-8A` / `SRC-BERKELEY-PRELIM-FALL-2006`,
  Problem 8A. The source asks for the kernel, image, and cokernel of the
  displayed integer matrix.
- **Observed evidence:** `assets/attachments/extracted/f06solution.md`
  displays an integral equivalence reducing the matrix to
  `diag(3,0,0)`, but then states
  `cokernel(A) ≅ Z^2 ⊕ Z/2Z`. The displayed diagonal form instead gives
  `Z^2 ⊕ Z/3Z`. Directly, the image is generated by
  $(3,3,6)=3(1,1,2)$, with $(1,1,2)$ primitive, so the quotient has a
  torsion class of exact order $3$.
- **Impact and owner:** importing the source conclusion verbatim would give
  the wrong abelian-group structure on the authored card.
- **Uncertainty:** the contradiction is internal to the retained solution
  packet and independently verified from the matrix. It is consistent with a
  typographical `2` for `3` in the packet's prose.
- **Repair:** `P-BKF06-8A` now computes the image directly and records
  `coker(A) ≅ Z^2 ⊕ Z/3Z`. Retain this entry as source errata; the
  provenance packet itself is not rewritten.

### Berkeley Fall 2006 Problem 1B solution packet omits the factorial in Cauchy's estimate

- **Object and need:** `P-BKF06-1B` / `SRC-BERKELEY-PRELIM-FALL-2006`,
  Problem 1B. The retained proof uses Cauchy's estimates to force all positive
  derivatives of an entire function to vanish.
- **Observed evidence:** `assets/attachments/extracted/f06solution.md`
  states
  `|f^(m)(0)| <= (2^n M)/(R_n)^m`. For ordinary derivatives, Cauchy's
  estimate is
  `|f^(m)(0)| <= m! M(R_n)/(R_n)^m`; the factor `m!` is missing.
- **Impact and owner:** the printed inequality is not the standard derivative
  estimate, although the omitted constant is independent of `n` and the
  argument still tends to zero after it is restored.
- **Uncertainty:** verified against the retained extraction and the standard
  Cauchy integral formula. No normalized-derivative convention is stated in
  the packet.
- **Repair:** `P-BKF06-1B` includes the factor `m!` and retains the same
  limiting argument. Retain this entry as source errata; the provenance
  packet itself is not rewritten.

### Berkeley Fall 2012 Problem 7B solution packet uses a non-invariant quotient

- **Object and need:** P-BKF12-7B / SRC-BERKELEY-PRELIM-FALL-2012,
  Problem 7B. The retained solution packet must prove that a linear map
  satisfying $AB-BA=A$ is nilpotent.
- **Observed evidence:** assets/attachments/extracted/F12_Solutions.md
  first correctly computes
  $BAv=(\lambda-1)Av$ for a $B$-eigenvector $v$, but its final induction
  then says that $A$ is nilpotent on $V/\CC v$. The displayed relation only
  shows that $Av$ is zero or belongs to the $(\lambda-1)$-eigenspace; it does
  not show $Av\in\CC v$. Thus $\CC v$ need not be $A$-invariant, so $A$
  need not induce an operator on that quotient and the induction step is not
  defined.
- **Impact and owner:** the source solution does not establish the requested
  nilpotence. The owning authored card must supply an independent argument
  rather than inherit the quotient induction.
- **Uncertainty:** the invalid quotient step is present in the retained
  solution extraction. The preceding eigenvector calculation is correct, and
  no claim is made that another edition of the solution packet has the same
  final paragraph.
- **Repair:** P-BKF12-7B now uses the generalized eigenspace decomposition
  of $B$ and the identity
  $(B-(\lambda-1)I)A=A(B-\lambda I)$ to show that $A$ shifts generalized
  eigenspaces from $\lambda$ to $\lambda-1$ and hence satisfies
  $A^{\dim V}=0$. Retain this entry as source errata; the provenance packet
  itself is not rewritten.

## Workflow and rendering papercuts

### Overlapping workstream owners edited the same Author-solutions card

- **Object and need:** the `new-qual-site` Core2 workstream must have one
  active author on its selected card, under `QUAL-03` and `QUAL-07`.
- **Observed evidence:** on 2026-09-22, repeated successful `workstream`
  continuation calls were followed by `WORKSTREAM_SETUP_REQUIRED` on calls
  carrying the returned ID. One response explicitly reported a superseded
  owner's already-admitted call still settling. During the same session,
  `1b56ef019` committed `P-BERK90S-07` with this session's partial solution
  followed by another complete solution; subsequent edits completed the
  first block, producing two proofs of the same integral by the same method.
- **Impact and owner:** the workstream handoff/dispatch boundary permits
  overlapping authorship and rejected calls. This is not a corpus parser,
  mathematical, or publication-gate defect.
- **Uncertainty:** the rejected calls and overlapping card contents were
  observed directly; the mechanism initiating the competing continuations
  has not been established.
- **Repair:** the card is reconciled by removing this session's duplicate
  and retaining the other complete proof unchanged. The external handoff
  remains unresolved: a successor must not race a still-writing predecessor,
  and must reread the final settled card before editing it.
