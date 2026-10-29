---
schema: qual/card@1
id: P-CV2MR
kind: problem
title: $\abs{z}^2$ is complex-differentiable only at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Prove that $f(z) = \abs{z}^2$ has a derivative at $z=0$ and nowhere else.
:::

::: {.solution}

::: pf

::: pf-step
$f'(0)$ exists and equals $0$.

::: pf-proof
For $z\ne0$, $\frac{f(z)-f(0)}{z}=\frac{z\bar z}{z}=\bar z\to0$ as $z\to0$.
:::

:::

::: pf-step
$f$ has no derivative at any $w\ne0$.

::: pf-proof
For $z\ne w$,
$$
\frac{f(z)-f(w)}{z-w}=\frac{\abs{z}-\abs{w}}{z-w}\,(\abs{z}+\abs{w}).
$$
Along the circle $\abs{z}=\abs{w}$ this quotient is $0$, so its limit is $0$.
Along the ray $z=tw$, $t\to1$, it equals $\frac{\abs{w}(t-1)}{w(t-1)}\abs{w}(t+1)=\bar w(t+1)\to2\bar w\ne0$.
The two limits differ, so the difference quotient has no limit at $w$.
:::

:::

:::

:::

::: {.remark}
Equivalently, $f$ is real-differentiable and $\delbar_z(z\bar z)=z$, so the Cauchy--Riemann equation $\delbar_z f=0$ holds only at $z=0$.
:::
