---
schema: qual/card@1
id: P-UCLARA13F-09
kind: problem
title: Separate boundedness of a bilinear form implies joint boundedness
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Let $X$ be a Banach space, $Y$ a normed linear space, and $B:X\times Y\to\mathbb R$ bilinear.
Suppose that for each $x\in X$ there is $C_x\ge0$ with
\[
|B(x,y)|\le C_x\|y\|\qquad(y\in Y),
\]
and for each $y\in Y$ there is $C_y\ge0$ with
\[
|B(x,y)|\le C_y\|x\|\qquad(x\in X).
\]
Show that there is $C\ge0$ such that
\[
|B(x,y)|\le C\|x\|\|y\|
\]
for all $x\in X$ and $y\in Y$.
:::
