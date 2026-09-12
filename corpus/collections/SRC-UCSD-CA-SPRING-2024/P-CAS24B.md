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

::: problem
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire nowhere zero function.
Define $U = \{z : |f(z)| < 1\}$.
If $U \neq \emptyset$, show that the connected components of $U$ are unbounded.
:::

::: solution
Suppose that a component $V$ of
\[
U=\{|f|<1\}
\]
were bounded. Since $f$ is nowhere zero, $1/f$ is entire. Every boundary point
of $V$ satisfies $|f|=1$: if $|f|<1$ at a boundary point, that point would lie
in the same open component of $U$, while $|f|>1$ is excluded by continuity
from points of $V$.

Thus
\[
\left|\frac1f\right|=1
\qquad\text{on }\partial V,
\]
while $|1/f|>1$ throughout $V$. Because $V$ is bounded, the maximum modulus
principle applied to $1/f$ on $V$ gives
\[
\left|\frac1{f(z)}\right|\le1
\qquad(z\in V),
\]
a contradiction. Hence every component of $U$ is unbounded.
:::
