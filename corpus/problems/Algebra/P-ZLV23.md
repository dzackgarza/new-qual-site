---
schema: qual/card@1
id: P-ZLV23
kind: problem
title: No simple group of order $160$, and the structure of groups of that order
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Prove that there is no simple group of order 160. What can you say about the structure of groups of that order?
:::

::: {.solution}
Let $|G|=160=2^5\cdot5$, and let $P$ be a Sylow $2$-subgroup. Then
\[
[G:P]=5.
\]
The action of $G$ on the five left cosets of $P$ gives
\[
\rho:G\to S_5.
\]
If $G$ were simple, the kernel of this nontrivial action would be trivial, so $G$ would embed in $S_5$. But
\[
|G|=160>120=|S_5|,
\]
which is impossible. Hence no group of order $160$ is simple.

More generally, every group of order $160$ is solvable by Burnside's $p^aq^b$ theorem. Sylow gives
\[
n_5\in\{1,16\}.
\]
If $n_5=1$, the unique Sylow $5$-subgroup $C_5$ is normal. For any Sylow $2$-subgroup $P$, we then have
\[
G=C_5P,
\qquad C_5\cap P=1,
\]
so
\[
G\cong C_5\rtimes P,
\]
with $|P|=32$ and the action factoring through
\[
\operatorname{Aut}(C_5)\cong C_4.
\]
Thus the strongest uniform structural conclusion is solvability; in the normal-Sylow-$5$ case one obtains the displayed semidirect product.
:::
