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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Part (b) of the source prints F(x,y)=f(x,y)+g(x-y) with f a one-variable polynomial. The statement now reads F(x,y)=f(x+y)+g(x-y).
---

::: {.problem}
Consider the equation
$$
\frac{\partial^2F}{\partial x^2}
=
\frac{\partial^2F}{\partial y^2}
\tag{*}
$$
for a function $F(x,y)$ on $\RR^2$.

(a) Show that if
$$
F(x,y)=f(x+y)+g(x-y),
$$
where $f,g:\RR\to\RR$ are twice differentiable, then $F$ satisfies $(*)$.

(b) Show that if
$$
F(x,y)=ax^2+bxy+cy^2,
\qquad a,b,c\in\RR,
$$
satisfies $(*)$, then
$$
F(x,y)=f(x+y)+g(x-y)
$$
for some one-variable polynomials $f$ and $g$.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Part (a) holds.

::: pf-proof
By the chain rule,
$$
F_{xx}=f''(x+y)+g''(x-y),
\qquad
F_{yy}=f''(x+y)+(-1)^2g''(x-y),
$$
so $F_{xx}=F_{yy}$.
:::

:::

::: {.pf-step #s2}
Part (b) holds.

::: pf-proof
Here $F_{xx}=2a$ and $F_{yy}=2c$, so $(*)$ gives $c=a$.
Put
$$
\alpha=\frac a2+\frac b4,
\qquad
\beta=\frac a2-\frac b4,
\qquad
f(t)=\alpha t^2,
\qquad
g(t)=\beta t^2.
$$
Then
$$
f(x+y)+g(x-y)
=(\alpha+\beta)(x^2+y^2)+2(\alpha-\beta)xy
=a(x^2+y^2)+bxy
=F(x,y).
$$
:::

:::

:::
:::
