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

::: {.problem}
Let $H$ be a Hilbert space.
Suppose that there is a sequence $\{x_j\}$ in $H$ such that the finite linear combinations of the $x_j$ are dense in $H$ and
$$
\abs{\langle x_j, x_k \rangle} \leq 1/2^{\abs{j-k}} \quad \forall j, k \in \NN.
$$
Prove that $x_j \to 0$ weakly.
:::

::: {.solution}

::: pf

::: pf-step

Obtain a uniform norm bound.

::: pf-proof

Taking $j=k$ in the assumed estimate gives
$$
\norm{x_j}^2=\abs{\langle x_j,x_j\rangle}\le1.
$$
Hence
$$
\sup_j\norm{x_j}\le1.
$$

:::

:::

::: pf-step

Prove convergence against the dense linear span.

::: pf-proof

Let
$$
y=\sum_{k=1}^N a_kx_k.
$$
Then
$$
\begin{aligned}
\abs{\langle x_j,y\rangle}
&\le \sum_{k=1}^N \abs{a_k}\,\abs{\langle x_j,x_k\rangle}\\
&\le \sum_{k=1}^N \abs{a_k}\,2^{-\abs{j-k}}.
\end{aligned}
$$
For each fixed $k$, $2^{-\abs{j-k}}\to0$ as $j\to\infty$, and the sum has only finitely many terms. Therefore
$$
\langle x_j,y\rangle\longrightarrow0
$$
for every finite linear combination $y$ of the $x_k$.

:::

:::

::: pf-step

Extend the convergence to every vector in $H$.

::: pf-proof

Fix $y\in H$ and $\varepsilon>0$. By density of the finite linear span, choose a finite linear combination $z$ of the $x_k$ such that
$$
\norm{y-z}<\varepsilon.
$$
Then
$$
\abs{\langle x_j,y\rangle}
\le \abs{\langle x_j,z\rangle}+\abs{\langle x_j,y-z\rangle}
\le \abs{\langle x_j,z\rangle}+\varepsilon,
$$
using Step 1. Taking $j\to\infty$ and applying Step 2 gives
$$
\limsup_{j\to\infty}\abs{\langle x_j,y\rangle}\le\varepsilon.
$$
Since $\varepsilon$ is arbitrary,
$$
\langle x_j,y\rangle\to0
$$
for every $y\in H$. Thus
$$
\boxed{x_j\rightharpoonup0.}
$$

:::

:::

:::

:::
