---
schema: qual/card@1
id: E-CKXKK
kind: exercise
title: G-delta subspaces of compact Hausdorff or complete metric spaces are Baire
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
solved: false
---

Show that if $Y$ is a $G_\delta$ set in $X$, and if $X$ is compact Hausdorff or complete metric, then $Y$ is a Baire space in the subspace topology. [Hint: Suppose that $Y = \bigcap W_n$, where $W_n$ is open in $X$, and that $B_n$ is closed in $Y$ and has empty interior in $Y$. Given $U_0$ open in $X$ with $U_0 \cap Y \neq \varnothing$, find a sequence of open sets $U_n$ of $X$ with $U_n \cap Y$ nonempty, such that

$$
\begin{array}{c}
\overline{U}_n \subset U_{n-1}, \\
\overline{U}_n \cap \overline{B}_n = \varnothing, \\
\operatorname{diam} U_n < 1/n \quad \text{in the metric case}, \\
\overline{U}_n \subset W_n.]
\end{array}
$$

::: {.remark}
Munkres, *Topology*, §48 Exercise 5.
:::
