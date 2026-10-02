---
schema: qual/card@1
id: C-O7CP3
kind: corollary
title: Class equation
slogan: A finite group is its center plus its noncentral conjugacy classes.
prompts:
- State the class equation for a finite group $G$.
classification:
  areas:
  - algebra
  topics:
  - Class Equation
  - Conjugacy
  - Centralizers and Normalizers
relations: []
review: draft
---

::: {.corollary}
Let $G$ be a finite group with [[D-NK7G7|center]] $Z(G)$, and for $g\in G$ let $Z(g) = \theset{h\in G \st hgh^{-1} = g}$ be the [[D-PX64W|centralizer]] of $g$.
Let $g_1, \ldots, g_r$ be representatives of the [[D-HLDEY|conjugacy classes]] of $G$ that have more than one element.
Then
$$
\size G = \size Z(G) + \sum_{i=1}^{r} [G : Z(g_i)],
$$
where $[G:Z(g_i)]$ is the [[D-VJGH5|index]] of $Z(g_i)$ in $G$.
:::

::: {.proof}
The group $G$ acts on itself by conjugation, $h\cdot g=hgh^{-1}$. Its orbits are the conjugacy classes and the stabilizer of $g$ is its centralizer $Z(g)$.
By orbit--stabilizer, the conjugacy class of $g$ has $[G:Z(g)]$ elements.
The conjugacy class of $g$ is a singleton exactly when $g\in Z(G)$.
Summing the sizes of all conjugacy classes therefore gives the displayed formula.
:::
