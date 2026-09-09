---
schema: qual/card@1
id: E-AMD-I4NOLHWA
kind: problem
title: Groups of order 10
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - Sylow Theory
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
Classify all groups of order 10.
:::

::: {.solution}
Let $|G|=10=2\cdot5$. Sylow gives
\[
n_5\mid2,\qquad n_5\equiv1\pmod5,
\]
so $n_5=1$. Thus the Sylow $5$-subgroup $P\cong C_5$ is normal.

If $Q\cong C_2$ is a Sylow $2$-subgroup, then $P\cap Q=1$ and $PQ=G$, so
\[
G\cong C_5\rtimes C_2.
\]
The action is a homomorphism
\[
C_2\to\Aut(C_5)\cong C_4.
\]
There are exactly two possibilities: the trivial action and the unique nontrivial action of order $2$, namely inversion.

The trivial action gives
\[
C_5\times C_2\cong C_{10}.
\]
The inversion action gives
\[
\langle r,s\mid r^5=s^2=1,\ srs=r^{-1}\rangle\cong D_5.
\]
Hence the groups of order $10$ are exactly
\[
\boxed{C_{10}\quad\text{and}\quad D_5}.
\]
:::
