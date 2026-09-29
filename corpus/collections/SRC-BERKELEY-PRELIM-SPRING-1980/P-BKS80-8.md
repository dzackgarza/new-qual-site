---
schema: qual/card@1
id: P-BKS80-8
kind: problem
title: Four assertions about diagonalizable matrices
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked explicit two-by-two counterexamples for the sum and product
    assertions, the squarefree minimal-polynomial proof for idempotents, and
    the invariant eigenspace decomposition of A^2 in the invertible case.
---

::: {.problem}
Let $A,B$ be complex $n\times n$ matrices. Prove or disprove each assertion:

1. If $A$ and $B$ are diagonalizable, then $A+B$ is diagonalizable.
2. If $A$ and $B$ are diagonalizable, then $AB$ is diagonalizable.
3. If $A^2=A$, then $A$ is diagonalizable.
4. If $A$ is invertible and $A^2$ is diagonalizable, then $A$ is diagonalizable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Assertion (1) is false.

::: pf-proof

Take
$$
A=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&1\\
0&1
\end{pmatrix}.
$$
The matrix $A$ is diagonal. The matrix $B$ has the two distinct
eigenvalues $0$ and $1$, so it is diagonalizable over $\CC$. But
$$
A+B
=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
$$
has characteristic polynomial $(t-1)^2$ and is not the identity matrix.
Its $1$-eigenspace is one-dimensional, so it is not diagonalizable.

:::

:::

::: {.pf-step #s2}

Assertion (2) is false.

::: pf-proof

Take
$$
A=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1&1\\
0&1/2
\end{pmatrix}.
$$
Again $A$ is diagonal, while $B$ has the two distinct eigenvalues $1$ and
$1/2$, so $B$ is diagonalizable. However,
$$
AB
=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
$$
which is the same nondiagonalizable Jordan block as in step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

Assertion (3) is true.

::: pf-proof

If $A^2=A$, then
$$
A(A-I)=0.
$$
Hence the minimal polynomial of $A$ divides
$$
t(t-1).
$$
This polynomial splits over $\CC$ and has no repeated root. Therefore the
minimal polynomial of $A$ also splits with no repeated root, which is
equivalent to diagonalizability over $\CC$.

:::

:::

::: {.pf-step #s4}

Suppose $A$ is invertible and $A^2$ is diagonalizable. Then every
eigenspace of $A^2$ is invariant under $A$.

::: pf-proof

Let
$$
E_\mu\coloneqq\ker(A^2-\mu I)
$$
be an eigenspace of $A^2$. If $v\in E_\mu$, then
$$
A^2(Av)
=
A(A^2v)
=
A(\mu v)
=
\mu Av.
$$
Thus $Av\in E_\mu$.

:::

:::

::: {.pf-step #s5}

For every eigenvalue $\mu$ of $A^2$, the restriction
$$
A|_{E_\mu}
$$
is diagonalizable.

::: pf-proof

Because $A$ is invertible, $A^2$ is invertible, so $\mu\ne0$. On
$E_\mu$ one has
$$
(A|_{E_\mu})^2=\mu I.
$$
Therefore the minimal polynomial of the restriction divides
$$
t^2-\mu.
$$
Over $\CC$, this polynomial has the two distinct roots
$$
\sqrt\mu
\qquad\text{and}\qquad
-\sqrt\mu,
$$
because $\mu\ne0$. Thus the restriction is diagonalizable.

:::

:::

::: {.pf-step #s6}

Assertion (4) is true.

::: pf-proof

Since $A^2$ is diagonalizable,
$$
\CC^n
=
\bigoplus_{\mu\in\Spec(A^2)}E_\mu.
$$
By step [](#s4){.pf-ref} each summand is $A$-invariant, and by step [](#s5){.pf-ref} the
restriction of $A$ to each summand has a basis of eigenvectors. Combining
these bases gives an eigenbasis of $\CC^n$ for $A$. Hence $A$ is
diagonalizable.

:::

:::

::: {.pf-step #s7}

Therefore the answers are
$$
\boxed{
(1)\ \text{false},\qquad
(2)\ \text{false},\qquad
(3)\ \text{true},\qquad
(4)\ \text{true}.
}
$$

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give counterexamples to the first two assertions, while
steps [](#s3){.pf-ref} and [](#s6){.pf-ref} prove the last two.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} gives the complete requested classification.

:::

:::

:::
