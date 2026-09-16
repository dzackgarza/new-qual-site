---
schema: qual/card@1
id: T-VCX3Y
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
relations:
- kind: variant-of
  target: T-JXDQT
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be a bounded open set whose boundary $\gamma\coloneqq\partial\Omega$ consists of finitely many piecewise smooth closed curves, oriented positively with respect to $\Omega$.
Let $f$ be [[D-7DFVJ|meromorphic]] on an open set containing $\overline{\Omega}$, with no [[D-65VIK|zeros]] or [[D-AUD6K|poles]] on $\gamma$, and let $Z_f$ and $P_f$ be the numbers of zeros and poles of $f$ in $\Omega$, counted with multiplicity.
Then
$$
\frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\dz=Z_f-P_f.
$$
:::
