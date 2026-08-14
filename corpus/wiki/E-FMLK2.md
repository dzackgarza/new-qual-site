---
schema: qual/card@1
id: E-FMLK2
kind: exercise
title: "Derivatives detect multiplicity of zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - zeros
  - power-series
  - holomorphic-functions
relations: []
review: draft
---
:::{.exercise title="Derivatives detect multiplicity of zeros"}
Show that if $f$ is holomorphic in $\DD_r(a)$ and $a$ is a zero of $f$ of multiplicity $n$, then $f^{(k)}(a) = 0$ for $k\leq n-1$ and $f^{(n)}(a) \neq 0$.
Show that this is an iff.

:::

:::{.solution}
$\implies$:
Suppose the first $m-1$ derivatives vanish.
Then
\[
f(z) = \sum_{k\geq 0} c_k (z-a)^k = \sum_{k\geq m+1} c_k (z-a)^k = (z-a)^m \sum_{k\geq m+1} c_k (z-a)^{k-m} = (z-a)^m (c_m + c_{m+1}(z-a) + \cdots) \da (z-a)^m g(z)
,\]
using that $c_k \approx f^{(k)}(a)$.
Noting that $g(a) = c_m \neq 0$, we have $f(z) = (z-a)^m g(z)$ where $g$ is nonvanishing in a neighborhood of $a$, making $a$ a zero of $f$ of order $m$.

Conversely, if $a$ is an order $m$ zero, then $f(z) = (z-a)^m h(z)$ for $h$ nonvanishing near $a$.
So as above, writing 
\[
f(z) = \sum_{k\geq 0} c_k (z-a)^k = \sum_{k\leq m} c_k (z-a)^k + (z-a)^m g(z)
,\]
we have
\[
0 = f(z) - (z-a)^m h(z) = \sum_{k \leq m} c_k (z-a)^k + (z-a)^m(g(z) - h(z))
.\]
But this is a power series expansion of the zero function, and by uniqueness of power series we have $c_k = 0$ for $k\leq m-1$ and $g(z) = h(z)$.
In particular, $g(a) = c_{m}$ by definition, and $g(a) = h(a) \neq 0$.
:::
