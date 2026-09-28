---
schema: qual/card@1
id: E-5KI4G
kind: problem
title: Uniform convergence of $\sin(nx)/(1+nx)$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Determine where the following real-valued function is or is not uniformly convergent:
\[
f_n(x) \da {\sin(nx)\over 1+nx}
.\]

:::

::: {.solution}
For each $x\geq0$, $\abs{f_n(x)}\le 1/(1+nx)$ for $x>0$ and $f_n(0)=0$, so $f_n\to0$ pointwise on $[0,\infty)$.

The convergence is uniform on $[a, \infty)$ for every $a>0$:
\[
\sup_{x\geq a}\abs{\sin(nx) \over 1+nx} \leq {1\over 1 + na} \convergesto{n\to\infty} 0
.\]

The convergence is not uniform on $(0, \infty)$: 
\[
x_n \da {1\over n} \implies \sup_{x>0}\abs{f_n(x)}\geq\abs{f_n(x_n)} = {\sin(1) \over 2}
\]
for every $n$.
:::

