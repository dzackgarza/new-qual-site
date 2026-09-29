---
schema: qual/card@1
id: P-HCAO34
kind: problem
title: A higher-dimensional Noetherian normal domain
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Integral Closure
  - Krull Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Give an example of a Noetherian integrally closed domain whose Krull dimension is not one.
:::

::: {.solution}
Take $R=k[x,y]$ for any field $k$.

::: pf

::: pf-step
The ring $R$ is Noetherian.

::: pf-proof
The field $k$ is Noetherian, and Hilbert's basis theorem applied twice shows
that $k[x,y]$ is Noetherian.
:::

:::

::: pf-step
The ring $R$ is integrally closed.

::: pf-proof
A polynomial ring over a field is a unique factorization domain. Every UFD is
integrally closed in its fraction field.
:::

:::

::: pf-step
The Krull dimension of $R$ is at least $2$, hence is not $1$.

::: pf-proof
There is a strict chain of prime ideals
\[
(0)\subsetneq(x)\subsetneq(x,y).
\]
Indeed, $R/(x)\cong k[y]$ is a domain, so $(x)$ is prime, and
$R/(x,y)\cong k$ is a field, so $(x,y)$ is maximal and therefore prime.
Thus $\dim R\ge2$.
:::

:::

:::
:::
