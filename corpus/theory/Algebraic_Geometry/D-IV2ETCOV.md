---
schema: qual/card@1
id: D-IV2ETCOV
kind: definition
title: Étale covers, trivial covers, and simple connectedness of $\PP^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Étale Morphisms
  - Fundamental Group
  - Riemann-Hurwitz
relations:
- kind: uses
  target: D-MORETALE
- kind: uses
  target: T-LKT0U
review: draft
prompts:
- What is an étale cover, and what is a trivial one?
- What does it mean for a curve to be simply connected?
- Prove that $\PP^1$ has no nontrivial étale covers.
- Is $\AA^1$ simply connected?
---

::: {.definition title="Étale cover"}
A morphism $f : X \to Y$ is an **étale cover** if it is finite and étale.
It is a **trivial** cover if $X \cong \coprod_{i \in I} Y$ for a finite index set $I$, with $f$ the identity on each copy.
$Y$ is **simply connected** if every étale cover of $Y$ is trivial, equivalently $\pi_1^{\Et}(Y) = 0$.
:::

::: {.theorem}
$\PP^1_k$ over $k = \kbar$ is simply connected, in every characteristic.
:::

::: {.proof}
Let $f : X \to \PP^1$ be an étale cover; it is enough to treat $X$ connected, and then to show $f$ is an isomorphism.
$X$ is regular because $f$ is étale and $\PP^1$ is smooth over $k$, and a connected regular scheme is irreducible, so $X$ is a curve; $f$ is finite, so $X$ is projective; $f$ is unramified, so $k(X)/k(\PP^1)$ is separable.
Riemann--Hurwitz therefore applies, and $R = 0$ since $f$ is unramified, so with $n = \deg f$,
\[
2 g_X - 2 = n(2 \cdot 0 - 2) = -2n .
\]
Then $g_X \geq 0$ gives $-2n \geq -2$, so $n = 1$ and $g_X = 0$, and a finite morphism of degree $1$ between curves is an isomorphism.
:::

::: {.remark title="Reading the argument"}
Finiteness makes $X$ a projective curve so that the genus exists, étaleness supplies both the separability needed for Riemann--Hurwitz and the vanishing $R = 0$, and the inequality $g_X \geq 0$ bounds the degree.
The argument is the algebraic analogue of the topological computation of $\pi_1(S^2)$ by Euler characteristic, with $2 - 2g$ in the role of $\chi$.

The argument holds in every characteristic.
$\AA^1$ is *not* simply connected in characteristic $p$: the Artin--Schreier cover $y^p - y = x$ is finite étale of degree $p$ and connected, because $d(y^p - y) = -dy$ never vanishes.
So the projective line and the affine line separate here, the missing point at infinity is where the cover of $\AA^1$ ramifies wildly, and $\pi_1^{\Et}(\AA^1_{\overline{\FF}_p})$ is enormous while $\pi_1^{\Et}(\PP^1) = 0$.
Over $\CC$ both are topologically simply connected.
:::

::: {.remark title="Finiteness of covers"}
The finite étale covers of [[D-MORETALE]] are classified by $\pi_1^{\Et}$. An open immersion is étale but need not be finite, so finiteness is required in the statement about covers of $\PP^1$.
:::
