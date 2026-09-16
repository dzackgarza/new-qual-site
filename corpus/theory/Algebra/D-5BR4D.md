---
schema: qual/card@1
id: D-5BR4D
kind: definition
title: Nondegenerate symmetric and Hermitian forms
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Inner Product Spaces
  - Vector Spaces
relations:
- kind: related-to
  target: D-O4WWN
review: draft
---

::: {.definition}
Let $V$ be a real vector space with a symmetric bilinear form, or a complex vector space with a Hermitian form, and write $\inner{\wait}{\wait}$ for the form.
A vector $v\in V$ is a \dfn{null vector} if $\inner v w = 0$ for every $w\in V$; the null vectors form the \dfn{nullspace} of the form.
The form is \dfn{nondegenerate} if its nullspace is $\theset 0$, that is, if for every $v \neq 0$ there is some $v'\in V$ with $\inner{v}{v'} \neq 0$.
Otherwise it is \dfn{degenerate}.
:::

::: {.proposition}
Let $V$ and $\inner{\wait}{\wait}$ be as in the definition, with $V$ finite-dimensional.

1. Fix a basis of $V$ and let $A$ be the matrix of the form in that basis. Then $v$ is a null vector if and only if its coordinate vector $Y$ satisfies $AY = 0$, so the form is nondegenerate if and only if $A$ is invertible.

2. For a subspace $W \subseteq V$ with $W^\perp \coloneqq \theset{v\in V \st \inner w v = 0 \text{ for all } w\in W}$, the restriction of the form to $W$ is nondegenerate if and only if $W \cap W^\perp = \theset 0$, if and only if $V = W \oplus W^\perp$.
:::

::: {.example}
Nondegeneracy of the form on $V$ and nondegeneracy of its restriction to a subspace are independent.
On $V = \RR^2$ with standard basis $e_1, e_2$, the form $\inner x y = x_1y_1 - x_2y_2$ is nondegenerate, but its restriction to $W = \RR(e_1 + e_2)$ is zero, hence degenerate.
The form $\inner x y = x_1y_1$ on $\RR^2$ is degenerate, with nullspace $\RR e_2$, but its restriction to $\RR e_1$ is nondegenerate.
:::

::: {.concept}
See Artin, *Algebra*, §8.4, Lemma 8.4.2, Proposition 8.4.4 and Theorem 8.4.5, pp. 235-238. The formulation over an arbitrary field, through the adjoint $V \to V\dual$, is [[D-O4WWN]].
:::
