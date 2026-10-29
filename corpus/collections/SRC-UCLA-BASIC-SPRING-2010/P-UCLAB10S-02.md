---
schema: qual/card@1
id: P-UCLAB10S-02
kind: problem
title: Courant-Fischer characterization of ordered eigenvalues
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
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 2. Let $A$ be an $n\times n$ real symmetric matrix with eigenvalues $\lambda_1\ge\cdots\ge\lambda_n$.
Prove that
\[
\lambda_k=
\max_{\substack{U\subseteq\RR^n\\ \dim U=k}}
\min_{\substack{x\in U\\ \|x\|=1}}
\langle Ax,x\rangle.
\]
:::

::: {.solution}

Let
\[
e_1,\ldots,e_n
\]
be an orthonormal basis of eigenvectors of $A$ with
\[
Ae_i=\lambda_i e_i,
\qquad
\lambda_1\ge\cdots\ge\lambda_n.
\]

::: pf

::: {.pf-step #s1-1}

Define
\[
U_0
=
\operatorname{span}\{e_1,\ldots,e_k\}.
\]
Then for every unit vector
\[
x\in U_0,
\]
one has
\[
\langle Ax,x\rangle\ge\lambda_k.
\]


::: pf-proof

Write
\[
x=\sum_{i=1}^k c_i e_i.
\]
Since the basis is orthonormal and $\|x\|=1$,
\[
\sum_{i=1}^k c_i^2=1.
\]
Also,
\[
Ax=\sum_{i=1}^k c_i\lambda_i e_i.
\]
Therefore
\[
\begin{aligned}
\langle Ax,x\rangle
&=
\sum_{i=1}^k\lambda_i c_i^2\\
&\ge
\lambda_k\sum_{i=1}^k c_i^2\\
&=
\lambda_k.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-2}

The minimum over the unit sphere in $U_0$ is exactly
\[
\boxed{\lambda_k}.
\]


::: pf-proof

Step [](#s1-1){.pf-ref} gives the lower bound
\[
\langle Ax,x\rangle\ge\lambda_k
\]
for every unit $x\in U_0$.

The unit vector
\[
e_k\in U_0
\]
satisfies
\[
\langle Ae_k,e_k\rangle
=
\lambda_k.
\]
Hence the minimum is attained and equals $\lambda_k$.

:::

:::

::: {.pf-step #s1-3}

Consequently,
\[
\max_{\substack{U\subseteq\RR^n\\ \dim U=k}}
\min_{\substack{x\in U\\ \|x\|=1}}
\langle Ax,x\rangle
\ge
\lambda_k.
\]


::: pf-proof

The maximum is taken over all $k$-dimensional subspaces.
In particular, it is at least the value obtained for the specific subspace $U_0$.
By step [](#s1-2){.pf-ref}, that value is $\lambda_k$.

:::

:::

::: pf-step

Let
\[
U\subseteq\RR^n
\]
be an arbitrary $k$-dimensional subspace, and define
\[
W
=
\operatorname{span}\{e_k,e_{k+1},\ldots,e_n\}.
\]
Then
\[
U\cap W\ne\{0\}.
\]


::: pf-proof

One has
\[
\dim U=k
\]
and
\[
\dim W=n-k+1.
\]
Hence
\[
\dim U+\dim W
=
n+1
>
n.
\]
For subspaces of an $n$-dimensional vector space,
\[
\dim(U\cap W)
=
\dim U+\dim W-\dim(U+W).
\]
Since
\[
\dim(U+W)\le n,
\]
it follows that
\[
\dim(U\cap W)\ge1.
\]
Thus the intersection contains a nonzero vector.

:::

:::

::: {.pf-step #s1-5}

Choose a unit vector
\[
x\in U\cap W.
\]
Then
\[
\langle Ax,x\rangle\le\lambda_k.
\]


::: pf-proof

Since
\[
x\in W,
\]
write
\[
x=\sum_{i=k}^n c_i e_i.
\]
Because $\|x\|=1$,
\[
\sum_{i=k}^n c_i^2=1.
\]
Therefore
\[
\begin{aligned}
\langle Ax,x\rangle
&=
\sum_{i=k}^n\lambda_i c_i^2\\
&\le
\lambda_k\sum_{i=k}^n c_i^2\\
&=
\lambda_k,
\end{aligned}
\]
because
\[
\lambda_i\le\lambda_k
\]
for every $i\ge k$.

:::

:::

::: {.pf-step #s1-6}

For every $k$-dimensional subspace $U$,
\[
\min_{\substack{x\in U\\ \|x\|=1}}
\langle Ax,x\rangle
\le
\lambda_k.
\]


::: pf-proof

Step [](#s1-5){.pf-ref} produces a unit vector
\[
x\in U
\]
whose Rayleigh quotient is at most $\lambda_k$.
The minimum over all unit vectors in $U$ cannot exceed that particular value.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\max_{\substack{U\subseteq\RR^n\\ \dim U=k}}
\min_{\substack{x\in U\\ \|x\|=1}}
\langle Ax,x\rangle
\le
\lambda_k.
\]


::: pf-proof

Step [](#s1-6){.pf-ref} gives the upper bound $\lambda_k$ for the inner minimum for every admissible subspace $U$.
Taking the maximum over all such $U$ preserves that upper bound.

:::

:::

::: {.pf-step #s1-8}

Combining the two inequalities gives
\[
\boxed{
\lambda_k=
\max_{\substack{U\subseteq\RR^n\\ \dim U=k}}
\min_{\substack{x\in U\\ \|x\|=1}}
\langle Ax,x\rangle.
}
\]


::: pf-proof

Step [](#s1-3){.pf-ref} gives the lower bound by $\lambda_k$, and step [](#s1-7){.pf-ref} gives the upper bound by $\lambda_k$.
Hence equality holds.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required Courant--Fischer formula.

:::

:::

:::
