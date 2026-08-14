---
schema: qual/card@1
id: P-2HIC2
kind: problem
title: "Let $f, g \\in L^1([0, 1])$ and for all $x\\in [0, 1]$ define $F(x) \\definedas \\int _{0}^{x} f(y) \\, dy \\qtext{and} G(x)\\definedas \\int _{0}^{x} g(y) \\, dy$"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - fubini-tonelli
relations: []
review: draft
---

::: {.problem title="?"}
Let $f, g \in L^1([0, 1])$ and for all $x\in [0, 1]$ define
\[
F(x) \definedas \int _{0}^{x} f(y) \, dy 
\qtext{and}
G(x)\definedas \int _{0}^{x} g(y) \, dy.
\]

Prove that
\[
\int _{0}^{1} F(x) g(x) \, dx = 
F(1) G(1) - \int _{0}^{1} f(x) G(x) \, dx
\]
:::
