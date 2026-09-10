---
schema: qual/card@1
id: E-AMD-ELQV5ZEQ
kind: problem
title: Groups of order 99
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Classify all groups of order 99 up to isomorphism.
:::

::: {.solution}
Let $|G|=99=3^2\cdot11$.

For a Sylow $11$-subgroup,
\[
n_{11}\mid9,\qquad n_{11}\equiv1\pmod{11},
\]
so $n_{11}=1$. Thus the Sylow $11$-subgroup $Q\cong C_{11}$ is normal.

For a Sylow $3$-subgroup,
\[
n_3\mid11,\qquad n_3\equiv1\pmod3.
\]
The only possibilities dividing $11$ are $1$ and $11$, and $11\equiv2\pmod3$, so $n_3=1$. Hence the Sylow $3$-subgroup $P$ of order $9$ is also normal.

Since $P\cap Q=1$ and $|P||Q|=99$, we have
\[
G=P\times Q.
\]
Every group of order $9$ is abelian and is isomorphic either to $C_9$ or to $C_3\times C_3$. Therefore the two possibilities are
\[
C_9\times C_{11}\cong C_{99}
\]
and
\[
(C_3\times C_3)\times C_{11}\cong C_3\times C_{33}.
\]
Thus there are exactly two groups of order $99$ up to isomorphism:
\[
\boxed{C_{99}\quad\text{and}\quad C_3\times C_{33}.}
\]
:::
