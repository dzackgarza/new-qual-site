---
schema: qual/card@1
id: P-AGH528STABLEBUNDLE
kind: problem
title: Stability of rank two bundles and classification of the unstable indecomposables
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.8 and the retained companion proof. The corpus
    transcription in part (c) said "up to isomorphism"; that statement is
    false because tensoring by any line bundle preserves rank, indecomposability,
    and (non-)semistability while generally changing the isomorphism class.
    The companion proof itself twists the unique maximal destabilizing line
    subbundle to O_C before extracting the extension data. The selected card is
    therefore repaired to the mathematically coherent classification up to
    tensoring by an invertible sheaf. The proof below also supplies the
    boundedness and uniqueness of the maximal destabilizing line subbundle.
- event: source-corrected
  by: chatgpt
  date: 2026-09-18
  note: Replaced the impossible "up to isomorphism" in part (c) by "up to tensoring with an invertible sheaf".
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.8, printed page 384. Checked every step: the slope
    rearrangement of s1, with the saturation case added because a line
    subbundle whose quotient has torsion is not one of the quotients the
    printed definition tests; the boundedness of degrees of line subbundles in
    s7 via E-dual(n) globally generated; the uniqueness of the maximal-degree
    subbundle in s8 from the nonzero map A tensor B -> det E; the Ext
    identification of s10; and the Serre-duality bound e <= 2g-2 of s11.
    Confirmed the printed defect independently: tensoring by a line bundle of
    degree m preserves indecomposability, non-semistability and the normalized
    data (e, L, xi) while changing the degree from -e to 2m-e, so the printed
    "up to isomorphism" cannot hold and the classification is up to tensor
    equivalence. Searched outside the twelve retained sets: Algebraic Geometry
    II, National Taiwan University, 2020 Spring, Chapter V homework, Exercise 8
    of section 2, PDF p. 8 (tmp/sources/ntu-ag2-chapter5.pdf), whose (c) is the sentence "This is just
    the proof of Theorem 2.12, combined with (b)"; Yang Pi-Yeh, Hartshorne
    Solutions, exercise 5.2.8, printed pp. 103-104
    (tmp/sources/lfwin-hartshorne-solutions.pdf), which repeats "up to
    isomorphism"; and Egbert, PDF pp. 265-266. None repairs the printed clause.
    Not checked: whether Hartshorne intended the clause to classify the
    normalized models only; the card states the printed wording and proves the
    tensor-equivalence reading.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3) on 2026-11-16: it states no
    stability condition for locally free sheaves on a curve, so it does not reach
    part (c); its Theorem 3.2 is a citation of the book's Theorem V.2.12. Two
    Math StackExchange threads were saved for the section, neither bearing on (c):
    4398506, tmp/sources/mse-4398506-hart77-v25-linear-system-notation.md, asks
    only what the notation $\linearsystem{D+K-E}+E$ of V.2.5(b) means, and 5101697,
    tmp/sources/mse-5101697-hart77-v2-elementary-transformation.md, asks how
    Hartshorne's E' = pi_*(O(1) x I_P) realises the elementary transformation of
    Example V.5.7.1, printed p. 416, which the questioner proves and KReiser's
    accepted answer confirms, with a proof that a section through the blown-up
    point exists. No complete published argument for (c) was located, and the
    printed "up to isomorphism" stays defective as recorded at the head of the
    solution: a bundle and its twist by a line bundle of nonzero degree carry the
    same triple and have different determinants.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the reference in the event above and restored the event of
    2026-11-11 to its text of that date. The elementary transformation is the
    book's Example V.5.7.1, printed p. 416, where the monoidal transform at a
    point of a fibre is blown down along the strict transform of that fibre; it
    is not V.2.11, which is the base-point-freeness and very-ampleness criterion
    for C_0 + bf. The page was read in the text version of the book: the example
    sits on the PDF page before the marker for PDF p. 432, so printed p. 416 at
    the offset 15 this book's extractions take. The text-version names that a
    later commit of 2026-11-16 put into the event of 2026-11-11 are removed, and
    every source cited in the remark names its text version. Nothing else in the
    audit changes: no complete published argument for (c) was located, and the
    printed "up to isomorphism" stays defective.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed all three parts on 2026-11-16 from Gunning, Lectures on vector
    bundles over Riemann surfaces, read in the text version
    tmp/sources/gunning-1967-vector-bundles-riemann-surfaces-pp69-92.md, whose
    OCR corrupts most displayed formulas but whose statements and arguments are
    legible in outline, and from the book's own Theorem 2.12 and Example 2.11.6;
    re-read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.8, printed p. 384 (PDF p. 399), whose part (c) still reads "up to
    isomorphism". Printed pages of Gunning were established from the PDF's
    folios, printed page = PDF page - 9: Theorem 13 on printed pp. 71-74,
    Lemma 14 on pp. 81-82, the stability definitions and div Phi on pp. 82-83,
    Lemma 15 on pp. 83-85, Theorem 14 on pp. 87-90. (a) is Gunning's remark that
    div Phi is at least (1/rank)c(det Phi) for a decomposable bundle, from his
    Lemma 14; (b) is his "Phi is stable precisely when div Phi < half c(xi)"
    together with div E = 0 for a normalized E; the uniqueness of the maximal
    subbundle is Lemma 15(i), whose proof by the two diagonal bundles is carried
    in step s8; and the classification of (c) is Theorem 14, with phi = O and
    xi = L, so that the parameter space is P H^1(C, L^dual) and proportional
    classes give isomorphic middle bundles. The bound 0 < e <= 2g-2 is the
    argument of the book's Theorem 2.12, printed p. 376. Checked that
    non-semistability is div E > half deg E, not the weak inequality, which is
    what makes Lemma 15(i) apply. Not checked: whether Gunning's displayed
    computations in Lemma 15 and Theorem 14 are free of error, which the OCR
    does not permit; the steps that depend on them are carried by their
    statements alone and by the rank-two arguments written on the card. The
    printed "up to isomorphism" stays defective, and the card classifies
    tensor-equivalence classes.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card against its sources again on 2026-11-16, after the event
    above of the same date. Part (a) is now proved for any rank, as the exercise
    states it: Gunning's Lemma 14, printed pp. 81-82, gives div Phi at least
    (1/m)c(det Phi) for a decomposable Phi of rank m, and the passage from line
    subbundles to locally free quotients for m greater than 2 is marked as the
    card's own. The bound on subbundle degrees that step s7 needs is Gunning's,
    printed p. 80 in the paragraph before his (9), where he shows c(phi) at most
    max c(Psi_j) over the diagonal bundles of a complete reduction and says that
    those Chern classes are bounded from above; the earlier sentence calling
    that bound the card's is withdrawn, and the card's global-generation proof
    is kept as a second proof. Semistability is the exercise's definition, not
    Gunning's, who defines stability and instability only; step s6 now says so
    and is marked as the card's own. The proof of Proposition 2.8 ends on
    printed p. 372, not p. 373. Theorem 14 is stated for a compact Riemann
    surface, so step s12 says which part of it carries the classification
    without that setting, namely the direct rank-two argument. Not checked:
    whether the classification of part (c) holds in positive characteristic;
    nothing in the sources read states it there, and the card does not claim it.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card again on 2026-11-16 on the reader's report, after the
    event above of the same date, which is left as written. Three corrections.
    First, part (a) is proved again in rank two only, as the card proved it
    before this batch. The argument the event above records for any rank is
    withdrawn and was wrong twice: Gunning's Lemma 14, printed pp. 81-82,
    treats a decomposable bundle written as a direct sum of line bundles, and a
    decomposable bundle of rank three or more is not in general such a sum; and
    the translation written on the card exhibited a rank-one quotient of slope
    at least mu(Phi), which is not the inequality that contradicts stability,
    since stability requires every quotient's slope to exceed mu(Phi). Step s2
    now carries the rank-two argument through step s1, is marked as the card's
    own, and states Lemma 14 with its hypothesis. Part (a) for a decomposable
    bundle of higher rank is not proved here, and no source read proves it.
    Second, the remark's sentence that the rank-two argument of step s12
    carries part (c) without Gunning's setting is withdrawn: step s12's
    rank-two argument proves only that the constructed bundle is
    indecomposable, and the injectivity of the classification rests on Theorem
    14, a statement about a compact Riemann surface. Steps s12, s13, the qed
    and the remark now say that part (c) is established for a curve over the
    complex numbers, which is what the record of this date says as well.
    Third, the same remark sentence is where the card claimed the setting
    without giving it; the remark now names what Theorem 14 supplies and what
    step s12 supplies. Read for this repair: Gunning's §(c), Lemma 14 and
    Theorem 14 in the text version
    tmp/sources/gunning-1967-vector-bundles-riemann-surfaces-pp69-92.md, whose
    OCR garbles the displays, so the statements were taken from its sentences
    and the mathematics checked on the card. Not checked: whether Gunning's
    displayed computations in Lemma 14 and Theorem 14 are free of error, and
    whether part (a) holds in rank above two, which is a question about the
    exercise and not about the sources read.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Repaired the card on 2026-11-19 for issue #159. Re-read the printed exercise
    at Hartshorne, Algebraic Geometry (1977), V.2, exercise 2.8, printed p. 384
    (PDF p. 399): its (c) reads "classified, up to isomorphism, by giving (1) an
    integer 0 < e <= 2g-2, (2) an element L in Pic C of degree -e, and (3) a
    nonzero xi in H^1(L^dual) determined up to a nonzero scalar multiple", and
    the printed "up to isomorphism" is false, since tensoring by an invertible
    sheaf of nonzero degree preserves indecomposability and non-semistability
    and leaves the triple (e, L, xi) fixed while changing the determinant. Under
    QUAL-01 the statement now reads "up to tensoring with an invertible sheaf",
    which is what steps s9 to s13 prove, and it records the field: "for C a
    curve over C", Gunning's Theorem 14 being a statement about a compact
    Riemann surface. Part (a) is now proved in every rank, where the event above
    of 2026-11-16 says it was not and no source read proves it; that event is
    left as written and this one supersedes it. The proof is Yang Pi-Yeh,
    Hartshorne Solutions, Solution 5.2.8(a), printed pp. 103-104, read on the
    retained PDF: the solution displays the weighted mean
    mu(E) = (r'/(r'+r''))mu(E') + (r''/(r'+r''))mu(E'') at its head on printed
    p. 104 and argues "If E = F (+) G is stable, we may assume mu(F) <= mu(G).
    Then consider the morphism E -> F -> 0, we have mu(E) < mu(F). Since
    mu(F) <= mu(E) <= mu(G), we have mu(E) < mu(F) <= mu(E), which is
    impossible". The two summand quotient sequences are also in Algebraic
    Geometry II, National Taiwan University, 2020 Spring, Chapter V Surfaces
    homework, Exercise 8 of section 2 (Tzu-Yang Chou), PDF p. 8 of
    tmp/sources/ntu-ag2-chapter5.pdf, which concludes that "looking at the
    slopes we see that E can not be stable". Read for the rank-two statements:
    Gunning, printed p. 82 for the decomposable clause of Lemma 14 with its
    hypothesis, a direct sum phi_1 (+) ... (+) phi_m of line bundles, which the
    card now states with (13) as its proof; printed p. 85 for "every
    decomposable bundle is unstable"; printed pp. 83-85 for Lemma 15; and
    printed pp. 87-90 for Theorem 14. The pages were checked on rendered pages
    of tmp/sources/gunning-1967-vector-bundles-riemann-surfaces.pdf at 150 dpi,
    printed page = PDF page - 9, the folio "-85-" on PDF p. 94 confirming the
    offset there; the text version
    tmp/sources/gunning-1967-vector-bundles-riemann-surfaces-pp69-92.md has no
    page markers and its OCR garbles the displays. Not checked: whether part (c)
    holds in positive characteristic, which nothing read here states and which
    the statement does not claim.
