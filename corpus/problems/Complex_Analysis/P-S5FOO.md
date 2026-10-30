---
schema: qual/card@1
id: P-S5FOO
kind: problem
title: The sup norm of a holomorphic function on $D_s(z_0)$ is bounded by its $L^1$
  norm on $D_r(z_0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Norms
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The card printed only the two norm definitions and posed no question. The statement now asks for the estimate the solution proves: for f holomorphic on D_r(z_0) and 0<s<r, the sup norm on D_s(z_0) is at most 1/(pi (r-s)^2) times the L^1 norm on D_r(z_0).'
---

::: {.problem}
For $f$ holomorphic on a disc $D_r(z_0)$ and $0<s<r$, let
$\displaystyle \norm{f}_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}\abs{f(z)}$ and $\displaystyle \norm{f}_{(1, r)} = \int_{D_r(z_0)} \abs{f(z)}dx dy$.
Prove that
$$
\norm{f}_{(\infty, s)} \le \frac{1}{\pi (r-s)^2}\, \norm{f}_{(1, r)}.
$$
:::

::: {.solution}
Fix $w\in D_s(z_0)$ and set $\rho\coloneqq r-s>0$.

::: pf

::: {.pf-step #contained}

$D_\rho(w)\subseteq D_r(z_0)$.

::: pf-proof

For $\zeta\in D_\rho(w)$, $\abs{\zeta-z_0}\le\abs{\zeta-w}+\abs{w-z_0}<\rho+s=r$.

:::

:::

::: {.pf-step #area-mean}

$\displaystyle f(w)=\frac1{\pi\rho^2}\iint_{D_\rho(w)}f(z)\,dx\,dy$.

::: pf-proof

For $0<t<\rho$, the closed disc $\overline D_t(w)$ lies in $D_r(z_0)$ by step [](#contained){.pf-ref}, so the mean value property gives $f(w)=\frac1{2\pi}\int_0^{2\pi}f(w+te^{i\theta})\,d\theta$. Multiply by $t$ and integrate over $0<t<\rho$; in polar coordinates about $w$,
$$
\frac{\rho^2}2f(w)=\frac1{2\pi}\int_0^\rho\int_0^{2\pi}f(w+te^{i\theta})\,t\,d\theta\,dt=\frac1{2\pi}\iint_{D_\rho(w)}f(z)\,dx\,dy.
$$

:::

:::

::: pf-step

$\norm{f}_{(\infty,s)}\le\dfrac1{\pi(r-s)^2}\norm{f}_{(1,r)}$.

::: pf-proof

By steps [](#area-mean){.pf-ref} and [](#contained){.pf-ref}, since $\abs f\ge0$,
$$
\abs{f(w)}\le\frac1{\pi\rho^2}\iint_{D_\rho(w)}\abs{f(z)}\,dx\,dy\le\frac1{\pi(r-s)^2}\norm{f}_{(1,r)}.
$$
Take the supremum over $w\in D_s(z_0)$.

:::

:::

:::

:::
