---
schema: qual/card@1
id: E-BAZND
kind: problem
title: Uncountable powers of the line are not normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem.
If $J$ is uncountable, then $\mathbb{R}^J$ is not normal.

Proof.
(This proof is due to A. H. Stone, as adapted in [S-S].) Let $X = (\mathbb{Z}_+)^J$; it will suffice to show that $X$ is not normal, since $X$ is a closed subspace of $\mathbb{R}^J$.
We use functional notation for the elements of $X$, so that the typical element of $X$ is a function $\mathbf{x}: J \to \mathbb{Z}_+$.

(a) If $\mathbf{x} \in X$ and if $B$ is a finite subset of $J$, let $U(\mathbf{x}, B)$ denote the set consisting of all those elements $\mathbf{y}$ of $X$ such that $\mathbf{y}(\alpha) = \mathbf{x}(\alpha)$ for $\alpha \in B$.
Show the sets $U(\mathbf{x}, B)$ are a basis for $X$.

(b) Define $P_n$ to be the subset of $X$ consisting of those $\mathbf{x}$ such that on the set $J - \mathbf{x}^{-1}(n)$, the map $\mathbf{x}$ is injective.
Show that $P_1$ and $P_2$ are closed and disjoint.

(c) Suppose $U$ and $V$ are open sets containing $P_1$ and $P_2$, respectively.
Given a sequence $\alpha_1, \alpha_2, \ldots$ of distinct elements of $J$, and a sequence

$$
0 = n_0 < n_1 < n_2 < \dots
$$

of integers, for each $i \geq 1$ let us set

$$
B_i = \ts{\alpha_1, \dots, \alpha_{n_i}}
$$

and define $\mathbf{x}_i \in X$ by the equations

$$
\begin{array}{ll}
\mathbf{x}_i(\alpha_j) = j & \text{for } 1 \leq j \leq n_{i-1}, \\
\mathbf{x}_i(\alpha) = 1 & \text{for all other values of } \alpha.
\end{array}
$$

Show that one can choose the sequences $\alpha_j$ and $n_j$ so that for each $i$, one has the inclusion

$$
U(\mathbf{x}_i, B_i) \subset U.
$$

[Hint: To begin, note that $\mathbf{x}_1(\alpha) = 1$ for all $\alpha$; now choose $B_1$ so that $U(\mathbf{x}_1, B_1) \subset U$.]

(d) Let $A$ be the set $\ts{\alpha_1, \alpha_2, \ldots}$ constructed in (c). Define $\mathbf{y}: J \to \mathbb{Z}_+$ by the equations

$$
\mathbf{y}(\alpha_j) = j \quad \text{for } \alpha_j \in A,
$$

$$
\mathbf{y}(\alpha) = 2 \quad \text{for all other values of } \alpha.
$$

Choose $B$ so that $U(\mathbf{y}, B) \subset V$.
Then choose $i$ so that $B \cap A$ is contained in the set $B_i$.
Show that

$$
U(\mathbf{x}_{i+1}, B_{i+1}) \cap U(\mathbf{y}, B)
$$

is not empty.
:::
