---
schema: qual/card@1
id: PR-MORJAC
kind: proposition
title: The jacobian criterion for smoothness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Jacobian Criterion
  - Singularities
relations:
- kind: uses
  target: D-MORSM
review: draft
prompts:
- State the jacobian criterion.
- How do you check in practice that a variety is smooth at a point?
---

::: {.proposition title="Jacobian criterion"}
Let $k = \kbar$ and let $X = V(f_1, \dots, f_r) \subseteq \AA^n_k$ be of pure dimension $n - r$.
Then $X$ is smooth at a closed point $p$ exactly when the jacobian matrix
\[
J(p) = \qty{ \partial f_i / \partial x_j (p) }_{i,j}
\]
has rank $r$.
In general $X$ is smooth at $p$ of dimension $n - \rank J(p)$ when the two agree, and $\rank J(p) \leq r$ always, with strict inequality exactly at the singular points.
:::

::: {.remark}
This is the only computational tool in the topic, and the exam use is always the same: write the equations, differentiate, and solve $J = 0$ together with the equations themselves.
The last clause is the one people drop: a point of $V(J)$ is singular only if it also lies on $X$.

The hypothesis $k = \kbar$ is load-bearing and its failure is the same characteristic-$p$ inseparability seen elsewhere.
So is the pure-dimension hypothesis: for $X = V(xy, xz) \subseteq \AA^3$, a plane meeting a line, the jacobian rank is wrong along the whole line because the codimension is not constant.

The intrinsic statement behind the criterion is that $\mfm_p/\mfm_p^2$ has dimension $\dim \OO_{X,p}$, that is, $\OO_{X,p}$ is a regular local ring; the jacobian just computes the dimension of that cotangent space from a presentation.
That equivalence between smooth over $\kbar$ and regular is what the criterion is really testing.
:::
