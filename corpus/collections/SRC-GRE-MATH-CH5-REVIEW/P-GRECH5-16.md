---
schema: qual/card@1
id: P-GRECH5-16
kind: problem
title: Composition of a quarter-turn and reflection
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
  note: Re-transcribed from Chapter 5 review Question 16 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
Define linear operators $S$ and $T$ on the $xy$-plane ($\RR^2$) as follows: $S$ rotates each vector $90^\circ$ counterclockwise, and $T$ reflects each vector through the $y$-axis. If $ST$ and $TS$ denote the compositions $S \circ T$ and $T \circ S$, respectively, and $I$ is the identity map, which of the following is true?

(A) $ST = I$
(B) $ST = -I$
(C) $TS = I$
(D) $ST = TS$
(E) $ST = -TS$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In the standard basis, the matrices of $S$ and $T$ are
$$
[S]=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},
\qquad
[T]=\begin{pmatrix}-1&0\\ 0&1\end{pmatrix}.
$$


::: pf-proof

A $90^\circ$ counterclockwise rotation sends $(1,0)$ to $(0,1)$ and $(0,1)$ to $(-1,0)$, giving the two columns of $[S]$. Reflection through the $y$-axis sends $(1,0)$ to $(-1,0)$ and fixes $(0,1)$, giving the two columns of $[T]$.

:::

:::

::: {.pf-step #s1-2}

The two compositions satisfy
$$
[ST]=\begin{pmatrix}0&-1\\ -1&0\end{pmatrix},
\qquad
[TS]=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}.
$$


::: pf-proof

Because $ST=S\circ T$ and $TS=T\circ S$, step [](#s1-1){.pf-ref} gives
$$
[ST]=[S][T]
=\begin{pmatrix}0&-1\\ -1&0\end{pmatrix}
$$
and
$$
[TS]=[T][S]
=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{ST=-TS},
$$
so the answer is (E).


::: pf-proof

The two matrices in step [](#s1-2){.pf-ref} are negatives of one another. Equality of standard matrices is equivalent to equality of the corresponding linear operators.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the true relation.

:::

:::

:::
