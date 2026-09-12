---
schema: qual/card@1
id: P-HCAO17
kind: problem
title: A polynomial ring in two variables is not a Dedekind domain
classification:
  areas:
  - algebra
  topics:
  - Dedekind Domains
  - Krull Dimension
  - Polynomials
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

::: problem
Let $k$ be a field.
Prove that $k[x,y]$ is not a Dedekind domain.
:::

::: solution
Consider the ideal
\[
(x)\subset k[x,y].
\]

<1>1. The ideal $(x)$ is a nonzero prime ideal.
::: proof
There is an isomorphism
\[
k[x,y]/(x)\cong k[y].
\]
Since $k[y]$ is an integral domain, $(x)$ is prime. It is nonzero because
$x\ne0$ in $k[x,y]$.
:::

<1>2. The ideal $(x)$ is not maximal.
::: proof
The quotient $k[y]$ is not a field: for example, $y$ is a nonzero nonunit.
Hence $k[x,y]/(x)$ is not a field, so $(x)$ is not maximal.

Equivalently, one has the strict chain
\[
(x)\subsetneq(x,y)\subsetneq k[x,y].
\]
:::

<1>3. Therefore $k[x,y]$ is not a Dedekind domain.
::: proof
In a Dedekind domain every nonzero prime ideal is maximal. The nonzero prime
ideal $(x)$ violates this condition by <1>1--<1>2.
:::
:::
