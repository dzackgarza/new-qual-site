---
schema: qual/card@1
id: P-GRECH3-08
kind: problem
title: Distance from the origin to a plane
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 8 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Find the perpendicular distance from the origin to the plane $x+2y+2z=6$.

(A) $1$
(B) $\frac{4}{3}$
(C) $2$
(D) $\frac{8}{3}$
(E) $3$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A line through the origin perpendicular to the plane is
$$
(x,y,z)=t(1,2,2).
$$


::: pf-proof

The vector
$$
\mathbf{n}=(1,2,2)
$$
is normal to the plane $x+2y+2z=6$, since its coordinates are the coefficients of $x,y,z$ in the plane equation. Hence the line through the origin in direction $\mathbf{n}$ is perpendicular to the plane.

:::

:::

::: {.pf-step #s1-2}

This perpendicular line meets the plane at
$$
P=\left(\frac23,\frac43,\frac43\right).
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, a point on the line has coordinates
$$
(x,y,z)=(t,2t,2t).
$$
Substituting these into the plane equation gives
$$
t+2(2t)+2(2t)=9t=6,
$$
so $t=2/3$. Substitution into the line parametrization yields the displayed point $P$.

:::

:::

::: {.pf-step #s1-3}

The perpendicular distance from the origin to the plane is
$$
\boxed{2},
$$
so the answer is (C).


::: pf-proof

By step [](#s1-1){.pf-ref}, the segment from the origin to the intersection point in step [](#s1-2){.pf-ref} is perpendicular to the plane. Its length is
$$
\|P\|
=\sqrt{\left(\frac23\right)^2+\left(\frac43\right)^2+\left(\frac43\right)^2}
=\sqrt{\frac{36}{9}}
=2.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested perpendicular distance and corresponding choice.

:::

:::

:::
