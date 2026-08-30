---
schema: qual/card@1
id: P-RAF09B
kind: problem
title: "Dominated convergence implies convergence in measure"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Assume that $f_n$ is a sequence of measurable functions on $(X, \mathcal{M}, \mu)$.
Assume that there exists an integrable function $F$ such that $|f_n| \leq F$ $\mu$-a.e., and $f_n \to f$ $\mu$-a.e. Show that $f_n \to f$ in measure.
:::

::: {.solution}
<1>1. For $\epsilon>0$, $|\{|f_n-f|>\epsilon\}|\le \epsilon^{-p}\int|f_n-f|^p$ but use dominated: $|f_n-f|\le2F$.
Proof: Chebyshev.

<1>2. $f_n\to f$ a.e. and $|f_n-f|\le2F\in L^1$, so $\int|f_n-f|\wedge1\to0$ by DCT.
Proof: DCT.

<1>3. Hence $\mu(\{|f_n-f|>\epsilon\})\to0$.
Proof: <1>2.

<1>4. Q.E.D.
Proof: <1>3.
:::
