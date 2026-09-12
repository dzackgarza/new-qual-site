---
schema: qual/card@1
id: E-CKXKK
kind: problem
title: G-delta subspaces of compact Hausdorff or complete metric spaces are Baire
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
---

::: {.exercise}

Show that if $Y$ is a $G_\delta$ set in $X$, and if $X$ is compact Hausdorff or complete metric, then $Y$ is a Baire space in the subspace topology.
[Hint: Suppose that $Y = \bigcap W_n$, where $W_n$ is open in $X$, and that $B_n$ is closed in $Y$ and has empty interior in $Y$.
Given $U_0$ open in $X$ with $U_0 \cap Y \neq \varnothing$, find a sequence of open sets $U_n$ of $X$ with $U_n \cap Y$ nonempty, such that

$$
\begin{array}{c}
\overline{U}_n \subset U_{n-1}, \\
\overline{U}_n \cap \overline{B}_n = \varnothing, \\
\operatorname{diam} U_n < 1/n \quad \text{in the metric case}, \\
\overline{U}_n \subset W_n.]
\end{array}
$$
:::

::: {.solution}
Write $Y=\bigcap_{n\ge1}W_n$ with $W_n$ open in $X$. To prove $Y$ Baire, let $B_n$ be closed nowhere dense subsets of $Y$ and let $U_0$ be open in $X$ with $U_0\cap Y\ne\varnothing$. We construct nonempty open $U_n$ meeting $Y$ such that
\[
\overline U_n\subset U_{n-1}\cap W_n,\qquad
\overline U_n\cap\overline{B_n}^{\,X}=\varnothing,
\]
and in the metric case also $\operatorname{diam}U_n<1/n$.

Indeed, since $B_n$ has empty interior in $Y$, the nonempty relatively open set $U_{n-1}\cap W_n\cap Y$ contains a point outside $B_n$. Because $B_n$ is closed in $Y$, choose an $X$-open neighborhood $V$ of that point whose closure is contained in $U_{n-1}\cap W_n$ and avoids $\overline{B_n}^{\,X}$; in the metric case shrink its diameter below $1/n$. (In the compact-Hausdorff case use regularity.) Set $U_n=V$.

If $X$ is compact Hausdorff, the nested compact sets $\overline U_n$ have nonempty intersection. If $X$ is complete metric, choose $x_n\in\overline U_n$; nestedness and the diameter bound make $(x_n)$ Cauchy, with limit in every $\overline U_n$. Thus choose $x\in\bigcap_n\overline U_n$. Since $\overline U_n\subset W_n$, $x\in Y$; since $\overline U_n$ avoids $B_n$, $x\notin\bigcup B_n$; and $x\in\overline U_1\subset U_0$. Hence no nonempty relatively open subset of $Y$ is covered by countably many nowhere dense closed sets, so $Y$ is Baire.
:::