---

::: {.problem}
A locally free sheaf $\mathcal{E}$ on a curve $C$ is said to be **stable** if for every quotient locally free sheaf
$$
\mathcal{E} \rightarrow \mathcal{F} \rightarrow 0, \qquad \mathcal{F} \neq \mathcal{E}, \mathcal{F} \neq 0
,$$
we have
$$
(\deg \mathcal{F}) / \rank \mathcal{F}>(\deg \mathcal{E}) / \rank \mathcal{E}
.$$
Replacing $>$ by $\geqslant$ defines **semistable**.

(a) A decomposable $\mathcal{E}$ is never stable.

(b) If $\mathcal{E}$ has rank 2 and is normalized, then $\mathcal{E}$ is stable (respectively, semistable) if and only if $\deg \mathcal{E}>0$ (respectively, $\geqslant 0$).

(c) For $C$ a curve over $\CC$, show that the indecomposable locally free sheaves $\mathcal{E}$ of rank 2 that are not semistable are classified, up to tensoring with an invertible sheaf, by giving

   (1) an integer $0<e \leqslant 2 g-2$,

   (2) an element $\mathcal{L} \in \Pic C$ of degree $-e$, and

   (3) a nonzero $\xi \in H^1\left(\dualof{\mathcal{L}}\right)$, determined up to a nonzero scalar multiple.

