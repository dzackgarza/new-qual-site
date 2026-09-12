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
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $f$ be analytic in a domain $D$ and $\gamma$ be a closed, piecewise smooth curve in $D$.
For any $z_0 \in D$ not lying on $\gamma$, show that: $$\oint_\gamma \frac{f'(z)}{z - z_0} \, dz = \oint_\gamma \frac{f(z)}{(z - z_0)^2} \, dz.$$ Give a generalization of this result for higher-order derivatives and powers.
:::

::: solution
Since $z_0\notin\gamma$, the function
\[
F(z)=\frac{f(z)}{z-z_0}
\]
is holomorphic on a neighborhood of the curve. Hence
\[
F'(z)=\frac{f'(z)}{z-z_0}-\frac{f(z)}{(z-z_0)^2},
\]
and the integral of $F'$ around the closed curve is zero. Therefore
\[
\oint_\gamma\frac{f'(z)}{z-z_0}\,dz
=
\oint_\gamma\frac{f(z)}{(z-z_0)^2}\,dz.
\]

More generally, for integers $k,m\ge1$,
\[
\left(\frac{f^{(k-1)}(z)}{(z-z_0)^m}\right)'
=
\frac{f^{(k)}(z)}{(z-z_0)^m}
-m\frac{f^{(k-1)}(z)}{(z-z_0)^{m+1}}.
\]
Thus
\[
\oint_\gamma\frac{f^{(k)}(z)}{(z-z_0)^m}\,dz
=m\oint_\gamma\frac{f^{(k-1)}(z)}{(z-z_0)^{m+1}}\,dz.
\]
Iterating gives
\[
\boxed{
\oint_\gamma\frac{f^{(k)}(z)}{(z-z_0)^m}\,dz
=
\frac{(m+k-1)!}{(m-1)!}
\oint_\gamma\frac{f(z)}{(z-z_0)^{m+k}}\,dz }.
\]
:::
