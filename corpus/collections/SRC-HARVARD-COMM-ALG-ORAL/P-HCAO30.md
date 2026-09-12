---
schema: qual/card@1
id: P-HCAO30
kind: problem
title: A term order which refines total degree
classification:
  areas:
  - algebra
  topics:
  - Term Orders
  - Gröbner Bases
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
Give an example of a term order which refines the partial order by total degree.
:::

::: solution
Graded lexicographic order is one example.

For monomials $x^\alpha,x^\beta$ in $k[x_1,\ldots,x_n]$, declare
\[
x^\alpha\prec x^\beta
\]
when either
\[
|\alpha|<|\beta|,
\]
or $|\alpha|=|\beta|$ and $\alpha$ precedes $\beta$ lexicographically.

<1>1. This is a term order.
::: proof
Lexicographic order is a term order on exponent vectors. Comparing total degree
first preserves totality and well-ordering. Moreover, adding the same exponent
vector $\gamma$ preserves both the total-degree comparison and, when the
degrees tie, the lexicographic comparison. Hence multiplication by a monomial
preserves the order.
:::

<1>2. It refines total degree.
::: proof
If $|\alpha|<|\beta|$, the first clause forces
$x^\alpha\prec x^\beta$, independently of the lexicographic tie-breaker.
:::
:::
