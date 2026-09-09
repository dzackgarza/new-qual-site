---
schema: qual/card@1
id: P-TUGZG
kind: problem
title: A uniformly convergent series of continuous functions is continuous
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the UGA Fall 2014 real-analysis qualifying exam source recorded by this collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(f_n)$ be a sequence of continuous functions such that $\sum_{n=1}^\infty f_n$ converges uniformly.
Prove that $\sum_{n=1}^\infty f_n$ is continuous.
:::

::: solution
<1>1. Apply the uniform-limit theorem to the partial sums.
::: proof
Let
\[
F_N(x):=\sum_{n=1}^N f_n(x),
\qquad
F(x):=\sum_{n=1}^\infty f_n(x).
\]
Each $F_N$ is continuous because it is a finite sum of continuous functions, and the hypothesis says that $F_N\to F$ uniformly.

Fix $x_0$ and $\varepsilon>0$. Choose $N$ so large that
\[
\sup_x|F(x)-F_N(x)|<\frac{\varepsilon}{3}.
\]
By continuity of $F_N$ at $x_0$, there is $\delta>0$ such that
\[
|x-x_0|<\delta
\quad\Longrightarrow\quad
|F_N(x)-F_N(x_0)|<\frac{\varepsilon}{3}.
\]
Hence, whenever $|x-x_0|<\delta$,
\[
\begin{aligned}
|F(x)-F(x_0)|
&\le |F(x)-F_N(x)|
 +|F_N(x)-F_N(x_0)|
 +|F_N(x_0)-F(x_0)|\\
&<\varepsilon.
\end{aligned}
\]
Thus $F$ is continuous at $x_0$. Since $x_0$ was arbitrary,
\[
\boxed{\sum_{n=1}^\infty f_n\text{ is continuous}.}
\]
:::
:::
