---
schema: qual/card@1
id: P-BERK98S-17
kind: problem
title: A trace-zero complex matrix is similar to one with zero diagonal
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
  date: 2026-09-24
---

::: {.problem}
Let $A$ be an $n\times n$ complex matrix with
\[
\operatorname{tr}A=0.
\]
Show that $A$ is similar to a matrix whose main diagonal consists entirely of zeros.
:::

::: {.solution}
Regard $A$ as the matrix of an endomorphism
$$
T:\CC^n\longrightarrow\CC^n.
$$

::: pf

::: {.pf-step #s1}

The assertion holds when $n=1$.

::: pf-proof

In this case $A=(a)$ for some $a\in\CC$, and
$$
0=\operatorname{tr}A=a.
$$
Thus $A=(0)$.

:::

:::

::: {.pf-step #s2}

Assume $n\ge2$ and that the assertion holds for $(n-1)\times(n-1)$ complex matrices of trace zero. There is a basis of $\CC^n$ in which the matrix of $T$ has the form
$$
M=
\begin{pmatrix}
0&r\\
c&B
\end{pmatrix},
$$
where $B$ is an $(n-1)\times(n-1)$ matrix with $\operatorname{tr}B=0$.

::: pf-proof

If $T=0$, any basis gives the asserted form with $B=0$.

Suppose $T\ne0$. Since $\operatorname{tr}T=0$, the map $T$ cannot be a scalar multiple of the identity: if $T=\lambda I$, then
$$
0=\operatorname{tr}T=n\lambda,
$$
so $\lambda=0$ over $\CC$, contrary to $T\ne0$.

Therefore there is a vector $v_1$ such that $Tv_1$ is not a scalar multiple of $v_1$. Indeed, if every nonzero vector were an eigenvector, then for linearly independent $u,v$ one could write
$$
Tu=\alpha u,\qquad Tv=\beta v,\qquad T(u+v)=\gamma(u+v).
$$
Comparing the coefficients of $u$ and $v$ gives $\alpha=\beta=\gamma$. Comparing in this way with a fixed nonzero vector shows that every vector has the same eigenvalue, so $T$ would be scalar.

Set
$$
v_2=Tv_1.
$$
Then $v_1,v_2$ are linearly independent; extend them to a basis $v_1,v_2,\ldots,v_n$ of $\CC^n$. Since $Tv_1=v_2$, the coefficient of $v_1$ in the first column of the matrix of $T$ is zero. Thus that matrix has the displayed block form. Trace is invariant under change of basis, so
$$
0=\operatorname{tr}M=0+\operatorname{tr}B,
$$
and hence $\operatorname{tr}B=0$.

:::

:::

::: {.pf-step #s3}

The matrix $M$ from step [](#s2){.pf-ref} is similar to a matrix whose diagonal entries are all zero.

::: pf-proof

By the induction hypothesis applied to $B$, there is
$$
S\in\operatorname{GL}_{n-1}(\CC)
$$
such that $S^{-1}BS$ has zero diagonal. Put
$$
P=
\begin{pmatrix}
1&0\\
0&S
\end{pmatrix}.
$$
Then
$$
P^{-1}MP=
\begin{pmatrix}
0&rS\\
S^{-1}c&S^{-1}BS
\end{pmatrix}.
$$
Its first diagonal entry is zero, and all remaining diagonal entries are zero because they are the diagonal entries of $S^{-1}BS$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives the base case, and steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give the induction step. Since $M$ is a matrix of $T$ in a basis, it is similar to the original matrix $A$, so step [](#s3){.pf-ref} proves the required assertion.

:::

:::

:::
