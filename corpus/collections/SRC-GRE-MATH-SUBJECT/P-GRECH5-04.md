---
schema: qual/card@1
id: P-GRECH5-04
kind: problem
title: Powers of two unipotent matrices
classification:
  areas:
  - applied-algebra
  topics:
  - Matrices
  - Matrix Powers
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 4 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
If

$$
\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^n - \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}^n = \begin{pmatrix} 0 & 6 \\ -6 & 0 \end{pmatrix}
$$

then $n =$

(A) $-7$
(B) $-5$
(C) $5$
(D) $6$
(E) $7$
:::

::: {.solution}

Set
$$
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
M=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

For every integer $n$,
$$
(I+N)^n=I+nN,
\qquad
(I+M)^n=I+nM.
$$


::: pf-proof

One has $N^2=M^2=0$. For $n\ge0$, the binomial theorem therefore gives
$$
(I+N)^n=I+nN
$$
and similarly for $M$. Also
$$
(I+N)^{-1}=I-N,
\qquad
(I+M)^{-1}=I-M,
$$
so the same formulas hold for negative integers by applying the nonnegative case to the inverses.

:::

:::

::: {.pf-step #s1-2}

The matrix difference in the problem is
$$
\begin{pmatrix}
0&n\\
-n&0
\end{pmatrix}.
$$


::: pf-proof

The two matrices in the statement are $I+N$ and $I+M$. By step [](#s1-1){.pf-ref},
$$
(I+N)^n-(I+M)^n
=n(N-M)
=
\begin{pmatrix}
0&n\\
-n&0
\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\boxed{n=6},
$$
so the answer is (D).


::: pf-proof

Comparing the $(1,2)$ entry in step [](#s1-2){.pf-ref} with the given matrix
$$
\begin{pmatrix}
0&6\\
-6&0
\end{pmatrix}
$$
gives $n=6$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
