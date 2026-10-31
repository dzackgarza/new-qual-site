---
schema: qual/card@1
id: E-HAT-3.2-18
kind: problem
title: Cup product nondegenerality on surfaces
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
For the closed orientable surface $M$ of genus $g \geq 1$, show that for each nonzero $\alpha \in H^1(M; \ZZ)$ there exists $\beta \in H^1(M; \ZZ)$ with $\alpha \beta \neq 0$.
Deduce that $M$ is not homotopy equivalent to a wedge sum $X \vee Y$ of CW complexes with nontrivial reduced homology.
Do the same for closed nonorientable surfaces using cohomology with $\ZZ_2$ coefficients.
:::

::: {.solution}
For an orientable surface $M_g$, choose the symplectic basis $a_1,b_1,\ldots,a_g,b_g$ of $H^1(M_g;\ZZ)$ from the surface cup-product calculation. With $u$ the orientation class,
$$
a_i\smile b_j=\delta_{ij}u,\qquad
b_i\smile a_j=-\delta_{ij}u,
$$
and all products of two $a$'s or two $b$'s vanish. If a class $\alpha$ has a nonzero $a_i$ coefficient, its product with $b_i$ is nonzero; if it has no $a_i$ coefficient but is nonzero, its product with a suitable $a_i$ is nonzero. Thus the pairing on $H^1(M_g;\ZZ)$ has zero radical.

Suppose $M_g\simeq X\vee Y$ with both factors having nontrivial reduced integral homology. Wedge homology splits, and $M_g$ has reduced integral homology only in degrees $1$ and $2$, with $H_2(M_g)\cong\ZZ$. Therefore one factor, say $X$, has $H_2(X)=0$, and its nontrivial reduced homology lies in $H_1(X)$. This group is a nonzero free abelian summand of $H_1(M_g)$, so $H^1(X;\ZZ)\ne0$ and the universal coefficient theorem gives $H^2(X;\ZZ)=0$. Choose a nonzero class $\alpha$ from this summand of $H^1(X\vee Y;\ZZ)$. Its product with a class from $Y$ is zero because products across wedge summands vanish; its product with a class from $X$ lies in $H^2(X;\ZZ)=0$. Thus $\alpha$ is in the radical of the cup-product pairing, a contradiction.

For a closed nonorientable surface $N_g$, use $\ZZ_2$ coefficients. In the basis dual to its $g$ crosscap loops, the pairing $H^1(N_g;\ZZ_2)^2\to H^2(N_g;\ZZ_2)\cong\ZZ_2$ has identity matrix, hence zero radical. Its reduced integral homology is confined to $H_1(N_g;\ZZ)\cong\ZZ^{g-1}\oplus\ZZ_2$. If $N_g\simeq X\vee Y$ with both factors having nontrivial reduced integral homology, then each factor has nonzero $H_1$ as a direct summand of this group and hence nonzero $H^1(-;\ZZ_2)$. Since $H^2(N_g;\ZZ_2)$ is one-dimensional and splits over the wedge, one factor has zero second cohomology. Any nonzero degree-one class from that factor pairs to zero with every degree-one class of the wedge, again a contradiction.
:::
