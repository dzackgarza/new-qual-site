---
schema: qual/card@1
id: P-5UUNM
kind: problem
title: $Z(G)$ is characteristic in $G$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Automorphisms
  - Subgroups
relations: []
review: draft
---

::: {.exercise}
Show that $Z(G) \leq G$ is always characteristic.
:::

::: {.solution}
Let $\psi\in \Aut(G)$, $g\in Z(G)$, and $h\in G$.
Since $g$ commutes with $\psi\inv(h)$,
$$\psi(g)h=\psi(g)\,\psi(\psi\inv(h))=\psi(g\,\psi\inv(h))=\psi(\psi\inv(h)\,g)=h\,\psi(g).$$
As $h$ is arbitrary, $\psi(g)\in Z(G)$, so $\psi(Z(G)) \subseteq Z(G)$.
Applying the same argument to $\psi\inv$ yields $\psi\inv(Z(G)) \subseteq Z(G)$.
Since $\psi$ is a bijection, $\psi\psi\inv(A) = A$ for all $A\leq G$, 
so $Z(G) \subseteq \psi(Z(G))$.

:::
