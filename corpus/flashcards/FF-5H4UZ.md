---
schema: qual/card@1
id: FF-5H4UZ
kind: fact
title: Prove the Schwarz lemma.
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.fact title="Prove the Schwarz lemma."}
- In parts:

- $ f(z) = \sum_{k\geq 1}c_k z^k $ since $ f(0) = 0 $ implies $ c_0 = 0 $.

- $ g(z) \coloneqq f(z)/z = \sum_{k\geq 1}c_k z^{k-1} $ and $ g(0) = c_1 = f'(0) $.

- $ {\left\lvert {f} \right\rvert}\leq 1\implies {\left\lvert {g} \right\rvert} \leq r^{-1} $ on $ {\left\lvert {z} \right\rvert} = r $, thus on $ {\left\lvert {z} \right\rvert} \leq r $ by MMP.

- Take the limit $ r\to 1 $.

- Part 2: extremum in interior implies $ g(z) \equiv c $ is constant.

- $ {\left\lvert {f'(0)} \right\rvert} = 1 $ or $ f(z) = z $ for some $ z\neq 0 $ implies $ {\left\lvert {c} \right\rvert} = 1 $.

- The actual source:
:::
