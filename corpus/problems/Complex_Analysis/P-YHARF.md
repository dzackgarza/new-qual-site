---
schema: qual/card@1
id: P-YHARF
kind: problem
title: Taylor coefficients of a function with a pole on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Convergence Tests
relations: []
review: draft
---

::: problem
Suppose that $f$ is holomorphic in an open set containing the closed
unit disc, except for a pole at $z_0$ on the unit circle. Let
$\displaystyle
%f(z) = \sum_{n = 1}^\infty a_n z^n
f(z) = \sum_{n = 1}^\infty c_n z^n$ denote the the power series in
the open disc. Show that (1) $c_n \neq 0$ for all large enough
$n$'s, and (2)
$\displaystyle \lim_{n \rightarrow \infty} \frac{c_n}{c_{n+1}}= z_0$.
:::

::: solution
Let the pole of $f$ at $z_0$ have order $m$, with principal part
\[
\sum_{j=1}^m\frac{A_j}{(z-z_0)^j},
\qquad A_m\ne0.
\]
Because $f$ is holomorphic on an open neighborhood of the closed unit disk
except at $z_0$, there is some $R>1$ such that after subtracting this principal
part the remainder
\[
h(z)=f(z)-\sum_{j=1}^m\frac{A_j}{(z-z_0)^j}
\]
is holomorphic on $|z|<R$.

For $|z|<1=|z_0|$,
\[
\frac1{(z-z_0)^j}
=(-1)^j z_0^{-j}
\sum_{n=0}^\infty
\binom{n+j-1}{j-1}\frac{z^n}{z_0^n}.
\]
Hence the coefficient $c_n$ of $z^n$ has the form
\[
c_n
=z_0^{-n}\sum_{j=1}^m
(-1)^jA_jz_0^{-j}\binom{n+j-1}{j-1}
+d_n,
\]
where the Taylor coefficients of $h$ satisfy $d_n=O(R^{-n})$ by Cauchy's
estimates.

The $j=m$ term has degree $m-1$ in $n$ and nonzero leading coefficient,
whereas all terms with $j<m$ have smaller polynomial degree. Therefore
\[
c_n=Cz_0^{-n}n^{m-1}\left(1+O\left(\frac1n\right)\right)
\]
for some constant $C\ne0$; the exponentially small term $d_n$ does not affect
this asymptotic. Consequently $c_n\ne0$ for all sufficiently large $n$, and
\[
\frac{c_n}{c_{n+1}}
=z_0\left(\frac{n}{n+1}\right)^{m-1}
\frac{1+O(1/n)}{1+O(1/n)}
\longrightarrow z_0.
\]
This proves both assertions.
:::
