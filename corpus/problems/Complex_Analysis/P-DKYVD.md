---
schema: qual/card@1
id: P-DKYVD
kind: problem
title: $\int_\gamma\frac{dz}{(z-\alpha)(z-\beta)}=\frac{2\pi i}{\alpha-\beta}$ without
  Cauchy's formula
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Contour Integration
  - Residues
relations: []
review: draft
---

::: problem
Without using Cauchy's integral formula, show that if $\abs{a} < r < \abs{b}$, then
\[
\int_{\gamma} \frac{d z}{(z-a)(z-b)}
=\frac{2 \pi i}{a-b}
\]
where $\gamma$ denotes the circle centered at the origin of radius $r$ with positive orientation.

> Hint: take a Laurent expansion.
:::

::: solution
Since $|a|<r<|b|$, on $|z|=r$ we may expand
\[
{1\over z-a}
={1\over z}{1\over1-a/z}
=\sum_{m=0}^\infty a^m z^{-m-1}
\]
and
\[
{1\over z-b}
=-{1\over b}{1\over1-z/b}
=-\sum_{n=0}^\infty {z^n\over b^{n+1}}.
\]
Both series converge uniformly on the circle. Multiplying them gives a
Laurent series for the integrand. Its coefficient of $z^{-1}$ is
\[
-\sum_{m=0}^\infty {a^m\over b^{m+1}}
=-{1\over b-a}
={1\over a-b}.
\]
Termwise integration around $\gamma$ therefore gives
\[
\int_\gamma {dz\over(z-a)(z-b)}
=2\pi i\,{1\over a-b},
\]
because every Laurent monomial except $z^{-1}$ integrates to zero.
:::
