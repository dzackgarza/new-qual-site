---
schema: qual/card@1
id: E-ISFYB
kind: problem
title: Uniformly bounded derivatives implies equicontinuous
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Mean Value Theorem
  - Sequences of Functions
relations: []
review: draft
---

::: {.exercise}
Let $f_k:[0,1]\to\CC$ be differentiable and suppose
\[
|f_k'(x)|\le M
\]
for every $k$ and every $x\in[0,1]$, where $M$ is independent of $k$.
Show that $\ts{f_k}$ is equicontinuous.

> Hint: MVT.
:::

::: solution
For all $x,y\in[0,1]$ and all $k$, the mean-value estimate gives
\[
|f_k(x)-f_k(y)|\le M|x-y|.
\]
Hence the sequence is uniformly Lipschitz. Given $\varepsilon>0$, take
$\delta=\varepsilon/M$ when $M>0$ (and arbitrary $\delta>0$ when $M=0$).
Then $|x-y|<\delta$ implies
\[
|f_k(x)-f_k(y)|<\varepsilon
\]
for every $k$, so $\ts{f_k}$ is equicontinuous.
:::
