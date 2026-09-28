---
schema: qual/card@1
id: E-C5QHZ
kind: problem
title: Uniformly bounded derivatives imply equicontinuity
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Normal Families
relations: []
review: draft
---

::: {.exercise}
Let $\mcf$ be a family of differentiable functions $f:[0,1]\to\CC$ such that
\[
|f'(x)|\le M
\]
for every $f\in\mcf$ and every $x\in[0,1]$, for one constant $M$ independent of $f$.
Show that $\mcf$ is equicontinuous.

> Hint: apply the MVT.
:::

::: {.solution}
For every $f\in\mcf$ and $x,y\in[0,1]$, the mean-value estimate gives
\[
|f(x)-f(y)|\le M|x-y|.
\]
Thus the whole family is uniformly Lipschitz with the same constant $M$.
Given $\varepsilon>0$, if $M>0$ take $\delta=\varepsilon/M$; if $M=0$ any
$\delta>0$ works. Then $|x-y|<\delta$ implies
\[
|f(x)-f(y)|<\varepsilon
\]
for every $f\in\mcf$. Hence $\mcf$ is equicontinuous.
:::
