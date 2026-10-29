---
schema: qual/card@1
id: P-MYZMF
kind: problem
title: A holomorphic function is locally $m$-to-$1$ near a zero of multiplicity $m$
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Open Mapping Theorem
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $f$ be analytic in a domain $D$ and fix $z_0 \in D$ with $w_0 \definedas f(z_0)$.
Suppose $z_0$ is a zero of $f(z) - w_0$ with finite multiplicity $m$.
Show that there exists $\delta >0$ and $\eps > 0$ such that for each $w$ such that $0 < \abs{w-w_0} < \eps$, the equation $f(z) - w = 0$ has exactly $m$ *distinct* solutions inside the disc $\abs{z-z_0} < \delta$.
:::

::: {.solution}
Let $\Delta=\theset{\abs{z-z_0}<\delta}$ and $\gamma=\bd\Delta$, oriented anticlockwise.

::: pf

::: {.pf-step #choose-delta}
There is $\delta>0$ with $\overline\Delta\subset D$ such that $z_0$ is the only zero of $f-w_0$ in $\overline\Delta$ and the only zero of $f'$ in $\overline\Delta$.

::: pf-proof
Since $f-w_0$ has a zero of finite order at $z_0$, it is not identically zero, so its zeros are isolated. Write $f(z)-w_0=(z-z_0)^mg(z)$ with $g(z_0)\neq0$; then $f'(z)=(z-z_0)^{m-1}h(z)$ with $h=mg+(z-z_0)g'$ and $h(z_0)=mg(z_0)\ne0$. By continuity $g$ and $h$ have no zero on a small closed disk about $z_0$.
:::

:::

::: {.pf-step #count}
With $\eps\definedas\min_{z\in\gamma}\abs{f(z)-w_0}>0$, the number $N(w)$ of zeros of $f-w$ in $\Delta$, counted with multiplicity, equals $m$ for every $w$ with $\abs{w-w_0}<\eps$.

::: pf-proof
For such $w$, $f-w$ has no zero on $\gamma$, so by the argument principle
$$
N(w)=\frac{1}{2\pi i}\oint_\gamma\frac{f'(z)}{f(z)-w}\,dz.
$$
The integrand depends continuously on $w$, uniformly for $z\in\gamma$, so $N$ is a continuous integer-valued function on the connected disk $\abs{w-w_0}<\eps$, hence constant, and $N(w_0)=m$ by step [](#choose-delta){.pf-ref}.
:::

:::

::: pf-step
For $0<\abs{w-w_0}<\eps$ these $m$ zeros are distinct.

::: pf-proof
A zero $z$ of $f-w$ in $\Delta$ is not $z_0$, since $f(z_0)=w_0\ne w$. By step [](#choose-delta){.pf-ref}, $f'(z)\ne0$, so $z$ is a simple zero. Hence the $m$ zeros of step [](#count){.pf-ref} are $m$ distinct points.
:::

:::

:::
:::

::: {.remark title="Alternative count by Rouché's theorem"}
Step [](#count){.pf-ref} also follows from Rouché's theorem. On $\abs{z-z_0}=\delta$, $\abs{w-w_0}<\eps\le\abs{f(z)-w_0}$, so $f-w=(f-w_0)-(w-w_0)$ has as many zeros in $\Delta$ as $f-w_0$, namely $m$.
:::
