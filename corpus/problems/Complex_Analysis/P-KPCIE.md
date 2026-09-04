---
schema: qual/card@1
id: P-KPCIE
kind: problem
title: Midpoint recurrence $x_n=\frac{x_{n-1}+x_{n-2}}{2}$ converges to $\frac{a+2b}{3}$
classification:
  areas:
  - complex-analysis
  topics:
  - Sequences of Numbers
  - Completeness
  - Convergence
relations: []
review: draft
---

::: {.problem}
Let $x_0 = a, x_1 = b$, and set
\[  
x_n \definedas {x_{n-1} + x_{n-2} \over 2} \quad n\geq 2
.\]

Show that $\theset{x_n}$ is a Cauchy sequence and find its limit in terms of $a$ and $b$.

:::

::: {.solution}
Put $d_n=x_n-x_{n-1}$. Then
\[
d_n=-{1\over2}d_{n-1},
\qquad
|d_n|=2^{-(n-1)}|b-a|.
\]
If $m>n$, then
\[
|x_m-x_n|
\le\sum_{j=n+1}^m|d_j|
\le |b-a|\sum_{j=n+1}^\infty2^{-(j-1)}
=2^{1-n}|b-a|,
\]
which tends to $0$ as $n\to\infty$. Thus $(x_n)$ is Cauchy.

To identify the limit, observe that
\[
x_{n-1}+2x_n
=x_{n-1}+x_{n-1}+x_{n-2}
=x_{n-2}+2x_{n-1}.
\]
Hence this quantity is independent of $n$, and from $n=1$ it equals
\[
a+2b.
\]
Since the sequence is Cauchy in $\CC$, let $x_n\to L$. Passing to the limit in the invariant gives
\[
3L=a+2b,
\qquad
L={a+2b\over3}.
\]
:::
