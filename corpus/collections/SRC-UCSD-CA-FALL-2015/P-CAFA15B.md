---
schema: qual/card@1
id: P-CAFA15B
kind: problem
title: "True or False: real-imaginary inequalities, entire surjection, conformal maps, and polynomial approximation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Are the following statements true or false?
Give a brief proof in each case.

(i) Let $f(z)$ be an entire function and let $u(z)$ and $v(z)$ be the real and imaginary parts of $f$.
There is a non-constant function $f(z)$ such that $u^2 \leq v^2 + 2015$.

(ii) If $f(z)$ is an entire function such that $g(z) = f(1/z)$ has a pole at zero, then $f$ is surjective.

(iii) There is a conformal map from the region $U = \{z = x + iy : 0 < x < 1\}$ to the region $\Delta = \{z : |z| < 1\}$.

(iv) There are polynomials $p_1, p_2, \ldots$ such that $\left|\frac{1}{z(z-4)} - p_n(z)\right|$ converges uniformly to zero on the annulus $U = \{z \in \mathbb{C} : 2 < |z| < 3\}$, as $n$ tends to infinity.
:::

::: solution
**(i) False.** If $f=u+iv$ satisfied $u^2\le v^2+2015$, then
\[
\operatorname{Re}(f^2)=u^2-v^2\le 2015.
\]
Hence $e^{f^2}$ is a bounded entire function, so by Liouville it is constant. Therefore $f^2$ is constant, hence $f$ is constant.

**(ii) True.** The statement that $g(z)=f(1/z)$ has a pole at $0$ means that $f$ has a pole at infinity. Thus $f$ is a nonconstant polynomial. For every $w\in\mathbb C$, the polynomial $f(z)-w$ is nonconstant, so by the fundamental theorem of algebra it has a zero. Therefore $f$ is surjective.

**(iii) True.** The map
\[
z\longmapsto e^{\pi i z}
\]
sends the strip $0<\operatorname{Re}z<1$ conformally onto the upper half-plane, and then the Cayley map
\[
w\longmapsto \frac{w-i}{w+i}
\]
sends the upper half-plane conformally onto the unit disk.

**(iv) False.** Suppose polynomials $p_n$ converged uniformly to
\[
h(z)=\frac1{z(z-4)}
\]
on the annulus. Fix $r$ with $2<r<3$. Then uniform convergence on the circle $|z|=r$ would give
\[
\int_{|z|=r}p_n(z)\,dz\longrightarrow \int_{|z|=r}h(z)\,dz.
\]
The left-hand side is always $0$, while the right-hand side is
\[
2\pi i\operatorname{Res}(h,0)=2\pi i\left(-\frac14\right)\ne0,
\]
a contradiction.
:::
