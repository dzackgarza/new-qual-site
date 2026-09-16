---
schema: qual/card@1
id: T-SSNLT
kind: theorem
title: Fractional residue theorem for a simple pole
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Poles
relations: []
review: draft
---

::: {.theorem}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc about $z_0\in\CC$ with a simple [[D-AUD6K|pole]] at $z_0$.
For real numbers $\alpha<\beta$ and $\varepsilon>0$, let $\gamma_\varepsilon$ be the arc $t\mapsto z_0+\varepsilon e^{it}$, $t\in[\alpha,\beta]$, of the circle $\{z : \abs{z-z_0}=\varepsilon\}$.
Then
$$
\lim_{\varepsilon\to0}\int_{\gamma_\varepsilon}f(z)\dz=i(\beta-\alpha)\Res_{z=z_0}f.
$$

![](../../assets/figures/2021-12-22_05-13-02.png)
:::
