---
schema: qual/card@1
id: P-UQOCE
kind: problem
title: $\int_\gamma\frac{f'(z)}{z-z_0}\,dz=\int_\gamma\frac{f(z)}{(z-z_0)^2}\,dz$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f$ be analytic in a domain $D$ and $\gamma$ be a closed, piecewise smooth curve in $D$.
For any $z_0 \in D$ not lying on $\gamma$, show that:
$$\oint_\gamma \frac{f'(z)}{z - z_0} \, dz = \oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz.$$
Give a generalization of this result for higher-order derivatives and powers.
:::

::: solution
Since $z_0\notin\gamma$, the function $f(z)/(z-z_0)$ is defined on a neighborhood of the curve. The product rule gives
\[
d\qty({f(z)\over z-z_0})
=\qty({f'(z)\over z-z_0}-{f(z)\over(z-z_0)^2})\,dz.
\]
The integral of an exact differential around a closed curve is zero, hence
\[
\oint_\gamma {f'(z)\over z-z_0}\,dz
=\oint_\gamma {f(z)\over(z-z_0)^2}\,dz.
\]

More generally, for integers $k\ge1$ and $m\ge1$,
\[
d\qty({f^{(k-1)}(z)\over(z-z_0)^m})
=\qty(
{f^{(k)}(z)\over(z-z_0)^m}
-m{f^{(k-1)}(z)\over(z-z_0)^{m+1}}
)\,dz.
\]
Integrating around $\gamma$ therefore gives the recursion
\[
\oint_\gamma {f^{(k)}(z)\over(z-z_0)^m}\,dz
=m\oint_\gamma {f^{(k-1)}(z)\over(z-z_0)^{m+1}}\,dz.
\]
Iterating $k$ times yields
\[
\boxed{
\oint_\gamma {f^{(k)}(z)\over(z-z_0)^m}\,dz
=\frac{(m+k-1)!}{(m-1)!}
\oint_\gamma {f(z)\over(z-z_0)^{m+k}}\,dz
}.
\]
:::
