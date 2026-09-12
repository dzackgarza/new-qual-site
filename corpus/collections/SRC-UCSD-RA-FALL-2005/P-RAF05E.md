---
schema: qual/card@1
id: P-RAF05E
kind: problem
title: "Dense sequence with Gram matrix approaching identity implies weak convergence to zero"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Weak Convergence
  - Gram Matrix
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2005 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $H$ be a Hilbert space.
Suppose that there is a sequence $\{x_j\}$ in $H$ such that the finite linear combinations of the $x_j$ are dense in $H$ and
$$
|\langle x_j, x_k \rangle| \leq 1/2^{|j-k|} \quad \forall j, k \in \mathbb{N}.
$$
Prove that $x_j \to 0$ weakly.
:::

::: solution
<1>1. Obtain a uniform norm bound.
::: proof
Taking $j=k$ in the assumed estimate gives
\[
\|x_j\|^2=|\langle x_j,x_j\rangle|\le1.
\]
Hence
\[
\sup_j\|x_j\|\le1.
\]
:::

<1>2. Prove convergence against the dense linear span.
::: proof
Let
\[
y=\sum_{k=1}^N a_kx_k.
\]
Then
\[
\begin{aligned}
|\langle x_j,y\rangle|
&\le \sum_{k=1}^N |a_k|\,|\langle x_j,x_k\rangle|\\
&\le \sum_{k=1}^N |a_k|\,2^{-|j-k|}.
\end{aligned}
\]
For each fixed $k$, $2^{-|j-k|}\to0$ as $j\to\infty$, and the sum has only finitely many terms. Therefore
\[
\langle x_j,y\rangle\longrightarrow0
\]
for every finite linear combination $y$ of the $x_k$.
:::

<1>3. Extend the convergence to every vector in $H$.
::: proof
Fix $y\in H$ and $\varepsilon>0$. By density of the finite linear span, choose a finite linear combination $z$ of the $x_k$ such that
\[
\|y-z\|<\varepsilon.
\]
Then
\[
|\langle x_j,y\rangle|
\le |\langle x_j,z\rangle|+|\langle x_j,y-z\rangle|
\le |\langle x_j,z\rangle|+\varepsilon,
\]
using Step 1. Taking $j\to\infty$ and applying Step 2 gives
\[
\limsup_{j\to\infty}|\langle x_j,y\rangle|\le\varepsilon.
\]
Since $\varepsilon$ is arbitrary,
\[
\langle x_j,y\rangle\to0
\]
for every $y\in H$. Thus
\[
\boxed{x_j\rightharpoonup0.}
\]
:::
:::
