---
schema: qual/card@1
id: P-GRECH5-07
kind: problem
title: Rank minus determinant of a $3\times3$ matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Rank
  - Determinants
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 7 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
For the matrix

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}
$$

let $r$ denote its rank and $d$ denote its determinant. What is the value of $r - d$?

(A) $-2$
(B) $-1$
(C) $0$
(D) $1$
(E) $2$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The rows of $A$ satisfy
$$
R_3-2R_2+R_1=0.
$$


::: pf-proof

Indeed,
$$
(7,8,9)-2(4,5,6)+(1,2,3)=(0,0,0).
$$
Thus the three rows are linearly dependent.

:::

:::

::: {.pf-step #s1-2}

The rank of $A$ is $r=2$.


::: pf-proof

Step [](#s1-1){.pf-ref} gives $r\le 2$. The first two rows $(1,2,3)$ and $(4,5,6)$ are not scalar multiples of one another, so they are linearly independent. Hence $r\ge 2$, and therefore $r=2$.

:::

:::

::: {.pf-step #s1-3}

The determinant of $A$ is $d=0$.


::: pf-proof

By step [](#s1-1){.pf-ref}, the rows of $A$ are linearly dependent. A square matrix with linearly dependent rows is singular, so its determinant is zero.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{r-d=2},
$$
so the answer is (E).


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, $r-d=2-0=2$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value.

:::

:::

:::
