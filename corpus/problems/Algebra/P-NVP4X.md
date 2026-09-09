---
schema: qual/card@1
id: P-NVP4X
kind: problem
title: Groups of order 55
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Discuss groups of order 55.
:::

::: {.solution}
Let $|G|=55=5\cdot11$. Sylow gives
\[
n_{11}\equiv1\pmod{11},\qquad n_{11}\mid5,
\]
so $n_{11}=1$. Hence the Sylow $11$-subgroup $P\cong C_{11}$ is normal. If $Q\cong C_5$ is a Sylow $5$-subgroup, then $P\cap Q=1$ and $PQ=G$, so
\[
G\cong C_{11}\rtimes C_5.
\]
The action is a homomorphism
\[
C_5\longrightarrow\operatorname{Aut}(C_{11})\cong C_{10}.
\]
There are two possibilities up to isomorphism. The action is trivial, giving
\[
C_{11}\times C_5\cong C_{55},
\]
or it is injective onto the unique subgroup of order $5$ in $C_{10}$, giving one nonabelian semidirect product. Thus there are exactly two groups of order $55$ up to isomorphism.
:::
