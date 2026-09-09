---
schema: qual/card@1
id: P-DUKEBA14-6
kind: problem
title: A convergent positive series has square-summable terms
classification:
  areas: [real-analysis]
  topics: [Series]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part I, Problem 6 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(a_n)_{n\ge1}$ be a sequence of positive numbers such that
\[
\sum_{n=1}^\infty a_n
\]
converges. Prove that
\[
\sum_{n=1}^\infty a_n^2
\]
converges.
:::

::: solution
<1>1. Use the necessary condition for convergence of a series.
::: proof
Since $\sum a_n$ converges,
\[
a_n\longrightarrow0.
\]
Hence there exists $N$ such that
\[
0<a_n\le1
\qquad(n\ge N).
\]
:::

<1>2. Compare the tails.
::: proof
For $n\ge N$,
\[
a_n^2\le a_n.
\]
The comparison test therefore gives convergence of
\[
\sum_{n=N}^\infty a_n^2.
\]
Adding the finitely many terms with $n<N$ proves that $\sum_{n=1}^\infty a_n^2$ converges.
:::
:::
