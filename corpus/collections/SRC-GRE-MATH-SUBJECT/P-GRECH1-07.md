---
schema: qual/card@1
id: P-GRECH1-07
kind: problem
title: Locus equidistant from two points
classification:
  areas:
  - algebra
  topics:
  - Analytic Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 7 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription. Choice (A) reads 2x - y = 3 in this extraction and 2x - 3y = 3 in the chapter-1.pdf extraction.
---

::: {.problem}
What's the equation of all points in the $xy$-plane that are equidistant from the points $(-1, 4)$ and $(5, -2)$?

(A) $2x - y = 3$
(B) $x - y = 1$
(C) $x + y = 3$
(D) $y = x^2 - 4x + 1$
(E) $(x - 2)^2 + (y - 1)^2 = 18$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A point $(x,y)$ is equidistant from $(-1,4)$ and $(5,-2)$ exactly when
$$
(x+1)^2+(y-4)^2=(x-5)^2+(y+2)^2.
$$


::: pf-proof

The two squared Euclidean distances are respectively
$$
(x+1)^2+(y-4)^2
\quad\text{and}\quad
(x-5)^2+(y+2)^2.
$$
The distances are nonnegative, so they are equal exactly when their squares are equal.

:::

:::

::: {.pf-step #s1-2}

The locus is
$$
\boxed{x-y=1},
$$
so the answer is (B).


::: pf-proof

Expanding the equation in step [](#s1-1){.pf-ref} gives
$$
x^2+2x+1+y^2-8y+16
=x^2-10x+25+y^2+4y+4.
$$
After cancellation this becomes
$$
12x-12y=12,
$$
equivalently $x-y=1$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the complete equidistance locus and identifies the corresponding choice.

:::

:::

:::
