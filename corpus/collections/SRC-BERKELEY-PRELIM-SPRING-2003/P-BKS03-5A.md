---
schema: qual/card@1
id: P-BKS03-5A
kind: problem
title: A singular perturbation of a symmetric matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $L$ be a real symmetric $n\times n$ matrix with $0$ as a simple eigenvalue, and let $v\in\mathbb R^n$.

(a) Show that for all sufficiently small $\varepsilon>0$, the equation
\[
Lx+\varepsilon x=v
\]
has a unique solution $x(\varepsilon)$.

(b) Evaluate $\lim_{\varepsilon\to0^+}\varepsilon x(\varepsilon)$ in terms of $v$ and the eigenvectors of $L$.
:::

::: {.solution}
Since L is real and symmetric, $\mathbb { R } ^ { n }$ has an orthonormal basis of eigenvectors $e _ { 1 } , \ldots , e _ { n }$ of L. Let $\lambda _ { 1 } , \ldots , \lambda _ { n }$ be the associated eigenvalues.
Without loss of generality, $\lambda _ { 1 } = 0$ and $\lambda _ { i } \neq 0$ for $i > 1$ Write $\textstyle v = \sum _ { i = 1 } ^ { n } v _ { i } e _ { i }$ and $x = \sum x _ { i } e _ { i }$ with $v _ { i } , x _ { i } \in \mathbb { R }$ The equation $L x + \epsilon x = v$ is equivalent to $\lambda _ { i } x _ { i } + \epsilon x _ { i } = v _ { i }$ for each i, which has the unique solution $x _ { i } = v _ { i } / ( \lambda _ { i } + \epsilon )$ , provided that $\begin{array} { r } { 0 < \epsilon < \operatorname* { m i n } _ { i \neq 1 } | \lambda _ { i } | } \end{array}$ . Now

$$
\epsilon x = \sum \epsilon x _ { i } e _ { i } = \sum \frac { \epsilon } { \lambda _ { i } + \epsilon } v _ { i } e _ { i } .
$$

As $\epsilon  0 .$ , all terms in the sum on the right tend to 0 except the first, which tends to $\boldsymbol { v } _ { 1 } \boldsymbol { e } _ { 1 } = ( v , e _ { 1 } ) \boldsymbol { e } _ { 1 }$
:::
