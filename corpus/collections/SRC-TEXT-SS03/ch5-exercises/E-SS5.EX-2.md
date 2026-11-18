---
schema: qual/card@1
id: E-SS5.EX-2
kind: problem
title: Orders of growth of $p(z)$, $e^{bz^n}$ and $e^{e^z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 5 growth-order convention.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the definition of order, the polynomial case, the two
    bounds for $e^{bz^{n}}$, and the real-axis growth of $e^{e^{z}}$. No retained solution set covers this
    exercise (the collection retains the textbook, not a solutions manual), so the argument is the card's
    own; each bound was re-read for this pass.
---

::: {.exercise}
Find the order of growth of the following entire functions:

(a) $p(z)$ where $p$ is a polynomial.

(b) $e^{bz^n}$ for $b \neq 0$.

(c) $e^{e^z}$.
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. The order of an entire function $f$ is the infimum of the positive $\rho$ for which $\abs{f(z)}\le Ae^{B\abs{z}^{\rho}}$ holds for all $z$ with suitable positive constants $A,B$.

::: pf

::: {.pf-step #polynomial}
(a) A polynomial has order $0$.

::: pf-proof
If $p$ has degree $m$ then $\abs{p(z)}\le C(1+\abs{z})^{m}$ for a suitable $C$. For any $\rho>0$ and all $z$, $\abs{z}^{m}\le C_{\rho}e^{\abs{z}^{\rho}}$: for large $\abs{z}$ the exponential dominates every power, and on a compact set both sides are bounded below away from $0$ by positive constants. Hence $\abs{p(z)}\le A e^{\abs{z}^{\rho}}$ for every $\rho>0$, so the infimum of admissible $\rho$ is $0$.
:::

:::

::: {.pf-step #exponential}
(b) $e^{bz^{n}}$ with $b\ne0$ has order exactly $n$.

::: pf-proof
Upper bound and lower bound.

::: {.pf-step #upper}
$\abs{e^{bz^{n}}}\le e^{\abs{b}\abs{z}^{n}}$, so the order is at most $n$.

::: pf-proof
$\abs{e^{bz^{n}}}=e^{\Re(bz^{n})}\le e^{\abs{bz^{n}}}=e^{\abs{b}\abs{z}^{n}}$ by the inequality $\Re w\le\abs{w}$.
:::

:::

::: {.pf-step #lower}
No $\rho<n$ is admissible.

::: pf-proof
Choose $\theta$ with $be^{in\theta}=\abs{b}$, which is possible because $e^{in\theta}$ sweeps the unit circle. Along the ray $z=re^{i\theta}$ one has $bz^{n}=\abs{b}r^{n}$, so $\abs{e^{bz^{n}}}=e^{\abs{b}r^{n}}$. A bound $Ae^{Br^{\rho}}$ with $\rho<n$ would give $e^{\abs{b}r^{n}}\le Ae^{Br^{\rho}}$, that is $\abs{b}r^{n}\le\log A+Br^{\rho}$ for all large $r$, which fails as $r\to\infty$ because the left side grows faster than the right when $\rho<n$.
:::

:::

:::

:::

::: {.pf-step}
(c) $e^{e^{z}}$ has infinite order.

::: pf-proof
Along the positive real axis, $\abs{e^{e^{x}}}=e^{e^{x}}$. If the order were a finite $\rho$ with constants $A,B$, then $e^{e^{x}}\le Ae^{Bx^{\rho}}$ for all large $x$, that is $e^{x}\le\log A+Bx^{\rho}$, which is impossible since the exponential of $x$ grows faster than any polynomial. So no finite $\rho$ is admissible and the order is infinite, which completes the three answers.
:::

:::

:::
:::
