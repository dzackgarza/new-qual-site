---
schema: qual/card@1
id: P-UCLAB12-11
kind: problem
title: $LU$ factorization when the leading principal minors are nonzero
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Show that an $n$ by $n$ matrix $A$ can be factored as $A = LU$, where $L$ is lower triangular, and $U$ is upper triangular, provided each determinant $\det A_j$, for $j = 1, \ldots, n-1$, is non-zero, where $A_j$ is the submatrix of $A$ consisting of the first $j$ rows and the first $j$ columns.
:::

::: {.solution}

The proof is by induction on $n$.

::: pf

::: {.pf-step #s1-1}

The result holds for $n=1$.


::: pf-proof

If
\[
A=(a),
\]
take
\[
L=(1),
\qquad
U=(a).
\]
Then $A=LU$, with $L$ lower triangular and $U$ upper triangular.

:::

:::

::: {.pf-step #s1-2}

Assume $n\ge2$ and write
\[
A=
\begin{pmatrix}
a&r\\
c&D
\end{pmatrix},
\]
where $a\in\FF$, $r$ is a $1\times(n-1)$ row, $c$ is an $(n-1)\times1$ column, and $D$ is an $(n-1)\times(n-1)$ matrix.
Then
\[
a\ne0.
\]


::: pf-proof

The first leading principal minor is
\[
A_1=(a).
\]
By hypothesis,
\[
\det A_1=a\ne0.
\]

:::

:::

::: {.pf-step #s1-3}

Define the Schur complement
\[
S=D-\frac1a\,cr.
\]
For each $j=1,\ldots,n-2$, the leading $j\times j$ principal minor $S_j$ of $S$ satisfies
\[
\det S_j=\frac{\det A_{j+1}}{a}.
\]


::: pf-proof

The leading $(j+1)\times(j+1)$ principal block of $A$ has the form
\[
A_{j+1}
=
\begin{pmatrix}
a&r_j\\
c_j&D_j
\end{pmatrix},
\]
where
\[
S_j=D_j-\frac1a\,c_jr_j.
\]
Perform the block row operation
\[
\begin{pmatrix}
1&0\\
-c_j/a&I_j
\end{pmatrix}
\begin{pmatrix}
a&r_j\\
c_j&D_j
\end{pmatrix}
=
\begin{pmatrix}
a&r_j\\
0&S_j
\end{pmatrix}.
\]
The left multiplier has determinant $1$. Hence
\[
\det A_{j+1}
=
a\det S_j,
\]
which gives the formula.

:::

:::

::: {.pf-step #s1-4}

Every leading principal minor of $S$ required by the induction hypothesis is nonzero.


::: pf-proof

For $j=1,\ldots,n-2$, step [](#s1-3){.pf-ref} gives
\[
\det S_j
=
\frac{\det A_{j+1}}{a}.
\]
The numerator is nonzero by the hypothesis on $A$, and the denominator is nonzero by step [](#s1-2){.pf-ref}. Thus
\[
\det S_j\ne0.
\]

:::

:::

::: {.pf-step #s1-5}

By induction, there exist an $(n-1)\times(n-1)$ lower triangular matrix $L_1$ and upper triangular matrix $U_1$ such that
\[
S=L_1U_1.
\]


::: pf-proof

Step [](#s1-4){.pf-ref} verifies exactly the leading-principal-minor hypothesis for the matrix $S$ of size $n-1$. The induction hypothesis therefore applies.

:::

:::

::: {.pf-step #s1-6}

Define
\[
L=
\begin{pmatrix}
1&0\\
c/a&L_1
\end{pmatrix}
\]
and
\[
U=
\begin{pmatrix}
a&r\\
0&U_1
\end{pmatrix}.
\]
Then $L$ is lower triangular and $U$ is upper triangular.


::: pf-proof

The block forms are triangular because $L_1$ is lower triangular and $U_1$ is upper triangular.

:::

:::

::: {.pf-step #s1-7}

One has
\[
\boxed{A=LU}.
\]


::: pf-proof

Multiply the two block matrices from step [](#s1-6){.pf-ref}:
\[
\begin{aligned}
LU
&=
\begin{pmatrix}
1&0\\
c/a&L_1
\end{pmatrix}
\begin{pmatrix}
a&r\\
0&U_1
\end{pmatrix}\\
&=
\begin{pmatrix}
a&r\\
c&(c/a)r+L_1U_1
\end{pmatrix}.
\end{aligned}
\]
By step [](#s1-5){.pf-ref},
\[
L_1U_1=S=D-\frac1a\,cr.
\]
Therefore
\[
\frac1a\,cr+L_1U_1
=
D,
\]
and hence
\[
LU=
\begin{pmatrix}
a&r\\
c&D
\end{pmatrix}
=A.
\]

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the base case, and steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref} prove the induction step. Thus the factorization exists for every $n$ under the stated hypotheses.

:::

:::

:::
