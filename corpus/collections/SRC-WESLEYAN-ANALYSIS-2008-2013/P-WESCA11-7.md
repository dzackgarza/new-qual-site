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
$$
f:\CC\to\CC
$$
be entire and bounded. Choose $M\ge0$ such that
$$
\boxed{\abs{f(z)}\le M}
$$
for every $z\in\CC$.

::: pf

::: pf-step

Fix an arbitrary point
$$
z_0\in\CC.
$$


::: pf-proof

It suffices to show that $f'(z_0)=0$ for every point.

:::

:::

::: pf-step

For every $R>0$, the closed disk
$$
\overline{D(z_0,R)}
$$
lies in the domain of holomorphy of $f$.


::: pf-proof

The function $f$ is entire, so it is holomorphic on all of $\CC$.

:::

:::

::: {.pf-step #s1-3}

On the circle
$$
\abs{z-z_0}=R,
$$
one has
$$
\max \abs{f(z)}\le M.
$$


::: pf-proof

Use the global boundedness hypothesis.

:::

:::

::: {.pf-step #s1-4}

Cauchy's estimate for the first derivative gives
$$
\boxed{
\abs{f'(z_0)}
\le
\frac{M}{R}}.
$$


::: pf-proof

The first-derivative Cauchy estimate states that if
$$
\abs{f(z)}\le M_R
$$
on $\abs{z-z_0}=R$, then
$$
\abs{f'(z_0)}
\le
\frac{M_R}{R}.
$$
Apply step [](#s1-3){.pf-ref} with $M_R\le M$.

:::

:::

::: {.pf-step #s1-5}

Since step [](#s1-4){.pf-ref} holds for every $R>0$,
$$
\boxed{f'(z_0)=0}.
$$


::: pf-proof

Let $R\to\infty$. The right-hand side
$$
\frac{M}{R}
$$
tends to $0$, while the left-hand side is independent of $R$. Hence
$$
\abs{f'(z_0)}=0.
$$

:::

:::

::: pf-step

The point $z_0$ was arbitrary, so
$$
\boxed{f'\equiv0}.
$$


::: pf-proof

Apply step [](#s1-5){.pf-ref} at every point of $\CC$.

:::

:::

::: {.pf-step #s1-7}

Therefore $f$ is constant.


::: pf-proof

An analytic function with identically zero derivative is constant on each
connected component of its domain. The plane $\CC$ is connected.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is Liouville's theorem.

:::

:::

:::
