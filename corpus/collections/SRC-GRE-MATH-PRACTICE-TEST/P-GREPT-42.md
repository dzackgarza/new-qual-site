---
schema: qual/card@1
id: P-GREPT-42
kind: problem
title: "Dimension of the span of five vectors in $\\RR^4$"
classification:
  areas: [applied-algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 42 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Find the dimension of the subspace of $\RR^4$ that is the span of the following vectors:

$$\mathbf{v}_1 = \begin{pmatrix} 1 \\ -1 \\ 0 \\ 1 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} -2 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \quad \mathbf{v}_3 = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad \mathbf{v}_4 = \begin{pmatrix} -1 \\ 0 \\ 1 \\ 2 \end{pmatrix}, \text{ and } \mathbf{v}_5 = \begin{pmatrix} 1 \\ 1 \\ -2 \\ -5 \end{pmatrix}$$

(A) $1$
(B) $2$
(C) $3$
(D) $4$
(E) $5$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The vectors $\mathbf v_1$ and $\mathbf v_2$ are linearly independent.


::: pf-proof

Neither vector is zero, and they are not scalar multiples: the first
coordinate would require a scalar $-2$, while the second coordinate would then
be $2$, not $1$. Thus they are independent.

:::

:::

::: {.pf-step #s1-2}

The remaining nonzero vectors lie in
$\operatorname{span}\{\mathbf v_1,\mathbf v_2\}$:
$$
\mathbf v_4=\mathbf v_1+\mathbf v_2,
\qquad
\mathbf v_5=-3\mathbf v_1-2\mathbf v_2.
$$


::: pf-proof

Direct coordinatewise addition gives
$$
\mathbf v_1+\mathbf v_2
=(-1,0,1,2)^T
=\mathbf v_4,
$$
and
$$
-3\mathbf v_1-2\mathbf v_2
=(1,1,-2,-5)^T
=\mathbf v_5.
$$
Also $\mathbf v_3=0$ belongs to every subspace.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\dim\operatorname{span}\{\mathbf v_1,\ldots,\mathbf v_5\}=\boxed{2},
$$
so the answer is (B).


::: pf-proof

Step [](#s1-2){.pf-ref} shows that all five vectors lie in the span of
$\mathbf v_1,\mathbf v_2$, while step [](#s1-1){.pf-ref} shows that this span has dimension
$2$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required dimension.

:::

:::

:::
