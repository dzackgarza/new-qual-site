---
schema: qual/card@1
id: P-GREPT-64
kind: problem
title: "Sum of determinants of the matrices with entries $i+j$"
classification:
  areas: [applied-algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 64 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $A$ is the $2$ by $2$ matrix whose $(i, j)$ entry is equal to $i + j$, and $B$ is the $3$ by $3$ matrix whose $(i, j)$ entry is equal to $i + j$, find the value of the sum $\det A + \det B$.

(A) $-2$
(B) $-1$
(C) $0$
(D) $2$
(E) $5$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

$\det A=-1$.


::: pf-proof

By the definition of the entries,
$$
A=
\begin{pmatrix}
2&3\\
3&4
\end{pmatrix},
$$
so
$$
\det A=2\cdot4-3\cdot3=-1.
$$

:::

:::

::: {.pf-step #s1-2}

$\det B=0$.


::: pf-proof

The matrix is
$$
B=
\begin{pmatrix}
2&3&4\\
3&4&5\\
4&5&6
\end{pmatrix}.
$$
First replace the third row by the third row minus the second, and then
replace the second row by the second row minus the first. Neither operation
changes the determinant, and the result is
$$
\begin{pmatrix}
2&3&4\\
1&1&1\\
1&1&1
\end{pmatrix}.
$$
This matrix has two equal rows, so its determinant is $0$.

:::

:::

::: {.pf-step #s1-3}

$\det A+\det B=\boxed{-1}$.


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref},
$$
\det A+\det B=-1+0=-1.
$$
Thus the correct choice is (B).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
