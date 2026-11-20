---
schema: qual/card@1
id: FF-VFWB6
kind: fact
title: $\cosh(x+iy)$ in terms of real and imaginary parts
slogan: '$\cosh(x+iy)$ splits as $\cosh x\cos y+i\sinh x\sin y$.'
prompts:
- What is the angle addition formula for $\cosh(x+iy)$?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Functions
  - Trigonometry
relations: []
review: draft
---

::: {.fact}
For $x,y\in\RR$,
$$
\cosh (x+i y) =\cosh (x) \cos (y)+i \sinh (x) \sin (y).
$$

The separation is Exercise 3 of [@Ahl73, ch. 2, §3.2, The Trigonometric Functions], which asks the reader to use the addition formulas to separate $\cos(x+iy)$ and $\sin(x+iy)$ into real and imaginary parts; the display above is its hyperbolic form, obtained from $\cosh w=\cos(iw)$ and $\sinh w=\frac1i\sin(iw)$ as those are defined in the same section.
:::
