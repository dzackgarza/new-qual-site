---
schema: qual/card@1
id: P-RHQC5
kind: problem
title: 'Weierstrass''s theorem: locally uniform limits of holomorphic functions are
  holomorphic'
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
  - Morera
relations: []
review: draft
---

::: problem
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of analytic functions on $\DD \definedas \theset{z\in \CC \suchthat \abs{z} < 1}$.

Show that if $f_n\to g$ for some $g: \DD \to \CC$ uniformly on every compact $K\subset \DD$, then $g$ is analytic on $\DD$.
:::

::: solution
Local uniform convergence implies that $g$ is continuous. Let $T$ be any
triangle whose closure lies in $\mathbb D$. Since $f_n\to g$ uniformly on
$\partial T$,
\[
\int_{\partial T}g(z)\,dz
=\lim_{n\to\infty}\int_{\partial T}f_n(z)\,dz.
\]
Each integral on the right is zero by Cauchy's theorem because $f_n$ is
holomorphic. Hence
\[
\int_{\partial T}g(z)\,dz=0
\]
for every such triangle. Morera's theorem therefore implies that $g$ is
holomorphic on $\mathbb D$.
:::
