---
schema: qual/card@1
id: T-SSNLT
kind: theorem
title: 'Residue formula: fractional residues'
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

:::{.theorem}
If $z_0$ is an order 1 pole of $f$ and $\gamma_{\eps, \theta}$ is an arc of the circle $C_\eps \da \ts{ \abs{z-z_0} = \eps}$ subtending an angle of $\theta$, then
\[
\lim_{\eps\to 0} \int_{\gamma_{\eps, \theta}} f(z) \dz  = i\theta \Res_{z = z_0}f(z)
.\]

![](../../assets/figures/2021-12-22_05-13-02.png)

:::
