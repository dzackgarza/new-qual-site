---
schema: qual/card@1
id: P-CASP06C
kind: problem
title: "Periodic entire function with subexponential growth is constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
$f$ is an entire function.
Assume that $f(z + 1) = f(z)$ and $|f(z)| \leq e^{C|z|}$ for some $C < 2\pi$.
Show that $f$ is a constant.
:::

::: {.solution}
Because $f$ is $1$-periodic, for each integer $n$ the quantity
\[
a_n(y)=\int_0^1 f(x+iy)e^{-2\pi i n(x+iy)}\,dx
\]
is independent of $y$; this follows by integrating the holomorphic function
$f(z)e^{-2\pi i nz}$ around a period rectangle.

The growth hypothesis gives, uniformly for $0\le x\le1$,
\[
|f(x+iy)|\le e^{C(|y|+1)}.
\]
If $n\ge1$, let $y\to-\infty$. Then
\[
|a_n|
\le e^{C(|y|+1)}e^{2\pi n y}
\longrightarrow0,
\]
because $2\pi n>C$. Hence $a_n=0$ for all $n\ge1$.

If $n\le-1$, let $y\to+\infty$; the same estimate gives
\[
|a_n|
\le e^{C(y+1)}e^{2\pi n y}
\longrightarrow0,
\]
so $a_n=0$ for all $n\le-1$.

Thus every nonconstant Fourier coefficient vanishes. For each fixed $y$ the
periodic holomorphic function $x\mapsto f(x+iy)$ therefore has only its
constant Fourier mode, so $f$ is constant.
:::
