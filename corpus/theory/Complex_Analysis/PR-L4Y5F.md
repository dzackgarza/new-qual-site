---
schema: qual/card@1
id: PR-L4Y5F
kind: proposition
title: Residue formula for simple poles
slogan: 'At a simple pole, the residue is the surviving coefficient after multiplying by $z-z_0$ and taking the limit.'
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
relations: []
review: draft
---

::: {.proposition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc about $z_0$ with a simple [[D-AUD6K|pole]] at $z_0$.
Then its [[D-C3JIU|residue]] at $z_0$ is
$$
\Res_{z=z_0}f = \lim_{z\to z_0} (z-z_0) f(z).
$$

This is the case $n=1$ of [@SS03, ch. 3, Theorem 1.4], which gives $\Res_{z_0}f=\lim_{z\to z_0}\frac{1}{(n-1)!}\qty{\frac{d}{dz}}^{n-1}(z-z_0)^nf(z)$ at a pole of order $n$.
:::
