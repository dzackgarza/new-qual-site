---
schema: qual/card@1
id: P-PGDPX
kind: problem
title: Integral equals integral of distribution function
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved JHU Fall 2013 Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the layer-cake identity at a
    point, the measurability of the indicator as the preimage of an open set under the measurable
    function |f(x)| - alpha, and the use of Tonelli, which needs nonnegativity and measurability
    and nothing about integrability of the inner integral. The prose's equality
    {alpha < |f(x)|} = {|f(x)| > alpha} is kept. Added that both sides are then finite because
    f is in L^1. Statement unchanged; the card says the argument is its own.
---

::: {.problem}
Let $f \in L^1(\RR)$ and define $E_\alpha = \{x : \abs{f(x)} > \alpha\}$.
Prove that

$$\int_{\RR} \abs{f(x)} \, dx = \int_0^\infty m(E_\alpha) \, d\alpha.$$
:::

::: {.solution}
Layer cake: $\abs{f(x)}$ is the measure of the set of levels $\alpha>0$ below it, and integrating that identity over $x$ and exchanging the order of integration — permitted by Tonelli, the integrand being a nonnegative measurable function of $(x,\alpha)$ — turns the integral of $\abs f$ into the integral over $\alpha$ of $m(E_\alpha)$. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #pointwise}
For every $x$, $\displaystyle\abs{f(x)}=\int_0^\infty\mathbf 1_{\{\alpha<\abs{f(x)}\}}\,\dd\alpha$.

::: pf-proof
For a fixed real $t\ge0$, the set of $\alpha>0$ with $\alpha<t$ is $(0,t)$, whose measure is $t$; and for $t=0$ it is empty, of measure $0$. Since $t\mapsto\mathbf 1_{\{\alpha<t\}}$ is the indicator of an interval, the integral equals $\abs{f(x)}$.
:::

:::


::: {.pf-step #measurable}
The function $(x,\alpha)\mapsto\mathbf 1_{\{\alpha<\abs{f(x)}\}}$ is nonnegative and measurable on $\RR\times(0,\infty)$.

::: pf-proof
$\{(x,\alpha):\alpha<\abs{f(x)}\}$ is the set where the measurable function $(x,\alpha)\mapsto\abs{f(x)}-\alpha$ is positive, since $\alpha\mapsto\alpha$ is continuous and hence Borel measurable on the product $\sigma$-algebra, and $\abs f$ is measurable as $f\in L^1$ is measurable. Being the preimage of an open set, it is measurable; its indicator is a nonnegative measurable function.
:::

:::


::: {.pf-step #tonelli}
$\displaystyle\int_\RR\abs{f(x)}\,\dd x=\int_0^\infty\!\!\int_\RR\mathbf 1_{\{\abs{f(x)}>\alpha\}}\,\dd x\,\dd\alpha$.

::: pf-proof
By step [](#pointwise){.pf-ref}, $\int_\RR\abs f\,\dd x=\int_\RR\int_0^\infty\mathbf 1_{\{\alpha<\abs{f(x)}\}}\,\dd\alpha\,\dd x$. The integrand is nonnegative and measurable by step [](#measurable){.pf-ref}, so Tonelli's theorem permits the interchange of the two integrals and gives the displayed identity; the condition $\alpha<\abs{f(x)}$ is the same as $\abs{f(x)}>\alpha$.
:::

:::


::: {.pf-step #conclusion}
$\displaystyle\int_\RR\abs{f(x)}\,\dd x=\int_0^\infty m(E_\alpha)\,\dd\alpha$, where $E_\alpha=\{x:\abs{f(x)}>\alpha\}$.

::: pf-proof
By step [](#tonelli){.pf-ref} the inner integral $\int_\RR\mathbf 1_{\{\abs{f(x)}>\alpha\}}\dd x$ equals the Lebesgue measure of $\{x:\abs{f(x)}>\alpha\}=E_\alpha$, for each fixed $\alpha>0$. Substituting gives the identity; both sides are finite or both infinite, and the left side is finite here because $f\in L^1$, so the right-hand side defines an integrable function of $\alpha$.
:::

:::

:::
:::
