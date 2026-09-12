---
schema: qual/card@1
id: E-JSSPA
kind: problem
title: Directness of sums via vanishing of finite sums
classification:
  areas:
  - topology
  topics:
  - Free Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Suppose that $G = \sum G_\alpha$.
Show this sum is direct if and only if the equation

$$
x_{\alpha_1} + \dots + x_{\alpha_n} = 0
$$

implies that each $x_{\alpha_i}$ equals 0. (Here $x_{\alpha_i} \in G_{\alpha_i}$ and the indices $\alpha_i$ are distinct.)
:::

::: {.solution}
Assume first that
\[
G=\bigoplus_\alpha G_\alpha.
\]
By definition, every element of \(G\) has a unique expression as a finite sum of elements from distinct \(G_\alpha\)'s. If
\[
x_{\alpha_1}+\cdots+x_{\alpha_n}=0
\]
with distinct indices, then this is one expression for \(0\), while
\[
0+\cdots+0
\]
is another. Uniqueness forces \(x_{\alpha_i}=0\) for every \(i\).

Conversely, assume the stated vanishing condition. Since \(G=\sum G_\alpha\), every element has at least one finite expression. Suppose
\[
x_{\alpha_1}+\cdots+x_{\alpha_r}
=y_{\beta_1}+\cdots+y_{\beta_s}.
\]
Move all terms to one side and combine terms belonging to the same subgroup. This yields
\[
z_{\gamma_1}+\cdots+z_{\gamma_t}=0
\]
with distinct \(\gamma_i\) and \(z_{\gamma_i}\in G_{\gamma_i}\). By hypothesis every \(z_{\gamma_i}=0\), so the two original expressions agree coordinate by coordinate. Thus finite decompositions are unique, and the sum is direct.
:::
