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

(c) Show that the indecomposable locally free sheaves $\mathcal{E}$ of rank 2 that are not semistable are classified, up to isomorphism, by giving

   (1) an integer $0<e \leqslant 2 g-2$,

   (2) an element $\mathcal{L} \in \Pic C$ of degree $-e$, and

   (3) a nonzero $\xi \in H^1\left(\dualof{\mathcal{L}}\right)$, determined up to a nonzero scalar multiple.

:::

::: {.solution}
For a nonzero locally free sheaf $\mathcal F$ on $C$, write
$$
\mu(\mathcal F)=\frac{\deg\mathcal F}{\rank\mathcal F}.
$$

Read as printed, the clause "up to isomorphism" in part (c) cannot hold, and what steps [](#s9){.pf-ref} to [](#s13){.pf-ref} classify is the same data up to tensoring by an invertible sheaf. Let $\mathcal E_0$ be normalized, not semistable, with data $(e,\mathcal L,\xi)$, and let $\mathcal A$ be a line bundle of degree $m\ne0$. Tensoring by $\mathcal A$ shifts every slope by $m$, so the maximal-degree line subbundle of $\mathcal E_0\tensor\mathcal A$ is $\OO_C\tensor\mathcal A$, and the invariant data read off from it are
$$
\det(\mathcal E_0\tensor\mathcal A)\tensor(\OO_C\tensor\mathcal A)^{-2}
\cong\det\mathcal E_0,\qquad
(\mathcal E_0\tensor\mathcal A)\tensor(\OO_C\tensor\mathcal A)^{-1}\cong\mathcal E_0,
$$
so $e$, $\mathcal L$ and $\xi$ are unchanged, while $\deg(\mathcal E_0\tensor\mathcal A)=2m-e\ne-e=\deg\mathcal E_0$. Thus two non-isomorphic bundles carry the same triple, and the classification is up to tensor equivalence.

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
A decomposable rank-two bundle is never stable. This is part (a).

::: pf-proof
Gunning, §(c) with Lemma 14, printed pp. 81--82: for a decomposable bundle $\Phi=\varphi_1\oplus\cdots\oplus\varphi_m$ the determinant has $c(\det\Phi)=c(\varphi_1)+\cdots+c(\varphi_m)$, so one summand satisfies $c(\varphi_j)\ge\frac1m c(\det\Phi)$, and $\operatorname{div}\Phi=\max_jc(\varphi_j)\ge\frac1m c(\det\Phi)$, which is instability. In rank two, $\mathcal E=\mathcal A\oplus\mathcal B$ with $\mathcal A,\mathcal B$ invertible and, after interchanging them, $\deg\mathcal A\ge\deg\mathcal B$ gives
$$
\deg\mathcal A\ge\frac{\deg\mathcal A+\deg\mathcal B}{2}=\frac12\deg\mathcal E,
$$
and step [](#s1){.pf-ref} applies to the line subbundle $\mathcal A$.

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
This is the last step of the proof of Proposition 2.8, printed p. 373: a nonzero section $s\in H^0(C,\mathcal E)$ gives an injective map $\OO_C\to\mathcal E$, and its image spans a line subbundle. Normalization makes the quotient invertible — the book shows it is torsion-free and hence invertible on a curve — and the subbundle is $\OO_C$; step [](#s3){.pf-ref} bounds its degree above by $0$ and the nonzero section bounds it below.

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
The same reading of $\operatorname{div}\mathcal E=0$ against $\operatorname{div}\Phi\ge\frac12c(\xi)$, Gunning §(c), printed p. 83, with the weak inequality, and the subbundle $\OO_C$ for the converse. Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (b).

:::

:::

::: {.pf-step #s7}
Let $\mathcal E$ be a rank-two bundle that is not semistable. Among all line subbundles of $\mathcal E$ there is one of maximal degree.

::: pf-proof
The maximum is what Gunning's $\operatorname{div}\Phi=\max_{\varphi\subset\Phi}c(\varphi)$, printed p. 83, presupposes; the bound that makes it a maximum is not proved there and is the card's. Line subbundles exist, since a nonzero section of $\mathcal E(n)$ for $n\gg0$ saturates to an invertible subsheaf. Their degrees are bounded above: fix an ample $\OO_C(1)$ of degree $h>0$ and take $n\gg0$ so that $\mathcal E^\vee(n)$ is globally generated; dualizing the locally free quotient of a line subbundle $\mathcal A\subseteq\mathcal E$ gives a surjection $\mathcal E^\vee\twoheadrightarrow\mathcal A^\vee$, so $\mathcal A^\vee(n)$ is a quotient of a globally generated bundle and is globally generated, whence $-\deg\mathcal A+nh\ge0$ and $\deg\mathcal A\le nh$. The degrees are integers, so they have a maximum.

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
Normalization is step [](#s10){.pf-ref}. The determinant is $\mathcal L$ of negative degree, so $\mathcal E_0$ is not semistable by step [](#s6){.pf-ref}. Indecomposability is Theorem 14 of Gunning, printed pp. 87--90, which parametrizes the indecomposable bundles with subbundle $\varphi$ and determinant $\xi$ by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$ and proves that two bundles are isomorphic exactly when their classes are proportional: for $\varphi=\OO_C$ that space is $\PP H^1(C,\mathcal L^\vee)$, and the nonzero class $\xi$ is one of its points. In rank two the same conclusion is direct: if $\mathcal E_0\cong\mathcal B\oplus\mathcal C$ then one summand has a nonzero section, hence degree $0$ by step [](#s3){.pf-ref} and is $\OO_C$, the other is $\det\mathcal E_0\cong\mathcal L$ of negative degree and so has no sections, and the given inclusion is then the standard summand up to scalar, so the extension splits.

:::

:::

::: {.pf-step #s13}
The construction of steps [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref} and [](#s12){.pf-ref} gives a bijection between tensor-equivalence classes of indecomposable non-semistable rank-two bundles and the data
$$
\boxed{\left(e,\mathcal L,[\xi]\right),\quad 0<e\le2g-2,\quad \deg\mathcal L=-e,\quad [\xi]\in\PP H^1(C,\mathcal L^\vee).}
$$

::: pf-proof
Starting from $\mathcal E$, step [](#s8){.pf-ref} gives its unique maximal-degree line subbundle $\mathcal A$, and tensoring by $\mathcal A^{-1}$ gives a canonical normalized representative $\mathcal E_0$ of its tensor-equivalence class, whose own maximal subbundle is $\OO_C$ with quotient $\mathcal L=\det\mathcal E_0$; this is Theorem 14 of Gunning, printed pp. 87--90, read with the uniqueness of Lemma 15, printed pp. 83--85. Two extensions with proportional nonzero classes have isomorphic middle bundles and otherwise distinct ones, again by Theorem 14, and step [](#s12){.pf-ref} shows that every displayed triple occurs. Tensoring by a line bundle preserves indecomposability and shifts every slope by the same degree, so it preserves non-semistability, and it changes the determinant, so the triples of a bundle and of its twists differ and the classification is up to tensor equivalence rather than up to isomorphism.

:::

:::

::: pf-qed
Step [](#s2){.pf-ref} proves part (a), steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (b), and steps [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref}, [](#s12){.pf-ref} and [](#s13){.pf-ref} prove the corrected classification in part (c).

:::

:::

:::

::: {.remark title="Published solution"}
Gunning, *Lectures on vector bundles over Riemann surfaces*, §(c), printed pp. 82--83, states the stability condition in the form $c(\varphi)<\frac12c(\det\Phi)$ for every line subbundle, defines $\operatorname{div}\Phi=\max_{\varphi\subset\Phi}c(\varphi)$, and observes that $\Phi$ is stable exactly when $\operatorname{div}\Phi<\frac12c(\det\Phi)$; his Lemma 14, printed pp. 81--82, gives $\operatorname{div}\Phi\ge\frac1{\rank}c(\det\Phi)$ for decomposable $\Phi$, which is part (a), and $\operatorname{div}\Phi\ge\frac1{\rank}c(\det\Phi)-g$ in general; his Lemma 15, printed pp. 83--85, is the uniqueness of the maximal-degree line subbundle; and his Theorem 14, printed pp. 87--90, parametrizes the indecomposable unstable bundles with a given subbundle $\varphi$ and determinant $\xi$ by the points of $\PP H^1(C,\OO(\varphi^2\xi^{-1}))$, which is the classification of part (c) with $\varphi=\OO_C$ and $\xi=\mathcal L$. Steps [](#s1){.pf-ref} to [](#s13){.pf-ref} follow that route, with the determinant bound $0<e\le2g-2$ of step [](#s11){.pf-ref} from the proof of Theorem 2.12, printed p. 376, the normalization of step [](#s10){.pf-ref} from Example 2.11.6, printed p. 375, and the existence of the maximum of step [](#s7){.pf-ref}, which Gunning's $\operatorname{div}$ presupposes, proved on the card by global generation.
Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.2.8, printed pp. 103--104, proves (a) and (b) by the slope inequalities, the same route as steps [](#s1){.pf-ref} to [](#s6){.pf-ref}, and concludes (c) with "all indecomposable locally free sheaves $\mathcal E$ of rank 2 that are not semistable are classified, up to isomorphism, by these three conditions" — the printed clause, with no tensor twist considered, so it carries the defect recorded at the head of this solution rather than repairing it.

Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework solutions, text version `tmp/sources/ntu-ag2-chapter5.md`, Exercise 8 of §2 (solution by Tzu-Yang Chou), printed p. 8 of that set, proves (a) by exhibiting both summand quotients and (b) in both directions, "if $\mathcal E$ is unstable, say $\exists F\subseteq\mathcal E$ invertible with $\deg F\ge\frac12\deg\mathcal E>0$, then $0\to\OO\to\mathcal E\tensor F^{-1}$ but $H^0(\mathcal E\tensor F^{-1})=0$ by the normalized assumption". Its (c) is the single sentence "This is just the proof of Theorem 2.12, combined with (b)", so it gives no argument for (c) and does not treat the twist either.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.2.8, PDF pp. 265--266. Part (a) he proves through "$\mathcal E$ stable $\Rightarrow$ every nonzero morphism $\mathcal E\to\mathcal E$ is an isomorphism", which fails for the endomorphism $\id\oplus0$ of a decomposable bundle. Part (b) he proves in both directions: a (semi)stable bundle of (negative) non-positive degree has no sections, so normalized forces degree $\ge0$, and conversely a line subbundle of degree $>\frac12\deg\mathcal E$ would give a section of $\mathcal E\tensor\mathcal F^\vee$ of negative degree. Part (c) he derives from a Harder--Narasimhan filtration, citing Potier for its uniqueness, concludes "Since the filtration was unique we have this up to isomorphism", and does not address the tensor twist: his $\mathcal L$ is the quotient $\mathcal E/F_1$ rather than the normalized determinant, and the subbundle $F_1$ is not among the data, so his last inference does not follow.

:::
