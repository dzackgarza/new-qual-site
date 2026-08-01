---
schema: qual/card@1
id: P-MMAQ-5WDF4PWP7U
kind: problem
title: Let $f, g \in L^1([0, 1])$ and for all $x\in [0, 1]$ define
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - fubini-tonelli
  - l1
relations: []
review: draft
---

::: problem
Let $f, g \in L^1([0, 1])$ and for all $x\in [0, 1]$ define
$$
F(x):=\int_{0}^{x} f(y) d y \quad \text { and } \quad G(x):=\int_{0}^{x} g(y) d y.
$$

Prove that
$$
\int_{0}^{1} F(x) g(x) d x=F(1) G(1)-\int_{0}^{1} f(x) G(x) d x
$$
:::
