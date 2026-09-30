---
schema: qual/card@1
id: D-0SYCY
kind: definition
title: Smooth and singular points; Jacobian and regularity criteria
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingularity
  - Tangent Spaces
  - Jacobian Criterion
relations:
- kind: uses
  target: D-5LJUX
review: draft
prompts:
- Give two criteria for a variety to be nonsingular at a point.
- What is the Zariski tangent space?
- In the Jacobian criterion, which polynomials are differentiated, and what rank is required?
---

::: {.definition title="Zariski tangent space"}
For $p \in X$ with local ring $\OO_{X,p}$ and maximal ideal $\mfm_p$, the \dfn{Zariski tangent space} is
$$
T_p X \definedas \dualof{(\mfm_p / \mfm_p^2)} .
$$
The point $p$ is \dfn{smooth} if $\dim_k T_p X = \dim_p X$, and \dfn{singular} otherwise.
:::

::: {.proposition title="Jacobian criterion"}
Let $X\subseteq\AA^n$ be an affine variety of dimension $d$, let $I(X) = \generators{f_1,\ldots,f_t} \subseteq k[x_1,\ldots,x_n]$, and let $J_X(p) = \left[ \partial f_i / \partial x_j (p) \right]$.
Then $\rank J_X(p)\le n-d$ for every $p\in X$, and $p$ is a smooth point if and only if $\rank J_X(p) = n-d$ [@Har10a, Theorem I.5.1].
:::

::: {.remark}
For every $p\in X$, $\dim_k T_pX\ge\dim_pX$.
The point $p$ is smooth if and only if $\OO_{X,p}$ is a regular local ring, and regularity of the local ring is defined at every point of a scheme, closed or not.

The $f_i$ in the Jacobian criterion generate the ideal $I(X)$.
Equations that cut out $X$ only as a set do not suffice: $V(x^2)=\{0\}\subseteq\AA^1$ has $J(0)=(0)$, of rank $0\ne1$, although $0$ is a smooth point of $\{0\}=V(x)$.

Over a perfect field, the Jacobian condition at $p$ is equivalent to regularity of $\OO_{X,p}$.
Over an imperfect field, the Jacobian condition is smoothness, which is preserved by base change to $\bar{k}$; regularity of $\OO_{X,p}$ is not.
Over $k = \FF_p(t)$ the closed subscheme $V(x^p - t) \subseteq \AA^1$ is the spectrum of a field, hence regular, but it is not smooth: after base change to $k(t^{1/p})$ it becomes $V((x - t^{1/p})^p)$, which is not reduced.
:::
