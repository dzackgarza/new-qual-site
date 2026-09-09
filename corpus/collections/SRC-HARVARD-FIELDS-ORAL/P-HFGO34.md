---
schema: qual/card@1
id: P-HFGO34
kind: problem
title: A field with $27$ elements
classification:
  areas: [algebra]
  topics: [Finite Fields]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Construct a field with $27$ elements.
:::

::: solution
Consider
\[
f(T)=T^3-T-1\in\mathbb F_3[T].
\]

<1>1. The polynomial $f$ is irreducible over $\mathbb F_3$.
::: proof
A cubic polynomial over a field is reducible if and only if it has a root in
that field. Direct evaluation gives
\[
f(0)=-1\ne0,
\qquad
f(1)=-1\ne0,
\qquad
f(2)=8-2-1=5\equiv2\ne0\pmod3.
\]
Thus $f$ has no root in $\mathbb F_3$ and is irreducible.
:::

<1>2. The quotient
\[
K=\mathbb F_3[T]/(T^3-T-1)
\]
is a field.
::: proof
Since $f$ is irreducible, the ideal $(f)$ is maximal in the PID
$\mathbb F_3[T]$.
:::

<1>3. The field $K$ has $27$ elements.
::: proof
Every class has a unique representative
\[
a+bT+cT^2,
\qquad
a,b,c\in\mathbb F_3.
\]
There are therefore $3^3=27$ residue classes.
:::
:::
