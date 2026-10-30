---
schema: qual/card@1
id: P-GRECH3-05
kind: problem
title: Intersection of a line and a plane
classification:
  areas:
  - real-analysis
  topics:
  - Lines and Planes
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 5 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. The chapter-3.pdf extraction read choice (A) as (5,4,1); the book extraction reads (5,-4,1), and the book's solution says choice (A) does not lie on the plane, which holds only for (5,-4,1)."
---

::: {.problem}
Let $L$ be the line in space that passes through the points $P=(-1,-2,4)$ and $Q=(4,2,1)$. At what point does $L$ intersect the plane $x+y+2z=11$?

(A) $(5,-4,1)$
(B) $(1,2,4)$
(C) $(8,9,-3)$
(D) $(6,7,-1)$
(E) $(9,6,-2)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A parametrization of $L$ is
$$
(x,y,z)=(-1,-2,4)+t(5,4,-3).
$$


::: pf-proof

The direction vector from $P$ to $Q$ is
$$
Q-P=(4,2,1)-(-1,-2,4)=(5,4,-3).
$$
Therefore every point of the line through $P$ and $Q$ has the displayed form.

:::

:::

::: {.pf-step #s1-2}

The point of $L$ lying in the plane occurs at $t=2$.


::: pf-proof

From step [](#s1-1){.pf-ref},
$$
x=-1+5t,\qquad y=-2+4t,\qquad z=4-3t.
$$
Substituting into $x+y+2z=11$ gives
$$
(-1+5t)+(-2+4t)+2(4-3t)=11,
$$
so
$$
5+3t=11,
$$
and hence $t=2$.

:::

:::

::: {.pf-step #s1-3}

The intersection point is
$$
\boxed{(9,6,-2)},
$$
so the answer is (E).


::: pf-proof

Substituting $t=2$ from step [](#s1-2){.pf-ref} into the parametrization from step [](#s1-1){.pf-ref} gives
$$
(-1+10,-2+8,4-6)=(9,6,-2).
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested intersection point and corresponding choice.

:::

:::

:::
