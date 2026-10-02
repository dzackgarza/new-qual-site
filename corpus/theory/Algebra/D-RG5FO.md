---
schema: qual/card@1
id: D-RG5FO
kind: proposition
title: Bilinear forms and Gram matrices
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Matrices
relations:
- kind: uses
  target: D-H4TDM
review: draft
---

::: {.proposition}
Let $k$ be a field, let $V$ be a finite-dimensional $k$-vector space, let $b$ be a bilinear form on $V$, and let $\mathbf B=(v_1,\ldots,v_n)$ be an ordered basis.
Let $A$ be the [[D-H4TDM|Gram matrix]] of $b$ with respect to $\mathbf B$.
If $X,Y\in k^n$ are the coordinate vectors of $v,w\in V$ with respect to $\mathbf B$, then
$$
b(v,w) = X^t A Y.
$$
Consequently, for fixed $\mathbf B$, the Gram-matrix assignment is a bijection from bilinear forms on $V$ to $\Mat_{n\times n}(k)$, and a form is symmetric if and only if its Gram matrix is symmetric.
[@Art11]
:::

::: {.proof}
Writing $v=\sum_i x_iv_i$ and $w=\sum_j y_jv_j$, bilinearity gives $b(v,w)=\sum_{i,j}x_iy_jb(v_i,v_j)=X^tAY$.
Conversely, every $A\in\Mat_{n\times n}(k)$ defines the bilinear form $(v,w)\mapsto X^tAY$, whose Gram matrix in $\mathbf B$ is $A$.
The form is symmetric if and only if $a_{ij}=a_{ji}$ for all $i,j$, by the displayed formula.
:::

::: {.remark}
If $\mathbf B'$ is another ordered basis and $P\in\GL_n(k)$ is the change-of-basis matrix, so that coordinates satisfy $X=PX'$, then the Gram matrix with respect to $\mathbf B'$ is $P^t A P$.
This preserves the rank of $A$ and, for $k=\RR$ and a symmetric form, its signature, but not its eigenvalues: for $P=2I_n$ the new Gram matrix is $4A$.
:::
