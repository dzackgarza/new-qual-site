---
schema: qual/card@1
id: P-AGH3411LERAYACYCLIC
kind: problem
title: Čech cohomology agrees with derived functor cohomology on acyclic covers
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Acyclic Covers
  - Sheaf Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the intersection-acyclicity hypothesis and both conclusions with the retained Hartshorne Chapter III section 4 transcription. The proof identifies both augmentations of the Cech-injective double complex as quasi-isomorphisms, handles products for an arbitrary cover, and identifies the resulting isomorphism with the canonical comparison map.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
This exercise shows that Čech cohomology will agree with the usual cohomology whenever the sheaf has no cohomology on any of the open sets.
More precisely, let $X$ be a topological space, $\mcf$ a sheaf of abelian groups, and $\mathfrak{U}=(U_i)$ an open cover.
Assume for any finite intersection $V=U_{i_0} \intersect \cdots \intersect U_{i_p}$ of open sets of the covering, and for any $k>0$, that $H^k(V, \restrictionof{\mcf}{V})=0$.
Then prove that for all $p \geq 0$, the natural maps
$$
\check{H}^p(\mathfrak{U}, \mcf) \to H^p(X, \mcf)
$$
of (4.4) are isomorphisms.
Show also that one can recover (4.5) as a corollary of this more general result.
:::

::: {.solution}
Choose an injective resolution $\mcf\to I^\bullet$ in the category of abelian sheaves on $X$.
Use the double complex
$$
B^{p,q}=C^p(\mathfrak U,I^q)
=\prod_{i_0<\cdots<i_p}\Gamma(U_{i_0}\cap\cdots\cap U_{i_p},I^q)
\qquad(p,q\ge0),
$$
with the Čech differential horizontally and the resolution differential vertically.
Its total differential on bidegree $(p,q)$ is $d_{\mathrm{Cech}}+(-1)^p d_I$.
Each total degree contains only finitely many bidegrees, even when the cover itself is infinite.

::: pf

::: {.pf-step #s1}

The augmentation $\Gamma(X,I^\bullet)\to\operatorname{Tot}B$ is a quasi-isomorphism.

::: pf-proof

Every injective abelian sheaf $I^q$ is flasque [@Har10a, Lemma III.2.4].
A flasque sheaf has zero positive-degree Čech cohomology on every open cover, and its degree-zero Čech cohomology is its group of global sections [@Har10a, Lemma III.4.1 and Proposition III.4.3].
Thus the horizontal cohomology of $B$ is concentrated in column zero, where it is the complex $\Gamma(X,I^\bullet)$.
The first-quadrant double-complex filtration gives the asserted quasi-isomorphism.
Equivalently, filter the cone of the augmentation by the resolution degree: its graded complexes are the exact augmented Čech rows, so its total cohomology is zero.
The filtration has finitely many terms in each total degree, which is the convergence condition used here.
This is the augmented double-complex construction in [[P-AGH344REFINEMENTH1]], step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s2}

Under the intersection-acyclicity hypothesis, $C^\bullet(\mathfrak U,\mcf)\to\operatorname{Tot}B$ is a quasi-isomorphism as well.

::: pf-proof

For every finite intersection $V$ of cover members, the restricted resolution $\mcf|_V\to I^\bullet|_V$ is exact and consists of flasque sheaves.
It therefore computes $H^q(V,\mcf|_V)$ after applying $\Gamma(V,-)$ [@Har10a, Proposition III.2.5].
For fixed $p$, the vertical complex $B^{p,\bullet}$ is the product of these section complexes over all the $(p+1)$-fold intersections.
Products are exact in abelian groups: their kernels are computed componentwise, and a tuple of images has a tuple of preimages by choosing one in each component.
Hence its cohomology is
$$
H^q(B^{p,\bullet})\cong
\prod_{i_0<\cdots<i_p}H^q(U_{i_0}\cap\cdots\cap U_{i_p},\mcf).
$$
By the hypothesis, these groups vanish for $q>0$.
For $q=0$ they are precisely $C^p(\mathfrak U,\mcf)$, with its usual Čech differential.
The vertical-first filtration consequently gives the claimed quasi-isomorphism, with the same finite-per-total-degree convergence as in step [](#s1){.pf-ref}.
Thus no finiteness of the index set of the cover was required.

:::

:::

::: {.pf-step #s3}

The natural comparison maps in the statement are isomorphisms in all degrees.

::: pf-proof

The augmentation from step [](#s1){.pf-ref} identifies the cohomology of $\operatorname{Tot}B$ with the cohomology of $\Gamma(X,I^\bullet)$, which is $H^p(X,\mcf)$.
Composing the cohomology map of step [](#s2){.pf-ref} with the inverse of the cohomology isomorphism in step [](#s1){.pf-ref} is exactly the canonical comparison map of [@Har10a, Lemma III.4.4], as described in [[P-AGH344REFINEMENTH1]], step [](#s3){.pf-ref}.
Both maps are now isomorphisms, giving
$$
\boxed{\check H^p(\mathfrak U,\mcf)\xrightarrow{\cong}H^p(X,\mcf)\qquad(p\ge0).}
$$
The construction is compatible with morphisms of sheaves and refinements of the cover by the same double-complex maps.

:::

:::

::: {.pf-step #s4}

The affine-cover comparison theorem (III.4.5) follows.

::: pf-proof

Let $X$ be a noetherian separated scheme, let $\mathfrak U$ be an affine open cover, and let $\mcf$ be quasi-coherent.
Every finite intersection of these opens is affine because $X$ is separated.
The restriction of $\mcf$ to such an intersection is quasi-coherent, so all its positive-degree cohomology vanishes by [[T-COHAFF]] [@Har10a, Theorem III.3.5].
The hypothesis of step [](#s2){.pf-ref} is therefore satisfied.
Step [](#s3){.pf-ref} supplies the Čech comparison isomorphisms in all degrees, which is the assertion of Theorem III.4.5.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove the general acyclic-cover theorem, and step [](#s4){.pf-ref} recovers the requested affine-cover corollary.

:::

:::

:::
