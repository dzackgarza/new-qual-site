---
schema: qual/card@1
id: P-GRECH5-05
kind: problem
title: Entry of an inverse matrix
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
  note: Re-transcribed from Chapter 5 review Question 5 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
If the matrices

$$
\begin{pmatrix} 3 & -2 & -2 \\ -1 & 1 & 1 \\ 3 & -1 & -2 \end{pmatrix} \quad \text{and} \quad \begin{pmatrix} 1 & a & 0 \\ -1 & b & 1 \\ 2 & c & -1 \end{pmatrix}
$$

are inverses of each other, what is the value of $c$?

(A) $-3$
(B) $-2$
(C) $0$
(D) $2$
(E) $3$
:::

::: {.solution}

Let
$$
A=
\begin{pmatrix}
3&-2&-2\\
-1&1&1\\
3&-1&-2
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1&a&0\\
-1&b&1\\
2&c&-1
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

Since $A$ and $B$ are inverses, their middle columns in the equation $AB=I$ give
$$
3a-2b-2c=0,
\qquad
-a+b+c=1,
\qquad
3a-b-2c=0.
$$


::: pf-proof

The middle column of $B$ is $(a,b,c)^{\mathsf T}$. Therefore the middle column of $AB$ is
$$
A
\begin{pmatrix}
a\\ b\\ c
\end{pmatrix}
=
\begin{pmatrix}
3a-2b-2c\\
-a+b+c\\
3a-b-2c
\end{pmatrix}.
$$
The middle column of the identity matrix is $(0,1,0)^{\mathsf T}$, yielding the displayed system.

:::

:::

::: pf-step

The system in step [](#s1-1){.pf-ref} implies
$$
b=0.
$$


::: pf-proof

Subtract the third equation from the first:
$$
(3a-2b-2c)-(3a-b-2c)=-b=0.
$$

:::

:::

::: {.pf-step #s1-3}

One then has
$$
a=2,\qquad c=3.
$$


::: pf-proof

With $b=0$, the second and third equations become
$$
-a+c=1,
\qquad
3a-2c=0.
$$
The first gives $c=a+1$. Substitution into the second gives
$$
3a-2(a+1)=0,
$$
so $a=2$ and hence $c=3$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{c=3},
$$
so the answer is (E).


::: pf-proof

This is the value obtained in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested matrix entry and corresponding choice.

:::

:::

:::
