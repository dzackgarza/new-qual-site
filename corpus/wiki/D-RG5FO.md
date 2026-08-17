---
schema: qual/card@1
id: D-RG5FO
kind: definition
title: Gram matrix of a bilinear form
classification:
  areas:
  - algebra
  topics:
  - bilinear-forms
  - matrices
relations:
- kind: related-to
  target: D-H4TDM
review: draft
---

::: {.definition title="Gram Matrix"}
Following Artin, let $\inner{\wait}{\wait}$ be a bilinear form on a finite-dimensional real vector space $V$ and $\mathbf B = (v_1, \cdots, v_n)$ an ordered basis; nothing below uses $\RR$ rather than an arbitrary field.
The **Gram matrix**, which Artin calls the *matrix of the form*, is
\[
A = (a_{ij}), \qquad a_{ij} \da \inner{v_i}{v_j}
.\]
It computes the form in coordinates: if $X$ and $Y$ are the coordinate vectors of $v$ and $w$, then
\[
\inner{v}{w} = X^t A Y
.\]
So a bilinear form on $V$ and an $n\times n$ matrix are the same data once a basis is fixed, and the form is symmetric iff $A$ is.
:::

::: {.remark}
Changing basis by an invertible $P$ replaces $A$ with $P^t A P$, which is *congruence*, not similarity: the two matrices of one form need not have the same eigenvalues, only the same rank and, over $\RR$, the same signature.
:::

::: {.concept}
See Artin, *Algebra*, §8.1, (8.1.4) and Proposition 8.1.5, pp. 229-230; the change-of-basis rule is Proposition 8.1.7 and Corollary 8.1.8.
:::
