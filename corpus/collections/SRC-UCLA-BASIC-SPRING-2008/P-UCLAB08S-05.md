---
schema: qual/card@1
id: P-UCLAB08S-05
kind: problem
title: Vanishing square integrals and equality of mixed partials
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
<1>1. Let $F\colon\mathbb R^2\to\mathbb R$ be continuous. Suppose that for every square $S$ whose sides are parallel to the coordinate axes,
\[
\iint_S F(x,y)\,dx\,dy=0.
\]
Prove that $F(x,y)=0$ for all $(x,y)$.

<1>2. Suppose $f$, $f_x$, $f_y$, $(f_x)_y$, and $(f_y)_x$ are continuous on $\mathbb R^2$. Use <1>1 to prove
\[
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
=
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right).
\]
You may use Fubini's theorem for the rectangular integrals involved.
:::
