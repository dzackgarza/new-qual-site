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

::: {.solution}
Let
\[
f:\mathbb C\to\mathbb C
\]
be entire and bounded. Choose \(M\ge0\) such that
\[
\boxed{|f(z)|\le M}
\]
for every \(z\in\mathbb C\).

<1>1. Fix an arbitrary point
\[
z_0\in\mathbb C.
\]

::: {.proof}
It suffices to show that \(f'(z_0)=0\) for every point.
:::

<1>2. For every \(R>0\), the closed disk
\[
\overline{D(z_0,R)}
\]
lies in the domain of holomorphy of \(f\).

::: {.proof}
The function \(f\) is entire, so it is holomorphic on all of \(\mathbb C\).
:::

<1>3. On the circle
\[
|z-z_0|=R,
\]
one has
\[
\max |f(z)|\le M.
\]

::: {.proof}
Use the global boundedness hypothesis.
:::

<1>4. Cauchy's estimate for the first derivative gives
\[
\boxed{
|f'(z_0)|
\le
\frac{M}{R}}.
\]

::: {.proof}
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

<1>5. Since step <1>4 holds for every \(R>0\),
\[
\boxed{f'(z_0)=0}.
\]

::: {.proof}
Let \(R\to\infty\). The right-hand side
\[
\frac{M}{R}
\]
tends to \(0\), while the left-hand side is independent of \(R\). Hence
\[
|f'(z_0)|=0.
\]
:::

<1>6. The point \(z_0\) was arbitrary, so
\[
\boxed{f'\equiv0}.
\]

::: {.proof}
Apply step <1>5 at every point of \(\mathbb C\).
:::

<1>7. Therefore \(f\) is constant.

::: {.proof}
An analytic function with identically zero derivative is constant on each
connected component of its domain. The plane \(\mathbb C\) is connected.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is Liouville's theorem.
:::
:::
