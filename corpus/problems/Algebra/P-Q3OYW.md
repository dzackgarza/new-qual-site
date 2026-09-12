---
schema: qual/card@1
id: P-Q3OYW
kind: problem
title: Separable polynomials of prescribed degree
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Polynomials
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Are there separable polynomials of any degree $n \ge 1$ over any field $F$?
What about irreducible separable polynomials?
:::

::: solution
Yes: for every field $F$ and every $n\ge1$, there exists a separable polynomial of degree $n$.

If $F$ is infinite, choose distinct $a_1,\dots,a_n\in F$ and take
\[
f(x)=\prod_{i=1}^n(x-a_i).
\]
If $F=\mathbb F_q$ is finite, there exists an irreducible polynomial of degree $n$ over $\mathbb F_q$; finite fields are perfect, so that polynomial is separable.

For irreducible separable polynomials, there is no corresponding statement for arbitrary fields and arbitrary degrees. Finite fields do have irreducible separable polynomials of every positive degree. In characteristic $0$, every irreducible polynomial is separable, but a given field need not possess irreducibles of every degree: an algebraically closed field has only linear irreducibles, and $\mathbb R$ has irreducibles only in degrees $1$ and $2$.

Thus “separable of every degree” holds over every field; “irreducible and separable of every degree” is a field-dependent property.
:::
