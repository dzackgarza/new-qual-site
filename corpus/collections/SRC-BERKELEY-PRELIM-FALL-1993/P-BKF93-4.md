---
schema: qual/card@1
id: P-BKF93-4
kind: problem
title: A rectangular-matrix sandwich map cannot be invertible when the dimensions differ
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    For m<n, used a nonzero vector in ker A to construct a nonzero matrix in
    ker T. For m>n, observed that every AXB has image contained in the proper
    subspace im A of F^m, so T is not surjective.
---

::: {.problem}
Let $F$ be a field. Fix positive integers $m,n$ and matrices $A,B\in M_{m\times n}(F)$. Define
\[
T:M_{n\times m}(F)\to M_{m\times n}(F),
\qquad
T(X)=AXB.
\]
Prove that if $m\ne n$, then $T$ is not invertible.
:::

::: {.solution}
Regard a matrix in $M_{a\times b}(F)$ as a linear map
$F^b\to F^a$.

<1>1. If $m<n$, then $T$ is not injective.

::: {.proof}
Since
$$
\operatorname{rank}A\leq m<n,
$$
the linear map
$$
A:F^n\longrightarrow F^m
$$
has a nonzero kernel. Choose $0\neq v\in\ker A$. Because $m>0$, there is a
nonzero matrix $X\in M_{n\times m}(F)$ whose first column is $v$ and whose
remaining columns are zero. Then
$$
AX=0,
$$
so
$$
T(X)=AXB=0.
$$
Thus $X\neq0$ lies in $\ker T$, and $T$ is not injective.
:::

<1>2. If $m>n$, then $T$ is not surjective.

::: {.proof}
Let
$$
W\coloneqq\im A\subseteq F^m.
$$
Since
$$
\dim W=\operatorname{rank}A\leq n<m,
$$
the subspace $W$ is proper. For every $X\in M_{n\times m}(F)$, the matrix
$T(X)=AXB$, viewed as a map $F^n\to F^m$, satisfies
$$
\im T(X)\subseteq\im A=W.
$$

Choose $y\in F^m\setminus W$. Since $n>0$, let
$Y\in M_{m\times n}(F)$ have first column $y$ and all remaining columns
zero. Then
$$
\im Y\nsubseteq W,
$$
so $Y\neq T(X)$ for every $X$. Hence $T$ is not surjective.
:::

<1>3. If $m\neq n$, then $T$ is not invertible.

::: {.proof}
If $m<n$, step <1>1 shows that $T$ is not injective. If $m>n$, step <1>2
shows that $T$ is not surjective. Since $m\neq n$, one of these two cases
holds, so $T$ cannot be invertible.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the desired conclusion.
:::
:::
