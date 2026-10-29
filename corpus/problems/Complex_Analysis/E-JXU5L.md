---
schema: qual/card@1
id: E-JXU5L
kind: problem
title: The Dirichlet function is nowhere continuous and not Riemann integrable
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Integrability
  - Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source leaves the interval I undeclared; the statement takes I=[0,1], the interval the solution uses.
---

::: {.problem}
Let $I=[0,1]$. Show that the Dirichlet function $f(x) = \chi_{I \intersect \QQ}$ on $I$ is not Riemann integrable and is everywhere discontinuous.
:::

::: {.solution}
::: pf

::: {.pf-step #oscillation}
Every open interval $J$ meeting $I$ in more than one point contains points $y,z\in I$ with $f(y)=1$ and $f(z)=0$.

::: pf-proof
$J\cap I$ is a nondegenerate interval, and $\QQ$ and $\RR\setminus\QQ$ are both dense in $\RR$.
:::

:::

::: pf-step
$f$ is not Riemann integrable on $I$.

::: pf-proof
By step [](#oscillation){.pf-ref}, on every subinterval of a partition $P$ of $I$ we have $\sup f=1$ and $\inf f=0$, so $U(f,P)=1$ and $L(f,P)=0$. The upper and lower Darboux integrals are $1\neq0$.
:::

:::

::: pf-step
$f$ is discontinuous at every $x\in I$.

::: pf-proof
For every $\delta>0$, step [](#oscillation){.pf-ref} applied to $(x-\delta,x+\delta)$ gives $y,z$ within $\delta$ of $x$ with $\abs{f(y)-f(z)}=1$, so $\abs{f(y)-f(x)}\ge\frac12$ or $\abs{f(z)-f(x)}\ge\frac12$. Continuity at $x$ fails for $\varepsilon=\frac12$.
:::

:::

:::

:::
