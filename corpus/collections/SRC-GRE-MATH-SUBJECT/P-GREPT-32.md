---
schema: qual/card@1
id: P-GREPT-32
kind: problem
title: "Lines in the tangent plane to $x^2-xy^2z+z^2=1$ at $(1,1,1)$"
classification:
  areas: [prelim]
  topics:
  - Tangent Planes
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 32 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $S$ be the surface whose equation is $x^2 - xy^2z + z^2 = 1$. The plane tangent to $S$ at the point $(1, 1, 1)$ contains which of the following lines?

(A) $x = y = z$
(B) $x = y$, $z = 1$
(C) $x = z$, $y = 1$
(D) $y = z$, $x = 1$
(E) $x - 1 = 2(y - 1) = z - 1$
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
F(x,y,z)=x^2-xy^2z+z^2.
$$
At $P=(1,1,1)$,
$$
\nabla F(P)=(1,-2,1).
$$


::: pf-proof

The partial derivatives are
$$
F_x=2x-y^2z,
\qquad
F_y=-2xyz,
\qquad
F_z=-xy^2+2z.
$$
Evaluating at $(1,1,1)$ gives $(1,-2,1)$.

:::

:::

::: {.pf-step #s1-2}

The tangent plane to $S$ at $P$ is
$$
x-2y+z=0.
$$


::: pf-proof

Since $\nabla F(P)\ne0$, it is a normal vector to the level surface
$F=1$ at $P$. Thus the tangent plane is
$$
(1,-2,1)\cdot(x-1,y-1,z-1)=0,
$$
which simplifies to $x-2y+z=0$.

:::

:::

::: {.pf-step #s1-3}

The line
$$
\boxed{x=y=z}
$$
lies in this tangent plane, so the answer is (A).


::: pf-proof

Every point on the line has the form $(t,t,t)$. Substitution into the plane
equation from step [](#s1-2){.pf-ref} gives
$$
t-2t+t=0
$$
for every $t\in\RR$. Hence the whole line is contained in the tangent plane.
The remaining choices are not contained in it: choices (B), (C), and (D)
contain respectively $(0,0,1)$, $(0,1,0)$, and $(1,0,0)$, none of which
satisfies $x-2y+z=0$; choice (E) contains $(2,3/2,2)$, which also does not
satisfy that equation.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies one of the listed lines contained in the tangent plane.

:::

:::

:::
