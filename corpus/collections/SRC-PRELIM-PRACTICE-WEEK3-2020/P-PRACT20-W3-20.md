---
schema: qual/card@1
id: P-PRACT20-W3-20
kind: problem
title: Minimizing $x+4z$ on the sphere $x^2+y^2+z^2=2$
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
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced OCR 'sec' with the source's 'so' in the solution, checked against Week3_solns.pdf (Problem 20).
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 6 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem minimises the same linear function on the same sphere, and the printed solution gives the same point
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's Lagrange equations and the value (lambda squared = 17/8) are transcribed, with both branch points written out and the minimum value computed.
---

::: {.problem}
Minimize the function $f(x, y, z) = x + 4z$ on the sphere $x^{2} + y^{2} + z^{2} = 2$.
:::

::: {.solution}

Minimise $f(x,y,z)=x+4z$ subject to $x^2+y^2+z^2=2$; the constraint set is the
sphere of radius $\sqrt2$, which is compact, so the minimum is attained.

::: pf

::: {.pf-step #lagrange}

At a constrained extremum there is $\lambda$ with $1=2\lambda x$, $0=2\lambda
y$, $4=2\lambda z$.

::: pf-proof

Write $g(x,y,z)=x^2+y^2+z^2-2$, whose gradient $(2x,2y,2z)$ is nonzero on the
constraint set; the Lagrange multiplier theorem then gives $\nabla
f=\lambda\nabla g$ at an extremum on the sphere, and $\nabla f=(1,0,4)$ gives
the three equations.

:::

:::

::: {.pf-step #solve}

$\lambda^2=\frac{17}{8}$, and the candidate points are
$\pm\big(\sqrt{2/17},\,0,\,\sqrt{32/17}\big)$ scaled by the common factor
$\frac1{2\lambda}\sqrt2$.

::: pf-proof

The equations give $x=\frac{1}{2\lambda}$, $y=0$, $z=\frac{2}{\lambda}$.
Substituting into the constraint,
$\frac{1}{4\lambda^2}+\frac{4}{\lambda^2}=2$, that is
$\frac{17}{4\lambda^2}=2$ and $\lambda^2=\frac{17}{8}$. Then
$x=\frac{1}{2\lambda}=\pm\sqrt{\frac{2}{17}}$ and
$z=\frac2\lambda=\pm\sqrt{\frac{32}{17}}$, with the same sign for $x$ and $z$
in each solution; $y=0$ in both.

:::

:::

::: {.pf-step #minimum}

$\boxed{f$ is minimised at $\big(-\sqrt{2/17},\,0,\,-\sqrt{32/17}\big)$ with
value $-\sqrt{34}$}.

::: pf-proof

Since $f$ is increasing in $x$ and in $z$, the negative branch gives the
smaller value:
$f=-\sqrt{\frac{2}{17}}-4\sqrt{\frac{32}{17}}=-\frac{\sqrt2}{\sqrt{17}}-\frac{16\sqrt2}{\sqrt{17}}=-\frac{17\sqrt2}{\sqrt{17}}=-\sqrt{34}$,
while the positive branch gives $+\sqrt{34}$. These are the only stationary
points, and the sphere is compact, so the minimum is the smaller value; the
printed solution names the same point.

:::

:::

:::


:::
