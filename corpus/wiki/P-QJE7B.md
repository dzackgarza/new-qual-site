---
schema: qual/card@1
id: P-QJE7B
kind: problem
title: $\{v_1+v_2,\, v_2-v_3,\, v_2+2v_3\}$ is a basis whenever $\{v_1,v_2,v_3\}$
  is
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Bases
relations: []
review: draft
solved: true
---

::: problem
Let $v_1$, $v_2$, $v_3$ form a basis for a vector space $V$. Prove that $v_1+v_2$, $v_2-v_3$, $v_2+2v_3$ form a basis for $V$.
:::

::: solution
Write $w_1 = v_1+v_2$, $w_2 = v_2-v_3$, $w_3 = v_2+2v_3$. In the ordered basis $(v_1,v_2,v_3)$ these have coordinate matrix
\[
A = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 0 & -1 & 2 \end{pmatrix}.
\]
A short expansion gives $\det A = 3 \neq 0$, so $A$ is invertible. Thus $(w_1,w_2,w_3)$ is obtained from a basis by an invertible linear change of coordinates, hence is itself a basis of $V$.
:::
