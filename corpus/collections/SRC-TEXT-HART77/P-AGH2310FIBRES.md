---
schema: qual/card@1
id: P-AGH2310FIBRES
kind: problem
title: Fibres of a morphism as schemes over the residue field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibre Products
  - Fibres
  - Residue Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.10 statement; the nonzero closed-fibre claim requires char(k) != 2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Hartshorne II.3.10(b) assumes only that k is algebraically closed, and in characteristic 2 the fibre over a != 0 is one nonreduced point, so the printed two-point assertion is false there. The card keeps the printed hypothesis and proves the two-point assertion under char k != 2, with the characteristic-2 fibre computed as a counterexample.

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), II.3.10(b),
    printed p. 92. A further published solution was located outside the twelve
    retained sets and it repeats the defect rather than repairing it:
    A. Shichijo, R.Hartshorne "Algebraic Geometry" 演習問題への解答
    (2020/March), <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>,
    Chapter 2 section 3, Exercise 3.10(b), printed p. 7, read in the MinerU
    extraction tmp/sources/shitijyou-ch2-section3.md, computes
    k[s,t]/(s-t^2) tensor_{k[s]} k[s,u]/(s-a,u) = k[t]/(t^2-a) and then writes
    that ring as k[t]/(t-sqrt a) x k[t]/(t+sqrt a) by the Chinese remainder
    theorem. That factorization needs the two roots distinct, i.e. char k != 2;
    in characteristic 2, a = r^2 and t^2-a = (t-r)^2, the ring is k[t]/((t-r)^2),
    one nonreduced point with residue field k, exactly the counterexample this
    card keeps as a step. The same slip is at Kim, PDF p. 23, text version `tmp/sources/hartshorne-solutions-kim.md` and Cais, 3.10(b).
    So no located source proves the printed two-point assertion in
    characteristic 2, and none can: the printed statement is false there. The
    card keeps its characteristic-two computation and the repair stays open on an
    erratum or on the owner's acceptance.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The text version of the Cais solutions now exists: it is read in
    tmp/sources/hartshorne-solutions-cais.pdf and in its MinerU text version
    tmp/sources/hartshorne-solutions-cais.md. The event above predates that file, records
    what was read from the PDF alone, and is left as it was dated.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Transcription pass for issue #121: the proof on the card is now the
    published argument with its source named at every step. Read at the
    cited places: Dongryul Kim, Exercise 2.3.10, PDF p. 23, text version
    tmp/sources/hartshorne-solutions-kim.md; the Cais solutions, Exercise
    3.10, PDF p. 12 of 29, the file having no printed folio, text version
    tmp/sources/hartshorne-solutions-cais.md; A. Shichijo, Exercise 3.10,
    printed p. 7, text version tmp/sources/shitijyou-ch2-section3.md; A.
    Egbert, Exercise II.3.10, printed p. 84, text version
    tmp/sources/hartshorne-solutions-egbert.md; Math StackExchange 1709194,
    comments 3488648 and 3489729, text version
    tmp/sources/mse-1709194-geometric-generic-fibre-hart-ii310.md. Checked
    against the book in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    where printed p. N is PDF p. N+15: II.3.10 as printed on p. 92, with
    its sole hypothesis that k is algebraically closed and its three
    assertions. What the transcription records beyond the earlier events:
    Egbert's idempotents carry the denominator 2 sqrt 2 where 2 sqrt a
    belongs, a misprint; Kim, Cais, Shichijo and Egbert reach k x k for
    the fibre over a != 0 only with char k != 2, and Cais writes that
    fibre as the two points (s-a, t - sqrt a) and (s-a, t + sqrt a)
    without the hypothesis. The two-point assertion of the exercise in
    characteristic 2 has no published proof and can have none, which the
    COMPLAINTS record of 2026-11-16 names. The card's own contributions
    are now confined to the characteristic-two computation and the
    valuation check of the irreducibility of t^2 - s, and both say so.
    Not checked: no source beyond the five named was searched in this
    pass, and no machine computation was run.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Page correction, on the transcription committed earlier today. The
    citation of Shichijo in the event above gives printed p. 7 for Exercise
    3.10 as a whole, and that is too narrow: the exercise's heading stands
    on printed p. 5, its part (a) runs pp. 5--7, and its part (b) runs pp.
    7--8 --- the lemma and the Chinese-remainder computation for a
    different from 0 on p. 7, the fibre over 0 and the generic fibre on p.
    8. Read in the PDF tmp/sources/shitijyou-ch2-section3.pdf, whose
    printed folio equals its PDF page: p. 5 carries the heading "Ex3.10
    Fibres of a Morphism", p. 6 the tensor computation and the equivalence
    (*), p. 7 the general case of (a), the lemma and the k x k display, p.
    8 the cases y = (s) and y = (0), including the irreducibility of t^2 -
    s and the degree-two residue field. The body of the card now cites
    those pages, and the event above is left as written. Not checked: no
    other page number on this card was re-read in this pass.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report. (i) The letters were inconsistent: this
    proof writes B for the base ring and A for the coordinate ring of the
    total space, taking that from its first step, while Kim, Cais and
    Egbert write A for the base and B for the total. Their displays in the
    steps fibre-ring-tensor-localization and
    uy-points-correspond-to-primes and uy-homeomorphism-onto-fiber are now
    stated in the letters of this proof, with a note at the first step and
    one in the remark that A and B are exchanged and nothing else; the one
    verbatim quotation (Kim's "we may assume first that Y is affine")
    carries no letters. Shichijo's phi : B -> A already matches. (ii) The
    remark's sentence "The proof above is the published argument with its
    sources named at each step" is removed as commentary on how the card
    was written. Checked against the book in
    tmp/sources/hartshorne-1977-algebraic-geometry.md (printed p. N is PDF
    p. N+15): II.3.10 on printed p. 92. Not checked: no source was re-read
    in this pass beyond the passages quoted, and no step was re-derived.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, two items. (i) The letter exchange the
    previous pass announced was incomplete. This proof writes B for the base
    ring and A for the coordinate ring of the total space; two places kept
    Cais's letters. The first is his display in step
    reduce-fibre-topology-to-affine, which read X_y = (X times_Y Spec A)
    times_{Spec A} Spec kappa(y) while the sentence introducing it says it is
    in the letters of this proof; with Spec B the affine neighbourhood of y
    it is (X times_Y Spec B) times_{Spec B} Spec kappa(y). The second is the
    image in step uy-homeomorphism-onto-fiber, written Spec phi(Spec B): phi
    there has source Spec(A tensor_B B_m), and the image lies in Spec A, so
    it is Spec phi(Spec(A tensor_B B_m)). Nothing else moves; Cais's own
    factorization and his S = g(A - p) remain quoted in his letters with the
    note already there. (ii) Two sentences of process left the rendered
    card: the pf-qed's "are the published proof of (a)" and the remark's
    "Two of the six parts are not published in the form the exercise prints"
    with its "asserted by the four sources rather than proved". What they
    recorded belongs here. The five steps of (a) are Cais's argument with
    Kim's reduction, Shichijo's affine computation and Egbert's chain, as the
    remark cites them; the two-point assertion is published by all four
    sources only under char k not 2, none of them saying that the roots must
    be distinct, and the failure in characteristic two is recorded only at
    Math StackExchange 1709194; the irreducibility of t^2 - s over k(s) is
    asserted by the four sources and proved on the card by the valuation. The
    pf-qed and the remark now state the mathematics, the remark keeping the
    characteristic hypothesis and the pointer to the quoted comments. Checked
    against the book in tmp/sources/hartshorne-1977-algebraic-geometry.md
    (printed p. N is PDF p. N+15): II.3.10 on printed p. 92; Cais's Exercise
    3.10(a) re-read in tmp/sources/hartshorne-solutions-cais.md at PDF p. 12
    of 29. Not checked: no step was re-derived in this pass, and no source
    beyond Cais's passage was re-read.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on two letters and one kernel in step
    uy-homeomorphism-onto-fiber. (i) Cais's factorization of the projection
    carries his own two maps, phi and psi, and his phi there is the structure
    map of the localization, A -> A tensor_B B_m, not Shichijo's phi : B -> A
    that the earlier steps of this proof quote; the map in the display is now
    written theta, with Cais's phi named as his in the sentence that follows it,
    so that phi denotes one map in the proof. (ii) The kernel of psi :
    A tensor_B B_m -> A tensor_B kappa(m) is the ideal the base prime generates
    in A tensor_B B_m, m(A tensor_B B_m), and not m A, an ideal of A: the source
    of psi is A tensor_B B_m. What the prime-level statement needs is that a
    prime of A meeting S = g(B - m) trivially contains the contraction of that
    kernel exactly when it contains m A = g(m)A, an element of S being outside
    the prime; with that the image of the composite is the set of primes of A
    containing m A and meeting S trivially, which is the set of primes
    contracting to m, and the step now says so rather than naming the kernel
    alone. Read in this
    pass: Cais, Exercise 3.10(a), PDF p. 12 of 29, the file having no printed
    folio, text version tmp/sources/hartshorne-solutions-cais.md, whose line 281
    carries the factorization B -> B tensor_A A_p -> B tensor_A k(p) and line 283
    the two homeomorphisms and "Since ker psi = pB"; the letters A and B of that
    source are the base and the total space, the opposite of this card's, as the
    first step of the proof records. Not checked: Shichijo's printed p. 6 was not
    re-read, the other steps of this proof were not re-derived, and no machine
    computation was run in this pass.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, two items of the rendered card. (i) Cais's
    kernel. The event above of even date, whose note begins "Repair on the
    reader's report, on two letters and one kernel", quotes his line 283 as
    "Since ker psi = pB" and does not say whose the sentence is; it is left as
    written, and the slip is named on the card. In Cais's letters B is the total
    space and p the base prime, so his pB is an ideal of B, whereas psi has
    B tensor_A A_p as its source; the step uy-homeomorphism-onto-fiber now says
    that the identity is his slip of notation, states the kernel as
    m(A tensor_B B_m) and proves the prime-level form his argument uses. The
    step's earlier ker psi = m A was that imprecision transcribed faithfully, so
    the kernel is his error and not the card's; the letter collision, his phi
    naming both the localization map and Shichijo's B -> A, was the card's and
    stands repaired where it was made. (ii) The head of the solution no longer
    names the text versions of the five sources: the paths stay in the
    transcription event of even date, which names them, and a rendered solution
    carries the mathematics and not the file store (PROSE-11, QUAL-08). Read in
    this pass: Cais, Exercise 3.10(a), PDF p. 12 of 29, line 283 carrying "Since
    ker psi = pB", and the primes of his conclusion being those of his B. Not
    checked: no step was re-derived, and no source was read beyond that passage.

- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on one clause of step uy-homeomorphism-onto-
    fiber. The sentence naming Cais's slip of notation closed "and is not copied
    here", which describes how the card was written rather than what the
    mathematics is (PROSE-11, QUAL-08). The clause is out; the sentence now says
    that the identity is his slip and that what his argument uses is the
    prime-level form, which the next sentence proves in the letters of this
    proof. The erratum itself stands as it was: his $pB$ is an ideal of the total
    space, while $\psi$ has the localized ring $B\otimes_AA_p$ as its source. No
    mathematics changes and nothing else on the card moves. Read in this pass:
    the sentence and the sentence after it; no source was reopened and no step was
    re-derived.

- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Repair on the reader's report, on the statement and on three points of the
    proof's form. (i) QUAL-01: the statement carried the printed text of
    II.3.10(b) verbatim, whose first assertion is false. As printed, with the
    sole hypothesis "(Assume k algebraically closed.)", it reads "If y in Y is the
    point a in k with a neq 0, show that the fibre X_y consists of two points,
    with residue field k"; in characteristic 2 the Frobenius of k is bijective,
    a = r^2 for some r, and the fibre is the one nonreduced point
    Spec k[t]/((t-r)^2), which step char-two-fibre-not-two-points computes. The
    statement now adds the missing hypothesis: "... the point a in k with a
    neq 0 and char k neq 2, show that the fibre X_y consists of two points, with
    residue field k". The other two assertions of (b) and the whole of (a) are
    unchanged, and the remark on the problem states what the printed claim
    asserts without the hypothesis and what the fibre is in every characteristic.
    The printed text is the one the earlier events of this card record, read in
    tmp/sources/hartshorne-1977-algebraic-geometry.md at printed p. 92; it was not
    re-read in this pass. (ii) STYLE-08: the pf-qed only listed the steps proving
    each part. It now carries the argument: over a closed point the fibre is
    Spec k[t]/(t^2-a), that algebra is k x k exactly when the two roots are
    distinct, and the four cases follow with their steps named. (iii) STYLE-08
    and PROSE-03: "The bijection above" in the claim of step
    uy-homeomorphism-onto-fiber is now the bijection of step
    uy-points-correspond-to-primes by reference, and "in the steps above" in its
    proof is the step that introduces Shichijo's phi. (iv) STYLE-04: the two
    occurrences of \mathrm{sp} in step xy-homeomorphism-global are
    \operatorname{sp}. (v) NOT-3: the proof of step generic-fibre-degree-two
    wrote the generic fibre as X_y, y naming a closed point in the steps before;
    it is X_eta, as the step's own claim has it. Nothing else changes, no step is
    re-derived beyond the case analysis in the pf-qed, and no source was reopened.

---

::: {.problem}
(a) If $f: X \to Y$ is a morphism and $y \in Y$ a point, show that $\underlyingspace{X_y}$ is homeomorphic to $\inverseof{f}(y)$ with the induced topology.

(b) Let $X = \Spec k[s,t]/(s - t^2)$, let $Y = \Spec k[s]$, and let $f: X \to Y$ be the morphism defined by sending $s \mapsto s$.

   - If $y \in Y$ is the point $a \in k$ with $a \neq 0$ and $\operatorname{char}k \neq 2$, show that the fibre $X_y$ consists of two points, with residue field $k$.

   - If $y \in Y$ corresponds to $0 \in k$, show that the fibre $X_y$ is a nonreduced one-point scheme.

   - If $\eta$ is the generic point of $Y$, show that $X_\eta$ is a one-point scheme whose residue field is an extension of degree two of the residue field of $\eta$.

   (Assume $k$ algebraically closed.)
:::

::: {.solution}
The sources cited at the steps are Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Exercise 2.3.10, PDF p. 23; the Cais solutions, Exercise 3.10, PDF p. 12 of 29, the file having no printed folio; A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (2020/March), Exercise 3.10, printed pp. 5--8; A. Egbert, *Solutions to Hartshorne's Algebraic Geometry*, Exercise II.3.10, printed p. 84; and, for the characteristic-two case, comments 3488648 and 3489729 on Math StackExchange question 1709194.

::: pf

::: {.pf-step #reduce-fibre-topology-to-affine}
The homeomorphism of (a) is proved with $Y$ affine and then $X$ affine, the affine pieces gluing.

::: pf-proof
The base ring is written $B$ and the coordinate ring of the total space $A$ throughout this proof.  Kim, Cais and Egbert use the opposite letters, writing $A$ for the base ring and $B$ for the total space; what is transcribed from them below is stated in the letters of this proof, with $A$ and $B$ interchanged and nothing else changed.  Shichijo writes $\phi:B\to A$ for the map of rings, the same letters as here.

Kim, Exercise 2.3.10(a), PDF p. 23: "Since the fiber product of schemes is fiber product of affine schemes glued together, we may assume first that $Y$ is affine and then $X$ is affine."

Cais, Exercise 3.10(a), PDF p. 12: for an affine neighbourhood $\Spec B$ of $y$, whose coordinate ring he calls $A$, the universal property of the fibre product gives, in the letters of this proof,
$$
X_y
=
(X\times_Y\Spec B)\times_{\Spec B}\Spec\kappa(y),
$$
and for $U\subseteq X$ open, $p^{-1}(U)=U\times_Y\Spec\kappa(y)$, so the affine statements glue.

Shichijo, Exercise 3.10(a), printed pp. 5--7, makes the same split into an affine case and a general case, where $f^{-1}(\tilde Y)=\bigcup X_i$ is an affine cover over the affine open $\tilde Y\ni y$ and $X_y$ is the gluing of the schemes $(X_y)_i=X_i\times_{\tilde Y}\Spec(\OO_{\tilde Y,y}/\mathfrak m_{\tilde Y,y})$.  He writes the affine case for $\phi:B\to A$, with $X=\Spec A$ over $Y=\Spec B$, as here.
:::

:::

::: {.pf-step #fibre-ring-tensor-localization}
There is a canonical ring isomorphism
$$
A\otimes_B\kappa(\mfp)
\cong
S^{-1}(A/\mfp A),
\qquad
S=B\setminus\mfp.
$$

::: pf-proof
Kim, Exercise 2.3.10(a), PDF p. 23, decomposes the total ring along the base prime,
$$
A\longrightarrow A/\mfp A\longrightarrow (B-\mfp)^{-1}(A/\mfp A)=A\otimes_B\kappa(\mfp),
$$
his decomposition $B\to B/\mathfrak pB\to(A-\mathfrak p)^{-1}(B/\mathfrak pB)$ being the same with the two letters exchanged.

Shichijo, Exercise 3.10(a), printed p. 6, computes the same tensor with $I_{\mfp}=\phi(\mfp)A$ and $T$ the image of $S$:
$$
A\otimes_B\frac{S^{-1}B}{S^{-1}\mfp}
\cong
A\otimes_B\frac{B}{\mfp}\otimes_BS^{-1}B
\cong
\frac{A}{I_{\mfp}}\otimes_BS^{-1}B
\cong
T^{-1}\Bigl(\frac{A}{I_{\mfp}}\Bigr),
$$
citing Atiyah--Macdonald Corollary 3.4, Proposition 3.5 and Exercise 2.2 for the steps.
:::

:::

::: {.pf-step #uy-points-correspond-to-primes}
The points of $U_y$ correspond bijectively to the primes
$$
\mfq\in\Spec A
$$
with
$$
\mfq\cap B=\mfp.
$$

::: pf-proof
Shichijo, Exercise 3.10(a), printed p. 6: by Atiyah--Macdonald Proposition 1.1 and 3.11 the primes of $T^{-1}(A/I_{\mfp})$ are the primes of $A$ containing $I_{\mfp}$ and meeting $T$ trivially, and his equivalence $(\ast)$ proves
$$
I_{\mfp}\subseteq\mfq\ \text{and}\ T\cap\bar\mfq=\emptyset
\iff
f(\mfq)=\phi^{-1}(\mfq)=\mfp .
$$

Egbert, Exercise II.3.10(a), printed p. 84, obtains the same set as
$$
\Spec(A_{\mfp}/\mfp A_{\mfp})
\approx
\set{\mfq\in\Spec A \st f^{-1}(\mfq)\subset\mfp,\ \mfq\supset f(\mfp)}
=
f^{-1}(\mfp),
$$
his $A$ being the base ring and his $B$ the total, so that his display reads $\Spec(B_{\mathfrak p}/\mathfrak pB_{\mathfrak p})\approx\{\mfq\in\Spec B\}$ with his letters.

Cais, Exercise 3.10(a), PDF p. 12, states the two conditions as $\mfp A\subseteq\mfq$ and $\mfq\cap g(B-\mfp)=\emptyset$, which together say $g^{-1}(\mfq)=\mfp$; his $g$ is the map of rings from the base to the total, $g:B\to A$ in the letters of this proof.
:::

:::

::: {.pf-step #uy-homeomorphism-onto-fiber}
The bijection of step [](#uy-points-correspond-to-primes){.pf-ref} is a homeomorphism of $\underlyingspace{U_y}$ onto $U\cap f^{-1}(y)$ with the induced topology.

::: pf-proof
Cais, Exercise 3.10(a), PDF p. 12, factors the projection $p$ as
$$
\Spec(A\otimes_B\kappa(\mfp))
\xrightarrow{\ \Spec\psi\ }
\Spec(A\otimes_BB_{\mfp})
\xrightarrow{\ \Spec\theta\ }
\Spec A,
$$
his factorization $\Spec(B\otimes_A\kappa(p))\to\Spec(B\otimes_AA_p)\to\Spec B$ being the same with the letters exchanged: its two maps are his $\phi$, the structure map of the localization $A\to A\otimes_BB_{\mfp}$, written $\theta$ here because $\phi$ is Shichijo's $B\to A$ of step [](#reduce-fibre-topology-to-affine){.pf-ref}, and his $\psi$.
The map $\psi$ is surjective, so by Exercise II.2.18(c) $\Spec\psi$ is a homeomorphism onto the closed subset $V(\ker\psi)$; and $\Spec\theta$ is a homeomorphism onto $\set{\mfq\in\Spec A \st \mfq\cap S=\emptyset}$ with $S=g(B-\mfp)$, since $\Spec\theta(V(I))=V(\theta^{-1}(I))\cap\Spec\theta(\Spec(A\otimes_BB_{\mfp}))$, the image lying in $\Spec A$. The kernel of $\psi$ is the ideal the base prime generates in $A\otimes_BB_{\mfp}$, that is $\ker\psi=\mfp(A\otimes_BB_{\mfp})$.  Cais writes this kernel as $\ker\psi=pB$, $pB$ being an ideal of the total space while $\psi$ has the localized ring $B\otimes_AA_p$ as its source, so that identity is his slip of notation; what his argument uses is the prime-level form, that a prime $\mfq$ of the total space with $\mfq\cap S=\emptyset$ contains $pB$ exactly when $g^{-1}(\mfq)=\mfp$, which holds, and which the next sentence proves in the letters of this proof.  A prime $\mfq\subseteq A$ with $\mfq\cap S=\emptyset$ contains the contraction of that kernel exactly when it contains $\mfp A=g(\mfp)A$, since every element of $S$ lies outside $\mfq$.  So the composite is a homeomorphism onto $\set{\mfq\in\Spec A \st \mfq\supseteq\mfp A,\ \mfq\cap S=\emptyset}$, which is $\set{\mfq \st g^{-1}(\mfq)=\mfp}$.

Shichijo, Exercise 3.10(a), printed p. 6, gives the same conclusion through the general facts that $\Spec(A/\mathfrak a)$ is homeomorphic to the closed subset $V(\mathfrak a)$ and $\Spec S^{-1}A$ to the primes of $A$ avoiding $S$.
:::

:::

::: {.pf-step #xy-homeomorphism-global}
Therefore
$$
\boxed{\underlyingspace{X_y}\xrightarrow{\sim}f^{-1}(y)}
$$
is a homeomorphism onto the set-theoretic fibre with the subspace topology.

::: pf-proof
The homeomorphisms of the affine pieces are compatible with the projections to $X$, so they glue: Kim, Exercise 2.3.10(a), PDF p. 23, and Shichijo, Exercise 3.10(a), printed p. 7, general case, where $\operatorname{sp}(X_y)$ is glued from the $\operatorname{sp}(X_y)_i$, and the restriction of $f$ to $X_i$ has fibre $f^{-1}(y)\cap X_i$, the pieces covering $f^{-1}(y)$.
:::

:::

::: {.pf-step #coordinate-ring-of-x-is-kt}
In part (b) the coordinate ring of $X$ is $k[t]$, with structural map
$$
k[s]\longrightarrow k[t],
\qquad
s\longmapsto t^2 .
$$

::: pf-proof
Kim, Exercise 2.3.10(b), PDF p. 23, and Shichijo, Exercise 3.10(b), printed p. 7, eliminate $s$ by the relation $s=t^2$, so that $k[s,t]/(s-t^2)\cong k[t]$ and the base ring maps by $s\mapsto t^2$; Egbert, printed p. 84, writes the elements of the fibre ring as $a_0+a_1t$ with $t^2=a$.
:::

:::

::: {.pf-step #closed-fibre-formula}
For a closed point $y=(s-a)$ of $Y$ the fibre is
$$
\boxed{X_y\cong\Spec k[t]/(t^2-a)}.
$$

::: pf-proof
Kim, Exercise 2.3.10(b), PDF p. 23: "the fiber is given by $\Spec k[s,t]/(s-t^2,s-a)\cong\Spec k[t]/(t^2-a)$". Egbert, printed p. 84, computes the same spectrum.

Shichijo, Exercise 3.10(b), printed p. 7, gets it from his Lemma Ex3.10.1,
$$
\frac{k[s][t]}{I}\otimes_{k[s]}\frac{k[s]}{J}\cong\frac{k[s][t]}{I+J^e},
$$
applied with $I=(s-t^2)$ and $J=(s-a)$.
:::

:::

::: {.pf-step #char-two-fibre-not-two-points}
If $\operatorname{char}k=2$ and $a\ne0$, then $X_y$ is a single nonreduced point with residue field $k$, so the assertion of the exercise as printed fails there.

::: pf-proof
The defect is stated in the comments to Math StackExchange 1709194. Comment 3488648 by kesa (2016-03-22): the two-point reading "is not true in characteristic 2, where you need that $t^2-a$ is separable (i.e. $a$ has two different square roots, else one ends up with the same situation as for $a=0$)". Comment 3489729 by Roland (2016-03-23) agrees: "in characteristic 2 the fiber over $s=a$ consist of a single point with multiplicity 2 exactly like the case $a=0$".

The computation is the card's, from step [](#closed-fibre-formula){.pf-ref}: in characteristic two the Frobenius map of the algebraically closed field $k$ is bijective, so $a=r^2$ for a unique $r\in k$, and $r\ne0$ because $a\ne0$; hence
$$
X_y\cong\Spec k[t]/(t^2-a)=\Spec k[t]/\bigl((t-r)^2\bigr),
$$
which has the unique prime $(t-r)$ and the nonzero nilpotent class of $t-r$.
:::

:::

::: {.pf-step #fibre-two-points-char-neq-2}
Assume $a\ne0$ and $\operatorname{char}k\ne2$. Then $X_y$ consists of two points, each with residue field $k$.

::: pf-proof
Kim, Exercise 2.3.10(b), PDF p. 23: "If $a\ne0$ then this is isomorphic to $k\times k$ so we have two points."

Shichijo, Exercise 3.10(b), printed p. 7, writes the same step as
$$
\frac{k[t]}{(t^2-a)}
=
\frac{k[t]}{(t-\sqrt a)\cap(t+\sqrt a)}
\cong
\frac{k[t]}{(t-\sqrt a)}\oplus\frac{k[t]}{(t+\sqrt a)}
\cong
k\times k
$$
by the Chinese remainder theorem, and notes that each of the two points has residue field $k$.

Egbert, printed p. 84, gives the idempotents: $(1,0)\mapsto\frac1{2\sqrt a}t+\frac12$ and $(0,1)\mapsto-\frac1{2\sqrt a}t+\frac12$, his printed $2\sqrt2$ in the second denominator being a misprint for $2\sqrt a$; the two points are the spectra of $k[t]/(t\mp\sqrt a)$.

All three need $\operatorname{char}k\ne2$: $t-\sqrt a$ and $t+\sqrt a$ are distinct only when $2\sqrt a\ne0$, and the idempotents use $\tfrac1{2}$. Under the printed hypothesis alone, step [](#char-two-fibre-not-two-points){.pf-ref} is the case that fails.
:::

:::

::: {.pf-step #fibre-nonreduced-a-zero}
If $a=0$, the fibre is a nonreduced one-point scheme.

::: pf-proof
Kim, Exercise 2.3.10(b), PDF p. 23: "if $a=0$ then it is $k[t]/(t^2)$ which is a non-reduced one-point scheme". Cais, Exercise 3.10(b), PDF p. 12, and Egbert, printed p. 84, the latter calling it the dual numbers; Shichijo, printed p. 8, adds that $(t^2)$ has the unique maximal ideal $(t)$, and that the spectrum is one point and not reduced.
:::

:::

::: {.pf-step #generic-fibre-ring}
For the generic point $\eta$ of $Y$,
$$
\kappa(\eta)=k(s),
\qquad
X_\eta\cong\Spec\bigl(k(s)[t]/(t^2-s)\bigr).
$$

::: pf-proof
Kim, Exercise 2.3.10(b), PDF p. 23: "If $\eta$ is the generic point, then the fiber is $\operatorname{Quot}(k[s,t]/(s-t^2))=k(s)[t]/(t^2-s)$ while $Y_\eta=\Spec k(s)$".

Shichijo, Exercise 3.10(b), printed p. 8, computes it by localizing at $S=k[s]\setminus\set0$,
$$
\frac{k[s,t]}{(s-t^2)}\otimes_{k[s]}S^{-1}k[s]\cong S^{-1}\frac{k[s,t]}{(s-t^2)}\cong\frac{k(s)[t]}{(t^2-s)},
$$
with $\kappa(\eta)=k(s)$.

Cais, Exercise 3.10(b), PDF p. 12, identifies the same fibre as the primes of $k[s,t]/(s-t^2)$ contracting to $(0)$, those containing no polynomial in $s$, and finds the single one $(s-t^2)$.
:::

:::

::: {.pf-step #t2-s-irreducible}
The polynomial $t^2-s\in k(s)[t]$ is irreducible.

::: pf-proof
Shichijo, Exercise 3.10(b), printed p. 8: "$t^2-s$ is an irreducible polynomial with coefficients in $k(s)$, so this ring is a field". Cais, PDF p. 12, and Egbert, printed p. 84, state the same: the quotient is a field, of degree two in $t$.

The card's check of the assertion is the valuation: $v_s(s)=1$ is odd, and every square in $k(s)$ has even $v_s$-valuation, so $s$ is not a square and the quadratic $t^2-s$ has no root. This holds in every characteristic, since it uses no separability.
:::

:::

::: {.pf-step #generic-fibre-degree-two}
The generic fibre is a one-point scheme whose residue field has degree two over $k(s)$:
$$
\boxed{X_\eta=\Spec k(s)(\sqrt s),\qquad [\kappa(X_\eta):k(s)]=2.}
$$

::: pf-proof
Shichijo, Exercise 3.10(b), printed p. 8: the quotient is a field, so $X_\eta=\Spec k(s)[t]/(t^2-s)$ "is a one point space", and its residue field is a degree two extension of $k(\eta)$. Kim, PDF p. 23, and Egbert, printed p. 84, conclude the same from the degree of the defining polynomial; Cais, PDF p. 12, writes it as a one-point scheme whose residue field is a degree-two extension of $k(s)$.
:::

:::

::: pf-qed
Over a closed point $y=(s-a)$ the fibre is $\Spec k[t]/(t^2-a)$ (step [](#closed-fibre-formula){.pf-ref}), and that algebra is $k\times k$ exactly when $t^2-a$ has two distinct roots in the algebraically closed field $k$. It has them when $a\ne0$ and $\operatorname{char}k\ne2$ (step [](#fibre-two-points-char-neq-2){.pf-ref}); in characteristic $2$ it is $(t-r)^2$ with $r^2=a$, giving the single nonreduced point of step [](#char-two-fibre-not-two-points){.pf-ref}; over $0$ the fibre is $k[t]/(t^2)$, one nonreduced point (step [](#fibre-nonreduced-a-zero){.pf-ref}); and over the generic point it is the field $k(s)(\sqrt s)$, of degree two over $k(s)$ (steps [](#generic-fibre-ring){.pf-ref} and [](#generic-fibre-degree-two){.pf-ref}). Part (a) is the homeomorphism of step [](#xy-homeomorphism-global){.pf-ref}, which is the affine case of steps [](#reduce-fibre-topology-to-affine){.pf-ref} through [](#uy-homeomorphism-onto-fiber){.pf-ref} glued along an affine cover.
:::

:::

:::

::: {.remark}
The exercise prints the two-point assertion for $a\neq0$ with no hypothesis on $k$ beyond algebraic closedness, and it is false in characteristic $2$: there the Frobenius map of $k$ is bijective, so $t^2-a=(t-r)^2$ with $r^2=a$, and the fibre is the one-point nonreduced scheme $\Spec k[t]/((t-r)^2)$ (step [](#char-two-fibre-not-two-points){.pf-ref}).  In every characteristic the fibre over $a\neq0$ is $\Spec k[t]/(t^2-a)$ (step [](#closed-fibre-formula){.pf-ref}), and it consists of two points with residue field $k$ exactly when the two roots are distinct, that is when $\operatorname{char} k\neq2$, which is the hypothesis the statement above carries and what step [](#fibre-two-points-char-neq-2){.pf-ref} proves.  The remaining two assertions of (b), $a=0$ and the generic fibre, hold in every characteristic.
:::

::: {.remark title="Published solution"}
For (a), Cais, Exercise 3.10(a), PDF p. 12, is the complete argument --- reduction to $Y=\Spec B$ and $X=\Spec A$ by the universal property, the factorization of $p$ through $\Spec(A\otimes_BB_{\mfp})$, and the identification of the composite as a homeomorphism onto $\set{\mfq \st g^{-1}(\mfq)=\mfp}$ --- with Kim, PDF p. 23, for the reduction, Shichijo, printed p. 6, for the affine computation $A\otimes_B\kappa(\mfp)\cong T^{-1}(A/I_{\mfp})$ and its equivalence $(\ast)$, Egbert, printed p. 84, for the chain $\Spec(A_{\mfp}/\mfp A_{\mfp})\approx f^{-1}(\mfp)$, and Shichijo for the gluing over an affine cover.  Kim, Cais and Egbert write the two rings with the opposite letters to those used here; their displays are transcribed above with $A$ and $B$ exchanged, the statements unchanged. For (b), the closed fibres are Kim, Shichijo and Egbert as cited, the generic fibre Kim, Shichijo, Cais and Egbert.

The two-point assertion for $a\ne0$ needs the two roots of $t^2-a$ to be distinct, that is $\operatorname{char}k\ne2$: the passage from $k[t]/(t^2-a)$ to $k\times k$ is the Chinese remainder theorem for coprime factors, and in characteristic two the polynomial is $(t-r)^2$ with $r^2=a$. Math StackExchange 1709194 records that the printed claim fails there (comments 3488648 and 3489729, quoted in step [](#char-two-fibre-not-two-points){.pf-ref}). The irreducibility of $t^2-s$ over $k(s)$ is step [](#t2-s-irreducible){.pf-ref}, by the $s$-adic valuation, which needs no separability and so holds in every characteristic.
:::
