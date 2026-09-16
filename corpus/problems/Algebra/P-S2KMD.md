---
schema: qual/card@1
id: P-S2KMD
kind: problem
title: If $N$ and $G/N$ are solvable then $G$ is solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Normal Subgroups
relations: []
review: draft
---

::: {.problem}
Let $N\normal G$. Show that if $N$ and $G/N$ are solvable, then $G$ is solvable.
:::

::: {.solution}
Let $\pi:G\to G/N$ be the quotient map. Since $G/N$ is solvable, its derived series reaches the identity:
\[
(G/N)^{(r)}=1
\]
for some $r$. Quotient maps preserve commutators, so
\[
\pi(G^{(r)})=(G/N)^{(r)}=1.
\]
Hence
\[
G^{(r)}\le N.
\]

Since $N$ is solvable, there is some $s$ with $N^{(s)}=1$. Because derived subgroups are monotone under inclusion,
\[
G^{(r+s)}=(G^{(r)})^{(s)}\le N^{(s)}=1.
\]
Thus the derived series of $G$ terminates, so $G$ is solvable.
:::
