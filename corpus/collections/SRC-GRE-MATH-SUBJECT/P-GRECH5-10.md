---
schema: qual/card@1
id: P-GRECH5-10
kind: problem
title: Column-space compatibility parameter
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
  note: Re-transcribed from Chapter 5 review Question 10 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
For what value of $d$ is the vector $\mathbf{b} = (12, 11, d)^T$ in the column space of this matrix?

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}
$$

(A) $-26$
(B) $10$
(C) $13$
(D) $-10$
(E) $26$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The vector $\mathbf b$ lies in the column space of $A$ exactly when the linear system $A\mathbf x=\mathbf b$ is consistent.


::: pf-proof

The column space of $A$ consists precisely of all linear combinations of the columns of $A$, equivalently of all vectors of the form $A\mathbf x$.

:::

:::

::: {.pf-step #s1-2}

Row reduction of the augmented matrix gives
$$
\left(
\begin{array}{ccc|c}
1&2&3&12\\
4&5&6&11\\
7&8&9&d
\end{array}
\right)
\sim
\left(
\begin{array}{ccc|c}
1&2&3&12\\
0&-3&-6&-37\\
0&0&0&d-10
\end{array}
\right).
$$


::: pf-proof

First replace $R_2$ by $R_2-4R_1$ and $R_3$ by $R_3-7R_1$, obtaining
$$
\left(
\begin{array}{ccc|c}
1&2&3&12\\
0&-3&-6&-37\\
0&-6&-12&d-84
\end{array}
\right).
$$
Then replace $R_3$ by $R_3-2R_2$. Its final augmented entry is $(d-84)-2(-37)=d-10$, giving the displayed echelon form.

:::

:::

::: {.pf-step #s1-3}

The required value is
$$
\boxed{d=10},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-1){.pf-ref}, the augmented system must be consistent. By step [](#s1-2){.pf-ref}, consistency holds exactly when its last row does not assert $0=d-10\ne0$, hence exactly when $d-10=0$. Thus $d=10$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the unique value for which $\mathbf b$ belongs to the column space of $A$.

:::

:::

:::
