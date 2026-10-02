---
schema: qual/card@1
id: PR-IN9ZP
kind: proposition
title: Inner automorphisms are the quotient by the center
slogan: 'The inner automorphism group is $G/Z(G)$.'
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Quotient Groups
relations: []
review: draft
---

::: {.proposition}
For every group $G$, the conjugation homomorphism
$$
\begin{aligned}
c\colon G&\longrightarrow\Inn(G),\\
g&\longmapsto c_g,\qquad c_g(x)=gxg^{-1},
\end{aligned}
$$
is surjective with kernel $Z(G)$.
Consequently,
$$
\Inn(G)\cong G/Z(G).
$$
:::

::: {.proof}
Surjectivity holds by the definition of $\Inn(G)$.
An element $g\in G$ lies in $\ker c$ exactly when
$$
gxg^{-1}=x
$$
for every $x\in G$, equivalently when $gx=xg$ for every $x$.
Thus $\ker c=Z(G)$, and the first isomorphism theorem gives
$$
G/Z(G)\cong\Inn(G).
$$
:::
