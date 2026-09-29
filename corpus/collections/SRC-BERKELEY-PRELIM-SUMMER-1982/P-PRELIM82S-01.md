---
schema: qual/card@1
id: P-PRELIM82S-01
kind: problem
title: Jordan canonical form of an upper-triangular $3\times3$ matrix
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The triangular matrix has eigenvalues 1,4,4. For lambda=4,
    ker(A-4I) is one-dimensional, so the eigenvalue of algebraic
    multiplicity two has only one Jordan block, necessarily of size two.
    The eigenvalue 1 contributes its single one-dimensional block.
---

::: {.problem}
Determine the Jordan canonical form of
\[
A=\begin{pmatrix}
1&2&3\\
0&4&5\\
0&0&4
\end{pmatrix}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The characteristic polynomial of $A$ is
$$
\chi_A(t)
=
(t-1)(t-4)^2.
$$

::: pf-proof

The matrix $A$ is upper triangular. Hence its characteristic polynomial is
the product of
$$
t-a_{ii}
$$
over its diagonal entries:
$$
\chi_A(t)
=
(t-1)(t-4)(t-4).
$$

:::

:::

::: {.pf-step #s2}

The eigenspace for the eigenvalue $4$ is one-dimensional.

::: pf-proof

One has
$$
A-4I
=
\begin{pmatrix}
-3&2&3\\
0&0&5\\
0&0&0
\end{pmatrix}.
$$
If
$$
\begin{pmatrix}
x\\
y\\
z
\end{pmatrix}
\in
\ker(A-4I),
$$
then the second row gives
$$
5z=0,
$$
so $z=0$. The first row then gives
$$
-3x+2y=0.
$$
Thus
$$
\ker(A-4I)
=
\operatorname{span}
\left\{
\begin{pmatrix}
2\\
3\\
0
\end{pmatrix}
\right\},
$$
which has dimension $1$.

:::

:::

::: {.pf-step #s3}

The eigenvalue $4$ contributes exactly one Jordan block, and that
block has size $2$.

::: pf-proof

Step [](#s1){.pf-ref} shows that the algebraic multiplicity of $4$ is $2$. The number
of Jordan blocks for the eigenvalue $4$ equals
$$
\dim\ker(A-4I),
$$
which is $1$ by step [](#s2){.pf-ref}. Thus there is one block whose total size is
$2$, namely
$$
J_2(4)
=
\begin{pmatrix}
4&1\\
0&4
\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s4}

The eigenvalue $1$ contributes the one-dimensional block
$$
(1).
$$

::: pf-proof

By step [](#s1){.pf-ref}, the algebraic multiplicity of $1$ is $1$. Hence its entire
Jordan contribution is the unique block of size $1$.

:::

:::

::: {.pf-step #s5}

The Jordan canonical form is
$$
\boxed{
\begin{pmatrix}
1&0&0\\
0&4&1\\
0&0&4
\end{pmatrix}.
}
$$

::: pf-proof

Combine the blocks from steps [](#s3){.pf-ref} and [](#s4){.pf-ref}. Jordan blocks may be reordered,
so any permutation of these diagonal blocks is the same Jordan canonical
form up to block ordering.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the requested Jordan canonical form.

:::

:::

:::
