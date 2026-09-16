---
schema: qual/card@1
id: FE-SRFFERMATQUARTIC
kind: example
title: The Fermat quartic is a K3 surface containing $48$ lines
classification:
  areas:
  - algebraic-geometry
  topics:
  - K3 Surfaces
  - Adjunction
  - Lines on Surfaces
relations:
- kind: uses
  target: T-SRFADJ
- kind: related-to
  target: T-SRFKOD
review: draft
prompts:
- What is the Fermat quartic?
---

::: {.example title="Fermat quartic"}
The \dfn{Fermat quartic} is $X = V(x^4 + y^4 + z^4 + w^4) \subseteq \PP^3_\CC$.

1. $X$ is smooth: the partial derivatives $4x^3, 4y^3, 4z^3, 4w^3$ vanish simultaneously only at the origin.

2. $X$ is a K3 surface. By adjunction $\omega_X \cong \OO_X(4 - 4) = \OO_X$, and the sequence $0 \to \OO_{\PP^3}(-4) \to \OO_{\PP^3} \to \OO_X \to 0$ gives $H^1(X, \OO_X) = 0$ because $H^1(\OO_{\PP^3}) = H^2(\OO_{\PP^3}(-4)) = 0$.

3. Its invariants are $\chi(\OO_X) = 2$, topological Euler characteristic $24$ by Noether's formula with $K_X^2 = 0$, $b_2 = 22$ and $h^{1,1} = 20$.

4. $X$ contains exactly $48$ lines. If $\zeta^4 = \eta^4 = -1$, the line $\{x = \zeta y,\ z = \eta w\}$ lies on $X$, since $x^4 + y^4 = (\zeta^4 + 1) y^4 = 0$ and likewise for $z, w$. There are $16$ such lines for each of the $3$ ways to split the coordinates into two pairs. Each line $L$ has $L^2 = -2$ by adjunction.

5. The lines span a sublattice of rank $20$ in $\operatorname{NS}(X)$, so $X$ has Picard number $20$, the maximum for a complex K3 surface.
:::
