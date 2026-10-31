---
schema: qual/card@1
id: P-PRACT20-W4-11
kind: problem
title: Possible dimensions of the intersection of two subspaces
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Subspaces
  - Dimension
relations: []
review: draft
---

::: {.problem}
(a) If $V, W$ are $2$-dimensional subspaces of $\RR^{4}$, what are the possible dimensions of $V \cap W$?

(b) What if $V, W$ are $4$-dimensional subspaces of $\RR^{7}$?
:::

::: {.solution}
Suppose that $V,W$ are subspaces of $\RR^n$. Since $V\cap W\subseteq V$ and $V\cap W\subseteq W$, the dimension of the intersection is at most $\min(\dim V,\dim W)$. The dimension formula gives

$$
\dim(V\cap W)=\dim V+\dim W-\dim(V+W),
$$

and $V+W\subseteq\RR^n$. Thus

$$
\dim(V\cap W)\geq\dim V+\dim W-n.
$$

(a) Here $0\leq\dim(V\cap W)\leq2$.

(b) Here $1\leq\dim(V\cap W)\leq4$.

Every value between the bounds occurs, using coordinate vectors. In (a):

- if $V=\operatorname{span}(e_1,e_2)$ and $W=\operatorname{span}(e_3,e_4)$, then $\dim(V\cap W)=0$;
- if $V=\operatorname{span}(e_1,e_2)$ and $W=\operatorname{span}(e_1,e_4)$, then $\dim(V\cap W)=1$;
- if $V=W=\operatorname{span}(e_1,e_2)$, then $\dim(V\cap W)=2$.

In (b), take $V=\operatorname{span}(e_1,\dots,e_4)$ and $W=\operatorname{span}(e_1,\dots,e_k,e_5,\dots,e_{8-k})$ for $k=1,\dots,4$; then $\dim(V\cap W)=k$.
:::
