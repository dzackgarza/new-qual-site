---
schema: qual/card@1
id: P-PRACT20-W3-26
kind: problem
title: Area of an ellipse as the line integral $\oint -y\,dx+x\,dy$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Green's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 8 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the same line integral around the same ellipse, and the printed solution gives 2 pi a b
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's application of Green's theorem with its polar parametrisation is transcribed; the orientation, which neither the sheet nor the booklet states, is named as counterclockwise, the one the printed computation uses.
---

::: {.problem}
Let $\mathcal{C}$ be the ellipse given by $(x/a)^{2} + (y/b)^{2} = 1$ (where $a, b > 0$). Calculate
$$
\oint_{\mathcal{C}} (-y)\, dx + x\, dy.
$$
:::

::: {.solution}

Let $\mathcal C$ be the ellipse $(x/a)^2+(y/b)^2=1$ traversed
counterclockwise, bounding the region $E$; apply Green's theorem to the field
$(-y,x)$.

::: pf

::: {.pf-step #green}

$\displaystyle\oint_{\mathcal C}-y\,dx+x\,dy=\iint_E\Big(\frac{\partial
x}{\partial x}-\frac{\partial(-y)}{\partial y}\Big)\,dA=2\,\mathrm{area}(E)$.

::: pf-proof

With $P(x,y)=-y$ and $Q(x,y)=x$, both polynomial and hence continuously
differentiable, Green's theorem gives $\oint_{\mathcal
C}P\,dx+Q\,dy=\iint_E(Q_x-P_y)\,dA$ for the positively oriented boundary. Here
$Q_x=1$ and $P_y=-1$, so $Q_x-P_y=2$ and the double integral is $2$ times the
area of $E$.

:::

:::

::: {.pf-step #area}

$\mathrm{area}(E)=\pi ab$.

::: pf-proof

The substitution $x=ar\cos\theta$, $y=br\sin\theta$ has Jacobian $ab\,r$ and
carries the unit disc onto $E$, so the area is
$\int_0^{2\pi}\int_0^1ab\,r\,dr\,d\theta=ab\cdot2\pi\cdot\frac12=\pi ab$.
Equivalently, the semiaxes are $a$ and $b$ and the area of an ellipse is $\pi$
times their product.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\oint_{\mathcal C}(-y)\,dx+x\,dy=2\pi ab}$.

::: pf-proof

Combining steps [](#green){.pf-ref} and [](#area){.pf-ref} gives $2\pi ab$.
The printed solution computes the same integral by pulling the double integral
back with the same polar substitution; the sign is that of the
counterclockwise orientation, and the reverse orientation would give $-2\pi
ab$, since Green's theorem as used requires the positive one.

:::

:::

:::


:::
