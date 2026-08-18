---
schema: qual/card@1
id: P-MMAQ-EPSA3BOVMI
kind: problem
title: Dual lattice of an integer Gram form, and $|\Lambda^\vee/\Lambda|=\det M$
classification:
  areas:
  - algebra
  topics:
  - bilinear-forms
  - dual-spaces
  - matrices
relations: []
review: draft
solved: false
---

::: problem
Let $\{e_1, \cdots, e_n \}$ be a basis of a real vector space $V$ and let
$$
\Lambda \definedas \theset{ \sum r_i e_i \mid ri \in \ZZ}
$$

Let $\cdot$ be a non-degenerate ($v \cdot w = 0$ for all $w \in V \iff v = 0$) symmetric bilinear form on V such that the Gram matrix $M = (e_i \cdot e_j )$ has integer entries.

Define the dual of $\Lambda$ to be

$$
\Lambda \dual \definedas \{v \in V \suchthat v \cdot x \in \ZZ \text{ for all } x \in \Lambda
\}
.$$

(a) Show that $\Lambda \subset \Lambda \dual$.

(b) Prove that $\det M \neq 0$ and that the rows of $M\inv$ span $\Lambda\dual$.

(c) Prove that $\det M = |\Lambda\dual /\Lambda|$.
:::
