---
schema: qual/card@1
id: D-MAGRK
kind: definition
title: Approximations to the identity
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
relations: []
review: draft
---

::: {.definition}
Let $\phi\in L^1(\RR^n)$ with $\int_{\RR^n} \phi = 1$, and for $t>0$ let $\phi_t$ be its [[D-EWXAT|dilation]] $\phi_t(x)=t^{-n}\phi(t^{-1}x)$.
Then $\phi$, or the family $(\phi_t)_{t>0}$, is called an \dfn{approximate identity}.
:::

::: {.remark}
For every $\phi\in L^1(\RR^n)$ and $t>0$, the substitution $x=ty$ gives $\int \phi_{t} = \int \phi$, so every dilation of an approximate identity also has integral $1$.
:::
