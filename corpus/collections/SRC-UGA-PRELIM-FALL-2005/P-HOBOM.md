---
schema: qual/card@1
id: P-HOBOM
kind: problem
title: Existence of nonabelian groups of order $5$ and $6$
classification:
  areas:
  - prelim
  topics:
  - Groups
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
For $n = 5, 6$, either give an example of a nonabelian group of order $n$, or prove that none exists.
:::

::: {.solution}

::: pf

::: pf-step

(n = 5) No nonabelian group of order $5$ exists.

::: pf-proof

Let $\cardinality{G}=5$ and choose $g\in G\setminus\{e\}$. By Lagrange's theorem $\cardinality{\langle g\rangle}$ divides $5$, and it exceeds $1$ because $g\neq e$, so $\cardinality{\langle g\rangle}=5$.
Hence $G=\langle g\rangle\cong\ZZ/5\ZZ$ is cyclic, and so abelian.

:::

:::

::: pf-step

(n = 6) The symmetric group $S_3$ is a nonabelian group of order $6$.

::: pf-proof

$\cardinality{S_3}=3!=6$. Composing right to left, $\sigma=(1\ 2)$ and $\tau=(2\ 3)$ give $\sigma\tau=(1\ 2\ 3)$, since $1\mapsto1\mapsto2$, $2\mapsto3\mapsto3$, $3\mapsto2\mapsto1$, and $\tau\sigma=(1\ 3\ 2)$, since $1\mapsto2\mapsto3$, $2\mapsto1\mapsto1$, $3\mapsto3\mapsto2$.
These differ, as they send $1$ to different elements, so $S_3$ is nonabelian.

:::

:::

:::

:::
