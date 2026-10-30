---
schema: qual/card@1
id: P-GRECH7-33
kind: problem
title: Unoriented incidence matrix of a drawn graph
classification:
  areas: [prelim]
  topics:
  - Graph Theory
  - Incidence Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 33 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The figure was not recovered by either extraction.
---

::: {.problem}
Which of the following represents the unoriented incidence matrix for the graph shown?

(A) $\begin{bmatrix} 1 & 1 & 0 & 0 & 1 \\ 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 \\ 0 & 1 & 0 & 1 & 0 \end{bmatrix}$
(B) $\begin{bmatrix} 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 \\ 1 & 0 & 0 & 1 & 0 \end{bmatrix}$
(C) $\begin{bmatrix} 0 & 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 \end{bmatrix}$
(D) $\begin{bmatrix} 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1 & 0 \end{bmatrix}$
(E) $\begin{bmatrix} 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 \\ 1 & 0 & 0 & 0 & 1 \end{bmatrix}$
:::

::: {.remark}
The source shows the graph in a figure that is not reproduced here.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

From the source figure, the five edges have endpoints
$$
e_1=\{v_1,v_4\},\quad
e_2=\{v_1,v_2\},\quad
e_3=\{v_2,v_3\},\quad
e_4=\{v_3,v_4\},\quad
e_5=\{v_1,v_3\}.
$$


::: pf-proof

These incidences are read directly from the labeled graph: $e_1$ is the upper-left slanted edge, $e_2$ the top horizontal edge, $e_3$ the upper-right slanted edge, $e_4$ the bottom horizontal edge, and $e_5$ the vertical edge from $v_1$ to $v_3$.

:::

:::

::: {.pf-step #s1-2}

Therefore the unoriented incidence matrix, with rows $v_1,v_2,v_3,v_4$ and columns $e_1,\ldots,e_5$, is
$$
\begin{bmatrix}
1&1&0&0&1\\
0&1&1&0&0\\
0&0&1&1&1\\
1&0&0&1&0
\end{bmatrix}.
$$


::: pf-proof

In an unoriented incidence matrix, the $(i,j)$ entry is $1$ exactly when $v_i$ is an endpoint of $e_j$. Applying this rule to the incidences in step [](#s1-1){.pf-ref} gives the displayed rows.

:::

:::

::: {.pf-step #s1-3}

Hence the answer is
$$
\boxed{\text{(B)}}.
$$


::: pf-proof

The matrix in step [](#s1-2){.pf-ref} is exactly choice (B).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required incidence matrix.

:::

:::

:::
