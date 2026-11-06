---
schema: qual/card@1
id: P-PRACT20-W3-28
kind: problem
title: Flux of $(x,y,z)$ through the upper unit hemisphere
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Divergence Theorem
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
    source used for the statement. the printed problem asks for the flux of the same field through the same hemisphere with the same upward normal, and the printed solution gives 2 pi
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's use of the divergence theorem is transcribed, with the flux through the base disc shown to vanish and the volume of the half-ball computed.
---

::: {.problem}
What is the flux of $\mathbf{F}(x, y, z) = (x, y, z)$ through the surface $z = \sqrt{1 - x^{2} - y^{2}}$ with normal pointing upward?
:::

::: {.solution}

Let $S$ be the upper hemisphere $z=\sqrt{1-x^2-y^2}$ with the upward normal,
and $V$ the unit half-ball it bounds; compute the flux of $F(x,y,z)=(x,y,z)$.

::: pf

::: {.pf-step #closed}

The flux of $F$ through $S$ equals the flux through $\partial V$ minus the
flux through the disc, and the flux through the disc is zero.

::: pf-proof

$\partial V$ is the union of $S$ and the base disc $B=\{z=0,\ x^2+y^2\le1\}$,
with the outward normal of $V$ agreeing with the upward normal on $S$ and
pointing downward on $B$. On $B$ the normal is $(0,0,-1)$ and $F=(x,y,0)$, so
$F\cdot n=-z=0$; hence the flux through $\partial V$ is the flux through $S$.

:::

:::

::: {.pf-step #divergence}

$\displaystyle\iint_{\partial V}F\cdot n\,dS=\iiint_V\nabla\cdot
F\,dV=3\,\mathrm{vol}(V)$.

::: pf-proof

$\nabla\cdot F=1+1+1=3$, a constant, and the divergence theorem applies to the
smooth field on the closed half-ball, so the flux equals $3$ times the volume
of the half-ball, which is $\frac12\cdot\frac{4\pi}{3}=\frac{2\pi}{3}$.

:::

:::

::: {.pf-step #flux}

$\boxed{\text{flux}=2\pi}$.

::: pf-proof

Steps [](#closed){.pf-ref} and [](#divergence){.pf-ref} give
$3\cdot\frac{2\pi}{3}=2\pi$. The printed solution records the same two facts
and notes that the flux through the bottom would ordinarily have to be
included but vanishes here because $F\cdot n=-z=0$ on the plane $z=0$; the
direct computation, integrating $F\cdot n\,dS$ over the hemisphere, gives the
same $2\pi$.

:::

:::

:::


:::
