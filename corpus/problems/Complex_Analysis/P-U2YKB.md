---
schema: qual/card@1
id: P-U2YKB
kind: problem
title: Uniform limits of continuous functions are continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Sequences of Functions
relations: []
review: draft
---

::: problem
- Show that a uniform limit of continuous functions is continuous.
:::

::: solution
Let $f_n:X\to\mathbb C$ be continuous and suppose $f_n\to f$ uniformly.
Fix $x_0\in X$ and $\varepsilon>0$. Choose $N$ such that
\[
|f_N(x)-f(x)|<\frac\varepsilon3
\]
for every $x\in X$. By continuity of $f_N$ at $x_0$, there is a neighborhood
of $x_0$ on which
\[
|f_N(x)-f_N(x_0)|<\frac\varepsilon3.
\]
Hence, for such $x$,
\[
|f(x)-f(x_0)|
\le |f(x)-f_N(x)|+|f_N(x)-f_N(x_0)|+|f_N(x_0)-f(x_0)|
<\varepsilon.
\]
Thus $f$ is continuous at $x_0$, and therefore continuous everywhere.
:::
