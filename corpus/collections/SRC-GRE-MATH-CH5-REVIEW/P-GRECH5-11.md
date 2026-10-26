---
schema: qual/card@1
id: P-GRECH5-11
kind: problem
title: Dimension of a displayed span in $\RR^5$
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
  note: Re-transcribed from Chapter 5 review Question 11 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
What is the dimension of the following subspace of $\RR^5$?

\[
\operatorname{span} \left\{ \begin{pmatrix} 1 \\ 0 \\ -1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ -1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ -1 \\ 1 \\ -1 \\ 0 \end{pmatrix} \right\}
\]

(A) $1$
(B) $2$
(C) $3$
(D) $4$
(E) $5$
:::

Label the six displayed vectors $v_1,\dots,v_6$ in the order in which they occur.

::: pf

::: pf-step

The displayed subspace is
$$
\operatorname{span}\{v_1,v_2,v_5\}.
$$


::: pf-proof

The third vector is $v_3=0$, while
$$
v_4=-v_1,
\qquad
v_6=-v_2.
$$
Thus $v_3,v_4,v_6$ add no new vectors to the span, and the span of all six vectors equals the span of $v_1,v_2,v_5$.

:::

:::

::: pf-step

The vectors $v_1,v_2,v_5$ are linearly independent.


::: pf-proof

Suppose
$$
\alpha v_1+\beta v_2+\gamma v_5=0.
$$
The first coordinate gives $\alpha=0$, and the second coordinate gives $\beta=0$. With these values, the third coordinate gives $\gamma=0$. Hence the only linear relation is the trivial one.

:::

:::

::: pf-step

The dimension of the subspace is
$$
\boxed{3},
$$
so the answer is (C).


::: pf-proof

By step <1>1, the subspace is spanned by $v_1,v_2,v_5$, and by step <1>2 these three vectors are linearly independent. They therefore form a basis of the subspace, which consequently has dimension $3$.

:::

:::

::: pf-qed

Step <1>3 gives the requested dimension.

:::

:::
