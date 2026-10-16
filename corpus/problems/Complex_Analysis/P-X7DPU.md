---
schema: qual/card@1
id: P-X7DPU
kind: problem
title: Partial sums $P_n(z)=\sum_{k=0}^n z^k/k!$ are eventually zero-free on $\abs{z}\le R$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Polynomials
relations: []
review: draft
---

::: {.problem}
For $R>0$, show that there is $N_R$ such that for $n>N_R$,
\[
P_n(z)=1+z+\frac{z^2}{2!}+\cdots+\frac{z^n}{n!}\ne0
\qquad(|z|\le R).
\]
:::

::: {.solution}
The polynomials $P_n$ converge uniformly to $e^z$ on every closed disk. On $|z|\le R$,
\[
|e^z|=e^{\Re z}\ge e^{-R}.
\]
Choose $N_R$ so that
\[
\sup_{|z|\le R}|P_n(z)-e^z|<e^{-R}/2
\qquad(n>N_R).
\]
Then $|P_n(z)|\ge e^{-R}/2>0$ on the disk.
:::