---
schema: qual/card@1
id: P-ALGREV1-10
kind: problem
title: Units of a finite direct product of rings
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, true/sometimes/false question 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved a finite product tuple is a unit exactly when each coordinate is a unit, with inverse taken coordinatewise."
---

::: {.problem}
Let $R_1,\dots,R_n$ be commutative rings with unity. Classify the following assertion as true, sometimes true, or false:
\[
U(R_1\oplus\cdots\oplus R_n)=U(R_1)\oplus\cdots\oplus U(R_n).
\]
:::

::: solution
The assertion is **true**.

<1>1. A unit in the product has unit coordinates.
::: proof
Suppose
$$
(r_1,\ldots,r_n)\in R_1\oplus\cdots\oplus R_n
$$
is a unit. Then there is $(s_1,\ldots,s_n)$ such that
$$
(r_1,\ldots,r_n)(s_1,\ldots,s_n)=(1,\ldots,1).
$$
Multiplication is coordinatewise, so
$$
r_is_i=1
$$
for every $i$. Thus each $r_i\in U(R_i)$.
:::

<1>2. A tuple of units is a unit in the product.
::: proof
Conversely, if every $r_i\in U(R_i)$, then
$$
(r_1^{-1},\ldots,r_n^{-1})
$$
is the inverse of $(r_1,\ldots,r_n)$. Therefore the tuple is a unit.
:::

<1>3. Hence the unit group is the product of the unit groups.
::: proof
Steps <1>1 and <1>2 give equality of the underlying sets, and the group law
on both sides is coordinatewise multiplication. Therefore
$$
\boxed{
U(R_1\oplus\cdots\oplus R_n)
=U(R_1)\oplus\cdots\oplus U(R_n).}
$$
For finitely many rings, the direct sum and direct product are the same
underlying ring.
:::
:::
