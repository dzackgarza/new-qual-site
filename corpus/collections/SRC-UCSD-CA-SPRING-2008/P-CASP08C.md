---
schema: qual/card@1
id: P-CASP08C
kind: problem
title: "Uniform limit of injective analytic functions on the upper half-plane is injective"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Suppose that $f_j \to f$ in $H(\{\operatorname{Im} z > 0\})$, with each $f_j$ one-to-one.
If $f$ is not constant, show that $f$ is one-to-one.
:::

::: solution
Fix distinct $a,b$ in the upper half-plane. For every $j$, injectivity gives
\[
f_j(z)-f_j(a)\ne0\qquad(z\ne a).
\]
On the domain obtained by deleting $a$, the functions
\[
g_j(z)=f_j(z)-f_j(a)
\]
converge locally uniformly to
\[
g(z)=f(z)-f(a).
\]
Hurwitz's theorem says that either $g$ is identically zero or it is nowhere
zero on that punctured domain. Since $f$ is assumed nonconstant, the first
alternative is impossible. Hence
\[
f(b)-f(a)=g(b)\ne0.
\]
As $a\ne b$ were arbitrary, $f$ is one-to-one.
:::
