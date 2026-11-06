---
schema: qual/card@1
id: P-PRACT20-W3-17
kind: problem
title: Point on the plane $2x+y+3z=3$ closest to the origin
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Lagrange Multipliers
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 5 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the closest point of the same plane to the origin, and the printed solution gives (6/14, 3/14, 9/14) with the multiplier 3/7
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's Lagrange equations and their solution are transcribed, with the shortcut along the normal added and the distance checked.
---

::: {.problem}
Find the point on the plane $2 x + y + 3 z = 3$ which is closest to the origin.
:::

::: {.solution}

Minimise $f(x,y,z)=x^2+y^2+z^2$ subject to $g(x,y,z)=2x+y+3z-3=0$.

::: pf

::: {.pf-step #lagrange}

At the minimum there is $\lambda$ with $2x=2\lambda$, $2y=\lambda$,
$2z=3\lambda$.

::: pf-proof

The plane is a smooth surface with $\nabla g=(2,1,3)\ne0$ everywhere, so a
minimum of $f$ on it exists (the distance function is coercive on the plane)
and the Lagrange multiplier condition $\nabla f=\lambda\nabla g$ holds at it.
Computing $\nabla f=(2x,2y,2z)$ gives the three equations.

:::

:::

::: {.pf-step #solve}

$\lambda=\frac37$, hence
$(x,y,z)=\big(\frac{6}{14},\frac{3}{14},\frac{9}{14}\big)$.

::: pf-proof

The equations give $x=\lambda$, $y=\frac\lambda2$, $z=\frac{3\lambda}2$.
Substituting into the constraint,
$2\lambda+\frac\lambda2+\frac{9\lambda}2=7\lambda=3$, so $\lambda=\frac37$,
$x=\frac37$, $y=\frac{3}{14}$, $z=\frac{9}{14}$.

:::

:::

::: {.pf-step #answer}

The closest point is $\boxed{\big(\frac37,\frac{3}{14},\frac{9}{14}\big)}$, at
distance $\frac{3}{\sqrt{14}}$.

::: pf-proof

Step [](#solve){.pf-ref} gives the unique stationary point, and since
$f\to\infty$ at infinity on the plane it is the global minimum. The same point
is found by the printed shortcut: it lies on the normal through the origin,
$(x,y,z)=t(2,1,3)$, and the constraint $2(2t)+t+3(3t)=14t=3$ gives
$t=\frac{3}{14}$, that is $(6,3,9)/14$. Its distance to the origin is
$\sqrt{\frac{9}{49}+\frac{9}{196}+\frac{81}{196}}=\sqrt{\frac{36+9+81}{196}}=\sqrt{\frac{126}{196}}=\frac{3}{\sqrt{14}}$,
and the value of $f$ there is $x^2+y^2+z^2=\frac{126}{196}=\frac{9}{14}$,
consistent with the gradient condition $2p=\lambda(2,1,3)$ at $p$.

:::

:::

:::


:::
