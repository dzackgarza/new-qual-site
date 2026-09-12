---
schema: qual/card@1
id: P-RAF10B
kind: problem
title: "Continuity and boundedness of an oscillatory integral"
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
  note: Checked against Problem 2 of the official UCSD Fall 2010 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in L^1(\mathbb{R})$.
Prove that the function
$$
g(y) = \int_{\mathbb{R}} \sin(y^2 x)\,f(x)\,dx
$$
is continuous and bounded on $\mathbb{R}$.
:::

::: solution
<1>1. Prove boundedness.
::: proof
For every $y\in\mathbb R$,
\[
|g(y)|
\le \int_{\mathbb R}|\sin(y^2x)|\,|f(x)|\,dx
\le \int_{\mathbb R}|f(x)|\,dx
=\|f\|_1.
\]
Hence
\[
\boxed{\|g\|_\infty\le\|f\|_1.}
\]
:::

<1>2. Prove continuity.
::: proof
Let $y_k\to y$. For each fixed $x\in\mathbb R$,
\[
\sin(y_k^2x)f(x)\longrightarrow \sin(y^2x)f(x).
\]
Moreover,
\[
|\sin(y_k^2x)f(x)|\le|f(x)|,
\]
and $f\in L^1(\mathbb R)$. By dominated convergence,
\[
g(y_k)\longrightarrow g(y).
\]
Therefore $g$ is continuous on $\mathbb R$.
:::
:::
