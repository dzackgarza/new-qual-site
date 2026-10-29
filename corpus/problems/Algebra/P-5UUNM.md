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
Let $\psi\in \Aut(G)$.

::: pf

::: {.pf-step #forward}
Every automorphism $\psi$ of $G$ satisfies $\psi(Z(G)) \subseteq Z(G)$.

::: pf-proof
Let $g\in Z(G)$ and $h\in G$. Since $g$ commutes with $\inverseof{\psi}(h)$,
$$
\psi(g)h=\psi(g)\,\psi(\inverseof{\psi}(h))=\psi(g\,\inverseof{\psi}(h))=\psi(\inverseof{\psi}(h)\,g)=h\,\psi(g).
$$
As $h$ is arbitrary, $\psi(g)\in Z(G)$.
:::

:::

::: pf-step
$\psi(Z(G))=Z(G)$, so $Z(G)$ is characteristic in $G$.

::: pf-proof
Step [](#forward){.pf-ref} applied to $\inverseof{\psi}$ gives $\inverseof{\psi}(Z(G)) \subseteq Z(G)$. Applying $\psi$ gives $Z(G)\subseteq\psi(Z(G))$, and step [](#forward){.pf-ref} gives the reverse inclusion.
:::

:::

:::

:::
