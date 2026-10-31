---
schema: qual/card@1
id: P-PRACT20-W3-27
kind: problem
title: Line integral of $(xy,x^2y^3)$ around a triangle
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Green's Theorem
relations: []
review: draft
---

::: {.problem}
Let $C$ be the triangle with vertices $(0, 0)$, $(1, 0)$, $(1, 2)$. Find the path integral of $\mathbf{F}(x, y) = (xy, x^{2} y^{3})$ around this curve.
:::

::: {.solution}
Traverse the triangle counterclockwise and let $D$ be the enclosed region. By Green's theorem, with $\frac{\partial}{\partial x}(x^2y^3) - \frac{\partial}{\partial y}(xy) = 2xy^3 - x$,

$$
\oint_{\mathcal{C}}\mathbf{F}\cdot d\mathbf{r}=\iint_D(2xy^3-x)\,dx\,dy=\int_0^1\int_0^{2x}(2xy^3-x)\,dy\,dx=\int_0^1(8x^5-2x^2)\,dx=\frac43-\frac23=\frac23.
$$
:::
