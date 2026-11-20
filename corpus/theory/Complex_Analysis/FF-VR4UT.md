---
schema: qual/card@1
id: FF-VR4UT
kind: fact
title: $\sinh(x+iy)$ in terms of real and imaginary parts
slogan: '$\sinh(x+iy)$ splits as $\sinh x\cos y+i\cosh x\sin y$.'
prompts:
- What is the angle addition formula for $\sinh(x+iy)$?
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
\sinh (x+i y) =\sinh (x) \cos (y)+i \cosh (x) \sin (y).
$$

The separation is Exercise 3 of [@Ahl73, ch. 2, §3.2, The Trigonometric Functions], which asks the reader to use the addition formulas to separate $\cos(x+iy)$ and $\sin(x+iy)$ into real and imaginary parts; the display above is its hyperbolic form, obtained from $\sinh w=\frac1i\sin(iw)$ and $\cosh w=\cos(iw)$ as those are defined in the same section.
:::
