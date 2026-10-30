---
schema: qual/card@1
id: P-B4HPX
kind: problem
title: Holomorphy of both $f(z)$ and $f(\bar{z})$ on the disk forces $f$ constant
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be an analytic function on $\abs{z}<1$.
Prove that $f(z)$ is necessarily a constant if $f(\bar{z})$ is also analytic.
:::

::: {.solution}

Let $\DD=\{\abs{z}<1\}$ and $g(z)=f(\bar z)$, which is analytic on $\DD$ by hypothesis.

::: pf

::: {.pf-step #deriv}

$f'(z_0)=0$ for every $z_0\in\DD$.

::: pf-proof

The function $g$ is complex differentiable at $\bar z_0$, so
$$
g'(\bar z_0)=\lim_{h\to0}\frac{g(\bar z_0+h)-g(\bar z_0)}{h}=\lim_{h\to0}\frac{f(z_0+\bar h)-f(z_0)}{h}.
$$
For real $h=t\to0$ the quotient tends to $f'(z_0)$. For $h=it$ with $t$ real, $\bar h=-it$ and the quotient is $-\frac{f(z_0-it)-f(z_0)}{-it}\to-f'(z_0)$. Both limits equal $g'(\bar z_0)$, so $f'(z_0)=-f'(z_0)$.

:::

:::

::: pf-qed

By Step [](#deriv){.pf-ref}, $f'\equiv0$ on the connected open set $\DD$, so $f$ is constant.

:::

:::

:::
