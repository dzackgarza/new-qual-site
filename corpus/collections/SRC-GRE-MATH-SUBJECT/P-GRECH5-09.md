---
schema: qual/card@1
id: P-GRECH5-09
kind: problem
title: Parameter making a $4\times4$ matrix singular
classification:
  areas:
  - applied-algebra
  topics:
  - Determinants
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 9 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
For what value of $x$ will the following matrix be noninvertible?

$$
\begin{pmatrix} 7 & 6 & 0 & 1 \\ 5 & 4 & x & 0 \\ 8 & 7 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{pmatrix}
$$

(A) $-1$
(B) $0$
(C) $1$
(D) $3$
(E) $9$
:::

::: {.solution}

Let
$$
M=
\begin{pmatrix}
7&6&0&1\\
5&4&x&0\\
8&7&0&1\\
0&0&1&1
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

The determinant of $M$ is
$$
\det M=-x-1.
$$


::: pf-proof

First replace $R_3$ by $R_3-R_1$. With the resulting third row $(1,1,0,0)$, replace $R_1$ by $R_1-7R_3$ and $R_2$ by $R_2-5R_3$. These row replacements preserve the determinant and give
$$
\begin{pmatrix}
0&-1&0&1\\
0&-1&x&0\\
1&1&0&0\\
0&0&1&1
\end{pmatrix}.
$$
Expanding along the first column gives
$$
\det M=
\det
\begin{pmatrix}
-1&0&1\\
-1&x&0\\
0&1&1
\end{pmatrix}
=-x-1.
$$

:::

:::

::: {.pf-step #s1-2}

The matrix is noninvertible exactly when
$$
\boxed{x=-1},
$$
so the answer is (A).


::: pf-proof

A square matrix is noninvertible exactly when its determinant is zero. By step [](#s1-1){.pf-ref}, this condition is $-x-1=0$, whose unique solution is $x=-1$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested parameter.

:::

:::

:::
