---
schema: qual/card@1
id: E-WIANB
kind: problem
title: Bounded holomorphic functions form a Banach space
classification:
  areas:
  - complex-analysis
  topics:
  - Function Spaces
  - Uniform Convergence
  - Morera
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source names the space A(C) while defining it on Omega, and leaves the norm implicit; the statement writes A(Omega) with the supremum norm. The source's hint is moved to a hint block.
---

::: {.exercise}
For an open set $\Omega\subseteq\CC$, show that $A(\Omega)\definedas \theset{f: \Omega \to \CC \st f\text{ is holomorphic, bounded}}$ with the norm $\norm{f}_\infty = \sup_{z\in\Omega}\abs{f(z)}$ is a Banach space.
:::

::: {.hint}
Apply Morera's theorem and Cauchy's theorem.
:::

::: {.solution}
Let $(f_n)$ be a Cauchy sequence in $A(\Omega)$.

::: pf

::: {.pf-step #uniform}
There is a function $f:\Omega\to\CC$ with $f_n\to f$ uniformly on $\Omega$.

::: pf-proof
For each $z\in\Omega$, $\abs{f_n(z)-f_m(z)}\le\norm{f_n-f_m}_\infty$, so $(f_n(z))$ is Cauchy in $\CC$; let $f(z)$ be its limit.
Given $\varepsilon>0$, choose $N$ with $\norm{f_n-f_m}_\infty<\varepsilon$ for $m,n\ge N$; letting $m\to\infty$ gives $\abs{f_n(z)-f(z)}\le\varepsilon$ for all $z\in\Omega$ and $n\ge N$.
:::

:::

::: {.pf-step #bounded}
$f$ is bounded.

::: pf-proof
By step [](#uniform){.pf-ref} choose $N$ with $\sup_\Omega\abs{f-f_N}\le1$; then $\sup_\Omega\abs f\le1+\norm{f_N}_\infty$.
:::

:::

::: {.pf-step #holomorphic}
$f$ is holomorphic.

::: pf-proof
$f$ is continuous as a uniform limit of continuous functions.
For a closed triangle $\Delta$ contained in a disk in $\Omega$, Cauchy's theorem gives $\int_{\partial\Delta}f_n\dz = 0$, and uniform convergence gives $\int_{\partial\Delta}f\dz = \lim_n\int_{\partial\Delta}f_n\dz = 0$.
Morera's theorem on each such disk shows that $f$ is holomorphic.
:::

:::

::: pf-step
$A(\Omega)$ is complete.

::: pf-proof
By steps [](#bounded){.pf-ref} and [](#holomorphic){.pf-ref}, $f\in A(\Omega)$, and by step [](#uniform){.pf-ref}, $\norm{f_n-f}_\infty\to0$.
:::

:::

:::

:::
