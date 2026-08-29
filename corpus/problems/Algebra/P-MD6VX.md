---
schema: qual/card@1
id: P-MD6VX
kind: problem
title: Why the character table is square
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Why is the character table a square?
:::

::: {.solution}
<1>1. The character table of a finite group $G$ has one row for each irreducible character and one column for each conjugacy class.
Proof: definition of the character table.

<1>2. The number of irreducible characters of $G$ equals the number of conjugacy classes of $G$.
Proof: the number of irreducible complex representations of a finite group equals the number of conjugacy classes (a standard theorem: the irreducible characters form an orthonormal basis of the space of class functions, whose dimension is the number of conjugacy classes).

<1>3. Hence the character table is square (same number of rows and columns).
Proof: <1>1 and <1>2.

<1>4. Q.E.D.
Proof: <1>3.
:::
