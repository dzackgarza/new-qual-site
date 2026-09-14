---
schema: qual/card@1
id: P-UCLAB03S-04
kind: problem
title: Quadratic solutions of the one-dimensional wave equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Examination, May 2003 PDF. In part (b), the source prints $F(x,y)=f(x,y)+g(x-y)$ while immediately saying that $f$ and $g$ are one-variable polynomials; $f(x,y)$ is therefore undefined as printed.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Records the malformed source expression and proves the intended correction $F(x,y)=f(x+y)+g(x-y)$ for quadratic solutions.
---

::: {.problem}
Consider the equation
\[
\frac{\partial^2F}{\partial x^2}
=
\frac{\partial^2F}{\partial y^2}
\tag{*}
\]
for a function $F(x,y)$ on $\mathbb R^2$.

(a) Show that if
\[
F(x,y)=f(x+y)+g(x-y),
\]
where $f,g:\mathbb R\to\mathbb R$ are twice differentiable, then $F$ satisfies $(*)$.

(b) The source asks to show that if
\[
F(x,y)=ax^2+bxy+cy^2,
\qquad a,b,c\in\mathbb R,
\]
satisfies $(*)$, then
\[
F(x,y)=f(x,y)+g(x-y)
\]
for some one-variable polynomials $f$ and $g$.
:::

::: {.solution}
Part (b) is not well-formed as printed because a one-variable polynomial $f$ cannot be evaluated at the ordered pair $(x,y)$.
The intended expression is forced by part (a):
\[
F(x,y)=f(x+y)+g(x-y).
\]

Indeed, for the quadratic polynomial in part (b), equation $(*)$ gives
\[
2a=2c,
\]
so $c=a$.
Put
\[
\alpha=\frac a2+\frac b4,
\qquad
\beta=\frac a2-\frac b4,
\]
and define
\[
f(t)=\alpha t^2,
\qquad
g(t)=\beta t^2.
\]
Then
\[
f(x+y)+g(x-y)
=(\alpha+\beta)(x^2+y^2)+2(\alpha-\beta)xy
=a(x^2+y^2)+bxy
=F(x,y).
\]
Thus the corrected version of part (b) follows.
:::
