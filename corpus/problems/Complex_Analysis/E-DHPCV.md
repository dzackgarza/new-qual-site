---
schema: qual/card@1
id: E-DHPCV
kind: problem
title: $\|f\|_{(\infty,s)}\le c\|f\|_{(1,r)}$ for holomorphic $f$
classification:
  areas:
  - complex-analysis
  topics:
  - Mean Value Property
  - Cauchy Estimates
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $f$ be holomorphic in a neighborhood of $\overline{D_r(z_0)}$. Show that for any $s < r$, there exists a constant $c > 0$ such that
$$
\norm{f}_{(\infty, s)} \leq c \norm{f}_{(1, r)},
$$
where
$\displaystyle \norm{f}_{(\infty, s)} = \sup_{z \in D_s(z_0)}\abs{f(z)}$
and $\displaystyle \norm{f}_{(1, r)} = \iint_{D_r(z_0)} \abs{f(z)}\,dx\,dy$.
:::

::: {.solution}
Put $\delta=r-s>0$.

::: pf

::: {.pf-step #area-mean}
For every $z\in D_s(z_0)$,
$$
f(z)=\frac1{\pi\delta^2}\iint_{D_\delta(z)}f(w)\,dA(w).
$$

::: pf-proof
Since $\abs{z-z_0}<s$, the closed disk $\overline{D_\delta(z)}$ is contained in $D_r(z_0)$, where $f$ is holomorphic.
For every $0<\rho<\delta$, the mean value property gives
$$
f(z)=\frac1{2\pi}\int_0^{2\pi}f(z+\rho e^{i\theta})\,d\theta.
$$
Multiplying by $2\rho$, integrating over $\rho\in(0,\delta)$, and using polar coordinates about $z$ gives
$$
\delta^2 f(z)=\frac1\pi\iint_{D_\delta(z)}f(w)\,dA(w).
$$
:::

:::

::: {.pf-step #pointwise}
For every $z\in D_s(z_0)$,
$$
\abs{f(z)}\le\frac1{\pi(r-s)^2}\norm{f}_{(1,r)}.
$$

::: pf-proof
By step [](#area-mean){.pf-ref} and $D_\delta(z)\subseteq D_r(z_0)$,
$$
\abs{f(z)}
\le\frac1{\pi\delta^2}\iint_{D_\delta(z)}\abs{f(w)}\,dA(w)
\le\frac1{\pi\delta^2}\norm{f}_{(1,r)}.
$$
:::

:::

::: pf-step
The inequality holds with $\boxed{c=\frac1{\pi(r-s)^2}}$.

::: pf-proof
Take the supremum over $z\in D_s(z_0)$ in step [](#pointwise){.pf-ref}.
:::

:::

:::

:::
