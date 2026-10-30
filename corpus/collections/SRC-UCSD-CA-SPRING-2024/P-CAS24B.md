---
schema: qual/card@1
id: P-CAS24B
kind: problem
title: Sublevel set of a nowhere-zero entire function has unbounded components
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Let $f : \CC \to \CC$ be an entire nowhere zero function.
Define $U = \{z : \abs{f(z)} < 1\}$.
If $U \neq \emptyset$, show that the connected components of $U$ are unbounded.
:::

::: {.solution}
Suppose that a component $V$ of
$$
U=\{\abs{f}<1\}
$$
were bounded. Since $f$ is nowhere zero, $1/f$ is entire. Every boundary point
of $V$ satisfies $\abs{f}=1$: if $\abs{f}<1$ at a boundary point, that point would lie
in the same open component of $U$, while $\abs{f}>1$ is excluded by continuity
from points of $V$.

Thus
$$
\abs{\frac1f}=1
\qquad\text{on }\partial V,
$$
while $\abs{1/f}>1$ throughout $V$. Because $V$ is bounded, the maximum modulus
principle applied to $1/f$ on $V$ gives
$$
\abs{\frac1{f(z)}}\le1
\qquad(z\in V),
$$
a contradiction. Hence every component of $U$ is unbounded.
:::
