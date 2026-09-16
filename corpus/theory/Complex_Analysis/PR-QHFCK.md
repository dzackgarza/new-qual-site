---
schema: qual/card@1
id: PR-QHFCK
kind: proposition
title: Zeros of $\zeta$ outside the critical strip
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta
  - Zeros
relations: []
review: draft
---

::: {.proposition}
Let $\zeta$ be the [[D-HJYH3|Riemann zeta function]], continued meromorphically to $\CC$.
The only [[D-65VIK|zeros]] of $\zeta$ outside the critical strip $\ts{s\st0\le\Re s\le1}$ are the simple zeros at $s=-2,-4,-6,\ldots$.
Moreover, $\zeta$ has no zeros on the line $\Re s=1$.
:::

::: {.proof}
For $\Re s>1$ the Euler product $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ converges absolutely, and an absolutely convergent product of nonzero factors is nonzero.
For $\Re s<0$ use the functional equation
$$
\zeta(s)=\pi^{s-1/2}\,\frac{\Gamma\big(\frac{1-s}{2}\big)}{\Gamma\big(\frac s2\big)}\,\zeta(1-s).
$$
There $\Re(1-s)>1$, so $\zeta(1-s)\neq0$; $\Gamma\big(\frac{1-s}{2}\big)$ is finite and nonzero because $\Gamma$ has no zeros and its poles lie at $0,-1,-2,\ldots$; and $1/\Gamma(s/2)$ is entire with simple zeros exactly at $s=0,-2,-4,\ldots$.
So the zeros of $\zeta$ with $\Re s<0$ are the simple zeros at $s=-2,-4,\ldots$.
The nonvanishing of $\zeta$ on $\Re s=1$ is the theorem of Hadamard and de la Vallée Poussin.
:::

::: {.remark}
The zeros at the negative even integers are the trivial zeros of $\zeta$.
The Riemann hypothesis is the conjecture that every zero of $\zeta$ in the critical strip lies on the line $\Re s=\frac12$.
:::
