---
schema: qual/card@1
id: P-BKS80-9
kind: problem
title: Centralizer of the matrix displayed in the Spring 1980 exam
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction loses part of the displayed 2-by-2 matrix A. It preserves entries 1, 2, and 3 but not enough layout to recover the fourth entry safely. An archival Berkeley problem compilation reproduces the same problem but likewise drops the display, so the missing matrix is not guessed here.
---

:::{.problem}
Let $A$ be the real $2\times2$ matrix displayed in the Spring 1980 source exam.
Show that every real matrix $B$ satisfying
\[
AB=BA
\]
has the form
\[
B=sI+tA
\]
for some $s,t\in\mathbb R$.

The retained extraction does not preserve the full displayed matrix $A$.
:::
