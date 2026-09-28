---
schema: qual/card@1
id: P-PRACT20-W4-12
kind: problem
title: Nullity of a linear map from $2\times3$ matrices onto $\mathbb R^4$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Rank and Nullity
relations: []
review: draft
---

::: {.problem}
Suppose that V is the vector space of real $2 \times 3$ matrices.
If T is a linear transformation from V onto $\mathbb { R } ^ { 4 }$ , what is the dimension of the null space of T ?
:::

::: {.solution}
T is mapping a 6-dimensional vector space onto a 4-dimensional vector space.
By the Rank-Nullity theorem, we have

$$
\mathrm { d i m } \left( R ( T ) \right) + \mathrm { d i m } \left( N ( T ) \right) = 6
$$

and since T is onto, we have dim $( R ( T ) ) = \mathrm { d i m } ( \mathbb { R } ^ { 4 } ) = 4 \ \mathrm { s o } | \mathrm { d i m } ( N ( T ) ) = 2 .$
:::
