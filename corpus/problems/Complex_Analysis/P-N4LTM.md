---
schema: qual/card@1
id: P-N4LTM
kind: problem
title: 'Local mapping theorem: a zero of multiplicity $m$ splits into $m$ distinct
  nearby preimages'
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Zeros
  - Argument Principle
relations: []
review: draft
---

::: {.problem}
Let $f$ be analytic in a domain $D$ and fix $z_0 \in D$ with $w_0 \definedas f(z_0)$.
Suppose $z_0$ is a zero of $f(z) - w_0$ with finite multiplicity $m$.
Show that there exists $\delta >0$ and $\eps > 0$ such that for each $w$ such that $0 < \abs{w-w_0} < \eps$, the equation $f(z) - w = 0$ has exactly $m$ *distinct* solutions inside the disc $\abs{z-z_0} < \delta$.
:::

::: {.solution}
Write $f(z)-w_0=(z-z_0)^mg(z)$ with $g$ holomorphic on $D$ and $g(z_0)\ne0$, and let $\Delta=\theset{\abs{z-z_0}<\delta}$.

::: pf

::: {.pf-step #choose-delta}
There is $\delta>0$ with $\overline\Delta\subset D$ such that $z_0$ is the only zero of $f-w_0$ in $\overline\Delta$ and the only zero of $f'$ in $\overline\Delta$.

::: pf-proof
Differentiating gives $f'(z)=(z-z_0)^{m-1}h(z)$ with $h=mg+(z-z_0)g'$ holomorphic and $h(z_0)=mg(z_0)\ne0$. By continuity $g$ and $h$ have no zero on a small closed disk about $z_0$.
:::

:::

::: {.pf-step #rouche}
With $\eps\definedas\min_{\abs{z-z_0}=\delta}\abs{f(z)-w_0}>0$, for each $w$ with $0<\abs{w-w_0}<\eps$ the function $f-w$ has exactly $m$ zeros in $\Delta$, counted with multiplicity.

::: pf-proof
The minimum is positive by step [](#choose-delta){.pf-ref}. On $\abs{z-z_0}=\delta$, $\abs{w-w_0}<\eps\le\abs{f(z)-w_0}$, so by Rouché's theorem $f-w=(f-w_0)-(w-w_0)$ has as many zeros in $\Delta$ as $f-w_0$, namely $m$.
:::

:::

::: pf-step
These $m$ zeros are distinct.

::: pf-proof
A zero $z$ of $f-w$ in $\Delta$ is not $z_0$, since $f(z_0)=w_0\ne w$. By step [](#choose-delta){.pf-ref}, $f'(z)\ne0$, so $z$ is a simple zero. Hence the $m$ zeros of step [](#rouche){.pf-ref}, counted with multiplicity, are $m$ distinct points.
:::

:::

:::
:::
