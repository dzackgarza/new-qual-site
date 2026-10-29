---
schema: qual/card@1
id: P-GRECH6-11
kind: problem
title: Subgroups of $\GL(2,\RR)$ defined by determinant, triangularity, and trace
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Re-transcribed from Chapter 6 review Question 11 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
Which of the following are subgroups of $\GL(2, \RR)$, the group of invertible $2$ by $2$ matrices (with real entries) under matrix multiplication?

I. $T = \{A \in \GL(2, \RR) : \det A = 2\}$

II. $U = \{A \in \GL(2, \RR) : A \text{ is upper triangular}\}$

III. $V = \{A \in \GL(2, \RR) : \tr(A) = 0\}$

Note: $\tr(A)$ denotes the trace of $A$, which is the sum of the entries on the main diagonal.

(A) I and II only
(B) II only
(C) II and III only
(D) III only
(E) I and III only
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The set $T$ is not a subgroup of $\GL(2,\RR)$.


::: pf-proof

The identity matrix has determinant $1$, so it does not belong to $T$. Hence $T$ cannot be a subgroup. Equivalently, if $A,B\in T$, then
$$
\det(AB)=\det(A)\det(B)=4\ne2,
$$
so $T$ is not closed under multiplication.

:::

:::

::: {.pf-step #s1-2}

The set $U$ is a subgroup of $\GL(2,\RR)$.


::: pf-proof

The identity matrix is upper triangular. The product of two upper-triangular matrices is upper triangular. Finally, if
$$
A=\begin{pmatrix}a&b\\0&d\end{pmatrix}\in U,
$$
then $a,d\ne0$ because $A$ is invertible, and
$$
A^{-1}=\begin{pmatrix}a^{-1}&-b/(ad)\\0&d^{-1}\end{pmatrix},
$$
which is again upper triangular. Thus $U$ contains the identity and is closed under multiplication and inverses.

:::

:::

::: {.pf-step #s1-3}

The set $V$ is not a subgroup of $\GL(2,\RR)$.


::: pf-proof

The identity matrix has trace $2$, not $0$, so it does not belong to $V$. Hence $V$ is not a subgroup.

:::

:::

::: {.pf-step #s1-4}

Therefore the only subgroup among I, II, and III is
$$
\boxed{\text{II only}},
$$
so the answer is (B).


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} show respectively that $T$ is not a subgroup, $U$ is a subgroup, and $V$ is not a subgroup.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
