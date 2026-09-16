---
schema: qual/card@1
id: T-HRPNO
kind: theorem
title: Residue theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Winding Number
  - Meromorphic Functions
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open and let $f$ be [[D-7DFVJ|meromorphic]] on $\Omega$ with finitely many [[D-AUD6K|poles]] $z_1,\ldots,z_N$.
Let $\gamma$ be a piecewise smooth closed curve in $\Omega\setminus\{z_1,\ldots,z_N\}$ whose [[D-PJ7JM|winding number]] $n_\gamma(a)$ is $0$ for every $a\in\CC\setminus\Omega$.
Then
$$
\frac{1}{2\pi i}\int_\gamma f(z)\dz=\sum_{j=1}^Nn_\gamma(z_j)\Res_{z=z_j}f.
$$
In particular, if $n_\gamma(z_j)=1$ for every $j$, then
$$
\frac{1}{2\pi i}\int_\gamma f(z)\dz=\sum_{j=1}^N\Res_{z=z_j}f.
$$
:::

::: {.remark}
See [@SS03, Chapter 3, Theorem 2.4].
:::
