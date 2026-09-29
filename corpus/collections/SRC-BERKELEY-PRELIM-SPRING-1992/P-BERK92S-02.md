---
schema: qual/card@1
id: P-BERK92S-02
kind: problem
title: Square roots of an upper-triangular $3\times3$ matrix
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
  date: 2026-09-23
---

::: {.problem}
Find a square root of
\[
\begin{pmatrix}
1&3&-3\\
0&4&5\\
0&0&9
\end{pmatrix}.
\]
How many square roots does this matrix have?
:::

::: {.solution}
Write
$$
A\coloneqq
\begin{pmatrix}
1&3&-3\\
0&4&5\\
0&0&9
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1}

One square root is
$$
B=\boxed{
\begin{pmatrix}
1&1&-1\\
0&2&1\\
0&0&3
\end{pmatrix}
}.
$$

::: pf-proof

Direct multiplication gives
$$
B^2=
\begin{pmatrix}
1&3&-3\\
0&4&5\\
0&0&9
\end{pmatrix}
=A.
$$

:::

:::

::: {.pf-step #s2}

Every square root of $A$ acts by a scalar on each eigenspace of
$A$.

::: pf-proof

The matrix $A$ is upper triangular with three distinct eigenvalues
$1,4,9$. Hence it has three one-dimensional eigenspaces whose direct
sum is $\CC^3$.

If $X^2=A$, then
$$
XA=X^3=AX.
$$
Thus $X$ preserves every eigenspace of $A$: if $Av=\lambda v$, then
$A(Xv)=X(Av)=\lambda Xv$. Since each eigenspace is one-dimensional,
$X$ acts on it by some scalar $\mu_\lambda$.

:::

:::

::: {.pf-step #s3}

The matrix $A$ has exactly $\boxed{8}$ square roots.

::: pf-proof

On the eigenspace for $\lambda\in\{1,4,9\}$, the equation $X^2=A$
forces
$$
\mu_\lambda^2=\lambda.
$$
There are exactly two choices for each scalar:
$$
\mu_1\in\{1,-1\},
\qquad
\mu_4\in\{2,-2\},
\qquad
\mu_9\in\{3,-3\}.
$$
The three choices are independent, giving $2^3=8$ operators. Step
[](#s2){.pf-ref} shows that every square root arises in this way, so there are no
others.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives a square root, and step [](#s3){.pf-ref} gives the complete count.

:::

:::

:::
