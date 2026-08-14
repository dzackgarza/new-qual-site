---
schema: qual/card@1
id: D-5BR4D
kind: definition
title: "Nondegenerate Bilinear Form"
classification:
  areas:
  - algebra
  topics:
  - bilinear-forms
  - inner-product-spaces
  - vector-spaces
relations:
- kind: related-to
  target: D-O4WWN
review: draft
---

::: {.definition title="Nondegenerate Bilinear Form"}
Work with a symmetric form on a real vector space $V$, or a Hermitian form on a complex one, and write $\inner{\wait}{\wait}$ for the form.
A vector $v$ is a **null vector** iff $\inner v w = 0$ for every $w\in V$; the null vectors form the **nullspace** of the form.
The form is **nondegenerate** iff its nullspace is $\ts 0$, i.e. iff for every $v \neq 0$ there is some $v'$ with $\inner{v}{v'} \neq 0$.
Otherwise it is **degenerate**.

Two criteria:

- Fixing a basis and letting $A$ be the matrix of the form, $v$ is a null vector iff its coordinate vector $Y$ solves $AY = 0$, so the form is nondegenerate iff $A$ is invertible.

- The form is nondegenerate on a subspace $W \subseteq V$ iff $W \intersect W^\perp = \ts 0$, equivalently iff $V = W \oplus W^\perp$ as an orthogonal sum.

Nondegeneracy on $V$ neither implies nor is implied by nondegeneracy on a given subspace.
:::

::: {.concept}
See Artin, *Algebra*, §8.4, Lemma 8.4.2, Proposition 8.4.4 and Theorem 8.4.5, pp. 235-238. The formulation over an arbitrary field, through the adjoint $V \to V\dual$, is the related card of the same title.
:::
