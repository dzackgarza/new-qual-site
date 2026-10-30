---
schema: qual/card@1
id: P-MMAQ-YUXDCVQRF5
kind: problem
title: $\int_0^{\pi/2}\frac{1}{3+\sin^2 x}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Integrals
  - Residues
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Evaluate the following by the method of residues: $\int_0^{\pi /2} \frac{1}{3+\sin^2x}dx$
:::

::: {.solution}
Let $I\coloneqq\int_0^{\pi/2}\frac{dx}{3+\sin^2x}$, and let $C$ be the unit circle, oriented counterclockwise.

::: pf

::: {.pf-step #full-circle}

$\displaystyle I=\frac12\int_0^{2\pi}\frac{d\theta}{7-\cos\theta}$.

::: pf-proof

Since $\sin^2x=\frac{1-\cos 2x}{2}$, the integrand is $\frac{2}{7-\cos 2x}$.
The substitution $\theta=2x$ gives $I=\int_0^\pi\frac{d\theta}{7-\cos\theta}$, and $\cos(2\pi-\theta)=\cos\theta$ doubles the range to $[0,2\pi]$ at the cost of a factor $\frac12$.

:::

:::

::: {.pf-step #contour}

$\displaystyle I=i\oint_C\frac{dz}{z^2-14z+1}$.

::: pf-proof

With $z=e^{i\theta}$, $\cos\theta=\frac{z+z^{-1}}{2}$ and $d\theta=\frac{dz}{iz}$, so
$$
\frac{d\theta}{7-\cos\theta}=\frac{2z}{14z-z^2-1}\cdot\frac{dz}{iz}=\frac{2i\,dz}{z^2-14z+1}.
$$
Multiply by $\frac12$ as in step [](#full-circle){.pf-ref}.

:::

:::

::: {.pf-step #residue}

$\displaystyle\oint_C\frac{dz}{z^2-14z+1}=-\frac{\pi i}{4\sqrt3}$.

::: pf-proof

The roots of $z^2-14z+1$ are $z_\pm=7\pm4\sqrt3$, and $z_+z_-=1$ with $z_+>1$, so only $z_-$ lies inside $C$.
It is a simple pole with residue $\frac{1}{z_--z_+}=-\frac{1}{8\sqrt3}$, and the residue theorem gives $2\pi i\cdot\qty(-\frac1{8\sqrt3})$.

:::

:::

::: pf-step

$\displaystyle I=\boxed{\frac{\pi}{4\sqrt3}}$.

::: pf-proof

Combine steps [](#contour){.pf-ref} and [](#residue){.pf-ref}: $i\cdot\qty(-\frac{\pi i}{4\sqrt3})=\frac{\pi}{4\sqrt3}$.

:::

:::

:::

:::
