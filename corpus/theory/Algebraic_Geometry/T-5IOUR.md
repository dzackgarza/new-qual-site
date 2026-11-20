---
schema: qual/card@1
id: T-5IOUR
kind: theorem
title: Serre's cohomological criterion for affineness
slogan: 'For Noetherian schemes, affine means no higher quasicoherent cohomology; it already suffices to kill $H^1$ of coherent ideals.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Criterion
  - Affine Schemes
  - Cohomology
relations:
- kind: uses
  target: T-SK599
- kind: uses
  target: D-PTIW0
review: draft
prompts:
- State Serre's criterion for affineness.
- Can the Noetherian hypothesis be weakened?
- What fails without quasicompactness?
---

::: {.theorem}
Let $X$ be a Noetherian scheme.
The following are equivalent:

(i) $X$ is affine.

(ii) $H^p(X, \mcf) = 0$ for all quasicoherent $\mcf$ and all $p > 0$.

(iii) $H^1(X, \mci) = 0$ for every coherent sheaf of ideals $\mci$.

[@Har77, Theorem III.3.7]
:::

::: {.proof}
The implication (i) $\Rightarrow$ (ii) is Serre vanishing on an affine scheme, [[T-COHAFF]], which is [@Har77, Theorem III.3.5]; (ii) $\Rightarrow$ (iii) is immediate, a coherent sheaf of ideals being quasicoherent.
The substance is (iii) $\Rightarrow$ (i), proved in [@Har77, Theorem III.3.7] by Serre's criterion for affineness [@Har77, Exercise II.2.17]: one first covers $X$ by open affines of the form $X_f$, which uses only (iii) applied to the ideal sheaf of the complement of an affine open set, and then applies the criterion to conclude that $X$ is affine.
:::

::: {.remark title="Scope of the hypotheses"}
For a quasicompact quasi-separated scheme $X$, affineness is equivalent to
$$
H^p(X,\mcf)=0
$$
for every quasicoherent $\mcf$ and every $p>0$. In the ideal-sheaf form, coherent ideals in the Noetherian theorem are replaced by quasicoherent ideals.

Quasicompactness cannot be omitted. Let
$$
X=\coprod_{i\in I}\Spec k
$$
for an infinite set $I$. For every quasicoherent sheaf $\mcf$, cohomology is computed componentwise and
$$
H^p(X,\mcf)=0\qquad(p>0).
$$
However $X$ is not affine. Indeed
the open cover by its components has no finite subcover, so $X$ is not quasicompact, whereas every affine scheme is quasicompact by [[PR-SCHUNITCOVER]].
:::
