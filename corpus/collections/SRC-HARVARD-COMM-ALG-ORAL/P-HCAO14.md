---
schema: qual/card@1
id: P-HCAO14
kind: problem
title: Division algorithm over the real quaternions
classification:
  areas:
  - algebra
  topics:
  - Division Rings
  - Polynomials
  - Ring Theory
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
Let $R$ be the ring of real quaternions.
Does $R[x]$ satisfy the division algorithm?
:::

::: {.solution}
Yes, for the usual polynomial ring over the quaternion division ring with a
central indeterminate $x$. In fact one has both right and left division with
remainder.

::: pf

::: {.pf-step #right-division-possible}
Right division is possible.

::: pf-proof
Let
\[
f=a_mx^m+\cdots+a_0,
\qquad
g=b_nx^n+\cdots+b_0\ne0,
\]
with $m\ge n$. Since the real quaternions form a division ring,
$b_n^{-1}$ exists. Put
\[
c=a_m b_n^{-1}.
\]
Because $x$ is central, the leading term of
\[
c x^{m-n}g
\]
is $cb_nx^m=a_mx^m$. Hence
\[
f_1=f-cx^{m-n}g
\]
has degree strictly less than $m$. Repeating this degree-lowering step
terminates and produces
\[
f=qg+r,
\qquad
\deg r<\deg g.
\]
:::

:::

::: {.pf-step #left-division-possible}
Left division is possible as well.

::: pf-proof
At the same step choose
\[
c=b_n^{-1}a_m.
\]
Then the leading term of
\[
g c x^{m-n}
\]
is $b_nc x^m=a_mx^m$, again because $x$ commutes with quaternion coefficients.
Induction on the degree gives
\[
f=gq+r,
\qquad
\deg r<\deg g.
\]
:::

:::

::: pf-step
Thus $R[x]$ has the usual degree division algorithm, with sidedness
specified because $R[x]$ is noncommutative.

::: pf-proof
This is exactly step [](#right-division-possible){.pf-ref} and step [](#left-division-possible){.pf-ref}.
:::

:::

:::
:::
