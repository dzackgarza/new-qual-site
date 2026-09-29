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
$$
F(x)=3x+85\cos x.
$$

::: pf

::: {.pf-step #s1}

There is a unique maximal solution
$$
x:(\alpha,\beta)\longrightarrow\RR,
\qquad
x(0)=77,
$$
with $-\infty\le\alpha<0<\beta\le\infty$.

::: pf-proof

The function $F$ is smooth on $\RR$, so the local existence and uniqueness
theorem and continuation of solutions give the maximal solution.

:::

:::

::: {.pf-step #s2}

For every $x\in\RR$,
$$
\abs{F(x)}\le3\abs{x}+85.
$$

::: pf-proof

One has $\abs{3x+85\cos x}\le3\abs{x}+85\abs{\cos x}\le3\abs{x}+85$.

:::

:::

::: {.pf-step #s3}

If $\beta<\infty$, then
$$
\abs{x(t)}\le(77+85\beta)e^{3\beta}
\qquad(0\le t<\beta).
$$

::: pf-proof

For $0\le t<\beta$,
$$
x(t)=77+\int_0^t F(x(s))\,ds,
$$
so step [](#s2){.pf-ref} gives
$$
\abs{x(t)}
\le77+85\beta+3\int_0^t\abs{x(s)}\,ds.
$$
Gronwall's inequality gives
$$
\abs{x(t)}\le(77+85\beta)e^{3t}
\le(77+85\beta)e^{3\beta}.
$$

:::

:::

::: {.pf-step #s4}

If $\alpha>-\infty$, then
$$
\abs{x(t)}\le(77+85\abs{\alpha})e^{3\abs{\alpha}}
\qquad(\alpha<t\le0).
$$

::: pf-proof

Set $y(s)=x(-s)$ for $-\beta<s<-\alpha$. Then
$$
y'(s)=-F(y(s)),
\qquad y(0)=77,
$$
and $\abs{-F(y)}\le3\abs{y}+85$ by step [](#s2){.pf-ref}. The argument of step [](#s3){.pf-ref}
applied to $y$ on $[0,\abs{\alpha})$ gives the bound.

:::

:::

::: {.pf-step #s5}

$\alpha=-\infty$ and $\beta=\infty$.

::: pf-proof

For a smooth vector field on $\RR$, a maximal solution with a finite
endpoint satisfies $\abs{x(t)}\to\infty$ as that endpoint is approached.
Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that $x$ stays bounded near any finite endpoint,
so neither endpoint is finite.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s5){.pf-ref}, the maximal solution is defined for every
$t\in\RR$.

:::

:::

:::
