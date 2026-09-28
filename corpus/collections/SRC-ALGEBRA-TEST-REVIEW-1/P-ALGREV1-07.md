---
schema: qual/card@1
id: P-ALGREV1-07
kind: problem
title: Classify abelian groups of order 200
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, open-ended question 7."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Applied the finite abelian group classification to the 2-primary and 5-primary parts and obtained six pairwise nonisomorphic groups."
---

::: {.problem}
Find all abelian groups of order $200$, up to isomorphism.
:::

::: {.solution}
Since
$$
200=2^3\cdot5^2,
$$
the classification theorem for finite abelian groups separates the problem
into the $2$-primary and $5$-primary parts.

<1>1. Classify the abelian groups of order $2^3$.
::: {.proof}
The partitions of $3$ are
$$
3,\qquad 2+1,\qquad 1+1+1.
$$
Therefore the three possibilities are
$$
\mathbb Z_8,
\qquad
\mathbb Z_4\times\mathbb Z_2,
\qquad
\mathbb Z_2\times\mathbb Z_2\times\mathbb Z_2.
$$
:::

<1>2. Classify the abelian groups of order $5^2$.
::: {.proof}
The partitions of $2$ are
$$
2,\qquad1+1.
$$
Hence the two possibilities are
$$
\mathbb Z_{25},
\qquad
\mathbb Z_5\times\mathbb Z_5.
$$
:::

<1>3. Combine the independent primary components.
::: {.proof}
Every finite abelian group of order $200$ is uniquely the direct product of
one group from step <1>1 and one group from step <1>2. Thus there are exactly
$3\cdot2=6$ isomorphism types:
$$
\boxed{
\begin{aligned}
&\mathbb Z_8\times\mathbb Z_{25},\\
&\mathbb Z_8\times\mathbb Z_5\times\mathbb Z_5,\\
&\mathbb Z_4\times\mathbb Z_2\times\mathbb Z_{25},\\
&\mathbb Z_4\times\mathbb Z_2\times\mathbb Z_5\times\mathbb Z_5,\\
&\mathbb Z_2\times\mathbb Z_2\times\mathbb Z_2\times\mathbb Z_{25},\\
&\mathbb Z_2\times\mathbb Z_2\times\mathbb Z_2\times\mathbb Z_5\times\mathbb Z_5.
\end{aligned}}
$$
The primary decomposition theorem also shows that no two groups in this list
are isomorphic.
:::
:::
