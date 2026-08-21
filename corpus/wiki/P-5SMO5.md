---
schema: qual/card@1
id: P-5SMO5
kind: problem
title: $g\in L^\infty([0,1])$ orthogonal to every continuous function vanishes a.e.
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Density
  - Integrals
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Let $g\in L^\infty([0, 1])$
Prove that
\[
\int _{[0,1]} f(x) g(x)\, dx = 0 
\quad\text{for all continuous } f:[0, 1] \to \RR 
\implies g(x) = 0 \text{ almost everywhere. }
\]
:::

:::{.concept}
\envlist

- Polar decomposition: $f = \sign(f) \cdot \abs{f}$.
- $L^\infty[0, 1] \subseteq L^1[0, 1]$.

:::

:::{.solution}
Use that $L^\infty[0, 1] \subseteq L^1[0, 1]$, so fixing $g$, choose a sequence of compactly supported continuous functions $f_k$ converging to $\sign(g)$ in $L^1$.
We can arrange so that $\abs{g_k} \leq 1$.
Then
\[
\int \abs{g}
&= \int\sign(g)\cdot g \\
&= \int \lim_k g_k\cdot g \\
&\equalsbecause{\text{DCT}} \lim_k \int g_k\cdot g \\
&=\lim_k 0 \\
&= 0
,\]
where the DCT applies since defining $h_k \da g_k\cdot g$ we have $\abs{h_k} \leq g\in L^1[0, 1]$, and each integral is zero since $g_k$ is continuous (and we use the hypothesis).
:::


