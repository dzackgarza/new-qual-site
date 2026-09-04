---
schema: qual/card@1
id: E-NIPUY
kind: problem
title: The false uniform-continuity claim for $x^{-n}$ near $0$
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
A source claims that
\[
f(x)=x^{-n},\qquad n\in\ZZ_{\geq0},
\]
is uniformly continuous on $[0,\infty)$.
Determine for which $n$ this is correct, and explain the defect when it is false.
:::

::: {.solution}
For $n=0$, $f\equiv1$, so $f$ is uniformly continuous on $[0,\infty)$.

For every $n\ge1$, the claim is already ill-posed at $0$, since $x^{-n}$ is not defined there.
Even on its natural domain $(0,\infty)$, the function is not uniformly continuous.
Take
\[
x_k={1\over k},
\qquad
y_k={1\over k+1}.
\]
Then
\[
|x_k-y_k|={1\over k(k+1)}\to0,
\]
but
\[
|f(x_k)-f(y_k)|
=|k^n-(k+1)^n|
\ge1
\]
for every $k$.
Hence no uniform-continuity modulus can exist.

The old solution instead proved an estimate for $x^{1/n}$, which is a different function.
:::
