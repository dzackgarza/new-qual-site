---
schema: qual/card@1
id: E-HAT-3.2-8
kind: problem
title: Spaces with isomorphic integral but distinct $\ZZ_p$ cohomology rings
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 8; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both coefficient computations: integrally both spaces are $\ZZ_p$ in degree $3$ and $\ZZ$
    in degree $4$, and every product of positive-dimensional classes vanishes for degree reasons,
    so the rings agree; over $\ZZ_p$ both are $\ZZ_p$ in degrees $2,3,4$, but in $X$ the class $x$
    restricts to the generator of $H^2(\CP^2)$, so $x^2\ne0$, while in $Y$ the class $y$ is
    supported on the Moore summand and $y^2=0$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 8 (p.229), with the printed description of X and Y intact. Rechecked integrally: d_3 = p and the other cellular boundaries vanish (Theorem 2.35 p.139, Cellular Boundary Formula p.141), so H_2 = Z_p, H_3 = 0, H_4 = Z; Theorem 3.2 p.195 then gives H^3 = Ext(Z_p,Z) = Z_p and H^4 = Z with everything else in positive degree zero, the same for Y, and all products vanish for degree reasons. Over Z_p both have one class in degrees 2,3,4; x^2 is nonzero by naturality of the inclusion CP^2 c X (which is an isomorphism in degrees 2 and 4), while y^2 lies in H^4(Y,S^4;Z_p) = H^4(M(Z_p,2);Z_p) = 0 by the relative cup product of p.209. So the rings differ. Not covered: nothing about higher powers, the rings having no classes above degree 4.
---

::: {.problem}
Let $X$ be $\CP^2$ with a cell $e^3$ attached by a map $S^2 \to \CP^1 \subset \CP^2$ of degree $p$, and let $Y = M(\ZZ_p, 2) \vee S^4$.
Thus $X$ and $Y$ have the same 3-skeleton but differ in the way their 4-cells are attached.
Show that $X$ and $Y$ have isomorphic cohomology rings with $\ZZ$ coefficients but not with $\ZZ_p$ coefficients.
:::

::: {.solution}
Give $X$ the CW structure with one cell in dimensions $0,2,3,4$. By Theorem 2.35 (p.139) with the Cellular Boundary Formula (p.141), the cellular boundary
$$
C_3(X;\ZZ)\longrightarrow C_2(X;\ZZ)
$$
is multiplication by $p$, the incidence number being the degree of the attaching map, while the other positive-dimensional cellular boundaries are zero. Hence
$$
H_2(X;\ZZ)\cong\ZZ_p,\qquad H_4(X;\ZZ)\cong\ZZ,
$$
and all other reduced integral homology groups vanish. The same is true for
$$
Y=M(\ZZ_p,2)\vee S^4.
$$
By the universal coefficient theorem (Theorem 3.2, p.195),
$$
\widetilde H^3(X;\ZZ)\cong\operatorname{Ext}(\ZZ_p,\ZZ)=\ZZ_p,\qquad
H^4(X;\ZZ)\cong\operatorname{Hom}(\ZZ,\ZZ)=\ZZ,
$$
with all other positive-degree integral cohomology zero, and identically for $Y$. Degree reasons force every product of positive-degree integral classes to vanish, so the integral cohomology rings are isomorphic.

Now use $\ZZ_p$ coefficients. Since multiplication by $p$ becomes zero, both spaces have one-dimensional cohomology in degrees $2,3,4$. Let
$$
x\in H^2(X;\ZZ_p)
$$
be the class restricting to the standard generator of $H^2(\CP^2;\ZZ_p)$. The attached $3$-cell does not alter the $4$-cell cup-product calculation, and by naturality with respect to the inclusion of the $\CP^2$ subcomplex one has
$$
x^2\ne0\in H^4(X;\ZZ_p);
$$
in fact it is the generator.

For $Y$, the unique nonzero degree-two class $y$ is supported on the Moore-space wedge summand: it restricts to $0$ on $S^4$, so it lifts to $H^2(Y,S^4;\ZZ_p)$, and the relative cup product of p.209 puts $y^2$ in $H^4(Y,S^4;\ZZ_p)=\widetilde H^4(M(\ZZ_p,2);\ZZ_p)$, which vanishes because the Moore space has cells only in dimensions $2$ and $3$. Therefore
$$
y^2=0.
$$
Thus
$$
H^*(X;\ZZ_p)\not\cong H^*(Y;\ZZ_p)
$$
as graded rings, although the integral cohomology rings are isomorphic.
:::
