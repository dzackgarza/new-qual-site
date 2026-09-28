---
schema: qual/card@1
id: P-TIE-F11-16
kind: problem
title: Entire functions with $|f(z)|\le M|z|^2$ are quadratic polynomials
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 16.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX against Fall 2011, question 16, page 6 of Questions_from_Tie.pdf, which prints f(z) <= M|z|^2 without the modulus, and added an erratum remark giving the intended hypothesis |f(z)| <= M|z|^2.
---

::: {.problem}
Let $f(z)$ be entire and assume that $f(z) \le M\abs{z}^2$ outside some disk for some constant $M$. Show that $f(z)$ is a polynomial in $z$ of degree $\le 2$.
:::

::: {.remark}
Erratum: the source writes the hypothesis as $f(z) \le M\abs{z}^2$, which has no meaning for complex values of $f$.
The intended hypothesis is $\abs{f(z)} \le M\abs{z}^2$ outside some disk.
:::
