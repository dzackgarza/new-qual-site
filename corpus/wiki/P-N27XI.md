---
schema: qual/card@1
id: P-N27XI
kind: problem
title: "Define a map \\begin{align} \\phi: Z(R) &\\to Z(M_n(R) \\\\ r &\\mapsto r I_n .\\end{align} By part 1, this map is surjective."
classification:
  areas:
  - algebra
  topics:
  - centralizers-and-normalizers
  - matrices
  - isomorphism-theorems
relations: []
review: draft
solved: false
---

::: problem
Define a map

\begin{align*}
\phi: Z(R) &\to Z(M_n(R) \\
r &\mapsto r I_n
.\end{align*}

By part 1, this map is surjective.
To see that it is also injective, we can consider $\ker \phi = \theset{r \in Z(r) \suchthat r I_n = 0_n}$, which clearly forces $r=0_R$.
It is also a homomorphism of $R\dash$modules, since $\phi(rx + y) = (rx + y) I_n = r(xI_n) + yI_n$.


Thus by the first isomorphism theorem, we have $Z(R) \cong Z(M_n(R))$.
:::
