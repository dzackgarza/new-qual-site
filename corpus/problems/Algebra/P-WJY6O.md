---
schema: qual/card@1
id: P-WJY6O
kind: problem
title: Nilpotent groups are solvable
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Solvable Groups
relations: []
review: draft
---

::: {.problem}
Show that every nilpotent group is solvable.
:::

::: {.solution}
Suppose $G$ is nilpotent. Then its lower central series
$$
\gamma_1(G)=G,
\qquad
\gamma_{i+1}(G)=[\gamma_i(G),G]
$$
terminates:
$$
\gamma_{c+1}(G)=1
$$
for some $c$.

Let $G^{(i)}$ denote the derived series,
$$
G^{(0)}=G,
\qquad
G^{(i+1)}=[G^{(i)},G^{(i)}].
$$
We claim inductively that
$$
G^{(i)}\le \gamma_{i+1}(G).
$$
For $i=0$ this is $G\le G$. If it holds for $i$, then, since $G^{(i)}\le G$,
$$
G^{(i+1)}=[G^{(i)},G^{(i)}]
\le [\gamma_{i+1}(G),G]
=\gamma_{i+2}(G).
$$
Taking $i=c$ gives
$$
G^{(c)}\le \gamma_{c+1}(G)=1.
$$
Hence the derived series terminates, so $G$ is solvable.
:::
