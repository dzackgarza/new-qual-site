---
schema: qual/card@1
id: FF-YJXMF
kind: fact
title: 'What is the uniform boundedness principle?'
classification:
  areas:
  - real-analysis
  topics:
  - functional-analysis
  - norms
relations: []
review: draft
---

::: {.fact title="What is the uniform boundedness principle?"}
If $ \mathcal{F} $ is a family of bounded operators $ T_n:X\to Y $ between Banach spaces with

$$\forall x\in X, \qquad \sup_{T_n \in \mathcal{F}} {\left\lVert {T_n(x)} \right\rVert}_Y < \infty$$

then $ \sup_{T_n\in \mathcal{F}} {\left\lVert {T_n} \right\rVert}_X < \infty $.

Slogan: pointwise bounded sequences of operators are uniformly bounded.
:::
