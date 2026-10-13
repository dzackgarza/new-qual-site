---
schema: qual/card@1
id: P-UCLAB09F-04
kind: problem
title: Dimension of an orthogonal complement
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
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
Let $V$ be a finite-dimensional real inner-product space and let $U\subseteq V$ be a vector subspace.
Prove that
\[
\dim U+\dim U^\perp=\dim V.
\]
:::

::: {.solution}
Let
\[
k=\dim U
\qquad\text{and}\qquad
n=\dim V.
\]

<1>1. There is an orthonormal basis
\[
u_1,\ldots,u_k
\]
of $U$.

::: {.proof}
Choose any basis of $U$ and apply the Gram--Schmidt process. Since $U$ is a subspace, every vector produced by Gram--Schmidt remains in $U$.
:::

<1>2. Extend the basis in step <1>1 to an orthonormal basis
\[
u_1,\ldots,u_k,u_{k+1},\ldots,u_n
\]
of $V$.

::: {.proof}
Extend $u_1,\ldots,u_k$ to an ordinary basis of $V$ and apply Gram--Schmidt while keeping the already orthonormal first $k$ vectors fixed. This yields the displayed orthonormal basis.
:::

<1>3. The vectors
\[
u_{k+1},\ldots,u_n
\]
belong to $U^\perp$.

::: {.proof}
For $j>k$ and every $i\le k$,
\[
\langle u_j,u_i\rangle=0
\]
because the basis in step <1>2 is orthonormal. Since $u_1,\ldots,u_k$ span $U$, linearity of the inner product shows that $u_j$ is orthogonal to every vector in $U$.
:::

<1>4. The vectors
\[
u_{k+1},\ldots,u_n
\]
span $U^\perp$.

::: {.proof}
Let $v\in U^\perp$. Expand $v$ in the orthonormal basis from step <1>2:
\[
v=\sum_{i=1}^n c_i u_i.
\]
For $i\le k$,
\[
c_i=\langle v,u_i\rangle=0
\]
because $v\in U^\perp$ and $u_i\in U$. Hence
\[
v=\sum_{i=k+1}^n c_i u_i,
\]
so the displayed vectors span $U^\perp$.
:::

<1>5. One has
\[
\dim U^\perp=n-k.
\]

::: {.proof}
By steps <1>3--<1>4, the $n-k$ vectors
\[
u_{k+1},\ldots,u_n
\]
form a basis of $U^\perp$.
:::

<1>6. Therefore
\[
\boxed{\dim U+\dim U^\perp=\dim V}.
\]

::: {.proof}
By definition,
\[
\dim U=k,
\qquad
\dim V=n,
\]
and step <1>5 gives
\[
\dim U^\perp=n-k.
\]
Adding yields the displayed identity.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required dimension formula.
:::
:::
