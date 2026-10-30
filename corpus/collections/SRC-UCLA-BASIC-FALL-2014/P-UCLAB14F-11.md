---
schema: qual/card@1
id: P-UCLAB14F-11
kind: problem
title: An integer sum of squares of eigenvalues
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Suppose a $4\times4$ integer matrix has four distinct real eigenvalues
$$
\lambda_1>\lambda_2>\lambda_3>\lambda_4.
$$
Prove that
$$
\lambda_1^2+\lambda_2^2+\lambda_3^2+\lambda_4^2\in\ZZ.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The matrix $A$ is diagonalizable over $\RR$.


::: pf-proof

The four eigenvalues
$$
\lambda_1,\lambda_2,\lambda_3,\lambda_4
$$
are real and pairwise distinct.
Choose corresponding nonzero real eigenvectors
$$
v_1,v_2,v_3,v_4.
$$
Eigenvectors belonging to distinct eigenvalues are linearly independent.
Since the ambient space has dimension $4$, these four vectors form a basis.
Thus, in this basis,
$$
A
\sim
\operatorname{diag}
(\lambda_1,\lambda_2,\lambda_3,\lambda_4).
$$

:::

:::

::: {.pf-step #s1-2}

Consequently,
$$
A^2
\sim
\operatorname{diag}
(\lambda_1^2,\lambda_2^2,\lambda_3^2,\lambda_4^2).
$$


::: pf-proof

If
$$
A=SDS^{-1},
$$
then
$$
A^2
=
SD^2S^{-1}.
$$
Apply this with the diagonal matrix $D$ from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The trace of $A^2$ is
$$
\operatorname{Tr}(A^2)
=
\lambda_1^2+\lambda_2^2+\lambda_3^2+\lambda_4^2.
$$


::: pf-proof

Trace is invariant under similarity.
By step [](#s1-2){.pf-ref},
$$
\operatorname{Tr}(A^2)
=
\operatorname{Tr}
\operatorname{diag}
(\lambda_1^2,\lambda_2^2,\lambda_3^2,\lambda_4^2),
$$
which is the sum of the diagonal entries.

:::

:::

::: {.pf-step #s1-4}

The number
$$
\operatorname{Tr}(A^2)
$$
is an integer.


::: pf-proof

The matrix $A$ has integer entries.
Therefore the product
$$
A^2
$$
also has integer entries.
In particular, every diagonal entry of $A^2$ is an integer, so their sum
$$
\operatorname{Tr}(A^2)
$$
is an integer.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\lambda_1^2+\lambda_2^2+\lambda_3^2+\lambda_4^2
\in\ZZ
}.
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
