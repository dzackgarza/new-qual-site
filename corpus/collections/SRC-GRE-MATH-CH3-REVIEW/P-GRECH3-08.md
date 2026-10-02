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
<1>1. A line through the origin perpendicular to the plane is
$$
(x,y,z)=t(1,2,2).
$$

::: {.proof}
The vector
$$
\mathbf{n}=(1,2,2)
$$
is normal to the plane $x+2y+2z=6$, since its coordinates are the coefficients of $x,y,z$ in the plane equation. Hence the line through the origin in direction $\mathbf{n}$ is perpendicular to the plane.
:::

<1>2. This perpendicular line meets the plane at
$$
P=\left(\frac23,\frac43,\frac43\right).
$$

::: {.proof}
By step <1>1, a point on the line has coordinates
$$
(x,y,z)=(t,2t,2t).
$$
Substituting these into the plane equation gives
$$
t+2(2t)+2(2t)=9t=6,
$$
so $t=2/3$. Substitution into the line parametrization yields the displayed point $P$.
:::

<1>3. The perpendicular distance from the origin to the plane is
$$
\boxed{2},
$$
so the answer is (C).

::: {.proof}
By step <1>1, the segment from the origin to the intersection point in step <1>2 is perpendicular to the plane. Its length is
$$
\|P\|
=\sqrt{\left(\frac23\right)^2+\left(\frac43\right)^2+\left(\frac43\right)^2}
=\sqrt{\frac{36}{9}}
=2.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested perpendicular distance and corresponding choice.
:::
:::
