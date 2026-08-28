---
schema: qual/card@1
id: FT-OGS76
kind: theorem
title: Egorov's Theorem
prompts:
- State Egorov's theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Egorov
  - Convergence of Functions
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
If $E\subset \RR^n$ is measurable, $m(E) > 0$, and $\theset{f_n}$ measurable with $f_k \to f$ with $f(x) < \infty$ existing and finite a.e., then $f_n\to f$ *almost uniformly*, i.e. for all $\varepsilon > 0$ there exists a closed $F\subset E$ such that $m(E\setminus F)<\varepsilon$ and $f\converges{u}\to f$ on $F$.
:::
