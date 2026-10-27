---
schema: qual/card@1
id: P-GRECH3-03
kind: problem
title: Area of a triangle in three-space
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
  note: "Checked against Chapter 3 review Question 3 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. Choice (D), lost in the chapter-3.pdf extraction, is taken from the book extraction."
---

::: {.problem}
What's the area of the triangle whose vertices are $(0,0,1)$, $(0,2,0)$, and $(3,0,0)$?

(A) $\frac{8}{3}$
(B) $\frac{7}{2}$
(C) $3$
(D) $6$
(E) $7$
:::

Let
$$
A=(0,0,1),\qquad B=(0,2,0),\qquad C=(3,0,0).
$$

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Two side vectors issuing from $C$ are
$$
\overrightarrow{CB}=(-3,2,0),
\qquad
\overrightarrow{CA}=(-3,0,1).
$$


::: pf-proof

Subtracting the coordinates of $C$ from those of $B$ and $A$ gives
$$
B-C=(0,2,0)-(3,0,0)=(-3,2,0)
$$
and
$$
A-C=(0,0,1)-(3,0,0)=(-3,0,1).
$$

:::

:::

::: {.pf-step #s1-2}

Their cross product is
$$
\overrightarrow{CB}\times\overrightarrow{CA}
=(2,3,6).
$$


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
\begin{aligned}
(-3,2,0)\times(-3,0,1)
&=(2\cdot1-0\cdot0,\,
0\cdot(-3)-(-3)\cdot1,\,
(-3)\cdot0-2\cdot(-3))\\
&=(2,3,6).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The triangle has area
$$
\boxed{\frac72},
$$
so the answer is (B).


::: pf-proof

The area is one half the area of the parallelogram spanned by the two side vectors. By step [](#s1-2){.pf-ref},
$$
\begin{aligned}
\operatorname{Area}(\triangle ABC)
&=\frac12\norm{(2,3,6)}\\
&=\frac12\sqrt{2^2+3^2+6^2}\\
&=\frac12\sqrt{49}
=\frac72.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested area and corresponding choice.

:::

:::

:::
