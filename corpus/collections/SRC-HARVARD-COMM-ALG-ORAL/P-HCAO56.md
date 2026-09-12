---
schema: qual/card@1
id: P-HCAO56
kind: problem
title: Ideal membership in polynomial rings
classification:
  areas:
  - algebra
  topics:
  - Gröbner Bases
  - Polynomial Ideals
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
Explain how to decide whether a given polynomial belongs to an ideal $I$ in a polynomial ring.
:::

::: solution
Suppose
\[
I=\langle f_1,\ldots,f_r\rangle\subseteq k[x_1,\ldots,x_n].
\]
Choose a term order and compute a Gröbner basis $G$ of $I$.

<1>1. Divide the given polynomial $f$ by $G$ to obtain a remainder $r$ whose
monomials are not divisible by any leading monomial of an element of $G$.
::: proof
This is the multivariate division algorithm. Because $G$ is a Gröbner basis,
the resulting normal form is independent of the reductions used.
:::

<1>2. Then
\[
f\in I\quad\Longleftrightarrow\quad r=0.
\]
::: proof
Division gives $f=\sum q_i g_i+r$, so if $r=0$ then $f\in I$. Conversely, if
$f\in I$ and $r\ne0$, then $r=f-\sum q_i g_i\in I$. Its leading monomial would
therefore lie in $\operatorname{in}(I)$ and hence be divisible by the leading
monomial of some $g_i$, contradicting the defining property of the remainder.
:::

Thus Gröbner-basis reduction gives an algorithm for ideal membership.
:::
