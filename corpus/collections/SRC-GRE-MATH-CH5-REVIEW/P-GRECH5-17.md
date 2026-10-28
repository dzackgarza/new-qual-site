---
schema: qual/card@1
id: P-GRECH5-17
kind: problem
title: Matrix of the cross-product operator
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
  note: Re-transcribed from Chapter 5 review Question 17 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
Choose a nonzero vector $\mathbf{v} = (a, b, c)^T$ in $\RR^3$ and define a linear operator $T\colon \RR^3 \to \RR^3$ by the equation $T(\mathbf{x}) = \mathbf{v} \times \mathbf{x}$, the cross product of $\mathbf{v}$ and $\mathbf{x}$. Then $T(\mathbf{x}) = A\mathbf{x}$ for every $\mathbf{x}$ in $\RR^3$ if $A =$

(A) $\begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ -b & a & 0 \end{pmatrix}$
(B) $\begin{pmatrix} 1 & -c & b \\ c & 1 & -a \\ -b & a & 1 \end{pmatrix}$
(C) $\begin{pmatrix} 0 & c & -b \\ -c & 0 & a \\ b & -a & 0 \end{pmatrix}$
(D) $\begin{pmatrix} 1 & c & -b \\ -c & 1 & a \\ b & -a & 1 \end{pmatrix}$
(E) $\begin{pmatrix} 0 & a & b \\ a & 1 & c \\ b & c & 0 \end{pmatrix}$
:::

::: {.solution}

Write $\mathbf x=(x,y,z)^T$.

::: pf

::: {.pf-step #s1-1}

The cross product is
$$
\mathbf v\times\mathbf x
=
\begin{pmatrix}
bz-cy\\
cx-az\\
ay-bx
\end{pmatrix}.
$$


::: pf-proof

Expanding the defining determinant for the cross product gives
$$
\mathbf v\times\mathbf x
=
\begin{vmatrix}
\mathbf e_1&\mathbf e_2&\mathbf e_3\\
a&b&c\\
x&y&z
\end{vmatrix}
=(bz-cy)\mathbf e_1-(az-cx)\mathbf e_2+(ay-bx)\mathbf e_3,
$$
which is the displayed vector.

:::

:::

::: {.pf-step #s1-2}

Therefore the matrix of $T$ in the standard basis is
$$
\boxed{
A=
\begin{pmatrix}
0&-c&b\\
c&0&-a\\
-b&a&0
\end{pmatrix}},
$$
so the answer is (A).


::: pf-proof

Multiplying the displayed matrix by $(x,y,z)^T$ yields
$$
\begin{pmatrix}
-cy+bz\\
cx-az\\
-bx+ay
\end{pmatrix},
$$
which equals $\mathbf v\times\mathbf x$ by step [](#s1-1){.pf-ref} for every $\mathbf x\in\RR^3$. Thus it is the required matrix representative.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the required matrix.

:::

:::

:::
