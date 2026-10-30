---
schema: qual/card@1
id: P-GRECH3-27
kind: problem
title: Volume under a surface in the first octant
classification:
  areas:
  - real-analysis
  topics:
  - Double Integrals
  - Volume
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 27 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Find the volume of the solid in the first octant of $xyz$-space, bounded below by the coordinate axes and the unit circle, and bounded above by the surface $z=8xy$.

(A) $\frac{1}{2}$
(B) $1$
(C) $2$
(D) $4$
(E) $8$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The base of the solid is the quarter unit disk
$$
R=\{(r,\theta):0\le r\le1,\ 0\le\theta\le\pi/2\}.
$$


::: pf-proof

The solid lies in the first octant, so its projection to the $xy$-plane has $x\ge0$ and $y\ge0$. It is bounded laterally by the coordinate axes and the unit circle $x^2+y^2=1$, which is exactly the displayed region in polar coordinates.

:::

:::

::: {.pf-step #s1-2}

The volume is
$$
\boxed{1},
$$
so the answer is (B).


::: pf-proof

The height above $(x,y)\in R$ is $z=8xy$. With
$$
x=r\cos\theta,\qquad y=r\sin\theta,\qquad dA=r\,dr\,d\theta,
$$
step [](#s1-1){.pf-ref} gives
$$
V
=\iint_R8xy\,dA
=8\int_0^{\pi/2}\int_0^1
r^3\cos\theta\sin\theta\,dr\,d\theta.
$$
Therefore
$$
V
=8\left[\frac{r^4}{4}\right]_0^1
\left[\frac{\sin^2\theta}{2}\right]_0^{\pi/2}
=8\cdot\frac14\cdot\frac12
=1.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested volume and corresponding choice.

:::

:::

:::
