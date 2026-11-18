---
schema: qual/card@1
id: P-JHUSP05ANB
kind: problem
title: 'The integral operator $g(x)=\int_x^1 f(t)/t\,dt$ on $L^1([0,1])$'
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
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Analysis Qualifying Exam, Spring 2005, in the preserved exam collection.
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
    Restructured as a Lamport proof of the same argument, with the order of the two theorems made
    explicit: Tonelli on the nonnegative integrand first, which gives integrability over the triangle,
    then Fubini for the signed integrand. The computation of the inner integral is written out (the
    x-integral of 1/t over [0,t] is 1) and the value at t = 0 is noted to be immaterial. The estimate
    of the L^1 norm of g is separated from the identity of the integrals. No published solution located;
    the card keeps its own argument and says so.
---

::: {.problem}
Suppose that $f\in L^1([0,1])$ and define
$$
g(x)=\int_x^1\frac{f(t)}{t}\,dt.
$$
Show that $g\in L^1([0,1])$ and that
$$
\int_0^1 g(x)\,dx=\int_0^1 f(x)\,dx.
$$
:::

::: {.solution}

No published solution was located for this examination problem; the argument is the card's own, and its one point of care is that the application of Tonelli precedes that of Fubini, since $f$ has no sign.

The statement was checked against Problem 3 of the JHU analysis qualifying examination of Spring 2005, as preserved in the collection holding this card. Throughout $f\in L^{1}([0,1])$ and $g(x)\coloneqq\int_{x}^{1}f(t)/t\,dt$.

::: pf

::: {.pf-step #tonelli}

$\int_{0}^{1}\int_{x}^{1}\frac{\abs{f(t)}}{t}\,dt\,dx=\int_{0}^{1}\abs{f(t)}\,dt$.

::: pf-proof

The integrand $\abs{f(t)}/t$ is nonnegative and measurable on the triangle $\theset{0\leq x\leq t\leq1}$, so Tonelli's theorem applies and the two iterated integrals are equal, both being the integral over the triangle:
$$
\int_{0}^{1}\int_{x}^{1}\frac{\abs{f(t)}}{t}\,dt\,dx=\int_{0}^{1}\int_{0}^{t}\frac{\abs{f(t)}}{t}\,dx\,dt=\int_{0}^{1}\frac{\abs{f(t)}}{t}\cdot t\,dt=\int_{0}^{1}\abs{f(t)}\,dt .
$$
The value at $t=0$ is immaterial, a single point having measure zero.

:::

:::

::: {.pf-step #g-integrable}

$g(x)$ is defined for almost every $x$, and $\norm{g}_{1}\leq\norm{f}_{1}$.

::: pf-proof

By step [](#tonelli){.pf-ref} the nonnegative function $(x,t)\mapsto\abs{f(t)}/t$ is integrable over the triangle, so for almost every $x$ the function $t\mapsto\abs{f(t)}/t$ is integrable on $[x,1]$; for those $x$ the integral defining $g(x)$ converges absolutely. Moreover
$$
\int_{0}^{1}\abs{g(x)}\,dx\leq\int_{0}^{1}\int_{x}^{1}\frac{\abs{f(t)}}{t}\,dt\,dx=\norm{f}_{1},
$$
the inequality by the triangle inequality for the integral. So $g\in L^{1}([0,1])$.

:::

:::

::: {.pf-step #fubini}

$\int_{0}^{1}g(x)\,dx=\int_{0}^{1}f(x)\,dx$.

::: pf-proof

The signed integrand $(x,t)\mapsto f(t)/t$ is absolutely integrable over the triangle by step [](#tonelli){.pf-ref}, so Fubini's theorem applies to it and the iterated integrals may be exchanged:
$$
\int_{0}^{1}g(x)\,dx=\int_{0}^{1}\int_{x}^{1}\frac{f(t)}{t}\,dt\,dx=\int_{0}^{1}\int_{0}^{t}\frac{f(t)}{t}\,dx\,dt=\int_{0}^{1}f(t)\,dt .
$$

:::

:::

::: pf-step

Both claims of the problem hold.

::: pf-proof

Step [](#g-integrable){.pf-ref} is $g\in L^{1}([0,1])$ and step [](#fubini){.pf-ref} the identity of the integrals.

:::

:::

:::

:::
