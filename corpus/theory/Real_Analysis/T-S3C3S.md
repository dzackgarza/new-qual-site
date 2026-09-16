---
schema: qual/card@1
id: T-S3C3S
kind: theorem
title: Convergence of interval averages $A_h f\to f$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Differentiation
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $f\colon\RR\to\CC$ be Lebesgue [[D-R5DL3|integrable]], and for $h>0$ define $A_h f\colon\RR\to\CC$ by
$$
A_h f(x)\coloneqq\frac{1}{2h}\int_{x-h}^{x+h}f(y)\,dy.
$$
Then:

(a) $\norm{A_h f-f}_{L^1(\RR)}\to0$ as $h\to0^+$;

(b) $A_h f(x)\to f(x)$ as $h\to0^+$ for almost every $x\in\RR$.
:::
