---
schema: qual/card@1
id: P-RAF17C
kind: problem
title: "Hilbert-Schmidt norm and operator norm of a bounded operator"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $H$ and $K$ be separable Hilbert spaces, $T : H \to K$ be a bounded linear operator, and $\{u_j\}_{j=1}^{\infty}$ and $\{v_k\}_{k=1}^{\infty}$ be orthonormal bases for $H$ and $K$ respectively.
Show:

1. $\sum_{j=1}^{\infty} \|Tu_j\|_K^2 = \sum_{k=1}^{\infty} \|T^*v_k\|_H^2$, allowing for the possibility that one and hence both of these sums are infinite.

2. $\|T\|_{op}^2 \leq \sum_{j=1}^{\infty} \|Tu_j\|_K^2$, where $\|T\|_{op}$ denotes the operator norm of $T$.
:::

::: solution
<1>1. Expand both sums in the two orthonormal bases.
::: proof
For each fixed $j$, Parseval's identity in $K$ gives
\[
\|Tu_j\|_K^2
=\sum_{k=1}^\infty |\langle Tu_j,v_k\rangle_K|^2.
\]
Hence, by Tonelli's theorem for the nonnegative double series,
\[
\sum_{j=1}^\infty\|Tu_j\|_K^2
=\sum_{j=1}^\infty\sum_{k=1}^\infty
|\langle Tu_j,v_k\rangle|^2
=\sum_{k=1}^\infty\sum_{j=1}^\infty
|\langle u_j,T^*v_k\rangle|^2.
\]
Applying Parseval in $H$ to each $T^*v_k$ yields
\[
\sum_{j=1}^\infty |\langle u_j,T^*v_k\rangle|^2
=\|T^*v_k\|_H^2.
\]
Therefore
\[
\boxed{
\sum_{j=1}^\infty\|Tu_j\|_K^2
=\sum_{k=1}^\infty\|T^*v_k\|_H^2,}
\]
with equality in $[0,\infty]$.
:::

<1>2. Bound $T$ on finite linear combinations of the basis vectors.
::: proof
Let
\[
x=\sum_{j=1}^N a_j u_j.
\]
Then
\[
Tx=\sum_{j=1}^N a_jTu_j,
\]
so by the triangle inequality and Cauchy--Schwarz,
\[
\begin{aligned}
\|Tx\|_K
&\le\sum_{j=1}^N|a_j|\,\|Tu_j\|_K\\
&\le
\left(\sum_{j=1}^N|a_j|^2\right)^{1/2}
\left(\sum_{j=1}^N\|Tu_j\|_K^2\right)^{1/2}\\
&\le \|x\|_H
\left(\sum_{j=1}^\infty\|Tu_j\|_K^2\right)^{1/2}.
\end{aligned}
\]
:::

<1>3. Pass to all of $H$.
::: proof
If
\[
\sum_{j=1}^\infty\|Tu_j\|_K^2=\infty,
\]
the desired inequality is trivial. Otherwise Step 2 gives a uniform bound on the dense subspace of finite linear combinations of the $u_j$. By continuity of $T$, the same bound holds for every $x\in H$:
\[
\|Tx\|_K
\le \|x\|_H
\left(\sum_{j=1}^\infty\|Tu_j\|_K^2\right)^{1/2}.
\]
Taking the supremum over $\|x\|_H=1$ and squaring gives
\[
\boxed{
\|T\|_{op}^2
\le\sum_{j=1}^\infty\|Tu_j\|_K^2.}
\]
:::
:::
