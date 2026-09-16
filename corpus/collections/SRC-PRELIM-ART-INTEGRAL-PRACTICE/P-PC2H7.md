---
schema: qual/card@1
id: P-PC2H7
kind: problem
title: Sum-to-product and product-to-sum identities for sine, cosine, and tangent
classification:
  areas:
  - prelim
  topics:
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
$\cos (x) + \cos (y) = 2 \cos (\frac {x + y}{2}) \cos (\frac {x - y}{2})​$

$\cos (x) - \cos (y) = - 2 \sin (\frac {x + y}{2}) \sin (\frac {x - y}{2})​$

$\tan (x) - \tan (y) = \frac {\sin (x - y)}{\cos {x} \cos (y)}$ whenever $\cos x\cos y\ne0$

$\sin (x) \cos (y) = \frac {1}{2} (\sin (x + y) + \sin (x - y))$

$\cos (x) \sin (y) = \frac {1}{2} (\sin (x + y) - \sin (x - y))$

$\cos (x) \cos (y) = \frac {1}{2} (\cos (x + y) + \cos (x - y))$

$\sin (x) \sin (y) = - \frac {1}{2} (\cos (x + y) - \cos (x - y))$
:::


::: {.solution}
All identities follow from
\[
\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B,
\qquad
\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B.
\]

Adding the two cosine formulas gives
\[
\cos(A+B)+\cos(A-B)=2\cos A\cos B.
\]
With $A=(x+y)/2$ and $B=(x-y)/2$ this becomes
\[
\cos x+\cos y
=2\cos\frac{x+y}{2}\cos\frac{x-y}{2}.
\]
Subtracting the same formulas gives
\[
\cos(A+B)-\cos(A-B)=-2\sin A\sin B,
\]
so
\[
\cos x-\cos y
=-2\sin\frac{x+y}{2}\sin\frac{x-y}{2}.
\]

When $\cos x\cos y\ne0$,
\[
\tan x-\tan y
=\frac{\sin x\cos y-\cos x\sin y}{\cos x\cos y}
=\frac{\sin(x-y)}{\cos x\cos y}.
\]

Adding and subtracting the sine formulas yields
\[
\sin(A+B)+\sin(A-B)=2\sin A\cos B,
\]
\[
\sin(A+B)-\sin(A-B)=2\cos A\sin B.
\]
Therefore
\[
\sin x\cos y=\frac12\bigl(\sin(x+y)+\sin(x-y)\bigr),
\]
\[
\cos x\sin y=\frac12\bigl(\sin(x+y)-\sin(x-y)\bigr).
\]
Finally, adding and subtracting the cosine formulas gives
\[
\cos x\cos y=\frac12\bigl(\cos(x+y)+\cos(x-y)\bigr),
\]
\[
\sin x\sin y=\frac12\bigl(\cos(x-y)-\cos(x+y)\bigr).
\]
:::
