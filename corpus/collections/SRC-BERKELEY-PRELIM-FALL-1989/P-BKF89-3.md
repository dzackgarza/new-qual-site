---
schema: qual/card@1
id: P-BKF89-3
kind: problem
title: An upper-triangular real matrix commuting with its transpose is diagonal
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $A$ be a real upper-triangular $n\times n$ matrix that commutes with its transpose. Prove that $A$ is diagonal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The assertion holds for $n=1$.

::: pf-proof

Every $1\times1$ matrix is diagonal.

:::

:::

::: {.pf-step #s2}

Suppose $n>1$. The equality
$$
AA^{\mathsf T}=A^{\mathsf T}A
$$
forces every off-diagonal entry in the first row of $A$ to vanish.

::: pf-proof

Because $A$ is upper triangular, its first column is
$$
(a_{11},0,\ldots,0)^{\mathsf T}.
$$
Hence
$$
(A^{\mathsf T}A)_{11}=a_{11}^2.
$$
On the other hand,
$$
(AA^{\mathsf T})_{11}
=
\sum_{j=1}^n a_{1j}^2.
$$
Since the two matrices are equal,
$$
\sum_{j=1}^n a_{1j}^2=a_{11}^2,
$$
so
$$
\sum_{j=2}^n a_{1j}^2=0.
$$
All summands are nonnegative, hence
$$
a_{1j}=0
\qquad
(j>1).
$$

:::

:::

::: {.pf-step #s3}

Consequently,
$$
A=
\begin{pmatrix}
a_{11}&0\\
0&A_1
\end{pmatrix},
$$
where $A_1$ is a real upper-triangular $(n-1)\times(n-1)$ matrix satisfying
$$
A_1A_1^{\mathsf T}=A_1^{\mathsf T}A_1.
$$

::: pf-proof

Upper triangularity already makes all entries below $a_{11}$ in the first column zero, and step [](#s2){.pf-ref} makes all entries to the right of $a_{11}$ in the first row zero. Thus $A$ has the displayed block form, with $A_1$ upper triangular.

Substituting the block form into
$$
AA^{\mathsf T}=A^{\mathsf T}A
$$
and comparing the lower-right blocks gives
$$
A_1A_1^{\mathsf T}=A_1^{\mathsf T}A_1.
$$

:::

:::

::: {.pf-step #s4}

The matrix $A$ is diagonal.

::: pf-proof

Proceed by induction on $n$. Step [](#s1){.pf-ref} is the base case. For $n>1$, step [](#s3){.pf-ref} reduces the lower-right block to an $(n-1)\times(n-1)$ upper-triangular matrix commuting with its transpose. By the induction hypothesis, $A_1$ is diagonal. The block form in step [](#s3){.pf-ref} then shows that $A$ itself is diagonal.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{A\text{ is diagonal}}.
$$

::: pf-proof

This is step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
