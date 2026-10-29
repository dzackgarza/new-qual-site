---
schema: qual/card@1
id: P-UCLAB03S-08
kind: problem
title: Diagonalization from distinct characteristic roots
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Examination, May 2003 PDF.
---

::: {.problem}
Let $V$ be an $n$-dimensional complex vector space and let $T:V\to V$ be linear.
Suppose the characteristic polynomial of $T$ has $n$ distinct roots.
Show that there is a basis $B$ of $V$ such that the matrix of $T$ in the basis $B$ is diagonal.

Make sure to prove that your chosen set $B$ is in fact a basis.
:::

::: {.solution}

Let
$$
\lambda_1,\ldots,\lambda_n
$$
be the distinct roots of the characteristic polynomial of $T$. For each $i$, choose a nonzero vector $v_i\in V$ satisfying
$$
Tv_i=\lambda_i v_i.
$$

::: pf

::: {.pf-step #s1-1}

The vectors $v_1,\ldots,v_n$ are linearly independent.


::: pf-proof

Suppose
$$
\sum_{i=1}^n c_i v_i=0.
$$
Fix $j\in\{1,\ldots,n\}$ and apply the linear operator
$$
p_j(T)=\prod_{\substack{1\le i\le n\\ i\ne j}}(T-\lambda_i I)
$$
to this relation. If $i\ne j$, then the factor $T-\lambda_i I$ annihilates $v_i$, so all terms except the $j$th vanish. Since $v_j$ is an eigenvector with eigenvalue $\lambda_j$,
$$
0
=
p_j(T)\left(\sum_{i=1}^n c_i v_i\right)
=
c_j\prod_{i\ne j}(\lambda_j-\lambda_i)v_j.
$$
The eigenvalues are distinct, so every factor $\lambda_j-\lambda_i$ is nonzero, and $v_j\ne0$. Hence $c_j=0$. Since $j$ was arbitrary, all coefficients vanish. Thus $v_1,\ldots,v_n$ are linearly independent.

:::

:::

::: {.pf-step #s1-2}

The ordered set
$$
B=(v_1,\ldots,v_n)
$$
is a basis of $V$.


::: pf-proof

By step [](#s1-1){.pf-ref}, $B$ consists of $n$ linearly independent vectors. Since $\dim V=n$, every linearly independent set of $n$ vectors is a basis.

:::

:::

::: {.pf-step #s1-3}

The matrix of $T$ in the basis $B$ is
$$
\boxed{[T]_B=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)}.
$$


::: pf-proof

For each basis vector $v_i$, one has
$$
Tv_i=\lambda_i v_i.
$$
Therefore the $i$th column of $[T]_B$ has the single nonzero entry $\lambda_i$ in position $i$, which is precisely the displayed diagonal matrix.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves that the chosen eigenvectors form a basis, and step [](#s1-3){.pf-ref} proves that the matrix of $T$ in this basis is diagonal.

:::

:::

:::
