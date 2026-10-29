---
schema: qual/card@1
id: P-QSGCO
kind: problem
title: Representations of $G$ lifted from $G/H$ have common kernel $H$, and the commutator
  subgroup
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Normal Subgroups
  - Commutators
relations: []
review: draft
---

::: {.problem}
Let $H\trianglelefteq G$ with $G$ finite. Lift every representation of $G/H$ along the quotient map $G\to G/H$.

(a) Show that the intersection of the kernels of all lifted representations is exactly $H$.

(b) Interpret the result when $H=[G,G]$.
:::

::: {.solution}
Let $\pi:G\to G/H$ be the quotient map.

::: pf

::: pf-step
(a) The common kernel is $H$.

::: pf-proof
Every lifted representation has the form $\rho\circ\pi$ for some representation $\rho$ of $G/H$, so every such kernel contains $\ker\pi=H$.

Conversely, the regular representation of $G/H$ is faithful: distinct elements of $G/H$ send the basis vector of the identity in the group algebra to distinct basis vectors. Hence the lifted regular representation has kernel exactly $\ker\pi=H$, and the intersection of the kernels of all lifted representations is exactly $H$.
:::

:::

::: pf-step
(b) For $H=[G,G]$, the representations of $G$ that factor through the abelianization $G/[G,G]$ have common kernel exactly $[G,G]$. Over $\CC$,
$$
[G,G]=\bigcap_{\chi:G\to\CC^\times}\ker\chi,
$$
where $\chi$ runs over the linear characters of $G$.

::: pf-proof
The first sentence is (a) with $H=[G,G]$. A linear character $\chi:G\to\CC^\times$ has abelian image, so it kills $[G,G]$ and is a lift of a representation of $G/[G,G]$. Conversely, a complex representation of the finite abelian group $G/[G,G]$ is a direct sum of one-dimensional representations, so its kernel is the intersection of the kernels of those characters. The intersection over all lifted representations therefore equals the intersection over all linear characters.
:::

:::

:::
:::
