---
schema: qual/card@1
id: E-KS2BT
kind: problem
title: Completeness of the compact convergence topology over sigma-compact domains
classification:
  areas:
  - topology
  topics:
  - Function Spaces
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

A space is locally compact if it can be covered by open sets each of which is contained in a compact subspace of $X$.
It is said to be $\sigma$-compact if it can be covered by countably many such open sets.

(a) Show that if $X$ is locally compact and second-countable, it is $\sigma$-compact.

(b) Let $(Y, d)$ be a metric space.
Show that if $X$ is $\sigma$-compact, there is a metric for the topology of compact convergence on $Y^X$ such that if $(Y, d)$ is complete, $Y^X$ is complete in this metric.
[Hint: Let $A_1, A_2, \ldots$ be a countable collection of compact subspaces of $X$ whose interiors cover $X$. Let $Y_i$ denote the set of all functions from $A_i$ to $Y$, in the uniform topology. Define a homeomorphism of $Y^X$ with a closed subspace of the product space $Y_1 \times Y_2 \times \cdots$.]
:::

::: {.solution}
(a) Let $\mathcal B$ be a countable basis for the locally compact space $X$. For each $x$, choose an open $U_x$ and compact $K_x$ with $x\in U_x\subset K_x$. Choose a basis element $B_x$ with $x\in B_x\subset U_x$. Only countably many distinct $B_x$ occur; choosing one compact $K_x$ for each such basis element gives countably many compact sets whose interiors cover $X$. Thus $X$ is $\sigma$-compact.

(b) Choose compact $A_1,A_2,\dots$ whose interiors cover $X$, and replace them by finite unions so that $A_i\subset A_{i+1}$. Put on $Y_i=Y^{A_i}$ the bounded uniform metric
\[
\rho_i(u,v)=\min\{1,\sup_{A_i}d(u,v)\}.
\]
Define
\[
\rho(f,g)=\sum_{i=1}^\infty2^{-i}\rho_i(f|_{A_i},g|_{A_i}).
\]
This induces exactly compact convergence: every compact $C\subset X$ is covered by finitely many $\operatorname{Int}A_i$, hence lies in some $A_N$, while each $A_i$ itself is compact.

The restriction map
\[
R:Y^X\to\prod_iY_i,\qquad f\mapsto(f|_{A_i})
\]
identifies $Y^X$ with the closed compatibility subspace $u_{i+1}|_{A_i}=u_i$. If $Y$ is complete, each uniform function space $Y_i$ is complete (pointwise limits of uniform Cauchy families exist and convergence is uniform), and the standard weighted product metric is complete. A closed subspace is complete, so $(Y^X,\rho)$ is complete.
:::
