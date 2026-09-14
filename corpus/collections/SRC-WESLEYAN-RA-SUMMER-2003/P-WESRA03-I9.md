---
schema: qual/card@1
id: P-WESRA03-I9
kind: problem
title: Uniform convergence on the real line need not imply convergence of integrals
classification:
  areas: [real-analysis]
  topics: [Integration, Uniform Convergence]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Suppose $f_n:\mathbb R\to\mathbb R$ are integrable and $f_n\to0$ uniformly on $\mathbb R$.
Must
\[
\int_{\mathbb R}f_n\,dm\longrightarrow0?
\]
:::

::: solution
No. Let
\[
f_n(x)=\frac1n\mathbf1_{[0,n]}(x).
\]
Then $f_n\in L^1(\mathbb R)$ and
\[
\|f_n\|_\infty=\frac1n\longrightarrow0,
\]
so $f_n\to0$ uniformly.
However,
\[
\int_{\mathbb R}f_n\,dm
=\frac1n\,m([0,n])=1
\]
for every $n$.
Hence uniform convergence on an infinite-measure domain does not by itself permit passage of the limit through the integral.
:::
