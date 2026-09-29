---
schema: qual/card@1
id: P-BKS81-9
kind: problem
title: Equivalent invertibility criteria for $W\mapsto AW+WA$ on skew-symmetric matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction writes the second condition using undefined symbols a,b,c. Since the same sentence names the eigenvalues lambda_1,lambda_2,lambda_3 and the three conditions are asserted equivalent, the card records the corresponding pairwise eigenvalue sums and leaves this reconstruction explicit here.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the trace/eigenvalue equivalence and diagonalized the anticommutator map on the three independent skew-symmetric entries.
---

::: {.problem}
Let $A$ be a real symmetric $3\times3$ matrix with eigenvalues $\lambda_1,\lambda_2,\lambda_3$.
Show that the following are equivalent:

1. $\operatorname{tr}A$ is not an eigenvalue of $A$.
2. $(\lambda_1+\lambda_2)(\lambda_2+\lambda_3)(\lambda_1+\lambda_3)\ne0$.
3. The map $L:S\to S$ is an isomorphism, where $S$ is the space of real $3\times3$ skew-symmetric matrices and
   \[
   L(W)=AW+WA.
   \]
:::

::: {.solution}
::: pf

::: {.pf-step #trace-eigenvalue-equivalence}
Conditions (1) and (2) are equivalent.

::: pf-proof
Since
$$
\operatorname{tr}A=\lambda_1+\lambda_2+\lambda_3,
$$
one has
$$
\begin{aligned}
\operatorname{tr}A\ne\lambda_1
&\iff \lambda_2+\lambda_3\ne0,\\
\operatorname{tr}A\ne\lambda_2
&\iff \lambda_1+\lambda_3\ne0,\\
\operatorname{tr}A\ne\lambda_3
&\iff \lambda_1+\lambda_2\ne0.
\end{aligned}
$$
Thus $\operatorname{tr}A$ is not any eigenvalue of $A$ exactly when all
three pairwise sums are nonzero, which is condition (2).
:::

:::

::: {.pf-step #condition-two-iff-three}
Condition (2) is equivalent to condition (3).

::: pf-proof

::: {.pf-step #diagonalize-a}
Orthogonal diagonalization reduces the map $L$ to the case in which
$A$ is diagonal.

::: pf-proof
Because $A$ is real symmetric, there is an orthogonal matrix $Q$ such that
$$
Q^{\mathsf T}AQ
=
D
\coloneqq
\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3).
$$
Conjugation
$$
\Psi:S\longrightarrow S,
\qquad
\Psi(W)=Q^{\mathsf T}WQ,
$$
is a linear isomorphism, and
$$
\Psi(AW+WA)
=
D\Psi(W)+\Psi(W)D.
$$
Hence $L$ is an isomorphism exactly when
$$
L_D:S\longrightarrow S,
\qquad
L_D(W)=DW+WD,
$$
is an isomorphism.
:::

:::

::: {.pf-step #l-diagonal-entries}
In the standard coordinates on $S$, the map $L_D$ is diagonal with
diagonal entries
$$
\lambda_1+\lambda_2,
\qquad
\lambda_1+\lambda_3,
\qquad
\lambda_2+\lambda_3.
$$

::: pf-proof
Write
$$
W=
\begin{pmatrix}
0&u&v\\
-u&0&w\\
-v&-w&0
\end{pmatrix}.
$$
Then
$$
L_D(W)
=
\begin{pmatrix}
0&(\lambda_1+\lambda_2)u&(\lambda_1+\lambda_3)v\\
-(\lambda_1+\lambda_2)u&0&(\lambda_2+\lambda_3)w\\
-(\lambda_1+\lambda_3)v&-(\lambda_2+\lambda_3)w&0
\end{pmatrix}.
$$
Thus, under the coordinate identification $S\cong\RR^3$ given by
$(u,v,w)$, the map is diagonal with the asserted entries.
:::

:::

::: {.pf-step #l-iso-iff-condition-two}
Therefore $L$ is an isomorphism exactly when condition (2) holds.

::: pf-proof
By step [](#l-diagonal-entries){.pf-ref}, $L_D$ is invertible exactly when none of its three diagonal
entries is zero, equivalently when
$$
(\lambda_1+\lambda_2)
(\lambda_1+\lambda_3)
(\lambda_2+\lambda_3)
\ne0.
$$
Step [](#diagonalize-a){.pf-ref} transfers this criterion back to $L$.
:::

:::

::: pf-qed
Steps [](#diagonalize-a){.pf-ref}, [](#l-diagonal-entries){.pf-ref}, and [](#l-iso-iff-condition-two){.pf-ref} prove the equivalence of conditions (2) and (3).
:::

:::

:::

::: {.pf-step #all-three-equivalent}
Hence conditions (1), (2), and (3) are all equivalent.

::: pf-proof
Step [](#trace-eigenvalue-equivalence){.pf-ref} proves $(1)\iff(2)$, and step [](#condition-two-iff-three){.pf-ref} proves $(2)\iff(3)$.
:::

:::

::: pf-qed
Step [](#all-three-equivalent){.pf-ref} is the required equivalence.
:::

:::
:::
