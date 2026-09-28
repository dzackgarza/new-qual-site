---
schema: qual/card@1
id: P-BERK80S-20
kind: problem
title: Global solution of a scalar autonomous ODE
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
  note: Checked against Problem 20 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the OCR-split constants $85$ and $77$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified local existence/uniqueness, a linear-growth Grönwall bound on every finite forward and backward interval, and global continuation.
---

::: {.problem}
Prove that the initial value problem
\[
\frac{dx}{dt}=3x+85\cos x,\qquad x(0)=77,
\]
has a solution $x(t)$ defined for all $t\in\mathbb R$.
:::

::: {.solution}
Let
\[
F(x)=3x+85\cos x.
\]
Since $F$ is smooth on $\mathbb R$, the standard local existence and uniqueness theorem gives a unique maximal solution
\[
x:(\alpha,\beta)\longrightarrow\mathbb R,
\qquad
x(0)=77.
\]
We prove that neither endpoint can be finite.

<1>1. The vector field has at most linear growth.
::: {.proof}
For every $x\in\mathbb R$,
\[
|F(x)|
=|3x+85\cos x|
\le3|x|+85.
\]
:::

<1>2. The solution is bounded on every finite forward time interval contained in its maximal interval.
::: {.proof}
For $0\le t<\beta$,
\[
x(t)=77+\int_0^t F(x(s))\,ds.
\]
Using <1>1,
\[
|x(t)|
\le77+85t+3\int_0^t|x(s)|\,ds.
\]
Fix $T<\beta$.
For $0\le t\le T$,
\[
|x(t)|
\le 77+85T+3\int_0^t|x(s)|\,ds.
\]
Gronwall's inequality gives
\[
|x(t)|\le(77+85T)e^{3t}
\le(77+85T)e^{3T}.
\]
Thus $x$ is bounded on every finite interval $[0,T]\subset(\alpha,\beta)$.
:::

<1>3. The solution is bounded on every finite backward time interval contained in its maximal interval.
::: {.proof}
Set
\[
y(s)=x(-s).
\]
Then, wherever it is defined,
\[
y'(s)=-F(y(s)),
\qquad y(0)=77.
\]
The vector field $-F$ satisfies the same growth estimate
\[
|-F(y)|\le3|y|+85.
\]
Applying the argument of <1>2 to $y$ shows that $x(t)$ is bounded on every finite interval $[-T,0]\subset(\alpha,\beta)$.
:::

<1>4. The maximal interval is all of $\mathbb R$.
::: {.proof}
For a smooth vector field on all of $\mathbb R$, a maximal solution can fail to extend through a finite endpoint only by leaving every compact subset of the state space; in one dimension this means
\[
|x(t)|\longrightarrow\infty
\]
as the endpoint is approached.

If $\beta<\infty$, <1>2 with any $T<\beta$ gives a bound that remains finite as $T\uparrow\beta$; for example
\[
|x(t)|\le(77+85\beta)e^{3\beta}
\qquad(0\le t<\beta).
\]
Thus finite-time blowup at $\beta$ is impossible, so $\beta=\infty$.
Likewise <1>3 rules out a finite left endpoint, so $\alpha=-\infty$.
Therefore the solution is defined for every
\[
t\in\mathbb R.
\]
:::
:::
