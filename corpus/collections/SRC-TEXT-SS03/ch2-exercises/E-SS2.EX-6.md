---
schema: qual/card@1
id: E-SS2.EX-6
kind: problem
title: "Cauchy's theorem for a triangle with one bounded interior singularity"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
6. Let $\Omega$ be an open subset of C and let $T \subset \Omega$ be a triangle whose interior is also contained in Ω. Suppose that f is a function holomorphic in Ω except possibly at a point w inside $T$ . Prove that if $f$ is bounded near w, then

$$
\int_ {T} f (z) d z = 0.
$$
:::

::: solution
Choose $r>0$ so small that the closed square
\[
Q_r=\{w+x+iy:|x|\le r,\ |y|\le r\}
\]
lies in the interior of $T$ and in a neighborhood on which $|f|\le M$ for some $M$.

The compact polygonal region $T\setminus\operatorname{int}(Q_r)$ can be triangulated into finitely many triangles whose closures avoid $w$. On each such triangle $f$ is holomorphic in a neighborhood of the triangle and its interior, so Goursat's theorem gives zero integral around its boundary. Summing over the triangulation cancels all interior edges and yields
\[
\int_T f(z)\,dz=\int_{\partial Q_r}f(z)\,dz,
\]
where $\partial Q_r$ is positively oriented.

The perimeter of $Q_r$ is $8r$, so
\[
\left|\int_{\partial Q_r}f(z)\,dz\right|
\le 8Mr.
\]
Letting $r\downarrow0$ gives
\[
\int_T f(z)\,dz=0.
\]
Thus a bounded isolated singularity inside the triangle does not affect the conclusion of Cauchy's theorem.
:::
