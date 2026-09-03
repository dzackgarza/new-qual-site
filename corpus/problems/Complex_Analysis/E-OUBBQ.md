---
schema: qual/card@1
id: E-OUBBQ
kind: problem
title: Uniform continuity of $x^n$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
relations: []
review: draft
---

::: {.problem}
For $n\geq1$, show that $f(x)=x^n$ is uniformly continuous on any interval $[-M,M]$.
:::

::: {.solution}
If $M=0$, the claim is immediate.
Assume $M>0$.
For $x,y\in[-M,M]$,
\[
\abs{x^n-y^n}
&=\abs{x-y}\abs{\sum_{k=0}^{n-1}x^{n-1-k}y^k} \\
&\leq nM^{n-1}\abs{x-y}.
\]
Thus $f$ is Lipschitz on $[-M,M]$, hence uniformly continuous.
Explicitly, given $\varepsilon>0$, take $\delta=\varepsilon/(nM^{n-1})$.
:::
