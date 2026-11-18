---
schema: qual/card@1
id: P-JHUSP01RAB
kind: problem
title: "Absolute continuity of the Lebesgue integral"
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Real Analysis Qualifying Exam, Spring 2001, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^1(\RR^n)$. Prove that for every $\varepsilon>0$ there exists $\delta>0$ such that if $A$ is measurable and $\setmeasure{A}<\delta$, then
$$
\abs{\int_A f}<\varepsilon.
$$
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the compilation `assets/attachments/JHU Years of Analysis Exams.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. It uses the dominated convergence theorem once, to get the tail bound at a level $M$, and otherwise only monotonicity of the integral and the triangle inequality for integrals.

Throughout, $\mu$ is Lebesgue measure on $\RR^{n}$, $f\in L^{1}(\RR^{n})$, and $\theset{\abs{f}>M}\coloneqq\theset{x\in\RR^{n}\mid\abs{f(x)}>M}$.

::: pf

::: {.pf-step #tail}
For every $\eta>0$ there is $M>0$ with $\int_{\theset{\abs{f}>M}}\abs{f}<\eta$.

::: pf-proof
For $k\geq1$ the functions $g_{k}\coloneqq\abs{f}\chi_{\theset{\abs{f}>k}}$ satisfy $\abs{g_{k}}\leq\abs{f}$ with $\abs{f}$ integrable, and $g_{k}(x)\to0$ as $k\to\infty$ at every $x$, since $\abs{f(x)}$ is a finite number and eventually exceeds no $k$. By the dominated convergence theorem $\int g_{k}\to0$; so for the given $\eta$ some $k$ has $\int_{\theset{\abs{f}>k}}\abs{f}<\eta$, and $M\coloneqq k$ works.
:::

:::

::: {.pf-step #bound}
Let $\varepsilon>0$, choose $M>0$ with $\int_{\theset{\abs{f}>M}}\abs{f}<\varepsilon/2$ by step [](#tail){.pf-ref}, and put $\delta\coloneqq\varepsilon/(2M)>0$. Then for every measurable $A$ with $\mu(A)<\delta$,
$$
\abs{\int_{A}f}<\varepsilon.
$$

:::: pf-proof

::: {.pf-step #split}
$\int_{A}\abs{f}\leq M\mu(A)+\int_{\theset{\abs{f}>M}}\abs{f}$.

::: pf-proof
$A$ is the disjoint union of $A\cap\theset{\abs{f}\leq M}$ and $A\cap\theset{\abs{f}>M}$, so by additivity and monotonicity of the integral
$$
\int_{A}\abs{f}=\int_{A\cap\theset{\abs{f}\leq M}}\abs{f}+\int_{A\cap\theset{\abs{f}>M}}\abs{f}\leq M\mu\big(A\cap\theset{\abs{f}\leq M}\big)+\int_{\theset{\abs{f}>M}}\abs{f},
$$
the first term bounded by $M\mu(A)$ because $\abs{f}\leq M$ on that set, and the second by monotonicity because $A\cap\theset{\abs{f}>M}\subset\theset{\abs{f}>M}$ and the integrand is nonnegative.
:::

:::

::: {.pf-step #estimate}
$\abs{\int_{A}f}\leq\int_{A}\abs{f}<M\delta+\varepsilon/2\leq\varepsilon$.

::: pf-proof
$\abs{\int_{A}f}\leq\int_{A}\abs{f}$ is the triangle inequality for the integral; step [](#split){.pf-ref} bounds $\int_{A}\abs{f}$ by $M\mu(A)+\int_{\theset{\abs{f}>M}}\abs{f}$, which is less than $M\delta+\varepsilon/2$ because $\mu(A)<\delta$ and the tail is below $\varepsilon/2$. With $\delta=\varepsilon/(2M)$ this gives $M\delta=\varepsilon/2$, so the sum is $\varepsilon/2+\varepsilon/2=\varepsilon$; the estimate is strict throughout, hence $\abs{\int_{A}f}<\varepsilon$.
:::

:::

::::

:::

::: pf-step
Therefore for every $\varepsilon>0$ there is $\delta>0$ such that every measurable $A$ with $\mu(A)<\delta$ satisfies $\abs{\int_{A}f}<\varepsilon$.

::: pf-proof
Given $\varepsilon>0$, step [](#bound){.pf-ref} produces $\delta>0$ with the required property: it chooses $M$ from step [](#tail){.pf-ref} at the level $\varepsilon/2$, sets $\delta=\varepsilon/(2M)$, and proves the conclusion for every measurable $A$ of measure below $\delta$. This is the statement that the Lebesgue integral of $f$ is absolutely continuous with respect to $\mu$.
:::

:::

:::

:::
