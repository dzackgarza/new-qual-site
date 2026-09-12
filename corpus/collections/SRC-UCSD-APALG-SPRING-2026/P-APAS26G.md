---
schema: qual/card@1
id: P-APAS26G
kind: problem
title: Eigenvalues and eigenspaces of the $3$-cube adjacency operator
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
  - Representation Theory
relations: []
review: draft
---

::: problem
Let $G = (S, T)$ be the graph whose vertex set $S$ consists of all bitstrings of length $3$, with $\{s_1, s_2\} \in T$ an edge if and only if $s_1$ and $s_2$ differ by a single bit.
Let $A \in \operatorname{End}\mathcal{F}(S)$ be the adjacency operator of $G$.
Find the eigenvalues of $A$, and give an orthonormal basis for each eigenspace.
:::

::: solution
Identify the vertex set with the group
\[
S=(\mathbb Z/2\mathbb Z)^3.
\]
For each subset $J\subseteq\{1,2,3\}$ define
\[
\chi_J(x_1,x_2,x_3)
=(-1)^{\sum_{j\in J}x_j}.
\]
The normalized functions
\[
2^{-3/2}\chi_J
\]
form an orthonormal basis of $\mathcal F(S)$, since they are the characters of the finite abelian group $(\mathbb Z/2)^3$.

Let $e_1,e_2,e_3$ be the standard bit vectors. The adjacency operator is
\[
(Af)(x)=\sum_{i=1}^3 f(x+e_i).
\]
For a character $\chi_J$,
\[
\chi_J(x+e_i)=(-1)^{\mathbf 1_{i\in J}}\chi_J(x),
\]
so
\[
A\chi_J
=\left(\sum_{i=1}^3(-1)^{\mathbf 1_{i\in J}}\right)\chi_J
=(3-2|J|)\chi_J.
\]
Thus the eigenvalues are
\[
\boxed{3,1,-1,-3}
\]
with multiplicities
\[
1,3,3,1,
\]
respectively.

An orthonormal basis of the eigenspace with eigenvalue $3-2k$ is
\[
\boxed{\{2^{-3/2}\chi_J:|J|=k\}}.
\]
Explicitly:
\[
E_3=\operatorname{span}\{2^{-3/2}\chi_\varnothing\},
\]
\[
E_1=\operatorname{span}\{2^{-3/2}\chi_{\{1\}},2^{-3/2}\chi_{\{2\}},2^{-3/2}\chi_{\{3\}}\},
\]
\[
E_{-1}=\operatorname{span}\{2^{-3/2}\chi_{\{1,2\}},2^{-3/2}\chi_{\{1,3\}},2^{-3/2}\chi_{\{2,3\}}\},
\]
\[
E_{-3}=\operatorname{span}\{2^{-3/2}\chi_{\{1,2,3\}}\}.
\]
:::
