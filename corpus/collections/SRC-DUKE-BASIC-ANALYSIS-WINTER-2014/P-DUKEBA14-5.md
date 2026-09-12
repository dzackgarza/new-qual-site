---
schema: qual/card@1
id: P-DUKEBA14-5
kind: problem
title: A bounded oscillatory sequence has a convergent subsequence
classification:
  areas: [real-analysis]
  topics: [Sequences, Bolzano-Weierstrass Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part I, Problem 5 of the preserved Duke Winter 2014 Basic Analysis qualifying exam extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let
\[
x_n=
\frac{\bigl(n^2+2\sin^2 n+34\bigr)\sin(n^3)}{n^2+n+5}.
\]
Prove that $(x_n)_{n\ge1}$ has a convergent subsequence.
:::

::: solution
<1>1. Prove that the sequence is bounded.
::: proof
Since $|\sin(n^3)|\le1$ and $0\le2\sin^2n\le2$,
\[
|x_n|
\le \frac{n^2+36}{n^2+n+5}.
\]
For $n\ge1$ this is bounded, for example by $37$. Hence $(x_n)$ is a bounded sequence of real numbers.
:::

<1>2. Apply Bolzano--Weierstrass.
::: proof
Every bounded sequence in $\mathbb R$ has a convergent subsequence. Therefore $(x_n)$ has a convergent subsequence.
:::
:::
