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
$G$ acts on itself by conjugation, $g\cdot x=gxg^{-1}$; its orbits are the conjugacy classes, which partition $G$, and the stabilizer of $x$ is $Z(x)$.
By the orbit-stabilizer theorem, the conjugacy class of $x$ has $[G:Z(x)]$ elements.
The class of $x$ is $\theset{x}$ exactly when $gxg^{-1}=x$ for all $g\in G$, that is, when $x\in Z(G)$.
Summing class sizes, the singleton classes contribute $\size Z(G)$ and the remaining classes contribute $\sum_{i=1}^r[G:Z(g_i)]$.
:::
