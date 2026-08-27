---
schema: qual/card@1
id: E-WTCTP
kind: exercise
title: Detecting injectivity using derivatives
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Rouché
  - Argument Principle
  - Open Mapping Theorem
relations: []
review: draft
---

:::{.exercise}
Show that if $z_0$ is a zero of $f'$ of order $n-1$, then $f$ is $n$-to-one in a neighborhood of $z_0$.

:::

:::{.solution}
Wlog, assume $z_0 = 0$.
We want to show that there exists discs $U = \DD_r(0)$ and $W = \DD_R(0)$ such that the fiber of $f:U\to W$ has exactly $n$ distinct points.
Since $0$ is a zero of order $n$, expand $f$ as $\sum_{k\geq n} c_k z^k = z^n\sum_{k\geq 0} c_{k+n}z^k$.
By dividing coefficients through, we may assume $c_n = 1$, so 
\[
f(z) = z^n + \qty{ c_{n+1} z^{n+1} + c_{n+2}z^{n+2} + \cdots} = z^n + z^{n+1} \sum_{k\geq 0} c_{k+n+1}z^k \da z^n + g(z)
.\]

:::{.claim}
By Rouché, $f(z)$ and $z^n$ have the same number of zeros in a small disc $\DD_\rho(0)$.
:::

:::{.proof}
Write $m(z) = \sum_{k\geq 0}c_{k+n}z^k$ and $M(z) = z^n$; then if $\abs{m(z)} < \abs{M(z)}$ for any circle $\abs{z} = \rho$ with $\rho< 1$ then $M$ and $m+M = f$ will have the same number of zeros ($n$ with multiplicity).

Bounding $m$, the tail of the Laurent series of $f$: by Cauchy's integral formula, on a disc of radius $R$,
\[
c_k = {f^{(n)}(z_0) \over n!} = {1\over 2\pi i} \oint_{\abs{\xi} = R} { f(\xi) \over (\xi - z_0)^{n+1} } \dxi
,\]
so
\[
\abs{c_k} \leq \max_{\abs{\xi} = R}\abs{f(\xi)} R^{-k} \da {M_R \over R^{k}}
.\]

We can now estimate $g$:
\[
\abs{g(z)} 
&= \abs{z^n \sum_{k\geq 0} c_{k+n+1} z^k} \\
&\leq \abs{z}^n \sum_{k\geq 0} \abs{ c_{k+n+1}} \abs{z}^k \\
&\leq \sum_{k\geq 0} {M_R \over R^{k+n+1}} \rho^k \\
&= \abs{z}^n {M_R \over R^{n+1}} \sum_{k\geq 0} \qty{\rho\over R}^k \\
&= \abs{z}^n {M_R \over R^{n+1}} \qty{1\over 1- {\rho \over R}} \\
&= \abs{z}^n {M_R \over R^{n+1}} {R\over R-\rho} \\
&= \abs{z}^n \qty{ {M_R\over R^n( R-\rho)} } \\
&\da \abs{z}^n C_{R, \rho}
,\]
and $R, \rho$ can be chosen such that $C_{R, \rho} < 1$.

Thus on $\abs{z} = \rho$,
\[
\abs{m(z)} = \abs{g(z) } \leq C_{R, \rho} \abs{z} < \abs{z} = \abs{M(z)}
.\]

:::

So the fiber above $z=0$ is of size $n$, the claim is that this is also true in a neighborhood of zero.
The above estimate also shows that for $0 < \abs{z}\leq \rho$, $\abs{g(z)} \leq \abs{z^n}$, and so
\[
\abs{g(z)} = \abs{g(z) - z^n + z^n} \geq \abs{ \abs{g(z) - z^n} - \abs{z^n} } > 0
,\]
so $g$ is nonzero on $\DD_\rho(0)\smz$.
For the zero-counting function
\[
F(w) \da {1\over 2\pi i} \oint_{\abs{\xi} = \rho'} {f'(\xi) \over f(\xi) - w }\dxi
.\]
Taking $\rho ' < \min_{\abs{\xi} = \rho} \abs{f(z)}$ makes this a holomorphic function of $w$ on $\DD_{\rho'}(0)$, and as a continuous $\ZZ\dash$valued function it is constant.
Since $F(0) = n$, this forces $F(w) = n$ for all $\abs{w} < \rho'$, so there are $n$ solutions to $f(z) = w$ in these discs.
After shrinking these discs if necessary, $f'\neq 0$ is nonvanishing on a punctured disc, so $f$ is injective there and these solutions are distinct.
:::

