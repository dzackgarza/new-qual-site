---
schema: qual/card@1
id: P-VACDU
kind: problem
title: Infinite unions of compact sets and attainment of distance to a compact set
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 7 (June 2003, #1b,c) in the preserved Day 2 Metric Spaces and Topology source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(b) Show by example that the union of infinitely many compact subsets of a metric space need not be compact.

(c) If $(X,d)$ is a metric space and $K\subset X$ is compact, define $d(x_0,K)=\inf_{y\in K} d(x_0,y)$. Prove that there exists a point $y_0\in K$ such that $d(x_0,K)=d(x_0,y_0)$.
:::

::: {.solution}

::: pf

::: pf-step

(b) In $\RR$, the compact sets $K_n = \theset{n}$, $n \in \NN$, have the noncompact union $\NN$.

::: pf-proof

Each $K_n$ is finite, hence compact. The open cover $\theset{(n - 1/2, n + 1/2) : n \in \NN}$ of $\NN$ has no finite subcover, since each interval contains exactly one point of $\NN$.

:::

:::

::: pf-step

(c) There is $y_0\in K$ with $d(x_0,K)=d(x_0,y_0)$.

::: pf-proof

::: {.pf-step #lipschitz}

The function $x \mapsto d(x_0, x)$ is continuous.

::: pf-proof

By the triangle inequality, $\abs{d(x_0,x) - d(x_0,y)} \le d(x,y)$, so the map is $1$-Lipschitz.

:::

:::

::: pf-qed

The definition of $d(x_0,K)$ requires $K \neq \varnothing$. A continuous function on a nonempty compact set attains its infimum, so by step [](#lipschitz){.pf-ref} there is $y_0 \in K$ with $d(x_0, y_0) = \inf_{y \in K} d(x_0, y) = d(x_0, K)$.

:::

:::

:::

:::

:::
