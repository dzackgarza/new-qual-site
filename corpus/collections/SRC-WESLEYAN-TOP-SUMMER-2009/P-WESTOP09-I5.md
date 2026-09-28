---
schema: qual/card@1
id: P-WESTOP09-I5
kind: problem
title: A Hausdorff continuous image of the unit interval is metrizable
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Suppose $X$ is Hausdorff and there is a continuous surjection
\[
f:I=[0,1]\to X.
\]
This problem proves the metrizability part of the Hahn--Mazurkiewicz theorem.

1. Show that $f$ is a closed map.
2. Show that $X$ is second countable. The source suggests choosing a countable basis $B$ for $I$, taking the set $C$ of finite unions of elements of $B$, and proving that
   \[
   \{X\setminus f(I\setminus U):U\in C\}
   \]
   is a basis for $X$.
3. Prove that $X$ is metrizable.
:::
