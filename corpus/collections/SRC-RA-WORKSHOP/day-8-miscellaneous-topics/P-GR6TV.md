---
schema: qual/card@1
id: P-GR6TV
kind: problem
title: A closed bounded noncompact subset of a metric space
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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Find an example of a metric space $X$ and a subset $E \subseteq X$ such that $E$ is closed and bounded but not compact.
:::

::: {.solution}

Let $X = (0, 1)$ with the metric $d(x,y) = \abs{x - y}$ restricted from $\RR$, and let $E = X$.

::: pf

::: pf-step

$E$ is closed in $X$.

::: pf-proof

The complement $X\setminus E=\varnothing$ is open in $X$, hence $E$ is closed in $X$.

:::

:::

::: pf-step

$E$ is bounded.

::: pf-proof

For every $x\in E$, $d(x,1/2)=\abs{x-1/2}<1/2$. Thus $E\subseteq B_X(1/2,1/2)$.

:::

:::

::: pf-step

$E$ is not compact, so $\boxed{X=E=(0,1)}$ with the usual metric is an example.

::: pf-proof

Consider $x_k=1/(k+1)\in E$ for $k\geq1$. Every subsequence converges to zero in $\RR$. If any subsequence converged in $X$ to a point $x\in X$, it would also converge to $x$ in $\RR$, contradicting uniqueness of limits because $0\notin X$. Hence $E$ is not sequentially compact and therefore is not compact, since compact metric spaces are sequentially compact.

:::

:::

:::

:::

::: {.remark}
Closedness and boundedness imply compactness in Euclidean spaces by Heine–Borel, but not in arbitrary metric spaces, even complete ones: the closed unit ball of $\ell^2$ is another example.
:::
