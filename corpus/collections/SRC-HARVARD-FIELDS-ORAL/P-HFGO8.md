---
schema: qual/card@1
id: P-HFGO8
kind: problem
title: Algebraically closed fields and splitting polynomials
classification:
  areas: [algebra]
  topics: [Field Theory]
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
Define an algebraically closed field.
Define what it means for a polynomial to split over a field.
:::

::: solution
A field $F$ is **algebraically closed** if every nonconstant polynomial
\[
f(x)\in F[x]
\]
has a root in $F$. Equivalently, every nonconstant polynomial in $F[x]$ factors
completely into linear factors over $F$.

A polynomial $f(x)\in F[x]$ of degree $n$ **splits over $F$** if there exist
$a\in F$ and elements $\alpha_1,\ldots,\alpha_n\in F$ such that
\[
f(x)=a\prod_{i=1}^n (x-\alpha_i),
\]
with roots repeated according to multiplicity. Thus splitting means that all
roots of the polynomial lie in the field in which the factorization is being
considered.
:::
