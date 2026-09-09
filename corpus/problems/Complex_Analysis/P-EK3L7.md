---
schema: qual/card@1
id: P-EK3L7
kind: problem
title: $\frac1z\sum_{k=1}^\infty z^k/k$ converges on $S^1\setminus\{1\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Series of Functions
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
Show that $\frac{1}{z}\sum_{k=1}^\infty \frac{z^k}{k}$ converges for all $z \in S^1 \setminus \{1\}$ using summation by parts (Dirichlet's test).
:::

::: solution
Fix $z\in S^1\setminus\{1\}$ and set
$$
A_n=\sum_{k=1}^n z^k
=z\frac{1-z^n}{1-z}.
$$
Since $|z|=1$,
$$
|A_n|\le\frac2{|1-z|}
$$
for every $n$.

Summation by parts gives
$$
\sum_{k=1}^N\frac{z^k}{k}
=\frac{A_N}{N}
+\sum_{k=1}^{N-1}A_k\left(\frac1k-\frac1{k+1}\right).
$$
The first term tends to $0$, while
$$
\sum_{k=1}^\infty
\left|A_k\left(\frac1k-\frac1{k+1}\right)\right|
\le \frac2{|1-z|}\sum_{k=1}^\infty\frac1{k(k+1)}<\infty.
$$
Hence $\sum_{k=1}^\infty z^k/k$ converges. Since $z\ne0$ on $S^1$, multiplication by $1/z$ preserves convergence.
:::
