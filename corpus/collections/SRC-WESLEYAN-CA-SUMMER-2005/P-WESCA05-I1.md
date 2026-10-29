---
schema: qual/card@1
id: P-WESCA05-I1
kind: problem
title: "Define analyticity on an open set"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 1 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $U\subseteq\CC$ be open.
Define what it means for a function $f:U\to\CC$ to be analytic.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $f:U\to\CC$ is **analytic on $U$** if it is complex differentiable at every point of $U$; that is, for every $z_0\in U$ the limit
$$
\boxed{
f'(z_0)
=
\lim_{z\to z_0}
\frac{f(z)-f(z_0)}{z-z_0}}
$$
exists as a complex number.


::: pf-proof

This is the standard definition of an analytic, or holomorphic, function on an open subset of $\CC$.

:::

:::

::: {.pf-step #s1-2}

Equivalently, for every $z_0\in U$ there is an $r>0$ with
$$
B(z_0,r)\subseteq U
$$
and complex coefficients $a_0,a_1,\ldots$ such that
$$
f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n
$$
for every $z\in B(z_0,r)$.


::: pf-proof

The equivalence between holomorphy and local representability by a convergent complex power series is the standard analyticity theorem for one complex variable.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition; step [](#s1-2){.pf-ref} records its equivalent power-series form.

:::

:::

:::
