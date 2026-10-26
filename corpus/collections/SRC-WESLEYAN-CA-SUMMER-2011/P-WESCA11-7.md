---
schema: qual/card@1
id: P-WESCA11-7
kind: problem
title: 'Liouville’s theorem from Cauchy estimates'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Using the simplest form of Cauchy's estimates, prove that every bounded entire function is constant.
:::

Let
\[
f:\mathbb C\to\mathbb C
\]
be entire and bounded. Choose \(M\ge0\) such that
\[
\boxed{|f(z)|\le M}
\]
for every \(z\in\mathbb C\).

::: pf

::: pf-step

Fix an arbitrary point
\[
z_0\in\mathbb C.
\]


::: pf-proof

It suffices to show that \(f'(z_0)=0\) for every point.

:::

:::

::: pf-step

For every \(R>0\), the closed disk
\[
\overline{D(z_0,R)}
\]
lies in the domain of holomorphy of \(f\).


::: pf-proof

The function \(f\) is entire, so it is holomorphic on all of \(\mathbb C\).

:::

:::

::: pf-step

On the circle
\[
|z-z_0|=R,
\]
one has
\[
\max |f(z)|\le M.
\]


::: pf-proof

Use the global boundedness hypothesis.

:::

:::

::: pf-step

Cauchy's estimate for the first derivative gives
\[
\boxed{
|f'(z_0)|
\le
\frac{M}{R}}.
\]


::: pf-proof

The first-derivative Cauchy estimate states that if
\[
|f(z)|\le M_R
\]
on \(|z-z_0|=R\), then
\[
|f'(z_0)|
\le
\frac{M_R}{R}.
\]
Apply step <1>3 with \(M_R\le M\).

:::

:::

::: pf-step

Since step <1>4 holds for every \(R>0\),
\[
\boxed{f'(z_0)=0}.
\]


::: pf-proof

Let \(R\to\infty\). The right-hand side
\[
\frac{M}{R}
\]
tends to \(0\), while the left-hand side is independent of \(R\). Hence
\[
|f'(z_0)|=0.
\]

:::

:::

::: pf-step

The point \(z_0\) was arbitrary, so
\[
\boxed{f'\equiv0}.
\]


::: pf-proof

Apply step <1>5 at every point of \(\mathbb C\).

:::

:::

::: pf-step

Therefore \(f\) is constant.


::: pf-proof

An analytic function with identically zero derivative is constant on each
connected component of its domain. The plane \(\mathbb C\) is connected.

:::

:::

::: pf-qed

Step <1>7 is Liouville's theorem.

:::

:::
