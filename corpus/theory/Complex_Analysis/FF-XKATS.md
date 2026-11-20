---
schema: qual/card@1
id: FF-XKATS
kind: fact
title: Taylor series of $\sinh z$
slogan: '$\sinh z$ keeps exactly the odd terms of the exponential series.'
prompts:
- What is the series expansion of $\sinh(z)$?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Functions
  - Power Series
relations: []
review: draft
---

::: {.fact}
For every $z\in\CC$,
$$
\sinh z=z+\frac{z^{3}}{3 !}+\frac{z^{5}}{5 !}+\frac{z^{7}}{7 !}+\cdots=\sum_{n=0}^{\infty} \frac{z^{2 n+1}}{(2 n+1) !}.
$$

This is the odd part of the exponential series of [@Ahl73, ch. 5, §1.2, The Taylor Series], where $e^z=\sum z^n/n!$ is listed, together with the definition $\sinh z=(e^z-e^{-z})/2$ of [@Ahl73, ch. 2, §3.2, The Trigonometric Functions]: subtracting the series for $-z$ cancels the even terms and leaves the display.
:::
