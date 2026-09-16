---
schema: qual/card@1
id: P-TIE-F09-19
kind: problem
title: 'Hadamard''s example: ill-posedness of the Cauchy problem for Laplace''s equation'
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 19.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Part (2) corrected to lim sup as printed under Fall 2009, question 19, of Questions_from_Tie.pdf.
---

::: {.problem}
(1) Show that the function $u=u(x,y)$ given by
\[
u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\qquad\text{for }n\in\mathbb{N}
\]
is the solution on $D=\{(x,y)\mid x^2+y^2<1\}$ of the Cauchy problem for the Laplace equation
\[
\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=0,\qquad u(x,0)=0,\qquad\frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.
\]

(2) Show that there exist points $(x,y)\in D$ such that $\limsup_{n\to\infty}|u(x,y)|=\infty$.
:::
