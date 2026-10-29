---
schema: qual/card@1
id: P-UCLAB13F-10
kind: problem
title: Signature from signs of leading principal minors
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Let $A$ be an $n\times n$ Hermitian matrix and, for $1\le j\le n$, let $A_j$ be the submatrix consisting of the entries of $A$ in its first $j$ rows and columns. Suppose
$$
\det(A_j)\neq0\quad\text{for all }j,
\qquad
\det(A_1)>0.
$$
Give and prove a rule, in terms of the signs of the $\det(A_j)$, that determines the signature of the Hermitian form defined by $A$.
:::

::: {.solution}

Write
$$
\Delta_j=\det(A_j),
\qquad
\Delta_0=1.
$$
By hypothesis,
$$
\Delta_j\ne0
$$
for all $j$, and
$$
\Delta_1>0.
$$

::: pf

::: {.pf-step #s1-1}

The matrix $A$ admits a factorization
$$
\boxed{A=LDL^*}
$$
where $L$ is invertible lower triangular with diagonal entries $1$, and
$$
D=\operatorname{diag}(d_1,\ldots,d_n)
$$
has real nonzero entries
$$
\boxed{d_j=\frac{\Delta_j}{\Delta_{j-1}}}.
$$


::: pf-proof

The proof is by Gaussian elimination without row exchanges.
Because every leading principal minor is nonzero, each successive pivot is nonzero.
Since $A$ is Hermitian, eliminating below a pivot and applying the conjugate-transpose operations on columns produces a factorization
$$
A=LDL^*
$$
with $L$ unit lower triangular and $D$ diagonal real.

It remains to identify the diagonal entries.
For each $j$,
$$
A_j=L_jD_jL_j^*,
$$
where $L_j$ is the leading $j\times j$ block of $L$ and
$$
D_j=\operatorname{diag}(d_1,\ldots,d_j).
$$
Since $L_j$ is unit lower triangular,
$$
\det L_j=1.
$$
Therefore
$$
\Delta_j
=
\det A_j
=
\det D_j
=
d_1\cdots d_j.
$$
Likewise
$$
\Delta_{j-1}=d_1\cdots d_{j-1}.
$$
Hence
$$
d_j=\frac{\Delta_j}{\Delta_{j-1}}.
$$

:::

:::

::: {.pf-step #s1-2}

The Hermitian forms defined by $A$ and by $D$ have the same signature.


::: pf-proof

For $x\in\CC^n$,
$$
\overline{x}^{\,t}Ax
=
\overline{x}^{\,t}LDL^*x.
$$
Set
$$
y=L^*x.
$$
Since $L$ is invertible, $x\mapsto y$ is an invertible linear change of variables.
Thus
$$
\overline{x}^{\,t}Ax
=
\overline{y}^{\,t}Dy.
$$
An invertible change of coordinates preserves the numbers of positive and negative squares in a diagonalization of a Hermitian form.
Therefore $A$ and $D$ have the same inertia, hence the same signature.

:::

:::

::: {.pf-step #s1-3}

The number of negative entries among
$$
d_1,\ldots,d_n
$$
equals the number of sign changes in the sequence
$$
\Delta_0,\Delta_1,\ldots,\Delta_n.
$$


::: pf-proof

Since
$$
d_j=\frac{\Delta_j}{\Delta_{j-1}},
$$
one has
$$
d_j<0
$$
exactly when $\Delta_j$ and $\Delta_{j-1}$ have opposite signs.
That is precisely a sign change between consecutive terms of the sequence.

:::

:::

::: {.pf-step #s1-4}

Let $q$ be the number of sign changes in
$$
\boxed{
1=\Delta_0,\Delta_1,\ldots,\Delta_n.
}
$$
Then the Hermitian form defined by $A$ has
$$
\boxed{q\text{ negative squares}}
$$
and
$$
\boxed{n-q\text{ positive squares}}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, exactly $q$ diagonal entries of $D$ are negative.
Because every $\Delta_j$ is nonzero, every $d_j$ is nonzero, so the remaining $n-q$ diagonal entries are positive.
Step [](#s1-2){.pf-ref} transfers these inertia counts from $D$ to $A$.

:::

:::

::: {.pf-step #s1-5}

Equivalently, if the signature is defined as
$$
\sigma(A)=n_+-n_-,
$$
then
$$
\boxed{\sigma(A)=n-2q},
$$
where $q$ is the number of sign changes in
$$
1,\det A_1,\det A_2,\ldots,\det A_n.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
n_+=n-q,
\qquad
n_-=q.
$$
Therefore
$$
\sigma(A)
=(n-q)-q
=n-2q.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} prove the rule and its relation to the signs of the leading principal minors.

:::

:::

:::
