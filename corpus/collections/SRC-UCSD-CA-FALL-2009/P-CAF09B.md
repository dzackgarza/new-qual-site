---
schema: qual/card@1
id: P-CAF09B
kind: problem
title: "Removable singularity for bounded analytic functions on punctured neighborhoods"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Suppose that $f(z)$ is defined and analytic in the punctured neighborhood of zero, $N = \{z \mid 0 < |z| < 1\}$, and that for all $z$ in $N$, $|f(z)| < 1$.
Provide a proof of the standard result that $f(z)$ has a removable singularity at $z = 0$.
:::

::: solution
Define
\[
g(z)=z^2f(z)
\]
for $z\ne0$, and set $g(0)=0$. Since $|f(z)|<1$,
\[
\frac{g(z)-g(0)}{z}=zf(z)\longrightarrow0
\qquad(z\to0).
\]
Thus $g$ is holomorphic at $0$ and $g'(0)=0$. Hence the Taylor expansion of
$g$ at $0$ starts in degree at least two:
\[
g(z)=z^2h(z)
\]
for some holomorphic $h$ near $0$.

For $z\ne0$ we have $h(z)=f(z)$. Therefore defining
\[
\widetilde f(0)=h(0),\qquad \widetilde f(z)=f(z)\ (z\ne0),
\]
gives a holomorphic extension across the origin. Thus the singularity is
removable.
:::
