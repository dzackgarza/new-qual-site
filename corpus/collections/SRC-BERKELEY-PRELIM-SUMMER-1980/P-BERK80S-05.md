---
schema: qual/card@1
id: P-BERK80S-05
kind: problem
title: Boundedness of a nonlinear planar system
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 5 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the OCR-split constant in $\log(20+x)$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified positive-quadrant invariance, the scalar damped equation, coercivity of the potential, and the energy estimate bounding both variables.
---

::: {.problem}
Consider the differential equations

$$
\frac{dx}{dt}=-x+y,\qquad \frac{dy}{dt}=\log(20+x)-y.
$$

Let $x(t)$ and $y(t)$ be a solution defined for all $t\ge0$ with $x(0)>0$ and $y(0)>0$.
Prove that $x(t)$ and $y(t)$ are bounded.
:::

::: {.solution}
Set
\[
U(x)=\frac{x^2}{2}-(x+20)\log(x+20)+(x+20),
\qquad x>-20.
\]
Then
\[
U'(x)=x-\log(20+x).
\]
We will show that the solution stays in the first quadrant and that
\[
E(t)=\frac12(x'(t))^2+U(x(t))
\]
is nonincreasing.

<1>1. One has $x(t)>0$ and $y(t)>0$ for every $t\ge0$.
::: {.proof}
As long as $x,y>0$, variation of constants gives
\[
x(t)=e^{-t}\left(x(0)+\int_0^t e^s y(s)\,ds\right)
\]
and
\[
y(t)=e^{-t}\left(y(0)+\int_0^t e^s\log(20+x(s))\,ds\right).
\]
If $x(s)>0$, then $\log(20+x(s))>0$.
Hence, on any interval on which both variables are positive, the two displayed formulas actually show that both remain strictly positive.

If there were a first time at which either variable reached $0$, these formulas evaluated at that time would still give a strictly positive value, a contradiction.
Thus the solution remains in the first quadrant.
:::

<1>2. The $x$-component satisfies a damped scalar equation with decreasing energy.
::: {.proof}
From
\[
x'=-x+y
\]
we have
\[
y=x'+x.
\]
Differentiating and using the second equation gives
\[
x''+x'=y'=\log(20+x)-y
=\log(20+x)-x'-x.
\]
Therefore
\[
x''+2x'+x-\log(20+x)=0,
\]
or equivalently
\[
x''+2x'+U'(x)=0.
\]
Multiplying by $x'$ yields
\[
\frac{d}{dt}\left(\frac12(x')^2+U(x)\right)=-2(x')^2\le0.
\]
Hence
\[
E(t)\le E(0)
\qquad (t\ge0).
\]
:::

<1>3. The energy bound forces $x$ and $y$ to be bounded.
::: {.proof}
On $[0,\infty)$,
\[
U(x)=\frac{x^2}{2}-(x+20)\log(x+20)+(x+20)
\longrightarrow +\infty
\]
as $x\to\infty$, because the quadratic term dominates the $x\log x$ term.
Thus the sublevel set
\[
\{x\ge0:U(x)\le E(0)\}
\]
is bounded.
Since $x(t)\ge0$ by <1>1 and $U(x(t))\le E(t)\le E(0)$, the function $x(t)$ is bounded.

Let
\[
m=\min_{x\ge0}U(x),
\]
which is finite because $U$ is continuous and coercive on $[0,\infty)$.
Then
\[
\frac12(x'(t))^2
=E(t)-U(x(t))
\le E(0)-m,
\]
so $x'(t)$ is bounded as well.
Finally,
\[
y(t)=x'(t)+x(t),
\]
so $y(t)$ is bounded.
Therefore both $x(t)$ and $y(t)$ remain bounded for all $t\ge0$.
:::
:::
