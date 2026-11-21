---
schema: qual/card@1
id: P-CJUIR
kind: problem
title: The line integral $\int_{\partial R} x\,dy+y\,dx$ on the upper region between
  $x^2+y^2=4$ and $(x-1)^2+y^2=1$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
  - Green's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $R$ be the planar region between the circles $x^2 + y^2 = 4$ and $(x-1)^2 + y^2 = 1$, and lying in the halfplane $y \ge 0$.
Let $\partial R$ be its boundary, oriented so that $R$ is on its left.
Either using the definition or by applying theorems of Calculus, compute the line integral $$\int_{\partial R} x\, dy + y\, dx .$$
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/grad_prelim_Fall06.pdf` and no solutions sheet accompanies it, so the computation below is the card's own. Both routes the problem allows are given: the form is exact, and Green's theorem is checked as a cross-check. The description of $\partial R$ as a closed curve is written out, since that is what the first route needs.

Throughout, $R$ is the set of points inside the circle $x^{2}+y^{2}=4$, outside the circle $(x-1)^{2}+y^{2}=1$, and with $y\geq0$, and $\omega\coloneqq x\,dy+y\,dx$.

::: pf

::: {.pf-step #exact}
$\omega=d(xy)$.

::: pf-proof
The differential of $f(x,y)=xy$ is $\frac{\partial f}{\partial x}dx+\frac{\partial f}{\partial y}dy=y\,dx+x\,dy$, which is $\omega$; so $\omega$ is exact on the whole plane, with potential $xy$.
:::

:::

::: {.pf-step #boundary}
$\partial R$ is a closed piecewise smooth curve.

::: pf-proof
The two circles meet the line $y=0$ at $(2,0)$ and $(-2,0)$ for the larger one, and at $(2,0)$ and $(0,0)$ for the smaller one, which is internally tangent to the larger at $(2,0)$ and passes through the origin. Accordingly the boundary of $R$ consists of: the upper semicircle of the larger circle, traversed from $(2,0)$ to $(-2,0)$; the segment of the line $y=0$ from $(-2,0)$ to $(0,0)$; and the upper semicircle of the smaller circle, traversed from $(0,0)$ to $(2,0)$. The segment $(0,2)\times\theset{0}$ is not part of the boundary, because points of $R$ with small positive second coordinate and first coordinate in $(0,2)$ lie inside the smaller circle and so are not in $R$. Each piece is smooth, and the endpoints match cyclically, so $\partial R$ is a closed piecewise smooth curve.
:::

:::

::: {.pf-step #exact-closed}
The integral of an exact form along a closed piecewise smooth curve vanishes.

::: pf-proof
Let $\gamma\colon[a,b]\to\RR^{2}$ be piecewise smooth with $\gamma(a)=\gamma(b)$ and $\omega=df$. On each smooth piece the fundamental theorem of calculus for line integrals gives $\int_{\gamma|_{[t_{i},t_{i+1}]}}\omega=f(\gamma(t_{i+1}))-f(\gamma(t_{i}))$; summing over the finitely many pieces, the sum telescopes to $f(\gamma(b))-f(\gamma(a))=0$.
:::

:::

::: pf-step
Therefore
$$
\boxed{\int_{\partial R}x\,dy+y\,dx=0,}
$$
and Green's theorem gives the same value.

::: pf-proof
By steps [](#boundary){.pf-ref} and [](#exact-closed){.pf-ref} applied to the exact form of step [](#exact){.pf-ref}, the integral over the closed curve $\partial R$ is $f(\gamma(b))-f(\gamma(a))=0$, whichever of the two orientations is used. For the cross-check, write $\omega=P\,dx+Q\,dy$ with $P(x,y)=y$ and $Q(x,y)=x$; then $\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=1-1=0$, so Green's theorem expresses the same integral as the double integral of $0$ over $R$, which is $0$. The orientation is immaterial for the value, since reversing it changes only the sign and both routes give $0$.
:::

:::

:::

:::
