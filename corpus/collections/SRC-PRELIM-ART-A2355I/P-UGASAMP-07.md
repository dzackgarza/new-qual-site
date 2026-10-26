---
schema: qual/card@1
id: P-UGASAMP-07
kind: problem
title: Three linear combinations of independent vectors are independent
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Assume $u,v,w\in\mathbb R^n$ are linearly independent. Prove that
\[
2u+v,\qquad u+v+w,\qquad v-w
\]
are linearly independent.
:::

::: pf

::: pf-step

Suppose
\[
a(2u+v)+b(u+v+w)+c(v-w)=0.
\]
Then
\[
(2a+b)u+(a+b+c)v+(b-c)w=0.
\]


::: pf-proof

Expand the three scalar multiples and collect the coefficients of \(u\), \(v\), and \(w\).

:::

:::

::: pf-step

The coefficients satisfy
\[
2a+b=0,\qquad a+b+c=0,\qquad b-c=0.
\]


::: pf-proof

The vectors \(u,v,w\) are linearly independent. Therefore the linear combination in step <1>1 can vanish only if each coefficient is zero.

:::

:::

::: pf-step

One has
\[
a=b=c=0.
\]


::: pf-proof

From the third equation in step <1>2,
\[
c=b.
\]
The first equation gives
\[
b=-2a.
\]
Substituting both into the second equation yields
\[
0=a+b+c
=a+2b
=a-4a
=-3a,
\]
so \(a=0\). Hence \(b=-2a=0\) and \(c=b=0\).

:::

:::

::: pf-step

Therefore
\[
\boxed{2u+v,\quad u+v+w,\quad v-w\text{ are linearly independent}.}
\]


::: pf-proof

Step <1>3 shows that the only linear relation among the three displayed vectors has all coefficients equal to zero. This is exactly the definition of linear independence.

:::

:::

::: pf-qed

Step <1>4 is the required conclusion.

:::

:::
