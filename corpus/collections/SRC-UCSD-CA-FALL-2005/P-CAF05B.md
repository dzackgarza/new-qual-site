---
schema: qual/card@1
id: P-CAF05B
kind: problem
title: "Local representation of an analytic function near a zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f$ be a nonconstant analytic function in $\mathbb{D}$ with $f(0) = 0$.
Show that there exist a real number $r$, $0 < r \leq 1$, a function $g \in H(B(0; r))$ with $g(0) \neq 0$, and a positive integer $m$, such that $$f(z) = (zg(z))^m, \qquad z \in B(0; r).$$
:::

::: solution
Since $f$ is holomorphic, nonzero as a function, and satisfies $f(0)=0$, its
Taylor series has a first nonzero term. Thus for some integer $m\ge1$,
\[
f(z)=z^m h(z),
\]
where $h$ is holomorphic near $0$ and $h(0)\ne0$.

Choose $0<r\le1$ so small that $h$ has no zeros on the simply connected disk
$B(0,r)$. Then $h$ has a holomorphic logarithm $L$ on this disk. Define
\[
g(z)=\exp\left(\frac{L(z)}m\right).
\]
Then $g$ is holomorphic, $g(0)\ne0$, and $g(z)^m=h(z)$. Therefore
\[
f(z)=z^m g(z)^m=(zg(z))^m
\qquad(z\in B(0,r)),
\]
as required.
:::
