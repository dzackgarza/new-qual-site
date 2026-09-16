---
schema: qual/card@1
id: T-HHFGB
kind: theorem
title: Convolution with an approximate identity converges in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $\phi\in L^1(\RR^n)$ with $\int_{\RR^n}\phi=1$, let $\phi_t(x)\coloneqq t^{-n}\phi(t\inv x)$ for $t>0$ be the corresponding [[D-ARQFC|approximate identity]], and let $f\in L^1(\RR^n)$.
Then
$$
\lim_{t\to 0^+}\norm{f * \phi_{t} - f}_1 = 0 .
$$
:::
