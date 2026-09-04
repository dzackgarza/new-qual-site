---
schema: qual/card@1
id: E-ZQGR5
kind: problem
title: Radius of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
relations: []
review: draft
---

::: {.exercise}
Find the radius of convergence of

- $\sum a^k z^k$ for $a$ a constant.

- $\sum a^{k^2}z^k$
:::

::: {.solution}
By Cauchy--Hadamard, for $\sum c_kz^k$,
\[
{1\over R}=\limsup_{k\to\infty}|c_k|^{1/k}.
\]

For $c_k=a^k$,
\[
{1\over R}=|a|,
\]
so
\[
R=
\begin{cases}
\infty,&a=0,\\
|a|^{-1},&a\neq0.
\end{cases}
\]

For $c_k=a^{k^2}$,
\[
{1\over R}
=\limsup_{k\to\infty}|a|^k.
\]
Hence
\[
R=
\begin{cases}
\infty,&|a|<1,\\
1,&|a|=1,\\
0,&|a|>1.
\end{cases}
\]
:::
