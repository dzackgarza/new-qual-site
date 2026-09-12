---
schema: qual/card@1
id: P-JHUFA06ANE
kind: problem
title: "Finite-dimensionality of trigonometric-polynomial subspaces of C[0, pi]"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, September 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $X$ be the Banach space of continuous real-valued functions on $[0,\pi]$ that vanish at $0$ and $\pi$, with the supremum norm. Suppose $Y\subset X$ is a closed subspace and every element of $Y$ is a trigonometric polynomial. Prove that $Y$ is finite dimensional.
:::

::: {.solution}
For each $N\ge0$, let
\[
V_N=\operatorname{span}\{1,\sin x,\cos x,\ldots,\sin Nx,\cos Nx\},
\]
and set
\[
Y_N=Y\cap V_N.
\]
Each $V_N$ is finite dimensional, hence closed in $X$, so $Y_N$ is closed in $Y$. By hypothesis, every $y\in Y$ is a trigonometric polynomial of some finite degree, therefore
\[
Y=\bigcup_{N=0}^\infty Y_N.
\]
Since $Y$ is closed in the Banach space $X$, it is itself Banach. By the Baire category theorem, some $Y_N$ has nonempty interior relative to $Y$. Because $Y_N$ is a linear subspace of $Y$, nonempty interior forces
\[
Y_N=Y.
\]
Indeed, if a ball $B_Y(y_0,r)\subset Y_N$, then $y_0\in Y_N$ and hence $B_Y(0,r)\subset Y_N$; by scalar multiplication every vector of $Y$ then lies in $Y_N$.

Thus
\[
Y\subset V_N,
\]
and $V_N$ is finite dimensional. Hence $Y$ is finite dimensional.
:::
