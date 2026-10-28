---
schema: qual/card@1
id: P-GRECH5-06
kind: problem
title: Exceptional parameter for a basis of $\RR^3$
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 6 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
The vectors $\mathbf{v}_1 = (-1, 1, 1)$, $\mathbf{v}_2 = (1, 1, 1)$, and $\mathbf{v}_3 = (1, -1, k)$ form a basis for $\RR^3$ for all real values of $k$ EXCEPT $k =$

(A) $-2$
(B) $-1$
(C) $0$
(D) $1$
(E) $2$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The three vectors form a basis of $\RR^3$ exactly when the determinant of the matrix having them as rows is nonzero.


::: pf-proof

Three vectors in $\RR^3$ form a basis exactly when they are linearly independent. The rows of a square matrix are linearly independent exactly when that matrix is invertible, equivalently when its determinant is nonzero.

:::

:::

::: {.pf-step #s1-2}

For
$$
M=
\begin{pmatrix}
-1&1&1\\
1&1&1\\
1&-1&k
\end{pmatrix},
$$
one has
$$
\det M=-2(k+1).
$$


::: pf-proof

Replace the second row by the sum of the first and second rows, and replace the third row by the sum of the first and third rows. These row replacements do not change the determinant and give
$$
\begin{pmatrix}
-1&1&1\\
0&2&2\\
0&0&k+1
\end{pmatrix}.
$$
This matrix is upper triangular, so its determinant is the product of its diagonal entries, namely $(-1)\cdot 2\cdot(k+1)=-2(k+1)$.

:::

:::

::: {.pf-step #s1-3}

The exceptional parameter is
$$
\boxed{k=-1},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-1){.pf-ref}, failure to be a basis occurs exactly when $\det M=0$. By step [](#s1-2){.pf-ref}, this is equivalent to $-2(k+1)=0$, hence to $k=-1$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the unique real parameter for which the three vectors fail to form a basis.

:::

:::

:::
