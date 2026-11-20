---
schema: qual/card@1
id: PR-B0TT5
kind: proposition
title: Bott periodicity in the stable range
slogan: 'The stable homotopy of $O$, $U$ and $Sp$ repeats with period 8, 2 and 8.'
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
  - Classical Groups
relations: []
review: draft
---

::: {.proposition}
Let $k$ be in the stable range: $k<n-2$ for $O(n)$, $k<2n-2$ for $U(n)$, and $k<4n-2$ for $Sp(n)$.
In this range $\pi_k$ of each family is independent of $n$, and writing the stable group as $\pi_k$ of $O$, $U$ or $Sp$,
$$
\pi_k(U)\cong\begin{cases}\ZZ & k\ \text{odd},\\ 0 & k\ \text{even},\end{cases}
\qquad
\pi_k(O)\cong\begin{cases}\ZZ/2 & k\equiv0,1\pmod 8,\\ \ZZ & k\equiv3,7\pmod 8,\\ 0 & \text{otherwise},\end{cases}
\qquad
\pi_k(Sp)\cong\begin{cases}\ZZ & k\equiv3,7\pmod 8,\\ \ZZ/2 & k\equiv4,5\pmod 8,\\ 0 & \text{otherwise},\end{cases}
$$
so the stable groups are periodic of period $8$ in $k$ for $O$ and $Sp$ and of period $2$ for $U$ [@Hat02, Example 4.55].
:::
