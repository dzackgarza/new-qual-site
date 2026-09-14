---
schema: qual/card@1
id: P-CHAVAN-CA-2-4
kind: problem
title: A Cauchy-Schwarz bound on the zeros of a monic polynomial
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let
\[
p(z)=a_0+a_1z+\cdots+a_{n-1}z^{n-1}+z^n,
\qquad
R=\sqrt{|a_0|^2+\cdots+|a_{n-1}|^2+1}.
\]

1. If $R=1$, show that the zero set of $p$ is $\{0\}$.
2. If $R>1$ and $|z|=R$, show, using Cauchy-Schwarz, that
   \[
   |z^n-p(z)|<|z^n|.
   \]

Conclude that every zero of $p$ lies in the open disk $|z|<R$.
:::
