---
schema: qual/card@1
id: PR-TNFL4
kind: proposition
title: Integration by parts for indefinite integrals of $L^1$ functions
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
---

::: {.proposition}
Let $f,g\in L^1([0,1])$ and put
$$
F(x)\coloneqq\int_{0}^{x} f(y) \,dy, \qquad G(x)\coloneqq\int_{0}^{x} g(y) \,dy \qquad (0\leq x\leq1).
$$
Then
$$
\int_{0}^{1} F(x) g(x) \,dx=F(1) G(1)-\int_{0}^{1} f(x) G(x) \,dx .
$$
:::
