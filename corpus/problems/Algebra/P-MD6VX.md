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
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Why is the character table a square?
:::

::: solution
For a finite group $G$, the character table has one row for each irreducible complex character and one column for each conjugacy class.

The irreducible characters form an orthonormal basis of the complex vector space of class functions on $G$. The dimension of that space is the number of conjugacy classes, because a class function is determined independently by its value on each conjugacy class.

Therefore
\[
\#\{\text{irreducible complex characters}\}
=
\#\{\text{conjugacy classes}\}.
\]
Hence the character table has the same number of rows and columns: it is square.
:::
