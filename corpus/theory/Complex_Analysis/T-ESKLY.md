---
schema: qual/card@1
id: T-ESKLY
kind: theorem
title: Residue at a pole of order $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
relations: []
review: draft
---

::: {.theorem}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc about $z_0\in\CC$ with a [[D-AUD6K|pole]] of order $n\geq1$ at $z_0$.
Then the [[D-C3JIU|residue]] of $f$ at $z_0$ is
$$
\Res_{z=z_0}f=\lim_{z\to z_0}\frac{1}{(n-1)!}\frac{d^{n-1}}{dz^{n-1}}\bigl((z-z_0)^nf(z)\bigr).
$$
In particular, if $z_0$ is a simple pole of $f$, then
$$
\Res_{z=z_0}f=\lim_{z\to z_0}(z-z_0)f(z).
$$
:::
