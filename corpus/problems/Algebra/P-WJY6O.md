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

::: problem
Show that every nilpotent group is solvable.
:::

::: solution
Suppose $G$ is nilpotent. Then its lower central series
\[
\gamma_1(G)=G,
\qquad
\gamma_{i+1}(G)=[\gamma_i(G),G]
\]
terminates:
\[
\gamma_{c+1}(G)=1
\]
for some $c$.

Let $G^{(i)}$ denote the derived series,
\[
G^{(0)}=G,
\qquad
G^{(i+1)}=[G^{(i)},G^{(i)}].
\]
We claim inductively that
\[
G^{(i)}\le \gamma_{2^i}(G).
\]
For $i=0$ this is clear. If it holds for $i$, then
\[
G^{(i+1)}=[G^{(i)},G^{(i)}]
\le [\gamma_{2^i}(G),\gamma_{2^i}(G)]
\le \gamma_{2^{i+1}}(G).
\]
Choose $i$ with $2^i>c$. Then
\[
G^{(i)}\le \gamma_{2^i}(G)=1.
\]
Hence the derived series terminates, so $G$ is solvable.
:::
