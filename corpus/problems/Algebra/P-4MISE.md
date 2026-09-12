---
schema: qual/card@1
id: P-4MISE
kind: problem
title: Groups of order 15
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Cyclic Groups
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

::: problem
Determine the number of groups of order $15$ up to isomorphism, and prove your result.
:::

::: solution
Let $|G|=15=3\cdot5$. By Sylow,
\[
n_5\mid3,\qquad n_5\equiv1\pmod5,
\]
so $n_5=1$. Likewise
\[
n_3\mid5,\qquad n_3\equiv1\pmod3,
\]
and since $5\not\equiv1\pmod3$, we get $n_3=1$.

Thus the Sylow subgroups $P$ of order $5$ and $Q$ of order $3$ are both normal. Their intersection is trivial, and
\[
|PQ|=\frac{|P||Q|}{|P\cap Q|}=15,
\]
so $G=PQ$. Since both factors are normal and intersect trivially, they commute and
\[
G\cong P\times Q\cong \mathbb Z/5\times\mathbb Z/3\cong\mathbb Z/15.
\]
Therefore there is exactly one group of order $15$ up to isomorphism.
:::
