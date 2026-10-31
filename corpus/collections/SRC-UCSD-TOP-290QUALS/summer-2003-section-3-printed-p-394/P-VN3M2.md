---
schema: qual/card@1
id: P-VN3M2
kind: problem
title: Homology and cohomology of a closed oriented $3$-manifold with $\pi_1=\ZZ^{*2}$
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Homology
  - Cohomology
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: >-
    Justin sheet 13, Problem 7 states the same task. Replaced the
    list-style solution with the abelianization, universal
    coefficient, and Poincare-duality argument.
---

::: {.problem}
Let $M^3$ be a closed connected oriented 3-manifold with fundamental group isomorphic to the free group on two generators.
Compute the homology and cohomology groups $H_*(M;\ZZ)$ and $H^*(M;\ZZ)$.
:::

::: {.solution}
The Hurewicz map in degree one identifies
$$
H_1(M;\ZZ)\cong\Ab(\pi_1(M))\cong\ZZ^2.
$$
Connectedness gives $H_0(M;\ZZ)=\ZZ$. The universal
coefficient theorem gives
$$
H^1(M;\ZZ)
\cong\Hom(H_1(M;\ZZ),\ZZ)
\oplus\Ext^1_{\ZZ}(H_0(M;\ZZ),\ZZ)
\cong\ZZ^2.
$$
Poincaré duality for the closed oriented three-manifold
then gives
$$
H_2(M;\ZZ)\cong H^1(M;\ZZ)\cong\ZZ^2,
\qquad
H_3(M;\ZZ)\cong H^0(M;\ZZ)\cong\ZZ.
$$
Duality also gives $H^i(M;\ZZ)\cong H_{3-i}(M;\ZZ)$.
Thus
$$
H_i(M;\ZZ)\cong H^i(M;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,3,\\
\ZZ^2,&i=1,2,\\
0,&i>3.
\end{cases}
$$
:::
