---
schema: qual/card@1
id: FF-YJXMF
kind: fact
title: The uniform boundedness principle
prompts:
- What is the uniform boundedness principle?
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Norms
relations: []
review: draft
---

::: {.fact}
Let $X$ be a [[D-BG455|Banach space]], let $Y$ be a normed vector space, and let $\mcf$ be a family of bounded linear operators $X\to Y$.
If
$$
\sup_{T \in \mcf} \norm{Tx}_Y < \infty \quad\text{for every } x\in X,
$$
then $\sup_{T\in \mcf} \norm{T} < \infty$, where $\norm{T}\coloneqq\sup_{\norm{x}_X\leq 1}\norm{Tx}_Y$ is the operator norm.
:::
