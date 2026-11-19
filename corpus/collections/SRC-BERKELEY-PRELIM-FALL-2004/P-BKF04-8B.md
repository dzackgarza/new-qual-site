---
schema: qual/card@1
id: P-BKF04-8B
kind: problem
title: Positivity of $\lambda$ for $y''+\lambda a y=0$ with $y(0)=0$, $y'(1)=0$, and $a>0$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Transcribed from the retained solution sheet — Berkeley preliminary examination, Fall 2004,
    solutions, assets/attachments/f04solution.pdf, Problem 8B on PDF p. 8 — and restructured
    into steps; the card's prose was that sheet's argument. Added: the continuity hypothesis
    that licenses integrating the product equation term by term, the two boundary evaluations
    separately, and the reason the two integrals are strictly positive — the minimum of the
    positive continuous weight a, and the interval on which a continuous nonzero y is bounded
    away from zero. The integration-by-parts identity had a stray `\evalfrom` in the card, now
    written as the bracket $[yy']_0^1$.
---

::: {.problem}
A $C^2$ function $y(x)$ for $0\leq x\leq1$, a positive continuous function $a(x)$ for $0\leq x\leq1$ and a real number $\lambda$ satisfy

$$
\begin{aligned}
&y''(x)+\lambda a(x)y(x)=0,\\
&y(0)=0,\\
&y'(1)=0.
\end{aligned}
$$

Suppose that $y(x)$ is not identically zero. Prove that $\lambda>0$.
:::

::: {.solution}
The argument is the retained solution sheet's: **Berkeley preliminary examination, Fall 2004, solutions** (`assets/attachments/f04solution.pdf`), Problem 8B, PDF p. 8. Throughout $y \in C^{2}[0,1]$ is not identically zero, $a$ is continuous and positive on $[0,1]$, $\lambda \in \RR$, and $y'' + \lambda a y = 0$ with $y(0) = 0$ and $y'(1) = 0$.

::: pf

::: {.pf-step #multiply}
$\lambda\int_{0}^{1}a(x)y(x)^{2}\,dx = -\int_{0}^{1}y(x)y''(x)\,dx$.

::: pf-proof
Multiply the differential equation by $y$: $y y'' + \lambda a y^{2} = 0$, that is $\lambda a y^{2} = -yy''$. Both sides are continuous on $[0,1]$, so they may be integrated term by term there.

:::

:::

::: {.pf-step #parts}
$-\int_{0}^{1}y y''\,dx = -\bigl[y y'\bigr]_{0}^{1} + \int_{0}^{1}(y')^{2}\,dx$.

::: pf-proof
Integration by parts with $u = y$ and $dv = y''dx$: since $y \in C^{2}$, $u$ and $v = y'$ are continuously differentiable, so $\int u\\,dv = [uv] - \int v\\,du$ on $[0,1]$.

:::

:::

::: {.pf-step #boundary}
$\bigl[y y'\bigr]_{0}^{1} = 0$.

::: pf-proof
At the lower end $y(0) = 0$ makes $y(0)y'(0) = 0$; at the upper end $y'(1) = 0$ makes $y(1)y'(1) = 0$. The values $y'(0)$ and $y(1)$ are finite because $y \in C^{2}$.

:::

:::

::: {.pf-step #positive}
$\int_{0}^{1}(y')^{2}\,dx > 0$.

::: pf-proof
The integrand is continuous and nonnegative, so the integral is $\ge 0$; it is $0$ only if $(y')^{2} \equiv 0$, i.e. $y' \equiv 0$ on $[0,1]$. Then $y$ is constant on the connected set $[0,1]$, and $y(0) = 0$ would give $y \equiv 0$, contradicting the hypothesis. So the integral is strictly positive.

:::

:::

::: {.pf-step #weight}
$\int_{0}^{1}a(x)y(x)^{2}\,dx > 0$.

::: pf-proof
$a$ is continuous and positive on the compact $[0,1]$, so it attains a minimum $m > 0$ there, and $\int a y^{2} \ge m\int y^{2}$. The function $y$ is continuous and not identically zero, so there is $x_{0}$ with $y(x_{0}) \ne 0$, and by continuity $y^{2} \ge \abs{y(x_{0})}^{2}/2$ on some interval of positive length about $x_{0}$; hence $\int y^{2} > 0$ and the weighted integral is positive as well.

:::

:::

::: pf-step
$\lambda = \frac{\int_{0}^{1}(y')^{2}dx}{\int_{0}^{1}a(x)y(x)^{2}dx} > 0$.

::: pf-proof
Steps [](#multiply){.pf-ref}, [](#parts){.pf-ref} and [](#boundary){.pf-ref} give $\lambda\int a y^{2} = \int (y')^{2}$, and the denominators are nonzero by steps [](#weight){.pf-ref} and [](#positive){.pf-ref}, so the quotient is defined and is a ratio of two positive numbers, hence positive.

:::

:::

:::
:::
