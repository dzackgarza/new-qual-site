---
schema: qual/card@1
id: E-LZTNT
kind: problem
title: Essential singularities
classification:
  areas:
  - complex-analysis
  topics:
  - Essential Singularities
  - Casorati-Weierstrass
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Fix $a\in \CC\union\ts{\infty}$ and let $f(z) \da e^{1\over z^2}$.
Find a sequence $z_k\to 0$ such that $f(z_k) \convergesto{k\to\infty} a$
:::

::: {.solution}
- If $a\in\CC^\times$, choose any logarithm $L\in\CC$ with $e^L=a$ and set
  \[
  z_k=\qty{L+2\pi i k}^{-1/2},
  \]
  choosing either square root for each $k$.
  Then $z_k\to0$ and
  \[
  {1\over z_k^2}=L+2\pi i k,
  \qquad
  f(z_k)=e^{L+2\pi i k}=a.
  \]

- For $a=0$, take $z_k=i/\sqrt{k}$.
  Then $z_k\to0$ and
  \[
  f(z_k)=e^{-k}\to0.
  \]

- For $a=\infty$, take $z_k=1/\sqrt{k}$.
  Then $z_k\to0$ and
  \[
  f(z_k)=e^k\to\infty
  \]
  in $\CP^1$.
:::
