---
schema: qual/card@1
id: P-UCLAB18F-11
kind: problem
title: Inner product on three-by-three skew-symmetric matrices
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $V$ be the vector space of real $3\times3$ skew-symmetric matrices.
Prove that
$$
\langle A,B\rangle=\frac12\operatorname{Tr}(AB^T)
$$
defines an inner product on $V$, and exhibit an orthonormal basis.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The formula
$$
\langle A,B\rangle
=
\frac12\operatorname{Tr}(AB^T)
$$
is bilinear in $A$ and $B$.


::: pf-proof

Matrix multiplication is bilinear, transpose is linear, and trace is linear.
Thus for scalars $\alpha,\beta$ and matrices $A_1,A_2,B$,
$$
\begin{aligned}
\langle \alpha A_1+\beta A_2,B\rangle
&=
\frac12\operatorname{Tr}
\bigl((\alpha A_1+\beta A_2)B^T\bigr)\\
&=
\alpha\langle A_1,B\rangle
+
\beta\langle A_2,B\rangle.
\end{aligned}
$$
The same argument applies in the second variable.

:::

:::

::: {.pf-step #s1-2}

The form is symmetric:
$$
\langle A,B\rangle
=
\langle B,A\rangle.
$$


::: pf-proof

Using invariance of trace under transpose,
$$
\begin{aligned}
\langle A,B\rangle
&=
\frac12\operatorname{Tr}(AB^T)\\
&=
\frac12\operatorname{Tr}\bigl((AB^T)^T\bigr)\\
&=
\frac12\operatorname{Tr}(BA^T)\\
&=
\langle B,A\rangle.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

For every $A=(a_{ij})\in V$,
$$
\langle A,A\rangle
=
\frac12\sum_{i,j=1}^3 a_{ij}^2.
$$


::: pf-proof

The $(i,i)$ entry of
$$
AA^T
$$
is
$$
\sum_{j=1}^3a_{ij}^2.
$$
Hence
$$
\operatorname{Tr}(AA^T)
=
\sum_{i,j=1}^3a_{ij}^2.
$$
Multiply by $1/2$.

:::

:::

::: {.pf-step #s1-4}

The form is positive definite.


::: pf-proof

Step [](#s1-3){.pf-ref} gives
$$
\langle A,A\rangle\ge0.
$$
Equality holds exactly when every entry $a_{ij}$ is zero, that is, exactly when
$$
A=0.
$$
Thus the form is positive definite.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\langle A,B\rangle
=
\frac12\operatorname{Tr}(AB^T)
}
$$
defines an inner product on $V$.


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, and [](#s1-4){.pf-ref} verify bilinearity, symmetry, and positive definiteness.

:::

:::

::: {.pf-step #s1-6}

Define
$$
E_1=
\begin{pmatrix}
0&1&0\\
-1&0&0\\
0&0&0
\end{pmatrix},
\quad
E_2=
\begin{pmatrix}
0&0&1\\
0&0&0\\
-1&0&0
\end{pmatrix},
\quad
E_3=
\begin{pmatrix}
0&0&0\\
0&0&1\\
0&-1&0
\end{pmatrix}.
$$
Then
$$
E_1,E_2,E_3
$$
form a basis of $V$.


::: pf-proof

Every real $3\times3$ skew-symmetric matrix has the form
$$
\begin{pmatrix}
0&a&b\\
-a&0&c\\
-b&-c&0
\end{pmatrix}
=
aE_1+bE_2+cE_3.
$$
This representation is unique, so the three matrices form a basis.

:::

:::

::: {.pf-step #s1-7}

The basis in step [](#s1-6){.pf-ref} is orthonormal.


::: pf-proof

Each $E_i$ has exactly two nonzero entries, namely $1$ and $-1$.
Hence step [](#s1-3){.pf-ref} gives
$$
\langle E_i,E_i\rangle
=
\frac12(1^2+(-1)^2)
=1.
$$

If $i\ne j$, the supports of $E_i$ and $E_j$ are disjoint.
Therefore
$$
\operatorname{Tr}(E_iE_j^T)
=
\sum_{r,s}(E_i)_{rs}(E_j)_{rs}
=0,
$$
so
$$
\langle E_i,E_j\rangle=0.
$$

:::

:::

::: {.pf-step #s1-8}

Thus an orthonormal basis is
$$
\boxed{
\left\{
\begin{pmatrix}
0&1&0\\
-1&0&0\\
0&0&0
\end{pmatrix},
\begin{pmatrix}
0&0&1\\
0&0&0\\
-1&0&0
\end{pmatrix},
\begin{pmatrix}
0&0&0\\
0&0&1\\
0&-1&0
\end{pmatrix}
\right\}.
}
$$


::: pf-proof

This follows from steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the inner-product assertion, and step [](#s1-8){.pf-ref} gives an explicit orthonormal basis.

:::

:::

:::
