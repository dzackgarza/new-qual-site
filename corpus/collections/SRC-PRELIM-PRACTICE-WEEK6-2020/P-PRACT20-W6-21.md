---
schema: qual/card@1
id: P-PRACT20-W6-21
kind: problem
title: Surjections from a $4$-element set onto a $3$-element set
classification:
  areas:
  - prelim
  topics:
  - Combinatorics
  - Inclusion-Exclusion
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray brace and restored the question mark, checked against Week6_solns.pdf (Problem 21).
---

::: {.problem}
How many surjective functions are there from $\{1, 2, 3, 4\}$ to $\{1, 2, 3\}$?
:::

::: {.solution}
There are $3$ choices for the image of each of the four elements, so there are $3^4=81$ functions $\{1,2,3,4\}\to\{1,2,3\}$. We count the functions that are not surjective.

A non-surjective function maps into one of $\{1,2\}$, $\{1,3\}$, $\{2,3\}$. There are $2^4=16$ maps into each, giving $48$, but each of the $3$ constant maps is counted twice (for example $x\mapsto1$ maps into both $\{1,2\}$ and $\{1,3\}$). So there are $48-3=45$ non-surjective maps and $81-45=36$ surjective maps.
:::
