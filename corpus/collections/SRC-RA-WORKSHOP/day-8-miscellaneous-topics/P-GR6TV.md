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

::: pf

::: pf-step

Example: $X = (0, 1)$ with the usual metric $d(x,y) = |x - y|$, and $E = (0, 1) = X$ itself.

::: pf-proof

The restriction of the Euclidean distance to $X\times X$ is a metric, and $E=X$ is a subset of this metric space.

:::

:::

::: {.pf-step #s2}

$E$ is closed in $X$.

::: pf-proof

The complement $X\setminus E=\varnothing$ is open in $X$, hence $E$ is closed in $X$.

:::

:::

::: {.pf-step #s3}

$E$ is bounded.

::: pf-proof

For every $x\in E$, $d(x,1/2)=|x-1/2|<1/2$. Thus $E\subseteq B_X(1/2,1/2)$.

:::

:::

::: {.pf-step #s4}

$E$ is not compact.

::: pf-proof

Consider $x_k=1/(k+1)\in E$ for $k\geq1$. Every subsequence converges to zero in $\mathbb R$. If any subsequence converged in $X$ to a point $x\in X$, it would also converge to $x$ in $\mathbb R$, contradicting uniqueness of limits because $0\notin X$. Hence $E$ is not sequentially compact and therefore is not compact, since compact metric spaces are sequentially compact.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} show that $E$ is closed and bounded in $X$ but not compact. Closedness and boundedness imply compactness in Euclidean spaces by Heine–Borel, but not in arbitrary metric spaces, even complete ones.

:::

:::

:::
