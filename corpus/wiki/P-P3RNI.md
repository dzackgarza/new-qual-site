---
schema: qual/card@1
id: P-P3RNI
kind: problem
title: "Let $G$ be a finite group with $n$ distinct conjugacy classes. Let\u2026"
classification:
  areas:
  - algebra
  topics:
  - conjugacy
  - centralizers-and-normalizers
  - class-equation
relations: []
review: draft
solved: true
---
Let $G$ be a finite group with $n$ distinct conjugacy classes.
Let $g_1 \cdots g_n$ be representatives of the conjugacy classes of $G$.
Prove that if $g_i g_j = g_j g_i$ for all $i, j$ then $G$ is abelian.

:::{.concept}
\envlist

- $Z(g) = G \iff g\in Z(G)$, i.e. if the centralizer of $g$ is the whole group, $g$ is central.

- If $H\leq G$ is a *proper* subgroup, then $\Union_{g\in G} hGh\inv$ is again a proper subgroup (subset?)
  I.e. $G$ is not a union of conjugates of any proper subgroup.
- So if $G$ *is* a union of conjugates of $H$, then $H$ must not be proper, i.e. $H= G$.
:::

:::{.solution}
\envlist

- We have $g_j \subseteq Z(g_k)$ for all $k$ by assumption.
- If we can show $Z(g_k) = G$ for all $k$, then $g_k \in Z(G)$ for all $k$.
  - Then each conjugacy class is size 1, and since $G = \disjoint_{i=1}^n [g_i] = \disjoint_{i=1}^n \ts{g_i}$, every $g\in G$ is some $g_i$.
  So $G \subseteq Z(G)$, forcing $G$ to be abelian.
- If we can show $G \subseteq \Union_{h\in H} h Z(g_k) h\inv$ for some $k$, this forces $Z(g_k) = G$ and $g_k \in Z(G)$.
  - If we can do this for all $k$, we're done!
- Since $g\in G$ is in some conjugacy class, write $g=hg_j h\inv$ for some $h\in G$ and some $1\leq j\leq n$.
- Now use $g_j \in Z(g_k)$ for all $k$:
\[
g\in G &\implies g = hg_j h\inv && \text{for some } h\in H \\
g_j \in Z(g_k) \forall k &\implies g\in hZ(g_k)h\inv &&\text{for some }h, \, \forall 1\leq k \leq n \\
&\implies g\in \Union_{h\in G} h Z(g_k) h\inv
&&\forall 1\leq k \leq n \\
.\]
  - Note that it's necessary to get rid of the $h$ dependence, since now now every $g\in G$ is in $\Union_{h\in G} hZ(g_k)h\inv$.
- Now
\[
G \subseteq \Union_{h\in G} hZ(g_k) \subseteq G \,\,\forall k \implies Z(g_k) = G\,\, \forall k
,\]
and we're done.



:::

