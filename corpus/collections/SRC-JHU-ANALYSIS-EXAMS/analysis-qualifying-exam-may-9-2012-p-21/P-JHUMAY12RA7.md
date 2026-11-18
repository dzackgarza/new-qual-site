---
schema: qual/card@1
id: P-JHUMAY12RA7
kind: problem
title: Integral transform is absolutely continuous and vanishes at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 9, 2012, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same two parts, with the two identities separated: h is the
    difference of the indefinite integral at x+1 and at x, and a difference of absolutely continuous
    functions is absolutely continuous, which is now argued from the definition by halving epsilon rather
    than asserted. The vanishing at infinity is the tail bound, and the tail of an integrable function
    tends to zero. No published solution located; the card keeps its own argument and says so.
---

::: {.problem}
Let $f\in L^1(\RR)$ and define
$$
h(x)=\int_x^{x+1}f(t)\,dt.
$$

(a) Prove that $h$ is absolutely continuous.

(b) Prove that $h(x)\to0$ as $x\to\infty$.
:::

::: {.solution}

No published solution was located for this examination problem; the argument is the card's own, and it rests on the fundamental theorem of calculus for the Lebesgue integral: for $f\in L^{1}(\RR)$ the indefinite integral is absolutely continuous, with derivative $f$ almost everywhere.

The statement was checked against Problem 7 of the JHU Analysis Qualifying Examination of 9 May 2012, as preserved in the collection holding this card. Throughout $f\in L^{1}(\RR)$ and $h(x)\coloneqq\int_{x}^{x+1}f(t)\,dt$.

::: pf

::: {.pf-step #a}

(a) $h$ is absolutely continuous.

:::: pf-proof

Write $h$ as a difference of indefinite integrals.

::: {.pf-step #indefinite-integral}

$F(x)\coloneqq\int_{0}^{x}f(t)\,dt$ is absolutely continuous with $F'=f$ almost everywhere.

::: pf-proof

This is the fundamental theorem of calculus for the Lebesgue integral, applied to $f\in L^{1}(\RR)$; for $x<0$ the integral is taken with the usual sign convention, $F(x)=-\int_{x}^{0}f$.

:::

:::

::: {.pf-step #difference-identity}

$h=F(\cdot+1)-F$.

::: pf-proof

$\int_{x}^{x+1}f=\int_{0}^{x+1}f-\int_{0}^{x}f=F(x+1)-F(x)$ by additivity of the integral over adjacent intervals.

:::

:::

::: pf-step

$h$ is absolutely continuous.

::: pf-proof

A difference of absolutely continuous functions is absolutely continuous: given $\varepsilon>0$ choose $\delta$ for $F$ so that finitely many disjoint intervals of total length below $\delta$ have total variation of $F$ below $\varepsilon/2$, and then the same $\delta$ bounds the total variation of $h$ by $\varepsilon$. Hence $h$ is absolutely continuous, and $h'=f(\cdot+1)-f$ almost everywhere by step [](#indefinite-integral){.pf-ref}.

:::

:::

::::

:::

::: {.pf-step #b}

(b) $h(x)\to0$ as $x\to\infty$.

::: pf-proof

For every $x$,
$$
\abs{h(x)}=\abs{\int_{x}^{x+1}f(t)\,dt}\leq\int_{x}^{x+1}\abs{f(t)}\,dt\leq\int_{x}^{\infty}\abs{f(t)}\,dt .
$$
Since $\abs{f}\in L^{1}(\RR)$, the tail integrals $\int_{x}^{\infty}\abs{f}$ tend to $0$ as $x\to\infty$, being the tails of a convergent integral; so $\abs{h(x)}\to0$, that is $h(x)\to0$.

:::

:::

::: pf-step

Both assertions hold.

::: pf-proof

Part [](#a){.pf-ref} gives the absolute continuity of $h$ and part [](#b){.pf-ref} its vanishing at infinity; those are (a) and (b).

:::

:::

:::

:::
