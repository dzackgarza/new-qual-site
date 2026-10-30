---
schema: qual/card@1
id: P-GRECH1-08
kind: problem
title: Classify a quadratic plane curve
classification:
  areas:
  - algebra
  topics:
  - Conic Sections
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 8 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Which of the following best describes the graph of the equation $x^2 + y^2 - 2x + 4y + 5 = 0$ in the $xy$-plane?

(A) circle
(B) parabola
(C) ellipse
(D) line
(E) point
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The equation is equivalent to
$$
(x-1)^2+(y+2)^2=0.
$$


::: pf-proof

Complete the two squares:
$$
\begin{aligned}
x^2-2x+y^2+4y+5=0
&\iff (x-1)^2-1+(y+2)^2-4+5=0\\
&\iff (x-1)^2+(y+2)^2=0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

The graph consists of the single point
$$
\boxed{(1,-2)},
$$
so the answer is (E), point.


::: pf-proof

Both terms in step [](#s1-1){.pf-ref} are squares of real numbers and hence are nonnegative. Their sum is zero exactly when both vanish, which gives $x=1$ and $y=-2$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} identifies the entire graph and its corresponding choice.

:::

:::

:::