:::

::: {.solution}
For a nonzero locally free sheaf $\mathcal F$ on $C$, write
$$
\mu(\mathcal F)=\frac{\deg\mathcal F}{\rank\mathcal F}.
$$

The data of part (c) are the data of the normalized model of a bundle, and tensoring by an invertible sheaf moves the bundle without moving them. Let $\mathcal E_0$ be normalized, not semistable, with data $(e,\mathcal L,\xi)$, and let $\mathcal A$ be a line bundle of degree $m\ne0$. Tensoring by $\mathcal A$ shifts every slope by $m$, so the maximal-degree line subbundle of $\mathcal E_0\tensor\mathcal A$ is $\OO_C\tensor\mathcal A$, and the data read off from it are
$$
\det(\mathcal E_0\tensor\mathcal A)\tensor(\OO_C\tensor\mathcal A)^{-2}
\cong\det\mathcal E_0,\qquad
(\mathcal E_0\tensor\mathcal A)\tensor(\OO_C\tensor\mathcal A)^{-1}\cong\mathcal E_0,
$$
so $e$, $\mathcal L$ and $\xi$ are unchanged, while $\deg(\mathcal E_0\tensor\mathcal A)=2m-e\ne-e=\deg\mathcal E_0$ and the two bundles have different determinants, hence are not isomorphic. Part (c) therefore classifies these bundles up to tensoring with an invertible sheaf, which is the form step [](#s13){.pf-ref} proves.

::: pf

::: {.pf-step #s1}
For a rank-two bundle $\mathcal E$, stability is equivalent to
$$
\deg\mathcal A<\frac12\deg\mathcal E
$$
for every line subbundle $\mathcal A\subsetneq\mathcal E$, and semistability to the same inequalities with $\le$.

::: pf-proof
Gunning, *Lectures on vector bundles over Riemann surfaces*, §(c), printed pp. 82--83, defines $\Phi$ to be stable when $c(\varphi)<\frac12c(\det\Phi)$ for every line bundle $\varphi\subset\Phi$, and unstable otherwise, and sets $\operatorname{div}\Phi=\max_{\varphi\subset\Phi}c(\varphi)$; the exercise states the same condition for locally free quotients. A rank-two bundle with a locally free nonzero proper quotient
$$
0\longrightarrow\mathcal A\longrightarrow\mathcal E\longrightarrow\mathcal F\longrightarrow0
$$
has $\rank\mathcal A=\rank\mathcal F=1$ and $\deg\mathcal F=\deg\mathcal E-\deg\mathcal A$, so $\deg\mathcal F>\frac12\deg\mathcal E$ is equivalent to $\deg\mathcal A<\frac12\deg\mathcal E$. A line subbundle that is not saturated lies in its saturation, whose quotient is torsion-free and hence invertible on a curve and whose degree is at least as large, so the inequalities for invertible quotients imply them for every line subbundle. The semistable statement is the same rearrangement with weak inequalities.

:::

:::

::: {.pf-step #s2}
A decomposable bundle is never stable, in any rank. This is part (a).

::: pf-proof
Write $\mathcal E\cong\mathcal F\oplus\mathcal G$ with $\mathcal F,\mathcal G$ locally free of ranks $r_{\mathcal F},r_{\mathcal G}\ge1$, and interchange the summands if necessary so that $\mu(\mathcal F)\le\mu(\mathcal G)$. The projection $\mathcal E\twoheadrightarrow\mathcal F$ with kernel $\mathcal G$ is a nonzero locally free quotient of $\mathcal E$ other than $\mathcal E$, so it is one of the quotients the definition of stability tests. Since $\deg\mathcal E=\deg\mathcal F+\deg\mathcal G$ and $\rank\mathcal E=r_{\mathcal F}+r_{\mathcal G}$,
$$
\mu(\mathcal E)=\frac{r_{\mathcal F}}{r_{\mathcal F}+r_{\mathcal G}}\mu(\mathcal F)+\frac{r_{\mathcal G}}{r_{\mathcal F}+r_{\mathcal G}}\mu(\mathcal G),
$$
a mean of $\mu(\mathcal F)$ and $\mu(\mathcal G)$ with positive weights, so $\mu(\mathcal F)\le\mu(\mathcal E)$; stability would require $\mu(\mathcal F)>\mu(\mathcal E)$, and $\mathcal E$ is therefore not stable. A decomposition into more than two summands is regrouped as a decomposition into two.

This is Solution 5.2.8(a) of Yang Pi-Yeh, *Hartshorne Solutions*, printed pp. 103--104, which displays the weighted mean at the head of the solution and reads the contradiction off the quotient $\mathcal E\twoheadrightarrow\mathcal F$; the same two quotient sequences, with kernels $\mathcal F$ and $\mathcal G$, are used in Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework, Exercise 8 of §2 (Tzu-Yang Chou), PDF p. 8, which concludes that "looking at the slopes we see that $\mathcal E$ can not be stable". In rank two the summands are line bundles, step [](#s1){.pf-ref} turns the quotient inequality of the exercise into the line-subbundle one, and Gunning records the conclusion for that case on printed p. 85, where Lemma 14 gives $\operatorname{div}\mathcal E\ge\frac12c(\xi)$ for a decomposable $\mathcal E$ and hence that "every decomposable bundle is unstable". The decomposable case of Lemma 14 itself, printed pp. 81--82, is stated for a direct sum $\varphi_1\oplus\cdots\oplus\varphi_m$ of line bundles, and its proof runs through (13), $\operatorname{div}(\varphi_1\oplus\cdots\oplus\varphi_m)=\max_jc(\varphi_j)$, so it does not reach a decomposable bundle of rank three or more; the mean of slopes does.

:::

:::

::: {.pf-step #s3}
If a rank-two bundle $\mathcal E$ is normalized, then every line subbundle $\mathcal A\subseteq\mathcal E$ satisfies
$$
\deg\mathcal A\le0 .
$$

::: pf-proof
The inclusion is a nonzero section of $\mathcal E\tensor\mathcal A^{-1}$; if $\deg\mathcal A>0$ then $\mathcal A^{-1}$ has negative degree, contrary to the defining vanishing of Proposition 2.8, printed p. 372. In Gunning's notation this says $\operatorname{div}\mathcal E\le0$, and $H^0(C,\mathcal E)\ne0$ gives the reverse inequality.

:::

:::

::: {.pf-step #s4}
If a rank-two bundle $\mathcal E$ is normalized, then it contains $\OO_C$ as a line subbundle.

::: pf-proof
This is the last step of the proof of Proposition 2.8, printed p. 372: a nonzero section $s\in H^0(C,\mathcal E)$ gives an injective map $\OO_C\to\mathcal E$, and its image spans a line subbundle. Normalization makes the quotient invertible — the book shows it is torsion-free and hence invertible on a curve — and the subbundle is $\OO_C$; step [](#s3){.pf-ref} bounds its degree above by $0$ and the nonzero section bounds it below.

:::

:::

::: {.pf-step #s5}
If $\mathcal E$ has rank two and is normalized, then
$$
\boxed{\mathcal E\text{ is stable}\iff\deg\mathcal E>0.}
$$

::: pf-proof
Gunning, §(c), printed p. 83: "$\Phi$ is stable precisely when $\operatorname{div}\Phi<\frac12c(\xi)$". A normalized bundle has $\operatorname{div}\mathcal E=0$ by step [](#s3){.pf-ref}, so that inequality is $0<\frac12\deg\mathcal E$. In the language of steps [](#s1){.pf-ref} and [](#s3){.pf-ref}: if $\deg\mathcal E>0$ then every line subbundle has $\deg\mathcal A\le0<\frac12\deg\mathcal E$ and stability follows, and if $\mathcal E$ is stable then the subbundle $\OO_C\subseteq\mathcal E$ of step [](#s4){.pf-ref} gives $0<\frac12\deg\mathcal E$.

:::

:::

::: {.pf-step #s6}
If $\mathcal E$ has rank two and is normalized, then
$$
\boxed{\mathcal E\text{ is semistable}\iff\deg\mathcal E\ge0.}
$$

::: pf-proof
Semistability is the exercise's definition, the weak inequalities of step [](#s1){.pf-ref}; Gunning defines stability and instability only, and states no semistable criterion, so this step is the card's own. With $\operatorname{div}\mathcal E=0$ by step [](#s3){.pf-ref} every line subbundle has $\deg\mathcal A\le0$, so $\deg\mathcal E\ge0$ gives the weak inequalities, and the subbundle $\OO_C$ of step [](#s4){.pf-ref} gives the converse. Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (b).

:::

:::

::: {.pf-step #s7}
Let $\mathcal E$ be a rank-two bundle that is not semistable. Among all line subbundles of $\mathcal E$ there is one of maximal degree.

::: pf-proof
The maximum is what Gunning's $\operatorname{div}\Phi=\max_{\varphi\subset\Phi}c(\varphi)$ presupposes, and he proves the bound on printed p. 80, in the paragraph before his (9): for a line bundle $\varphi\subset\Psi$ he shows $c(\varphi)\le\max_jc(\Psi_j)$ over the diagonal line bundles of a fixed complete reduction of $\Psi$, "or in other words, the Chern classes $c(\varphi)$ of line bundles $\varphi$ which are subbundles of a fixed complex vector bundle $\Psi$, are bounded from above". The proof below is that bound in the form of a rank-two bundle on a curve, and is the card's own. Line subbundles exist, since a nonzero section of $\mathcal E(n)$ for $n\gg0$ saturates to an invertible subsheaf. Their degrees are bounded above: fix an ample $\OO_C(1)$ of degree $h>0$ and take $n\gg0$ so that $\mathcal E^\vee(n)$ is globally generated; dualizing the locally free quotient of a line subbundle $\mathcal A\subseteq\mathcal E$ gives a surjection $\mathcal E^\vee\twoheadrightarrow\mathcal A^\vee$, so $\mathcal A^\vee(n)$ is a quotient of a globally generated bundle and is globally generated, whence $-\deg\mathcal A+nh\ge0$ and $\deg\mathcal A\le nh$. The degrees are integers, so they have a maximum.

:::

:::

::: {.pf-step #s8}
A rank-two bundle $\mathcal E$ that is not semistable has a unique line subbundle $\mathcal A$ of maximal degree, and
$$
2\deg\mathcal A>\deg\mathcal E .
$$

::: pf-proof
This is Lemma 15 of Gunning, printed pp. 83--85. Non-semistability is $\operatorname{div}\mathcal E>\frac12c(\xi)$, that is $2\deg\mathcal A>\deg\mathcal E$ for a maximal subbundle, which is the case of the lemma's part (i). Its part (i) states and proves uniqueness: if $\varphi_1\subset\Phi$ realizes $\operatorname{div}\Phi$ and $\varphi\subset\Phi$ is another subbundle with $c(\varphi)=\operatorname{div}\Phi$, then $\varphi^{-1}\varphi_1$ has a nontrivial section while $\varphi^{-1}\varphi_2$ has none, $\varphi_2=\Phi/\varphi_1$, because $c(\varphi^{-1}\varphi_2)=-2c(\varphi_1)+c(\xi)<0$; so $\varphi=\varphi_1$. In rank-two terms, a second maximal subbundle $\mathcal B$ with $\deg\mathcal A=\deg\mathcal B=a$ and no common generic line gives a nonzero map $\mathcal A\tensor\mathcal B\to\det\mathcal E$ and hence $2a\le\deg\mathcal E$, contradicting $2a>\deg\mathcal E$.

:::

:::

::: {.pf-step #s9}
Let $\mathcal E$ be indecomposable and not semistable and let $\mathcal A$ be its unique maximal-degree line subbundle. Then
$$
\mathcal E_0=\mathcal E\tensor\mathcal A^{-1}
$$
fits into a nonsplit exact sequence
$$
0\longrightarrow\OO_C\longrightarrow\mathcal E_0\longrightarrow\mathcal L\longrightarrow0
$$
with $\deg\mathcal L=-e<0$.

::: pf-proof
This is the opening of the proof of Theorem 2.12, printed p. 376: corresponding to a section of $\PP(\mathcal E)$ there is an exact sequence $0\to\OO_C\to\mathcal E\to\mathcal L\to0$ for some $\mathcal L$, and for an indecomposable $\mathcal E$ it "must be a nontrivial extension, so it corresponds to a nonzero element $\xi\in\Ext^1(\mathcal L,\OO_C)\cong H^1(C,\mathcal L^\vee)$". Tensoring the sequence of the subbundle $\mathcal A\subseteq\mathcal E$ by $\mathcal A^{-1}$ gives $\mathcal L\cong\det\mathcal E\tensor\mathcal A^{-2}$, so $\deg\mathcal L=\deg\mathcal E-2\deg\mathcal A<0$ by step [](#s8){.pf-ref}; write this degree as $-e$. A splitting would make $\mathcal E_0$, and hence $\mathcal E$, decomposable.

:::

:::

::: {.pf-step #s10}
The bundle $\mathcal E_0$ of step [](#s9){.pf-ref} is normalized, and its extension class is a nonzero $\xi\in H^1(C,\mathcal L^\vee)$ well defined up to nonzero scalar.

::: pf-proof
Normalization is the argument of Example 2.11.6, printed p. 375: the inclusion $\OO_C\subseteq\mathcal E_0$ gives a nonzero section; for $\mathcal M$ of negative degree both end terms of the twisted sequence have negative degree because $\deg\mathcal L=-e<0$, so $H^0(C,\mathcal E_0\tensor\mathcal M)=0$. The identification of extension classes with $H^1(C,\mathcal L^\vee)$ is Theorem 13 of Gunning, printed pp. 71--74, whose statement also attaches the split extension to the zero class, so a nonsplit sequence has nonzero class. Rescaling the inclusion of $\OO_C$, or the quotient to $\mathcal L$, rescales the class without changing the middle bundle, so only its nonzero scalar class is intrinsic; Theorem 14 of Gunning, printed pp. 87--90, proves that proportional classes give isomorphic bundles and non-proportional ones do not.

:::

:::

::: {.pf-step #s11}
The integer $e$ of step [](#s9){.pf-ref} satisfies
$$
\boxed{0<e\le2g-2.}
$$

::: pf-proof
The degree $\deg\mathcal L=-e$ is negative by step [](#s9){.pf-ref}. For the upper bound, the proof of Theorem 2.12, printed p. 376, argues from the nonvanishing of $H^1(C,\mathcal L^\vee)$: "in particular, $H^1(\mathcal L^\vee)\ne0$, so we must have $\deg\mathcal L^\vee\le2g-2$ (IV, 1.3.4). Since $e=-\deg\mathcal L$, we have $e\le2g-2$". Equivalently, Serre duality turns $0\ne\xi\in H^1(C,\mathcal L^\vee)$ into a nonzero section of $K_C\tensor\mathcal L$, whose degree $2g-2-e$ is therefore nonnegative.

:::

:::

::: {.pf-step #s12}
Conversely, given
$$
0<e\le2g-2,
\qquad
\deg\mathcal L=-e,
\qquad
0\ne\xi\in H^1(C,\mathcal L^\vee),
$$
let $0\to\OO_C\to\mathcal E_0\to\mathcal L\to0$ be the corresponding extension. Then $\mathcal E_0$ is normalized, indecomposable and not semistable.

::: pf-proof
Normalization is step [](#s10){.pf-ref}. The determinant is $\mathcal L$ of negative degree, so $\mathcal E_0$ is not semistable by step [](#s6){.pf-ref}. Indecomposability is Theorem 14 of Gunning, printed pp. 87--90, which parametrizes the indecomposable bundles with subbundle $\varphi$ and determinant $\xi$ by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$ and proves that two bundles are isomorphic exactly when their classes are proportional: for $\varphi=\OO_C$ that space is $\PP H^1(C,\mathcal L^\vee)$, and the nonzero class $\xi$ is one of its points. Theorem 14 is stated for a compact Riemann surface, as Gunning's whole book is; the direct rank-two argument that follows gives the indecomposability of $\mathcal E_0$ without that setting. In rank two: if $\mathcal E_0\cong\mathcal B\oplus\mathcal C$ then one summand has a nonzero section, hence degree $0$ by step [](#s3){.pf-ref} and is $\OO_C$, the other is $\det\mathcal E_0\cong\mathcal L$ of negative degree and so has no sections, and the given inclusion is then the standard summand up to scalar, so the extension splits.

:::

:::

::: {.pf-step #s13}
The construction of steps [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref} and [](#s12){.pf-ref} gives a bijection between tensor-equivalence classes of indecomposable non-semistable rank-two bundles and the data
$$
\boxed{\left(e,\mathcal L,[\xi]\right),\quad 0<e\le2g-2,\quad \deg\mathcal L=-e,\quad [\xi]\in\PP H^1(C,\mathcal L^\vee).}
$$

::: pf-proof
Starting from $\mathcal E$, step [](#s8){.pf-ref} gives its unique maximal-degree line subbundle $\mathcal A$, and tensoring by $\mathcal A^{-1}$ gives a canonical normalized representative $\mathcal E_0$ of its tensor-equivalence class, whose own maximal subbundle is $\OO_C$ with quotient $\mathcal L=\det\mathcal E_0$; this is Theorem 14 of Gunning, printed pp. 87--90, read with the uniqueness of Lemma 15, printed pp. 83--85. Two extensions with proportional nonzero classes have isomorphic middle bundles and otherwise distinct ones, again by Theorem 14, and step [](#s12){.pf-ref} shows that every displayed triple occurs; the bijection is therefore over a compact Riemann surface, Theorem 14 being what gives both the parametrization and the injectivity of the classification. Tensoring by a line bundle preserves indecomposability and shifts every slope by the same degree, so it preserves non-semistability, and it changes the determinant, so the triples of a bundle and of its twists differ and the classification is up to tensor equivalence rather than up to isomorphism.

:::

:::

::: pf-qed
Step [](#s2){.pf-ref} proves part (a) in every rank, steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (b), and steps [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref}, [](#s12){.pf-ref} and [](#s13){.pf-ref} prove part (c) for a curve over $\CC$, a compact Riemann surface, where the parametrization and the injectivity of the classification are Gunning's Theorem 14.

:::

:::

:::

::: {.remark title="Published solution"}
Gunning, *Lectures on vector bundles over Riemann surfaces*, §(c), printed pp. 82--83, states the stability condition in the form $c(\varphi)<\frac12c(\det\Phi)$ for every line subbundle, defines $\operatorname{div}\Phi=\max_{\varphi\subset\Phi}c(\varphi)$, and observes that $\Phi$ is stable exactly when $\operatorname{div}\Phi<\frac12c(\det\Phi)$; his Lemma 14, printed pp. 81--82, gives $\operatorname{div}\Phi\ge\frac1{\rank}c(\det\Phi)$ for a decomposable $\Phi=\varphi_1\oplus\cdots\oplus\varphi_m$, a direct sum of line bundles, which with his rank-two stability definition is part (a) in rank two, and on printed p. 85 he records that "every decomposable bundle is unstable"; in general $\operatorname{div}\Phi\ge\frac1{\rank}c(\det\Phi)-g$; his Lemma 15, printed pp. 83--85, is the uniqueness of the maximal-degree line subbundle; and his Theorem 14, printed pp. 87--90, parametrizes the indecomposable unstable bundles with a given subbundle $\varphi$ and determinant $\xi$ by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$, which is the classification of part (c) with $\varphi=\OO_C$ and $\xi=\mathcal L$. Steps [](#s3){.pf-ref} to [](#s13){.pf-ref} follow that route, and step [](#s2){.pf-ref} is the slope argument for part (a) in every rank, with the determinant bound $0<e\le2g-2$ of step [](#s11){.pf-ref} from the proof of Theorem 2.12, printed p. 376, the normalization of step [](#s10){.pf-ref} from Example 2.11.6, printed p. 375, and the existence of the maximum of step [](#s7){.pf-ref}, which Gunning establishes on printed p. 80 by bounding the Chern classes of subbundles from above, and which the card also proves by global generation. Gunning works over a compact Riemann surface, which is the case of part (c) that the statement records; the rank-two argument of step [](#s12){.pf-ref} supplies the indecomposability of the constructed bundle directly, while the parametrization and the injectivity of the classification are his Theorem 14.
Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.8, printed pp. 103--104, proves (a) in every rank from the weighted mean of the two slopes, which is step [](#s2){.pf-ref}, and (b) by the rearrangements of steps [](#s1){.pf-ref} to [](#s6){.pf-ref}, and concludes (c) with "all indecomposable locally free sheaves $\mathcal E$ of rank 2 that are not semistable are classified, up to isomorphism, by these three conditions" — the printed clause; its argument assumes the bundle has $\OO_C$ as a subbundle with $\deg\mathcal L<0$, that is, takes the bundle to be the normalized model, so the twist that changes the bundle and leaves the data fixed is not accounted for there.

Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework solutions, Exercise 8 of §2 (solution by Tzu-Yang Chou), PDF p. 8 of that set, proves (a) by exhibiting both summand quotients and (b) in both directions, "if $\mathcal E$ is unstable, say $\exists F\subseteq\mathcal E$ invertible with $\deg F\ge\frac12\deg\mathcal E>0$, then $0\to\OO\to\mathcal E\tensor F^{-1}$ but $H^0(\mathcal E\tensor F^{-1})=0$ by the normalized assumption". Its (c) is the single sentence "This is just the proof of Theorem 2.12, combined with (b)", so it gives no argument for (c) and does not treat the twist either.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.8, PDF pp. 265--266. Part (a) he proves through "$\mathcal E$ stable $\Rightarrow$ every nonzero morphism $\mathcal E\to\mathcal E$ is an isomorphism", which fails for the endomorphism $\id\oplus0$ of a decomposable bundle. Part (b) he proves in both directions: a (semi)stable bundle of (negative) non-positive degree has no sections, so normalized forces degree $\ge0$, and conversely a line subbundle of degree $>\frac12\deg\mathcal E$ would give a section of $\mathcal E\tensor\mathcal F^\vee$ of negative degree. Part (c) he derives from a Harder--Narasimhan filtration, citing Potier for its uniqueness, concludes "Since the filtration was unique we have this up to isomorphism", and does not address the tensor twist: his $\mathcal L$ is the quotient $\mathcal E/F_1$ rather than the normalized determinant, and the subbundle $F_1$ is not among the data, so his last inference does not follow.

:::
