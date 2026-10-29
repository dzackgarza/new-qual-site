---
schema: qual/card@1
id: P-GRECH5-08
kind: problem
title: Determinant after column operations
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
  note: Re-transcribed from Chapter 5 review Question 8 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
If

$$
\det \begin{pmatrix} a & b & c \\ k & l & m \\ p & q & r \end{pmatrix} = d
$$

then

$$
\det \begin{pmatrix} k & 2(a - k) & p + k \\ l & 2(b - l) & q + l \\ m & 2(c - m) & r + m \end{pmatrix} =
$$

(A) $-8d$
(B) $-6d$
(C) $-2d$
(D) $2d$
(E) $8d$
:::

::: {.solution}

Let
$$
M=
\begin{pmatrix}
a&b&c\\
k&l&m\\
p&q&r
\end{pmatrix},
\qquad \det M=d.
$$

::: pf

::: {.pf-step #s1-1}

Transposing $M$ and then interchanging its first two columns produces a matrix of determinant $-d$.


::: pf-proof

Transposition preserves determinant, so $\det(M^{\mathsf T})=d$. Interchanging two columns multiplies the determinant by $-1$.

:::

:::

::: {.pf-step #s1-2}

Starting from the matrix in step [](#s1-1){.pf-ref}, add its first column to its third column, multiply its second column by $2$, and then subtract twice its first column from its second column. The resulting matrix is
$$
\begin{pmatrix}
k&2(a-k)&p+k\\
l&2(b-l)&q+l\\
m&2(c-m)&r+m
\end{pmatrix}.
$$


::: pf-proof

The columns of $M^{\mathsf T}$ are
$$
\begin{pmatrix}a\\ b\\ c\end{pmatrix},
\quad
\begin{pmatrix}k\\ l\\ m\end{pmatrix},
\quad
\begin{pmatrix}p\\ q\\ r\end{pmatrix}.
$$
After the interchange in step [](#s1-1){.pf-ref}, they are ordered as the second, first, and third of these columns. The three stated operations therefore transform them respectively into
$$
\begin{pmatrix}k\\ l\\ m\end{pmatrix},
\quad
2\begin{pmatrix}a-k\\ b-l\\ c-m\end{pmatrix},
\quad
\begin{pmatrix}p+k\\ q+l\\ r+m\end{pmatrix},
$$
which are precisely the columns of the displayed matrix.

:::

:::

::: {.pf-step #s1-3}

The determinant in the question is
$$
\boxed{-2d},
$$
so the answer is (C).


::: pf-proof

Adding a multiple of one column to another does not change the determinant. Thus, among the operations in step [](#s1-2){.pf-ref}, only multiplying the second column by $2$ changes the determinant, multiplying it by $2$. By step [](#s1-1){.pf-ref}, the determinant before those operations is $-d$, so the final determinant is $2(-d)=-2d$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested determinant.

:::

:::

:::
