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
- Show that a nonsingular projective curve has $p_a = p_g = h^1(\OO_X)$.
---

::: {.definition}
For a projective integral curve $C$ over $k = \bar{k}$:

- the \dfn{arithmetic genus} is $p_a(C) = 1 - \chi(\OO_C)$, the constant term of the Hilbert polynomial read with a sign;

- the \dfn{geometric genus} is $p_g(C) = h^0(\tilde{C}, \omega_{\tilde{C}}) = p_a(\tilde{C})$, computed on the normalization $\tilde{C}$.
:::

::: {.proposition title="One genus for a nonsingular curve"}
If $X$ is a nonsingular projective curve over $k = \bar k$, then
$$
p_a(X) = p_g(X) = \dim_k H^1(X, \OO_X) ,
$$
the \dfn{genus} $g$ of $X$: since $h^0(\OO_X) = 1$, $p_a = 1 - \chi(\OO_X) = h^1(\OO_X)$, and Serre duality gives $h^0(\omega_X) = h^1(\OO_X)$.
[@Har10a, Exercise III.5.3]
:::

::: {.proposition}
$p_g \leq p_a$, with
$$
p_a(C) - p_g(C) = \sum_{p \in C} \delta_p ,
$$
the sum of the delta invariants $\delta_p = \dim_k (\nu_* \OO_{\tilde{C}} / \OO_C)_p$ over the singular points.
A node contributes $\delta = 1$, an ordinary cusp $\delta = 1$, an ordinary $m$-fold point $\binom{m}{2}$.
:::

::: {.remark}
The normalization formula gives $0\le p_g(C)\le p_a(C)$, with equality of the two genera exactly when $C$ is smooth.
A plane curve of degree $d$ has $p_a = \binom{d-1}{2}$ for every choice of singularities, and $p_g=\binom{d-1}{2}-\sum_p\delta_p$; a nodal cubic has $p_a = 1$ and $p_g = 0$.

Both genera are invariants of the abstract curve: $p_a = 1 - \chi(\OO_C)$, and $p_g$ is computed on the normalization.
The degree depends on the embedding.
For a nonsingular projective complex curve, both genera equal half its first Betti number, by the Hodge decomposition and Serre duality [@Har10a, Appendix B and Exercise III.5.3].
For a singular complex curve, the topological genus of its smooth model is $p_g(C)$; a nodal cubic has smooth model $\PP^1$, of genus zero, and arithmetic genus one.
:::
