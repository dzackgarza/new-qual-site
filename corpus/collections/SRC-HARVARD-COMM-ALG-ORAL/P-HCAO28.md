---
schema: qual/card@1
id: P-HCAO28
kind: problem
title: Gröbner bases, term orders, and initial ideals
classification:
  areas:
  - algebra
  topics:
  - Gröbner Bases
  - Term Orders
  - Initial Ideals
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
Define a term order, the initial ideal of an ideal, and a Gröbner basis.
:::

::: {.solution}
Let $S=k[x_1,\ldots,x_n]$.

::: pf

::: pf-step
A term order is a total order $\prec$ on the monomials of $S$ such that
$1\preceq m$ for every monomial $m$ and
\[
m\prec n\implies mp\prec np
\]
for every monomial $p$.

::: pf-proof
These conditions make $\prec$ a multiplicative well-order: there is no infinite
strictly descending sequence of monomials. This is the structure needed for
multivariate division to terminate.
:::

:::

::: pf-step
For $0\ne f\in S$, its initial monomial $\operatorname{in}_\prec(f)$ is
the largest monomial occurring in $f$ with respect to $\prec$.

::: pf-proof
The support of $f$ is finite, so it has a largest element under the total order.
If one includes the coefficient, the corresponding object is usually called
the leading term; the generated monomial ideal is unchanged by nonzero scalar
coefficients.
:::

:::

::: pf-step
For an ideal $I\subseteq S$, its initial ideal is
\[
\operatorname{in}_\prec(I)
=\langle \operatorname{in}_\prec(f):0\ne f\in I\rangle.
\]

::: pf-proof
This is a monomial ideal by construction.
:::

:::

::: pf-step
A finite subset $G=\{g_1,\ldots,g_r\}\subseteq I$ is a Gröbner basis
of $I$ with respect to $\prec$ if
\[
\operatorname{in}_\prec(I)
=\langle \operatorname{in}_\prec(g_1),\ldots,
\operatorname{in}_\prec(g_r)\rangle.
\]

::: pf-proof
This is the defining property. Equivalently, every nonzero $f\in I$ has initial
monomial divisible by the initial monomial of some $g_i$.
:::

:::

:::
:::
