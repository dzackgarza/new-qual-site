---
schema: qual/card@1
id: PR-L4Y5F
kind: proposition
title: Residue formula for simple poles
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
:::

::: {.proof}
Near $z_0$, $f(z)=\frac{a_{-1}}{z-z_0}+G(z)$ with $G$ holomorphic at $z_0$, so $(z-z_0)f(z)=a_{-1}+(z-z_0)G(z)\to a_{-1}=\Res_{z=z_0}f$.
:::
