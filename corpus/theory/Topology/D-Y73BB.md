---
schema: qual/card@1
id: D-Y73BB
kind: definition
title: Kronecker pairing
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homology
relations:
- kind: related-to
  target: D-VP4LC
review: draft
---

::: {.definition}
Let $X$ be a topological space, $R$ a commutative ring, and $n\geq 0$.
The \dfn{Kronecker pairing} is the $R$-bilinear map
$$
H^n(X;R)\times H_n(X;R)\longrightarrow R,
\qquad ([\psi],[\alpha])\longmapsto\psi(\alpha),
$$
for a singular cocycle $\psi\in C^n(X;R)$ and a singular cycle $\alpha\in C_n(X;R)$.
Its adjoint is the homomorphism
$$
h\colon H^n(X;R)\longrightarrow\Hom_R(H_n(X;R),R), \qquad h([\psi])([\alpha]) \coloneqq \psi(\alpha).
$$
:::

::: {.remark}
If $R$ is a principal ideal domain, $h$ is the surjection in the universal coefficient theorem, with kernel $\Ext_R(H_{n-1}(X;R),R)$.
The pairing can be degenerate: for $X=\RR P^2$, $R=\ZZ$, and $n=2$, $H^2(\RR P^2;\ZZ)\cong\ZZ/2$ while $H_2(\RR P^2;\ZZ)=0$.
:::

::: {.concept}
[@Hat02].
:::
