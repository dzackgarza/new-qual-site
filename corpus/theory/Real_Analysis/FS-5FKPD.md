---
schema: qual/card@1
id: FS-5FKPD
kind: strategy
title: Showing uniform convergence of a series of functions
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

::: {.strategy}
Use the Weierstrass $M$-test.
Let $S$ be a set and $f_n\colon S\to\CC$ for $n\geq1$.
Find constants $M_n\geq0$, independent of $x$, such that $\sup_{x\in S}\abs{f_n(x)} \le M_n$ for every $n$ and $\sum_{n\geq1} M_n < \infty$.
Then $\sum_{n\geq1} f_n$ converges absolutely at every point of $S$, and its partial sums [[D-YZC3C|converge uniformly]] on $S$, since for $N>N'$ and all $x\in S$,
$$
\abs{\sum_{n=N'+1}^{N} f_n(x)} \le \sum_{n>N'} M_n \xrightarrow{N'\to\infty} 0.
$$
:::
