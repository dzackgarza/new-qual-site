---
schema: qual/card@1
id: T-JXDQT
kind: theorem
title: Argument principle counting zeros and poles
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Zeros
  - Poles
  - Meromorphic Functions
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be a bounded open set whose boundary $\gamma\coloneqq\partial\Omega$ consists of finitely many piecewise smooth closed curves, oriented positively with respect to $\Omega$.
Let $f$ be [[D-7DFVJ|meromorphic]] on an open set containing $\overline{\Omega}$, with no [[D-65VIK|zeros]] or [[D-AUD6K|poles]] on $\gamma$.
Let $Z_f$ and $P_f$ be the numbers of zeros and poles of $f$ in $\Omega$, counted with multiplicity.
Then
$$
\frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\dz=Z_f-P_f.
$$
If moreover $f$ is [[D-E7A5W|holomorphic]] with zeros $z_1,\ldots,z_m$ in $\Omega$, listed with multiplicity, then
$$
\frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\dz=m
\quad\text{and}\quad
\frac{1}{2\pi i}\int_\gamma\frac{zf'(z)}{f(z)}\dz=\sum_{k=1}^mz_k.
$$
:::
