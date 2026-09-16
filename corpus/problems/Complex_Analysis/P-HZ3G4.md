---
schema: qual/card@1
id: P-HZ3G4
kind: problem
title: Uniform convergence of $\sum\sin(nz)/2^n$ on $\{\Im z<\ln 2\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Convergence Tests
  - Series of Functions
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
Prove that the following series converges uniformly on the set $\theset{z \suchthat \Im(z) < \ln 2}$:
\[
\sum_{n=1}^\infty {\sin(nz) \over 2^n}
.\]
:::

::: {.solution}
The statement is false on the stated half-plane. If $z=-iy$ with
$y>\log2$, then
\[
\left|\frac{\sin(nz)}{2^n}\right|
=\frac{\sinh(ny)}{2^n}
\sim \frac12\left(\frac{e^y}{2}\right)^n,
\]
so even the terms fail to tend to zero.

The exact pointwise convergence region is the strip
\[
|\Im z|<\log2.
\]
Indeed, writing $z=x+iy$,
\[
|\sin(nz)|
\le \frac12\left(e^{n|y|}+e^{-n|y|}\right)
\le e^{n|y|}.
\]
Hence if $|y|<\log2$, then
\[
\frac{|\sin(nz)|}{2^n}\le
\left(\frac{e^{|y|}}2\right)^n,
\]
which is summable. Conversely, if $|y|>\log2$, the terms do not tend to
zero by the same exponential asymptotics; at $|y|=\log2$ they also fail to
tend to zero for suitable $x$.

Moreover the convergence is uniform on every closed substrip
$|\Im z|\le a<\log2$, by the Weierstrass $M$-test with majorant
$(e^a/2)^n$. It is not uniform on the whole open strip because the suprema of
the individual terms there do not tend to zero.
:::
