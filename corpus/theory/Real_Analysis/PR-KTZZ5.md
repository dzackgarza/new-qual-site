---
schema: qual/card@1
id: PR-KTZZ5
kind: proposition
title: Inner products are jointly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Inner Product Spaces
  - Convergence of Functions
relations: []
review: draft
---

::: {.proposition}
Let $H$ be an inner product space with inner product $\inner{\cdot}{\cdot}$ and norm $\norm{x}\coloneqq\inner{x}{x}^{1/2}$.
If $x_k\to x$ and $y_k\to y$ in $H$, then $\inner{x_k}{y_k} \to \inner{x}{y}$.
:::

::: {.proof}
Add and subtract $\inner{x}{y_k}$:
$$
\abs{\inner{x_k}{y_k} - \inner{x}{y} }
= \abs{\inner{x_k - x}{y_k} + \inner{x}{y_k - y} }
\leq \norm{x_k - x}\norm{y_k} + \norm{x}\norm{y_k - y}
$$
by the triangle inequality and the Cauchy--Schwarz inequality.
Since $y_k \to y$, the sequence $(\norm{y_k})$ is bounded, and $\norm{x_k - x} \to 0$, so the first term tends to $0$.
Since $\norm{y_k - y}\to 0$, the second term tends to $0$.
:::
