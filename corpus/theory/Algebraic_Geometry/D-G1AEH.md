---
schema: qual/card@1
id: D-G1AEH
kind: definition
title: The genus in its several senses
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Curves
  - Singularities
relations:
- kind: uses
  target: D-L6ERW
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- What is the genus of a curve?
- Define the geometric genus.
- What might the geometric genus of a singular curve be?
- Does the genus depend on the embedding?
---

::: {.definition}
For a projective curve $C$ over $k = \bar{k}$:

- the **arithmetic genus** is $p_a(C) = 1 - \chi(\OO_C)$, the constant term of the Hilbert polynomial read with a sign;

- the **geometric genus** is $p_g(C) = h^0(\tilde{C}, \omega_{\tilde{C}}) = p_a(\tilde{C})$, computed on the normalization $\tilde{C}$.
:::

::: {.proposition}
$p_g \leq p_a$, with
\[
p_a(C) - p_g(C) = \sum_{p \in C} \delta_p ,
\]
the sum of the delta invariants $\delta_p = \dim_k (\nu_* \OO_{\tilde{C}} / \OO_C)_p$ over the singular points.
A node contributes $\delta = 1$, an ordinary cusp $\delta = 1$, an ordinary $m$-fold point $\binom{m}{2}$.
:::

::: {.remark}
The two genera agree exactly when $C$ is smooth, and the difference is a sum of local contributions. The geometric genus ranges from $0$ up to $p_a$, according to the singularities.
A plane curve of degree $d$ has $p_a = \binom{d-1}{2}$ regardless of its singularities, and its geometric genus is that number minus the $\delta$'s — which is how a nodal cubic has $p_a = 1$ and $p_g = 0$.

Neither number depends on the embedding.
$p_a$ is $1 - \chi(\OO_C)$, an invariant of the abstract curve, and $p_g$ is computed on the normalization.
The degree depends on the embedding, while the genus is unchanged.
Over $\CC$ both agree with half the first Betti number of the smooth model, which is the topological genus.
:::
