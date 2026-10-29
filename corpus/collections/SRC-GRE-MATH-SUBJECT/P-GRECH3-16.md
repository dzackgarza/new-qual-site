---
schema: qual/card@1
id: P-GRECH3-16
kind: problem
title: A second point on a tangent plane
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
  note: "Checked against Chapter 3 review Question 16 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. Choices (B) and (D) read (6,4,3) and (5,3,2) in the chapter-3.pdf extraction and (6,-4,3) and (5,3,-2) in the book extraction; neither reading lies in the plane 4x+5y-3z=6, and the book extraction is followed."
---

::: {.problem}
Let $P$ be the tangent plane to the surface
$$
y^2z-2xz^2+3x^2y=2
$$
at the point $Q=(1,1,1)$. Which of the following points also lies in $P$?

(A) $(4,5,-3)$
(B) $(6,-4,3)$
(C) $(3,-1,5)$
(D) $(5,3,-2)$
(E) $(-2,4,2)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
F(x,y,z)=y^2z-2xz^2+3x^2y,
$$
the gradient at $Q=(1,1,1)$ is
$$
\nabla F(Q)=(4,5,-3).
$$


::: pf-proof

The partial derivatives are
$$
F_x=-2z^2+6xy,\qquad
F_y=2yz+3x^2,\qquad
F_z=y^2-4xz.
$$
Evaluating at $Q=(1,1,1)$ gives
$$
F_x(Q)=4,\qquad F_y(Q)=5,\qquad F_z(Q)=-3.
$$

:::

:::

::: {.pf-step #s1-2}

The tangent plane at $Q$ has equation
$$
4x+5y-3z=6.
$$


::: pf-proof

The given surface is the level surface $F=2$. Since the gradient in step [](#s1-1){.pf-ref} is nonzero, it is normal to the tangent plane at $Q$. Hence the tangent plane is
$$
(4,5,-3)\cdot\bigl((x,y,z)-(1,1,1)\bigr)=0.
$$
Expanding gives
$$
4x+5y-3z=4+5-3=6.
$$

:::

:::

::: {.pf-step #s1-3}

Among the listed points, exactly
$$
\boxed{(-2,4,2)}
$$
lies in the tangent plane, so the answer is (E).


::: pf-proof

Substitution into the equation from step [](#s1-2){.pf-ref} gives
$$
4(-2)+5(4)-3(2)=-8+20-6=6,
$$
so $(-2,4,2)$ lies in the plane. For the other choices, the left-hand side $4x+5y-3z$ equals, respectively,
$$
50,\quad -5,\quad -8,\quad 41,
$$
none of which is $6$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the requested point and corresponding choice.

:::

:::

:::
