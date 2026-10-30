---
schema: qual/card@1
id: P-GRECH3-07
kind: problem
title: Plane containing a line and a point
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
  note: "Checked against Chapter 3 review Question 7 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
If $L$ is the line through the point $A=(3,2,1)$ and parallel to the vector $\mathbf{v}=(-2,1,3)$, what's the equation of the plane that contains $L$ and the point $B=(-2,3,1)$?

(A) $-x+y+z=6$
(B) $3x-2y-z=4$
(C) $x+6y-11z=5$
(D) $x+5y-z=12$
(E) $2x+10y-19z=7$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The plane contains the two independent direction vectors
$$
\mathbf{v}=(-2,1,3)
\qquad\text{and}\qquad
\overrightarrow{AB}=(-5,1,0).
$$


::: pf-proof

The line $L$ passes through $A$ with direction vector $\mathbf{v}$, so every plane containing $L$ contains $\mathbf{v}$ as a direction vector. Since the plane also contains $A$ and $B$,
$$
\overrightarrow{AB}=B-A=(-2,3,1)-(3,2,1)=(-5,1,0)
$$
is another direction vector in the plane. These vectors are independent because they are not scalar multiples of one another.

:::

:::

::: {.pf-step #s1-2}

A normal vector to the plane is
$$
\mathbf{n}=(1,5,-1).
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, a normal vector is obtained from the cross product
$$
\overrightarrow{AB}\times\mathbf{v}
=(-5,1,0)\times(-2,1,3)
=(3,15,-3)
=3(1,5,-1).
$$
Thus $\mathbf{n}=(1,5,-1)$ is normal to the plane.

:::

:::

::: {.pf-step #s1-3}

The plane has equation
$$
\boxed{x+5y-z=12},
$$
so the answer is (D).


::: pf-proof

Using the normal vector from step [](#s1-2){.pf-ref} and the point $A=(3,2,1)$, the plane equation is
$$
(1,5,-1)\cdot\bigl((x,y,z)-(3,2,1)\bigr)=0.
$$
Expanding gives
$$
x-3+5(y-2)-(z-1)=0,
$$
which simplifies to $x+5y-z=12$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required plane equation and corresponding choice.

:::

:::

:::
