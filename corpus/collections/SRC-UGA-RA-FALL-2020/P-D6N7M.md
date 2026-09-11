---
schema: qual/card@1
id: P-D6N7M
kind: problem
title: $nx_n\to 0$ for a decreasing positive summable sequence
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Sequences of Numbers
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 1 of the official UGA Fall 2020 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: "Reviewed and repaired the legacy proof: the original slice inequality had a sign/index error; the half-tail argument gives the result directly."
---

:::{.problem}
Show that if $x_n$ is a decreasing sequence of positive real numbers such that $\sum_{n=1}^\infty x_n$ converges, then
$$
\lim_{n\to\infty} n x_n = 0.
$$

:::

::: solution

Since $\sum_{n=1}^\infty x_n$ converges, its tails tend to zero. For $n\ge2$, put $m=\lfloor n/2\rfloor$. Because $(x_n)$ is decreasing and positive,
\[
\sum_{k=m+1}^{n}x_k\ge (n-m)x_n.
\]
Also $n-m\ge n/2$, so
\[
0\le nx_n\le 2\sum_{k=m+1}^{n}x_k
\le 2\sum_{k=m+1}^{\infty}x_k.
\]
As $n\to\infty$, also $m\to\infty$, and the last tail tends to $0$. Hence
\[
\boxed{\lim_{n\to\infty}nx_n=0.}
\]
:::
