---
schema: qual/card@1
id: E-HAT-3.2-11
kind: exercise
title: "Maps $S^{k+\\ell} \\to S^k \\times S^\\ell$ are trivial on top homology"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Using cup products, show that every map $S^{k+\ell} \to S^k \times S^\ell$ induces the trivial homomorphism $H_{k+\ell}(S^{k+\ell}) \to H_{k+\ell}(S^k \times S^\ell)$, assuming $k > 0$ and $\ell > 0$.

::: {.solution}
<1>1. Cohomology ring of the product $S^k \times S^\ell$:
<2>1. By the Künneth Theorem for cohomology with $\mathbb{Z}$ coefficients, the cohomology groups of $S^k \times S^\ell$ (with $k, \ell > 0$) are:
- $H^0(S^k \times S^\ell) \cong \mathbb{Z}$,
- $H^k(S^k \times S^\ell) \cong \mathbb{Z} \langle \alpha \rangle$,
- $H^\ell(S^k \times S^\ell) \cong \mathbb{Z} \langle \beta \rangle$,
- $H^{k+\ell}(S^k \times S^\ell) \cong \mathbb{Z} \langle \alpha \smile \beta \rangle$.
::: {.proof}
Künneth Theorem for product spaces.
:::
<2>2. In particular, the generator of top cohomology is the cup product $\gamma = \alpha \smile \beta \in H^{k+\ell}(S^k \times S^\ell)$.
::: {.proof}
cross product and cup product isomorphism in top degree.
:::

<1>2. Induced maps on cohomology:
<2>1. The cohomology of the sphere $S^{k+\ell}$ vanishes in all intermediate dimensions:
\[
H^i(S^{k+\ell}) = 0 \quad \text{for all } 0 < i < k + \ell.
\]
Because $k > 0$ and $\ell > 0$, we have $0 < k < k + \ell$ and $0 < \ell < k + \ell$, so $H^k(S^{k+\ell}) = 0$ and $H^\ell(S^{k+\ell}) = 0$.
::: {.proof}
cellular cohomology of spheres.
:::
<2>2. Therefore the induced homomorphisms in dimensions $k$ and $\ell$ must be zero:
\[
f^*(\alpha) = 0 \in H^k(S^{k+\ell}), \qquad f^*(\beta) = 0 \in H^\ell(S^{k+\ell}).
\]
::: {.proof}
unique homomorphism into the zero group.
:::
<2>3. Because $f^*: H^*(S^k \times S^\ell) \to H^*(S^{k+\ell})$ is a ring homomorphism respecting cup products:
\[
f^*(\alpha \smile \beta) = f^*(\alpha) \smile f^*(\beta) = 0 \smile 0 = 0 \in H^{k+\ell}(S^{k+\ell}).
\]
Thus $f^*: H^{k+\ell}(S^k \times S^\ell) \to H^{k+\ell}(S^{k+\ell})$ is the trivial (zero) homomorphism.
::: {.proof}
ring homomorphism property of pullback on cohomology.
:::

<1>3. Dualization to homology:
<2>1. By the Universal Coefficient Theorem for Cohomology, for any space $X$ with free finitely generated homology, $H^n(X) \cong \operatorname{Hom}(H_n(X), \mathbb{Z})$.
Under this canonical duality, the induced cohomology map $f^*$ is the transpose/dual of the induced homology map $f_*$:
\[
f^* = (f_*)^t: \operatorname{Hom}(H_{k+\ell}(S^k \times S^\ell), \mathbb{Z}) \to \operatorname{Hom}(H_{k+\ell}(S^{k+\ell}), \mathbb{Z}).
\]
::: {.proof}
Universal Coefficient Theorem naturality.
:::
<2>2. Since $f^* = 0$, its dual map on homology $f_*: H_{k+\ell}(S^{k+\ell}) \to H_{k+\ell}(S^k \times S^\ell)$ is also the zero homomorphism.
::: {.proof}
dual of the zero map on free abelian groups is zero.
:::

<1>4. Conclusion:
Every continuous map $S^{k+\ell} \to S^k \times S^\ell$ induces the trivial homomorphism on top homology. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
