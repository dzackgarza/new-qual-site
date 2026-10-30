---
schema: qual/card@1
id: P-GRECH3-19
kind: problem
title: Direction of steepest temperature decrease
classification:
  areas:
  - real-analysis
  topics:
  - Gradient
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 19 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
The temperature at each point $(x,y,z)$ in a room is given by the equation $T(x,y,z)=9x^2-3y^2+6xyz$. A fly is currently hovering at the point $(2,2,2)$. In the direction of which of the following vectors should the fly move in order to cool off as rapidly as possible?

(A) $-5\hat{\mathbf{i}}-\hat{\mathbf{j}}-2\hat{\mathbf{k}}$
(B) $-4\hat{\mathbf{i}}-3\hat{\mathbf{j}}-\hat{\mathbf{k}}$
(C) $3\hat{\mathbf{i}}+\hat{\mathbf{j}}-6\hat{\mathbf{k}}$
(D) $-2\hat{\mathbf{i}}+8\hat{\mathbf{j}}-5\hat{\mathbf{k}}$
(E) $-6\hat{\mathbf{i}}+4\hat{\mathbf{j}}-3\hat{\mathbf{k}}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The temperature gradient at $(2,2,2)$ is
$$
\nabla T(2,2,2)=(60,12,24)=12(5,1,2).
$$


::: pf-proof

From
$$
T(x,y,z)=9x^2-3y^2+6xyz,
$$
one has
$$
T_x=18x+6yz,\qquad
T_y=-6y+6xz,\qquad
T_z=6xy.
$$
Evaluating at $(2,2,2)$ gives
$$
T_x=60,\qquad T_y=12,\qquad T_z=24.
$$

:::

:::

::: {.pf-step #s1-2}

The direction of most rapid decrease of $T$ at $(2,2,2)$ is the direction of
$$
-\nabla T(2,2,2).
$$


::: pf-proof

For any unit direction vector $\mathbf{u}$, the directional derivative is
$$
D_{\mathbf{u}}T
=\nabla T(2,2,2)\cdot\mathbf{u}.
$$
By the Cauchy--Schwarz inequality,
$$
D_{\mathbf{u}}T
\ge -\norm{\nabla T(2,2,2)},
$$
with equality exactly when $\mathbf{u}$ points opposite to the gradient. Hence the maximal rate of decrease is attained in the direction of $-\nabla T(2,2,2)$.

:::

:::

::: {.pf-step #s1-3}

The required listed direction is
$$
\boxed{-5\hat{\mathbf{i}}-\hat{\mathbf{j}}-2\hat{\mathbf{k}}},
$$
so the answer is (A).


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
-\nabla T(2,2,2)=-12(5,1,2).
$$
Multiplying a nonzero direction vector by a positive scalar does not change its direction, so step [](#s1-2){.pf-ref} identifies $(-5,-1,-2)$, which is choice (A).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested direction and corresponding choice.

:::

:::

:::
