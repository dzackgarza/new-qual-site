---
schema: qual/card@1
id: T-2KGOX
kind: theorem
title: Standard conformal maps between half-planes, sectors, strips and discs
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.theorem}
Write $\HH=\ts{\Im z>0}$ for the upper half-plane, $\DD_{1/2}=\ts{\abs z<1,\ \Im z>0}$ for the upper half-disc, $Q_1=\ts{\Re z>0,\ \Im z>0}$ for the first quadrant, $S_\beta=\ts{re^{i\theta}\st r>0,\ 0<\theta<\beta}$ for the sector of opening $\beta$, $\Sigma=\ts{0<\Im z<\pi}$ for the horizontal strip, and $\Log$ for the principal branch of the logarithm.
Each of the following maps is a [[D-TM4TE|biholomorphism]] from the stated domain onto the stated target.

| Domain | Target | Map |
| --- | --- | --- |
| $\CC$ | $\CC$ | translation $z\mapsto z+h$, $h\in\CC$ |
| $\CC$ | $\CC$ | dilation $z\mapsto cz$, $c>0$ |
| $\CC$ | $\CC$ | rotation $z\mapsto e^{i\theta}z$, $\theta\in\RR$ |
| $S_{\pi/n}$, $n\ge1$ | $\HH$ | $z\mapsto z^n$ ([[PR-PDYJC]]) |
| $\DD_{1/2}$ | $Q_1$ | $z\mapsto\frac{1+z}{1-z}$ ([[PR-PW4Z6]]) |
| $\HH$ | $\Sigma$ | $z\mapsto\Log z$ ([[PR-XCDL5]]) |
| $\DD_{1/2}$ | $\ts{\Re w<0,\ 0<\Im w<\pi}$ | $z\mapsto\Log z$ ([[PR-PELLF]]) |
| $\ts{0<\Re z<\pi,\ \Im z>0}$ | $\DD_{1/2}$ | $z\mapsto e^{iz}$ |
| $\DD_{1/2}$ | $\HH$ | $z\mapsto-\frac12\big(z+\frac1z\big)$ ([[PR-OTMIR]]) |
| $\ts{-\frac\pi2<\Re z<\frac\pi2,\ \Im z>0}$ | $\HH$ | $z\mapsto\sin z$ |
:::
