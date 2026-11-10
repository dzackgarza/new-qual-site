---
schema: qual/card@1
id: E-MUN-8-3
kind: problem
title: Powers and factorials as cases of the recursive product
classification:
  areas:
  - topology
  topics:
  - Recursive Definition
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §8 Exercise 3, printed p. 56; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.3,
    printed p. 95 (tmp/sources/munkres-solutions-whitman.pdf): the constant sequence
    b_i = a gives a^n, and b_i = i gives n!, each checked against its own induction.
---

::: {.exercise}

Obtain the definitions of $a^n$ and $n!$ for $n \in \ZZ_+$ as special cases of Exercise 2.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.3, printed p. 95** (`tmp/sources/munkres-solutions-whitman.pdf`); both specializations and their verifications are his.

*Powers.* Apply the construction of [[E-MUN-8-2]] to the constant sequence $b_i=a$. The function obtained satisfies
$$
a^1=b_1=a,
\qquad
a^n=\prod_{k=1}^{n-1}b_k\cdot b_n=a^{n-1}\cdot a\quad(n>1),
$$
which is the inductive definition $a^1=a$, $a^{n+1}=a^n\cdot a$ of [[E-MUN-4-6]] written with the index shifted.

*Factorials.* Apply it to $b_i=i$. Then
$$
1!=b_1=1,
\qquad
n!=\prod_{k=1}^{n-1}b_k\cdot b_n=(n-1)!\cdot n\quad(n>1),
$$
which is the usual recursive definition of $n!$.
:::
