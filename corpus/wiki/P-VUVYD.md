---
schema: qual/card@1
id: P-VUVYD
kind: problem
title: An entire function with polynomial real part is a polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Cauchy-Riemann
  - Entire Functions
  - Polynomials
relations: []
review: draft
---

:::{.problem title="?"}
Let $f = u + iv$ be an entire function such that $\Re(f(x+iy))$ is polynomial in $x$ and $y$.
Show that $f(z)$ is polynomial in $z$.
:::

:::{.solution}
To clear up notation: write $f(z) = u(x, y) + iv(x, y)$, here we're assuming that $u$ is polynomial in $x$ and $y$.

:::{.claim}
If $u$ is polynomial in $x,y$, then so is $v$.
:::

:::{.proof title="?"}
This follows from the fact that $u$ is a harmonic conjugate of $v$, and the explicit process computing the conjugate will result in a polynomial.
Gamelin describes this process in detail, see Ch.2 Section 5 on Harmonic functions where he proves the formula
\[
v(x, y)
= \int_{y_{0}}^{y} \frac{\partial u}{\partial x}(x, t) \dt 
-\int_{x_{0}}^{x} \frac{\partial u}{\partial y}\left(s, y_{0}\right) \ds + C 
.\]

:::

:::{.claim}
Since $f(x, y)$ is a polynomial in $x, y$, $f(z)$ must be a polynomial in $z$.
:::

:::{.proof title="?"}
Since $f$ is entire, it's equal to its Laurent series everywhere, so
\[
f(z) = \sum_{k\geq 0} c_k z^k, \qquad c_k = {f^{(k) }(0) \over k!} = {1\over 2\pi i} \int_{S^1} {f(\xi) \over \xi^{k+1} } \dxi
.\]
Thus $f$ will be a polynomial if $c_{N} = 0$ for all $N$ large enough, which will be true if $f^{(N)}(z) = 0$ for large enough $N$.
But we can write
\[
\dd{}{z} f(z) = \dd{}{x} f(x, y)
\implies
0 = \qty{\dd{^N}{x^N}} f(x, y) = \qty{\dd{^N}{z^N}} f(z) \da f^{(N)}(z)
,\]
:::

:::

