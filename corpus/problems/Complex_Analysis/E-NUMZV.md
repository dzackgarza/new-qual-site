---
schema: qual/card@1
id: E-NUMZV
kind: exercise
title: Entire functions of quadratic growth are polynomials of degree at most $2$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
---

:::{.problem}
Let $f(z)$ be entire and assume that $f(z) \leq M |z|^2$ outside some
disk for some constant $M$. Show that $f(z)$ is a polynomial in $z$ of degree $\leq 2$.
:::

:::{.solution}
Take a Laurent expansion at zero:
\[
f(z) = \sum_{k\geq 0} c_k z^k,\qquad c_k = {1\over k!} f^{(k)}(0) = {1\over 2\pi i}\oint_{\abs{\xi} = R} {f(\xi) \over \xi^{k+1}}\dxi
.\]
The usual estimate:
\[
2\pi i\abs{c_k} \leq \oint_{\abs{\xi} = R} R^{-(k+1)}\abs{f(\xi)} \dxi
&\leq \oint_{\abs{\xi} = R}R^{-(k+1)} M R^2 \dxi \\
&= M R^{-(k-1)} \cdot 2\pi R \\
&= 2\pi M R^{-k+2} \\
&\convergesto{R\to\infty}0
,\]
provided $-k+2<0 \iff k>2$.
:::
