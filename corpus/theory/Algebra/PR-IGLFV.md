---
schema: qual/card@1
id: PR-IGLFV
kind: proposition
title: Classification of groups of order $p^2$
slogan: 'Every group of order $p^2$ is abelian: cyclic or $C_p\times C_p$.'
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Abelian Groups
relations: []
review: draft
---

::: {.proposition}
Let $p$ be a prime.
Every group $G$ of order $p^2$ is abelian, and hence $G \cong C_{p^2}$ or $G \cong C_p \times C_p$.
:::

::: {.proof}
By the class equation, the [[D-NK7G7|center]] $Z(G)$ of the $p$-group $G$ is nontrivial, so $\size{Z(G)}\in\theset{p,p^2}$.
If $\size{Z(G)} = p$, then $G/Z(G)$ has order $p$ and is cyclic, and a group whose quotient by its center is cyclic is abelian, so $Z(G)=G$, a contradiction.
Hence $Z(G)=G$ and $G$ is abelian.

If $G$ has an element of order $p^2$, then $G\cong C_{p^2}$.
Otherwise every nonidentity element has order $p$.
Choose $a\neq e$ and $b\notin\generators{a}$; then $\generators a\cap\generators b = 1$, both subgroups are normal because $G$ is abelian, and $\size{\generators a\generators b}=p^2$, so [[T-SVJUN]] gives $G\cong C_p\times C_p$.
:::
