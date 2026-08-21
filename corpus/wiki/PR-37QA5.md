---
schema: qual/card@1
id: PR-37QA5
kind: proposition
title: Complex differentiable implies Cauchy-Riemann
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

:::{.proposition title="Complex differentiable implies Cauchy-Riemann"}
If $f$ is differentiable at $z_0$, then the limit defining $f'(z_0)$ must exist when approaching from any direction.
Identify $f(z) = f(x, y)$ and write $z_0 = x+ iy$, then first consider $h\in RR$, so $h = h_1 + ih_2$ with $h_2 = 0$.
Then
\[
f'(z_0) =
\lim_{h_1\to 0} { f(x+h_1, y) - f(x, y) \over h_1}
\da \dd{f}{x}(x, y)
.\]
Taking $h \in i\RR$ purely imaginary, so $h= ih_2$,
\[
f'(z_0)
= \lim_{ih_2\to 0} { f(x, y+h_2) - f(x, y) \over ih_2 } \da {1\over i} \dd{f}{y}(x, y)
.\]
Equating,
\[
\dd{f}{x} = {1\over i} \dd{f}{y}
,\]
and writing $f = u + iv$ and $1/i = -i$ yields
\[
\dd{f}{x} &= \dd{u}{x} + i \dd{v}{x} \\
{1\over i} \dd{f}{y} &= {1\over i} \qty{ \dd{u}{y} + i \dd{v}{y}} = \dd{v}{y} - i\dd{u}{y}
.\]
Thus
\[
\dd{u}{x} = \dd{v}{y} \hspace{8em} \dd{u}{y} = -\dd{v}{x}
.\]
:::
