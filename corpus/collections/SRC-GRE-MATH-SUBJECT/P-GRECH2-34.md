---
schema: qual/card@1
id: P-GRECH2-34
kind: problem
title: Volume of revolution of the region between $y=x^2$ and $y=6-\abs{x}$
classification:
  areas: [prelim]
  topics:
  - Volumes of Revolution
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 34 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked independently of the card's own computation. The
    region is {x^2 <= y <= 6 - |x|}, the two curves meeting at (+-2, 4). Revolving about the y-axis,
    a horizontal slice at height y has |x| <= min(sqrt(y), 6-y): for y < 4 the parabola bound
    sqrt(y) is the smaller and the slice is a disk of radius sqrt(y), and for 4 < y < 6 the tent
    bound 6-y is smaller and the slice is a disk of radius 6-y. Hence V = pi int_0^4 y dy +
    pi int_4^6 (6-y)^2 dy = 8 pi + 8 pi/3 = 32 pi/3, which is choice (A). I first read the slice as
    an annulus and got 64 pi; the correct reading of the inequality x^2 <= y gives the disk, and the
    card is right. Checked a second way by shells: V = 2 pi int_0^2 x((6-x) - x^2) dx =
    2 pi [3x^2 - x^3/3 - x^4/4]_0^2 = 2 pi (12 - 8/3 - 4) = 32 pi/3, the same value. Not claimed: any evaluation beyond the volume.
---

::: {.problem}
The region bounded by the graphs of $y = x^2$ and $y = 6 - \abs{x}$ is revolved around the $y$-axis. What is the volume of the generated solid?

(A) $\frac{32}{3}\pi$
(B) $9\pi$
(C) $8\pi$
(D) $\frac{20}{3}\pi$
(E) $\frac{16}{3}\pi$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The two curves meet at $(\pm2,4)$.


::: pf-proof

By symmetry it suffices to solve for $x\ge0$, where the second curve is $y=6-x$. Intersections satisfy
$$
x^2=6-x,
$$
so
$$
x^2+x-6=(x-2)(x+3)=0.
$$
The nonnegative solution is $x=2$, giving $y=4$. Reflection across the $y$-axis gives the second point $(-2,4)$.

:::

:::

::: {.pf-step #s1-2}

A horizontal cross-section of the rotated solid has radius
$$
R(y)=
\begin{cases}
\sqrt y,&0\le y\le4,\\
6-y,&4\le y\le6.
\end{cases}
$$


::: pf-proof

The parabola gives $\abs{x}=\sqrt y$, while the graph $y=6-\abs{x}$ gives $\abs{x}=6-y$. The bounded region uses the smaller of these two radii. They are equal at $y=4$ by step [](#s1-1){.pf-ref}; below $4$ one has $\sqrt y\le6-y$, and above $4$ one has $6-y\le\sqrt y$.

:::

:::

::: {.pf-step #s1-3}

The volume is
$$
\boxed{\frac{32}{3}\pi},
$$
so the answer is (A).


::: pf-proof

Using the disk method and step [](#s1-2){.pf-ref},
$$
\begin{aligned}
V
&=\pi\int_0^4 y\,dy+\pi\int_4^6(6-y)^2\,dy\\
&=\pi\left[\frac{y^2}{2}\right]_0^4
+\pi\left[-\frac{(6-y)^3}{3}\right]_4^6\\
&=8\pi+\frac{8\pi}{3}
=\frac{32\pi}{3}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested volume and corresponding choice.

:::

:::

:::
