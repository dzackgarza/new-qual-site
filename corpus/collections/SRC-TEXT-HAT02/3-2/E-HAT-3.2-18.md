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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 18; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both halves. For $M_g$ the symplectic basis gives a nondegenerate pairing on $H^1$, so
    each nonzero class pairs nontrivially with something. If $M_g\simeq X\vee Y$ then one factor,
    say $X$, has $H_2=0$ and nonzero $H_1$, hence $H^2(X;\ZZ)=0$ by the universal coefficient
    theorem, and a nonzero class from that summand pairs trivially with everything. The
    nonorientable case repeats the argument over $\ZZ_2$, where the pairing on $H^1(N_g;\ZZ_2)$ is
    nondegenerate in the dual crosscap basis.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 18 (p.230) with all three sentences. Rechecked: the symplectic basis of Exercise 1 p.228 makes the cup product on H^1(M_g;Z) nondegenerate, so every nonzero class pairs nontrivially; a splitting M_g = X v Y with both reduced homologies nontrivial forces one factor to have H_2 = 0 and H_1 nonzero free, hence H^1 != 0 and H^2 = 0 by Theorem 3.2 p.195, and a class from that factor is in the radical; for N_g over Z_2 the intersection form is the identity, and the same splitting argument works since H^2(N_g;Z_2) is one-dimensional and splits, so one factor has zero second cohomology. The wedge vanishing is now attributed to the relative cup product of p.209. Not covered: nothing about the case g with both factors having trivial reduced homology, excluded by the hypothesis.
---

::: {.problem}
For the closed orientable surface $M$ of genus $g \geq 1$, show that for each nonzero $\alpha \in H^1(M; \ZZ)$ there exists $\beta \in H^1(M; \ZZ)$ with $\alpha \beta \neq 0$.
Deduce that $M$ is not homotopy equivalent to a wedge sum $X \vee Y$ of CW complexes with nontrivial reduced homology.
Do the same for closed nonorientable surfaces using cohomology with $\ZZ_2$ coefficients.
:::

::: {.solution}
For an orientable surface $M_g$, choose the symplectic basis $a_1,b_1,\ldots,a_g,b_g$ of $H^1(M_g;\ZZ)$ computed in Exercise 1 of this section (p.228). With $u$ the orientation class,
$$
a_i\smile b_j=\delta_{ij}u,\qquad
b_i\smile a_j=-\delta_{ij}u,
$$
and all products of two $a$'s or two $b$'s vanish. If a class $\alpha$ has a nonzero $a_i$ coefficient, its product with $b_i$ is nonzero; if it has no $a_i$ coefficient but is nonzero, its product with a suitable $a_i$ is nonzero. Thus the pairing on $H^1(M_g;\ZZ)$ has zero radical.

Suppose $M_g\simeq X\vee Y$ with both factors having nontrivial reduced integral homology. Wedge homology splits, and $M_g$ has reduced integral homology only in degrees $1$ and $2$, with $H_2(M_g)\cong\ZZ$. Therefore one factor, say $X$, has $H_2(X)=0$, and its nontrivial reduced homology lies in $H_1(X)$. This group is a nonzero free abelian summand of $H_1(M_g)$, so $H^1(X;\ZZ)\ne0$ and the universal coefficient theorem gives $H^2(X;\ZZ)=0$. Choose a nonzero class $\alpha$ from this summand of $H^1(X\vee Y;\ZZ)$. Its product with a class from $Y$ is zero because products across wedge summands vanish, by the relative cup product of p.209; its product with a class from $X$ is pulled back from $\alpha_X\smile\beta_X\in H^2(X;\ZZ)=0$ under the retraction of the wedge onto $X$. Thus $\alpha$ is in the radical of the cup-product pairing, a contradiction.

For a closed nonorientable surface $N_g$, use $\ZZ_2$ coefficients. In the basis dual to its $g$ crosscap loops, the pairing $H^1(N_g;\ZZ_2)^2\to H^2(N_g;\ZZ_2)\cong\ZZ_2$ has identity matrix, hence zero radical: each crosscap loop has self-intersection $1$ and distinct ones are disjoint, and the cup product of the dual classes is the intersection number (Exercise 1 of this section, p.228, and Theorem 3.2, p.195, for the identification of $H^2$ with $\ZZ_2$). Its reduced integral homology is confined to $H_1(N_g;\ZZ)\cong\ZZ^{g-1}\oplus\ZZ_2$. If $N_g\simeq X\vee Y$ with both factors having nontrivial reduced integral homology, then each factor has nonzero $H_1$ as a direct summand of this group and hence nonzero $H^1(-;\ZZ_2)$. Since $H^2(N_g;\ZZ_2)$ is one-dimensional and splits over the wedge, one factor has zero second cohomology. Any nonzero degree-one class from that factor pairs to zero with every degree-one class of the wedge, again a contradiction.
:::
