---
schema: qual/card@1
id: PR-KTZZ5
kind: proposition
title: Convergence implies convergence of inner products
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

:::{.proposition}
If $x_k\to x$ and $y_k\to y$ in $H$, then $\inner{x_k}{y_k} \to \inner{x}{y}$.
:::

::: {.proof}
Add and subtract the cross term $\inner{x}{y_k}$:
\[
\abs{\inner{x_k}{y_k} - \inner{x}{y} }
= \abs{\inner{x_k - x}{y_k} + \inner{x}{y_k - y} }
\leq \norm{x_k - x}\norm{y_k} + \norm{x}\norm{y_k - y}
\]
by the triangle inequality and Cauchy–Schwarz.
Since $y_k \to y$, the sequence $\norm{y_k}$ is bounded, and $\norm{x_k - x} \to 0$; hence the first term tends to $0$.
Since $y_k - y \to 0$, the second term tends to $0$ as well.
Therefore $\abs{\inner{x_k}{y_k} - \inner{x}{y}} \to 0$, so $\inner{x_k}{y_k} \to \inner{x}{y}$.
:::
