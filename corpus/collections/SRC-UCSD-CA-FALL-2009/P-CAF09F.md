---
schema: qual/card@1
id: P-CAF09F
kind: problem
title: "An entire function with real plus imaginary part bounded is constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Suppose that $f(z) = u(z) + iv(z)$ is an entire function with real part $u(z)$ and imaginary part $v(z)$ such that for all $z$, $u(z) + v(z) < 1$.
Prove that $f(z)$ is a constant.
:::

::: solution
Consider the entire function
\[
g(z)=e^{(1-i)f(z)}.
\]
Since
\[
(1-i)(u+iv)=(u+v)+i(v-u),
\]
we have
\[
|g(z)|=e^{u(z)+v(z)}<e
\]
for every $z\in\mathbb C$. Thus $g$ is bounded and entire, so Liouville's
theorem implies that $g$ is constant.

Differentiating,
\[
0=g'(z)=(1-i)f'(z)e^{(1-i)f(z)}.
\]
The exponential factor never vanishes, hence $f'(z)=0$ for all $z$. Therefore
$f$ is constant.
:::
