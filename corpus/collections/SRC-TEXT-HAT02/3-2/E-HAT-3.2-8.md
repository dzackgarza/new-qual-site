---
schema: qual/card@1
id: E-HAT-3.2-8
kind: problem
title: Hatcher Section 3.2 Exercise 8
classification:
  areas:
  - topology
  topics:
  - Cohomology
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
---

# E-HAT-3.2-8

Let $X$ be $\mathbb{CP}^2$ with a cell $e^3$ attached by a map $S^2 \to \mathbb{CP}^1 \subset \mathbb{CP}^2$ of degree $p$, and let $Y = M(\mathbb{Z}_p, 2) \vee S^4$.
Thus $X$ and $Y$ have the same 3-skeleton but differ in the way their 4-cells are attached.
Show that $X$ and $Y$ have isomorphic cohomology rings with $\mathbb{Z}$ coefficients but not with $\mathbb{Z}_p$ coefficients.

::: {.solution}
Give $X$ the CW structure with one cell in dimensions $0,2,3,4$. The cellular boundary
\[
C_3(X;\mathbb Z)\longrightarrow C_2(X;\mathbb Z)
\]
is multiplication by $p$, while the other positive-dimensional cellular boundaries are zero. Hence
\[
H_2(X;\mathbb Z)\cong\mathbb Z_p,\qquad H_4(X;\mathbb Z)\cong\mathbb Z,
\]
and all other reduced integral homology groups vanish. The same is true for
\[
Y=M(\mathbb Z_p,2)\vee S^4.
\]
By the universal coefficient theorem,
\[
\widetilde H^3(X;\mathbb Z)\cong\mathbb Z_p,\qquad
H^4(X;\mathbb Z)\cong\mathbb Z,
\]
with all other positive-degree integral cohomology zero, and identically for $Y$. Degree reasons force every product of positive-degree integral classes to vanish, so the integral cohomology rings are isomorphic.

Now use $\mathbb Z_p$ coefficients. Since multiplication by $p$ becomes zero, both spaces have one-dimensional cohomology in degrees $2,3,4$. Let
\[
x\in H^2(X;\mathbb Z_p)
\]
be the class restricting to the standard generator of $H^2(\mathbb{CP}^2;\mathbb Z_p)$. The attached $3$-cell does not alter the $4$-cell cup-product calculation, and by naturality with respect to the inclusion of the $\mathbb{CP}^2$ subcomplex one has
\[
x^2\ne0\in H^4(X;\mathbb Z_p);
\]
in fact it is the generator.

For $Y$, the unique nonzero degree-two class $y$ is supported on the Moore-space wedge summand. Products of positive-dimensional classes from different wedge summands vanish, and the Moore space has no $4$-dimensional cohomology. Therefore
\[
y^2=0.
\]
Thus
\[
H^*(X;\mathbb Z_p)\not\cong H^*(Y;\mathbb Z_p)
\]
as graded rings, although the integral cohomology rings are isomorphic.
:::
