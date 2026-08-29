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
Proof:
\[
\abs{\inner{x_k}{y_k} - \inner{x}{y} } =\abs{\inner{x_n - x}{y_n} + \inner{x}{y_n-y} } \leq \norm{x_n - x}\norm{y_n} + \norm{x} \norm{y_n - y}
.\]


:::
