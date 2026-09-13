---
schema: qual/card@1
id: PR-FULCRIT
kind: proposition
title: Smooth, complete, projective, Fano, read off the fan
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Fans
  - Ample Divisors
relations:
- kind: uses
  target: PR-D2F15
- kind: uses
  target: PR-TORMOR
- kind: uses
  target: PR-TORPOS
review: draft
prompts:
- State the fan condition equivalent to each of smooth, simplicial, complete, projective and Fano.
- Which fan conditions fail for a complete toric variety that is not projective?
---

::: {.proposition title="One table"}
Let $X_\Sigma$ be the toric variety of a fan $\Sigma$ in $N_\RR \cong \RR^n$.

| $X_\Sigma$ has the property | exactly when $\Sigma$ satisfies |
| --- | --- |
| normal | always: each $S_\sigma$ is saturated |
| smooth | every cone is spanned by part of a $\ZZ$-basis of $N$; in dimension $n$, $\det = \pm 1$ |
| simplicial, equivalently $\QQ$-factorial, equivalently finite quotient singularities only | every cone is spanned by $\RR$-independent vectors, that is $\det \neq 0$ |
| complete, equivalently compact | $\abs{\Sigma} = N_\RR$ |
| projective | $\Sigma$ is the normal fan of a lattice polytope, equivalently some $D$ has strictly convex support function |
| Fano | $\Sigma$ is the fan of cones over the faces of a reflexive polytope |

For a divisor $D = \sum a_\rho D_\rho$ with support function $\varphi_D$ on a complete $\Sigma$:

| $D$ has the property | exactly when |
| --- | --- |
| base point free | $\varphi_D$ is convex |
| ample | $\varphi_D$ is strictly convex |
| very ample | ample, and each vertex semigroup $\ts{m - m_\sigma \st m \in P_D \intersect M}$ is saturated in $M$ |
:::

::: {.remark title="How the rows depend on each other"}
Smooth implies simplicial, so a cone that is not simplicial is singular before any determinant is computed.
Projective implies complete, and the converse fails: a complete fan admitting no strictly convex support function gives a proper variety that is not projective.
Fano implies projective, since $-K_X$ ample is itself a strictly convex support function.

Two rows collapse in low dimension.
On a smooth complete toric variety ample and very ample agree, and on any complete toric surface they agree as well, so a counterexample needs dimension three and a singular point.
:::

::: {.remark title="Worked positivity on two families"}
On $\PP^n$ with $D = \sum a_i D_i$, base point free means $\sum a_i \geq 0$ and ample means $\sum a_i > 0$.

On $\FF_m$ with rays labelled as $D_1, \ldots, D_4$ in cyclic order, $\Pic(\FF_m) = \gens{D_1, D_4}$, and $D = a D_1 + b D_4$ is ample exactly when $a > 0$ and $b > 0$.
:::
