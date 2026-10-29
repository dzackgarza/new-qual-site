---
schema: qual/card@1
id: P-2UVDX
kind: problem
title: $e^{-\pi\xi^2}=\int_{-\infty}^\infty e^{-\pi x^2}e^{2\pi i x\xi}\,dx$ for all
  $\xi\in\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Entire Functions
  - Integrals
  - Identity Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source hint reads "You may use that fact in Example 1 on p. 42 of the textbook without proof, i.e., you may assume the above is true for real values of xi"; the statement keeps the permission and drops the reference to an unnamed textbook.'
---

::: {.problem}
Prove by *justifying all steps* that for all $\xi \in \CC$ we have $\displaystyle e^{- \pi \xi^2} = \int_{- \infty}^\infty e^{- \pi x^2} e^{2 \pi i x \xi} dx \; .$

You may assume without proof that the identity holds for real values of $\xi$.
:::

::: {.solution}

For $\xi\in\CC$, let $F(\xi)\coloneqq\int_{-\infty}^{\infty}e^{-\pi x^2}e^{2\pi i x\xi}\,dx$.

::: pf

::: {.pf-step #dominated}
For $V>0$ and $\abs{\Im\xi}\leq V$, $\abs{e^{-\pi x^2}e^{2\pi i x\xi}}\leq e^{-\pi x^2+2\pi V\abs{x}}$, which is integrable on $\RR$.

::: pf-proof
With $\xi=u+iv$, $\abs{e^{2\pi i x\xi}}=e^{-2\pi xv}\leq e^{2\pi V\abs{x}}$, and $e^{-\pi x^2+2\pi V\abs{x}}\leq e^{\pi V^2}e^{-\pi(\abs{x}-V)^2}$.
:::

:::

::: {.pf-step #entire}
$F$ is entire.

::: pf-proof
By step [](#dominated){.pf-ref}, $F$ is defined on $\CC$ and, by dominated convergence, continuous on each strip $\abs{\Im\xi}\leq V$.
For a closed triangle $T$ in such a strip, Fubini's theorem, justified by the same bound, gives $\oint_{\partial T}F(\xi)\,d\xi=\int_{-\infty}^\infty e^{-\pi x^2}\oint_{\partial T}e^{2\pi i x\xi}\,d\xi\,dx=0$, because $\xi\mapsto e^{2\pi i x\xi}$ is entire.
Morera's theorem then shows $F$ is holomorphic on every strip, hence on $\CC$.
:::

:::

::: pf-step
$F(\xi)=e^{-\pi\xi^2}$ for every $\xi\in\CC$.

::: pf-proof
Both sides are entire, by step [](#entire){.pf-ref}, and they agree on $\RR$ by the permitted real case.
Since $\RR$ has accumulation points in the connected set $\CC$, the identity theorem gives equality on $\CC$.
:::

:::

:::

:::
