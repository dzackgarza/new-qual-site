---
schema: qual/card@1
id: P-TIE-S15-11
kind: problem
title: Sup norm on a smaller disk bounded by the $L^1$ norm for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 11.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the garbled norm notation and the stray subscript on r, and moved the Stein note to a remark, against Spring 2015, question 11, page 12 of Questions_from_Tie.pdf (read from the page image).
---

::: {.problem}
Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$. Show that for any $s < r$, there exists a constant $c > 0$ such that
$$
\norm{f}_{(\infty,s)} \le c\norm{f}_{(1,r)},
$$
where $\norm{f}_{(\infty,s)} = \sup_{z\in D_s(z_0)} \abs{f(z)}$ and $\norm{f}_{(1,r)} = \int_{D_r(z_0)} \abs{f(z)}\,dx\,dy$.
:::

::: {.remark}
The source adds "Note: Exercise 3.8.20 on p.107 in Stein et al is a straightforward consequence of this stronger result using the integral form of the Cauchy-Schwarz inequality in real analysis.", a pointer to Stein and Shakarchi, *Complex Analysis*; the statement does not depend on it.
:::
