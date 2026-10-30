---
schema: qual/card@1
id: P-GRECH3-21
kind: problem
title: Normal vector to an implicit surface
classification:
  areas:
  - real-analysis
  topics:
  - Gradient
  - Normal Vectors
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 21 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Which of the following vectors is normal to the surface
$$
\log(x+y^2-z^3)=x-1
$$
at the point where $y=8$ and $z=4$?

(A) $\hat{\mathbf{i}}-\hat{\mathbf{j}}-2\hat{\mathbf{k}}$
(B) $2\hat{\mathbf{i}}-3\hat{\mathbf{j}}+\hat{\mathbf{k}}$
(C) $\hat{\mathbf{i}}+2\hat{\mathbf{j}}$
(D) $-2\hat{\mathbf{i}}+\hat{\mathbf{j}}+3\hat{\mathbf{k}}$
(E) $\hat{\mathbf{j}}-3\hat{\mathbf{k}}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The point on the surface with $y=8$ and $z=4$ is
$$
P=(1,8,4).
$$


::: pf-proof

Substituting $y=8$ and $z=4$ into the surface equation gives
$$
\log x=x-1,
$$
with $x>0$. Let
$$
g(x)=x-1-\log x.
$$
Then
$$
g'(x)=1-\frac1x=\frac{x-1}{x},
$$
so $g$ decreases on $(0,1)$ and increases on $(1,\infty)$. Since $g(1)=0$, its unique zero is $x=1$.

:::

:::

::: {.pf-step #s1-2}

For
$$
F(x,y,z)=\log(x+y^2-z^3)-x+1,
$$
one has
$$
\nabla F(P)=(0,16,-48)=16(0,1,-3).
$$


::: pf-proof

Writing $S=x+y^2-z^3$, the partial derivatives are
$$
F_x=\frac1S-1,\qquad
F_y=\frac{2y}{S},\qquad
F_z=-\frac{3z^2}{S}.
$$
At the point $P=(1,8,4)$ from step [](#s1-1){.pf-ref},
$$
S=1+8^2-4^3=1.
$$
Therefore
$$
\nabla F(P)=(0,16,-48)=16(0,1,-3).
$$

:::

:::

::: {.pf-step #s1-3}

A normal vector to the surface at $P$ is
$$
\boxed{\hat{\mathbf{j}}-3\hat{\mathbf{k}}},
$$
so the answer is (E).


::: pf-proof

The surface is the level set $F=0$. Since the gradient in step [](#s1-2){.pf-ref} is nonzero, it is normal to that level surface at $P$. Any nonzero scalar multiple is also normal, and
$$
\frac1{16}\nabla F(P)=(0,1,-3)
=\hat{\mathbf{j}}-3\hat{\mathbf{k}}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested normal vector and corresponding choice.

:::

:::

:::
