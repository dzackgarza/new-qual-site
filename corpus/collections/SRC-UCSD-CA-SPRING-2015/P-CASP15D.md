---
schema: qual/card@1
id: P-CASP15D
kind: problem
title: "Evaluate the integral of log(x)/(x^2 - 1) from 0 to infinity"
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residue Theorem
  - Improper Integrals
relations: []
review: draft
---

::: {.problem}
Evaluate
$$
\int_0^\infty \frac{\log x}{x^2 - 1} \, dx.
$$
:::

::: {.solution}
The apparent singularity at $x=1$ is removable, since
\[
\frac{\log x}{x^2-1}\longrightarrow\frac12.
\]
Split the integral at $1$ and in the second part set $x=1/t$. Then
\[
\int_1^\infty\frac{\log x}{x^2-1}\,dx
=-\int_0^1\frac{\log t}{1-t^2}\,dt.
\]
The first part is also
\[
\int_0^1\frac{\log x}{x^2-1}\,dx
=-\int_0^1\frac{\log x}{1-x^2}\,dx.
\]
Hence
\[
I=-2\int_0^1\frac{\log x}{1-x^2}\,dx.
\]
Using
\[
\frac1{1-x^2}=\sum_{n=0}^\infty x^{2n},\qquad 0\le x<1,
\]
and monotone/dominated convergence after replacing $\log x$ by $-\log x$,
\[
I=2\sum_{n=0}^\infty\int_0^1(-\log x)x^{2n}\,dx
=2\sum_{n=0}^\infty\frac1{(2n+1)^2}.
\]
Since
\[
\sum_{n=0}^\infty\frac1{(2n+1)^2}=\frac{\pi^2}{8},
\]
we obtain
\[
\boxed{I=\frac{\pi^2}{4}}.
\]
:::
