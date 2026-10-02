---
schema: qual/card@1
id: FD-L2TEC
kind: definition
title: Class equation
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

::: {.theorem}
Let $G$ be a finite group with [[D-NK7G7|center]] $Z(G)$, and let $x_1,\ldots,x_k$ be representatives of the [[D-HLDEY|conjugacy classes]] of $G$ that contain more than one element.
For $x\in G$, let $C_G(x) \coloneqq \theset{ g\in G \st gxg^{-1} = x }$ be the [[D-PX64W|centralizer]] of $x$.
Then
$$
\abs{G} = \abs{Z(G)} + \sum_{i=1}^k [G: C_G(x_i)].
$$
:::

::: {.proof}
$G$ acts on itself by conjugation, $g\cdot x=gxg^{-1}$; its orbits are the conjugacy classes, which partition $G$, and the stabilizer of $x$ is $C_G(x)$.
By the orbit-stabilizer theorem, the conjugacy class of $x$ has $[G:C_G(x)]$ elements.
The class of $x$ is $\theset{x}$ exactly when $gxg^{-1}=x$ for all $g\in G$, that is, when $x\in Z(G)$.
Summing class sizes, the singleton classes contribute $\abs{Z(G)}$ and the remaining classes contribute $\sum_{i=1}^k[G:C_G(x_i)]$.
:::
