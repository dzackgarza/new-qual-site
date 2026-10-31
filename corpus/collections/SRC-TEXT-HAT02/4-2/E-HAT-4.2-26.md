---
schema: qual/card@1
id: E-HAT-4.2-26
kind: problem
title: "Isomorphic homotopy but different homotopy type"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Generalizing the example of $\RP^2$ and $S^2 \times \RP^\infty$, show that if $X$ is a connected finite-dimensional CW complex with universal cover $\tilde{X}$, then $X$ and $\tilde{X} \times K(\pi_1(X), 1)$ have isomorphic homotopy groups but are not homotopy equivalent if $\pi_1(X)$ contains elements of finite order.
:::

::: {.solution}
Put $G=\pi_1(X)$ and $Y=\widetilde X\times K(G,1)$. The first homotopy groups of $X$ and $Y$ are both $G$. For $n\ge2$, the covering map and the product formula give
$$
\pi_n(X)\cong\pi_n(\widetilde X)\cong\pi_n(Y).
$$
These are abstract group isomorphisms; they need not preserve the $G$-actions.

Suppose that $X\simeq Y$ and let $C_p\le G$ be a cyclic subgroup of prime order, obtained from an element of finite order. The homotopy equivalence lifts to a homotopy equivalence between the covers corresponding to $C_p$. The cover of $Y$ is
$$
\widetilde X\times K(C_p,1),
$$
whereas the corresponding cover $X_{C_p}$ of $X$ has the same finite CW dimension as $X$. Projection and inclusion make $K(C_p,1)$ a retract of the cover of $Y$. Hence its homology would be a direct summand of $H_*(X_{C_p};\ZZ)$ and would vanish above $\dim X$.

But the standard periodic resolution of the cyclic group gives
$$
H_{2k+1}(K(C_p,1);\ZZ)\cong\ZZ/p\qquad(k\ge0).
$$
This contradicts the finite dimension of $X_{C_p}$. Therefore $X$ and $Y$ are not homotopy equivalent.
:::
