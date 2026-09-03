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
\envlist

- For $a\in \RR_{< 0}$: take $z_k\da {1\over \Log(a) + 2\pi i k - {\pi i \over 2}}$\
  Then $f(z_k) = a$ for all $k$ but $z_k\to 0$.

- For $a=0$: take $z_k = -1/k$.

- For $a=\infty$, take $z_k = 1/k$.

- For anything else, take $z_k \da {1\over \Log(a) + 2\pi i n}$ if $a \in \RR_{\geq 0}$.
  Again $f(z_k) = a$ for all $k$ but $z_k\to 0$.
:::
