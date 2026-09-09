---
schema: qual/card@1
id: E-FJZCL
kind: problem
title: Convergence of $\frac1z\sum_{k=1}^\infty\frac{z^k}{k}$ on $S^1\setminus\{1\}$
  by summation by parts
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

::: {.exercise}
Show that $\frac{1}{z}\sum_{k=1}^\infty \frac{z^k}{k}$ converges for all $z \in S^1 \setminus \{1\}$ using summation by parts.
:::

::: solution
Fix $z\in S^1\setminus\{1\}$ and set
\[
A_N=\sum_{k=1}^N z^k.
\]
Since
\[
A_N=z\frac{1-z^N}{1-z},
\]
we have the uniform-in-$N$ bound
\[
|A_N|\le \frac{2}{|1-z|}.
\]

Summation by parts gives
\[
\sum_{k=1}^N\frac{z^k}{k}
=rac{A_N}{N}
+\sum_{k=1}^{N-1}A_k\left(\frac1k-\frac1{k+1}\right).
\]
The first term tends to $0$, while
\[
\sum_{k=1}^\infty
|A_k|\left(\frac1k-\frac1{k+1}\right)
\le \frac{2}{|1-z|}
\sum_{k=1}^\infty\frac1{k(k+1)}<\infty.
\]
Thus \(\sum z^k/k\) converges. Since $z\ne0$, multiplication by $1/z$ preserves convergence.
:::
