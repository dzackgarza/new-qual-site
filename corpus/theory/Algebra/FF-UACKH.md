---
schema: qual/card@1
id: FF-UACKH
kind: fact
title: Cyclotomic polynomial $\Phi_{2p}$ for an odd prime $p$
prompts:
- What is the cyclotomic polynomial $\Phi_{2p}(x)$?
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Polynomials
relations: []
review: draft
---

::: {.fact}
For an odd prime $p$, the [[D-BLV6F|cyclotomic polynomial]] $\Phi_{2p}$ is
$$
\Phi_{2p}(x)=\Phi_p(-x)=1-x+x^2-\cdots+x^{p-1}.
$$
:::

::: {.proof}
Since $p$ is odd, $-1$ has order $2$ and $\zeta\mapsto-\zeta$ is a bijection from the primitive $p$th roots of unity to the primitive $2p$th roots of unity.
Hence
$$
\Phi_{2p}(x)=\prod_\zeta(x+\zeta)=(-1)^{p-1}\prod_\zeta(-x-\zeta)=\Phi_p(-x),
$$
the products running over the primitive $p$th roots of unity $\zeta$, because $p-1$ is even.
Substituting $-x$ in $\Phi_p(x)=1+x+\cdots+x^{p-1}$ ([[FF-MUJDE]]) gives the sum.
:::

::: {.remark}
For $p=2$ the formula fails: $\Phi_4(x)=x^2+1$, whereas $\Phi_2(-x)=1-x$.
:::
