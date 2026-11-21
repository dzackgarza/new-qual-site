---
schema: qual/card@1
id: PR-UGRV4
kind: corollary
title: Dimension of the orthogonal complement
slogan: 'A nondegenerate form gives the orthogonal complement the complementary dimension.'
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Inner Product Spaces
  - Vector Spaces
relations: []
review: draft
---

::: {.corollary}
Let $k$ be a field, let $V$ be a finite-dimensional $k$-vector space with a symmetric bilinear form $\inner{-}{-}$, and let $W\subseteq V$ be a subspace whose restriction of the form is nondegenerate.
Put $W^\perp\coloneqq\theset{v\in V\suchthat \inner{w}{v}=0 \text{ for every } w\in W}$.
Then
$$
\dim W^\perp = \dim V - \dim W,
\qquad
W^{\perp\perp} = W.
$$
:::

::: {.proof}
By [[D-5BR4D]] the restriction of the form to $W$ is nondegenerate exactly when $V = W\oplus W^\perp$, and then $\dim V = \dim W + \dim W^\perp$. For the second identity, $W\subseteq W^{\perp\perp}$ holds for any form, and applying the first identity twice gives $\dim W^{\perp\perp} = \dim V - \dim W^\perp = \dim W$, so the inclusion is an equality.
:::

::: {.remark}
Over $\RR$ or $\CC$ a positive definite form restricts to a positive definite form on every subspace, so there the conclusion holds for every $W$; this is the inner product case the term orthogonal complement comes from.
[[PR-WDPF7]] gives the complementary identity $(W_1+W_2)^\perp = W_1^\perp\cap W_2^\perp$ for a family of subspaces.
:::
