---
schema: qual/card@1
id: P-SXM4Q
kind: problem
title: The centralizer $C_G(s)$ is a subgroup in which $\langle s\rangle$ is normal
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
  - Normal Subgroups
relations: []
review: draft
---

::: problem
Let $s\in G$. Define $C_G(s)$, prove that it is a subgroup of $G$, and show that $\langle s\rangle\normal C_G(s)$.
:::

::: solution
The centralizer of $s$ in $G$ is
\[
C_G(s)=\{g\in G:gs=sg\}.
\]

It is a subgroup. The identity commutes with $s$. If $g,h\in C_G(s)$, then
\[
(gh)s=g(hs)=g(sh)=(gs)h=(sg)h=s(gh),
\]
so $gh\in C_G(s)$. If $g\in C_G(s)$, then $gs=sg$ implies
\[
g^{-1}s=sg^{-1},
\]
so $g^{-1}\in C_G(s)$.

Also $s\in C_G(s)$, hence $\langle s\rangle\le C_G(s)$. For $g\in C_G(s)$ and any integer $k$,
\[
gs^kg^{-1}=s^kgg^{-1}=s^k.
\]
Thus every element of $C_G(s)$ normalizes $\langle s\rangle$, and in fact conjugation acts trivially on it. Therefore
\[
\langle s\rangle\normal C_G(s).
\]
:::
