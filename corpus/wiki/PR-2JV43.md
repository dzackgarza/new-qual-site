---
schema: qual/card@1
id: PR-2JV43
kind: proposition
title: "a.e. convergence never implies $L^p$ convergence"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.proposition title="a.e. convergence never implies $L^p$ convergence"}
Sequences $f_k \converges{a.e.}\to f$ but $f_k \converges{L^p}{\not\to} f$:

- For $1\leq p < \infty$: The skateboard to infinity, $f_k = \chi_{[k, k+1]}$.

  Then $f_k \converges{a.e.}\to 0$ but $\norm{f_k}_p = 1$ for all $k$.

  > Converges pointwise and a.e., but not uniformly and not in norm.

- For $p = \infty$: The sliding boxes $f_k = k \cdot \chi_{[0, \frac 1 k]}$.

  Then similarly $f_k \converges{a.e.}\to 0$, but $\norm{f_k}_p = 1$ and $\norm{f_k}_\infty = k \to \infty$

  > Converges a.e., but not uniformly, not pointwise, and not in norm.
:::
