---
schema: qual/card@1
id: E-SS4.EX-1
kind: exercise
title: "Suppose f is continuous and of moderate decrease, and  for all  Sh"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
solved: false
---

::: exercise
1. Suppose f is continuous and of moderate decrease, and ${ \hat { f } } ( \xi ) = 0$ for all $\xi \in \mathbb { R }$ Show that $f = 0$ by completing the following outline:

(a) For each fixed real number t consider the two functions

$$

A (z) = \int_ {- \infty} ^ {t} f (x) e ^ {- 2 \pi i z (x - t)} d x \quad \text { and } \quad B (z) = - \int_ {t} ^ {\infty} f (x) e ^ {- 2 \pi i z (x - t)} d x.

$$

Show that $A ( \xi ) = B ( \xi )$ for all $\xi \in \mathbb { R } .$

(b) Prove that the function F equal to A in the closed upper half-plane, and B in the lower half-plane, is entire and bounded, thus constant. In fact, show that $F = 0$

(c) Deduce that

$$

\int_ {- \infty} ^ {t} f (x) d x = 0,

$$

for all t, and conclude that $f = 0$
:::
