---
schema: qual/card@1
id: P-HFGO35
kind: problem
title: $\mathbb F_{27}$ as a cubic extension of $\mathbb F_3$
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
Construct a field of order $27$ from $\mathbb F_3$ and an irreducible polynomial.
What degree must the polynomial have?
:::

::: solution
The polynomial must have degree $3$.

<1>1. If $f(T)\in\mathbb F_3[T]$ is irreducible of degree $d$, then
\[
\mathbb F_3[T]/(f)
\]
has $3^d$ elements.
::: proof
Every residue class has a unique representative of degree less than $d$, so it
is determined by $d$ coefficients in $\mathbb F_3$. Hence there are $3^d$
classes. Irreducibility of $f$ makes the quotient a field.
:::

<1>2. To obtain $27=3^3$ elements, one must take $d=3$.
::: proof
By <1>1 the field has $3^d$ elements, and $3^d=27$ if and only if $d=3$.
:::

<1>3. For example,
\[
f(T)=T^3-T-1
\]
is irreducible over $\mathbb F_3$.
::: proof
It has no root in $\mathbb F_3$:
\[
f(0)=2,
\qquad
f(1)=2,
\qquad
f(2)=2.
\]
A cubic over a field is reducible exactly when it has a linear factor, hence a
root. Therefore $f$ is irreducible.
:::

<1>4. Thus
\[
\mathbb F_3[T]/(T^3-T-1)
\]
is a field of order $27$.
::: proof
This follows from <1>1--<1>3.
:::
:::
