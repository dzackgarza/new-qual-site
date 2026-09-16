---
schema: qual/card@1
id: PR-UL3KL
kind: proposition
title: Homology of closed 3-manifolds
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Homology
  - Orientation
relations: []
review: draft
---

::: {.proposition}
Let $M$ be a closed connected $3$-manifold and write $H_1(M;\ZZ) \cong \ZZ^r \oplus F$ with $F$ finite.
Then
$$
H_*(M;\ZZ) \cong \begin{cases}
\qty{ \ZZ,\; \ZZ^r \oplus F,\; \ZZ^r,\; \ZZ } & M \text{ orientable},\\
\qty{ \ZZ,\; \ZZ^r \oplus F,\; \ZZ^{r-1} \oplus \ZZ/2,\; 0 } & M \text{ nonorientable},
\end{cases}
$$
in degrees $0, 1, 2, 3$, with all higher groups zero; in the nonorientable case $r \geq 1$ [@Hat02, §3.3, Exercise 24, p. 259]; [@Hat02, Theorem 3.26, p. 236].
:::

::: {.remark}
$H_1$ can have torsion: the lens space $L_p(1,1)$ has $H_1\cong\ZZ/p$.
:::
