---
schema: qual/card@1
id: P-UCI13H3-3
kind: problem
title: A bound $\abs{f^{(n)}(z)}\le\abs z^{-n}$ makes the origin removable
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $f$ be analytic in the punctured unit disk $U_0=\{0<\abs z<1\}$, and suppose there is a positive integer $n$ with $\abs{f^{(n)}(z)}\le\abs z^{-n}$ for all $z\in U_0$.
Show that $z=0$ is a removable singularity of $f$.
:::

::: {.solution}
The hypothesis says that the function $h(z)=z^nf^{(n)}(z)$ is bounded on the punctured disc $U_0$, since $\abs{h(z)}=\abs z^n\abs{f^{(n)}(z)}\le1$.

::: pf

::: {.pf-step #h-removable}
$h$ extends to an analytic function on the unit disc.

::: pf-proof
A function analytic on a punctured disc and bounded there has a removable singularity at the puncture, by Riemann's theorem on removable singularities.
:::

:::

::: {.pf-step #not-pole-not-essential}
$f$ has neither a pole nor an essential singularity at $0$.

::: pf-proof
If $f$ had a pole of order $m\ge1$ at $0$, then $f^{(n)}$ would have a pole of order $m+n$ there, so $\abs{f^{(n)}(z)}\ge C\abs z^{-(m+n)}$ for small $z\ne0$ and some $C>0$, and $\abs{h(z)}\ge C\abs z^{-m}\to\infty$, contradicting step [](#h-removable){.pf-ref}.
If $f$ had an essential singularity at $0$, its Laurent expansion $f=\sum_{k<0}a_kz^k$ would have infinitely many nonzero negative coefficients; differentiating $n$ times multiplies $a_kz^k$ by the nonzero constant $k(k-1)\cdots(k-n+1)$ and lowers the exponent by $n$, so $h=\sum_{k<0}c_ka_kz^k$ would again have infinitely many nonzero negative coefficients.
Then $h$ would have an essential singularity at $0$, which step [](#h-removable){.pf-ref} excludes.
:::

:::

::: {.pf-step #removable}
$z=0$ is a removable singularity of $f$.

::: pf-proof
An isolated singularity that is neither a pole nor an essential singularity is removable.
:::

:::

:::

:::
