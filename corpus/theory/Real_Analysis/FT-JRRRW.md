---
schema: qual/card@1
id: FT-JRRRW
kind: theorem
title: Uniform boundedness principle
prompts:
- State the uniform boundedness principle.
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Norms
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a [[D-BG455|Banach space]], let $Y$ be a normed vector space, and let $\mathcal{F}$ be a family of bounded linear operators $T\colon X\to Y$.
If
$$
\sup_{T \in \mathcal{F}} \norm{Tx}_Y < \infty \quad\text{for every } x\in X,
$$
then $\sup_{T\in \mathcal{F}} \norm{T} < \infty$, where $\norm{T}\coloneqq\sup_{\norm{x}_X\le1}\norm{Tx}_Y$ is the operator norm.
:::
