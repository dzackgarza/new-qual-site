---
schema: qual/card@1
id: P-PSCIU
kind: problem
title: The number of subgroups conjugate to $H\le G$ divides $\abs{G}$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Cosets and Lagrange
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and $H<G$ a subgroup. Let
$n_H$ be the number of subgroups of $G$ that are conjugate to $H$. Show
that $n_H$ divides the order of $G$.
:::

::: {.solution}
Let $C_H=\{gHg^{-1}: g\in G\}$, so $\abs{C_H}=n_H$, and let $N_G(H)=\{g\in G: gHg^{-1}=H\}$ be the normalizer of $H$.

::: pf

::: {.pf-step #index}
$n_H=[G:N_G(H)]$.

::: pf-proof
The map $\Phi$ from the set of left cosets of $N_G(H)$ to $C_H$ given by $gN_G(H)\mapsto gHg^{-1}$ is well defined and bijective. For $g,g'\in G$,
$$gHg^{-1}=g'Hg'^{-1}\iff (g'^{-1}g)H(g'^{-1}g)^{-1}=H\iff g'^{-1}g\in N_G(H)\iff gN_G(H)=g'N_G(H).$$
The implication from right to left shows that $\Phi$ is well defined, and the implication from left to right shows that it is injective. It is surjective by the definition of $C_H$.
:::

:::

::: pf-step
$n_H$ divides $\abs{G}$.

::: pf-proof
By Lagrange's theorem, $\abs{G}=[G:N_G(H)]\,\abs{N_G(H)}$, and by step [](#index){.pf-ref} this is $n_H\abs{N_G(H)}$.
:::

:::

:::

:::
