---
schema: qual/card@1
id: D-RG5FO
kind: definition
title: Gram matrix of a bilinear form
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Matrices
relations:
- kind: related-to
  target: D-H4TDM
review: draft
---

::: {.definition}
Let $k$ be a field, $V$ a finite-dimensional $k$-vector space, $\inner{\wait}{\wait}$ a bilinear form on $V$, and $\mathbf B = (v_1, \ldots, v_n)$ an ordered basis of $V$.
The \dfn{Gram matrix} of the form with respect to $\mathbf B$, also called the \dfn{matrix of the form}, is
$$
A = (a_{ij}), \qquad a_{ij} \coloneqq \inner{v_i}{v_j}.
$$
:::

::: {.proposition}
If $X,Y\in k^n$ are the coordinate vectors of $v,w\in V$ with respect to $\mathbf B$, then
$$
\inner{v}{w} = X^t A Y.
$$
Consequently, for a fixed basis $\mathbf B$, the assignment of the Gram matrix is a bijection from bilinear forms on $V$ to $\Mat_{n\times n}(k)$, and a form is symmetric if and only if its Gram matrix is symmetric.
:::

::: {.proof}
Writing $v=\sum_i x_iv_i$ and $w=\sum_j y_jv_j$, bilinearity gives $\inner{v}{w}=\sum_{i,j}x_iy_j\inner{v_i}{v_j}=X^tAY$.
Conversely, every $A\in\Mat_{n\times n}(k)$ defines the bilinear form $(v,w)\mapsto X^tAY$, whose Gram matrix is $A$.
The form is symmetric if and only if $a_{ij}=a_{ji}$ for all $i,j$, by the displayed formula.
:::

::: {.remark}
If $\mathbf B'$ is another ordered basis and $P\in\GL_n(k)$ is the change-of-basis matrix, so that coordinates satisfy $X=PX'$, then the Gram matrix with respect to $\mathbf B'$ is $P^t A P$.
This preserves the rank of $A$ and, for $k=\RR$ and a symmetric form, its signature, but not its eigenvalues: for $P=2I_n$ the new Gram matrix is $4A$.
:::

::: {.concept}
See Artin, *Algebra*, §8.1, (8.1.4) and Proposition 8.1.5, pp. 229-230; the change-of-basis rule is Proposition 8.1.7 and Corollary 8.1.8.
:::
