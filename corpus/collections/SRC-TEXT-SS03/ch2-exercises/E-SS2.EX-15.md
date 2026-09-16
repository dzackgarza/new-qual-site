---
schema: qual/card@1
id: E-SS2.EX-15
kind: problem
title: Boundary modulus one with f non-vanishing implies constant (Schwarz reflection)
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
15. Suppose $f$ is a non-vanishing continuous function on $\overline{\mathbb{D}}$ that is holomorphic in $\mathbb{D}$.
    Prove that if

$$
| f (z) | = 1 \quad \text { whenever } | z | = 1,
$$

then $f$ is constant.

[Hint: Extend $f$ to all of $\mathbb{C}$ by $f ( z ) = 1 / \overline { f ( 1 / \overline { { z } } ) }$ whenever $|z| > 1$, and argue as in the Schwarz reflection principle.]
:::

::: {.solution}
Because $f$ is continuous on $\overline{\mathbb D}$, holomorphic on $\mathbb D$, and satisfies $|f|=1$ on $\partial\mathbb D$, the maximum-modulus principle gives
\[
|f(z)|\le1\qquad(z\in\mathbb D).
\tag{1}
\]

Since $f$ is non-vanishing on $\overline{\mathbb D}$, the function $1/f$ is continuous on $\overline{\mathbb D}$ and holomorphic on $\mathbb D$. On the boundary,
\[
\left|\frac1{f(z)}\right|=1.
\]
Applying the maximum-modulus principle to $1/f$ yields
\[
\frac1{|f(z)|}\le1,
\]
so
\[
|f(z)|\ge1\qquad(z\in\mathbb D).
\tag{2}
\]
Combining (1) and (2) gives $|f(z)|=1$ throughout $\mathbb D$.

If $f$ were nonconstant, the open mapping theorem would imply that $f(\mathbb D)$ is open in $\mathbb C$, but it is contained in the unit circle, which has empty interior. This is impossible. Hence $f$ is constant.
:::
