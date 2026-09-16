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

1. Show that the intersection of the kernels of all lifted representations is exactly $H$.
2. Interpret the result when $H=[G,G]$.
:::

::: {.solution}
Let
\[
\pi:G\to G/H
\]
be the quotient map.

<1>1. The common kernel is $H$.
::: {.proof}
Every lifted representation has the form
\[
\rho\circ\pi
\]
for some representation $\rho$ of $G/H$, so every such kernel contains $H$.

Conversely, use the regular representation of $G/H$. It is faithful: distinct elements of $G/H$ act differently by left translation on the basis vectors of the group algebra. Hence the lifted regular representation has kernel exactly
\[
\ker\pi=H.
\]
Therefore the intersection of the kernels of all lifted representations is exactly $H$.
:::

<1>2. Take $H=[G,G]$.
::: {.proof}
Then
\[
G/H=G^{\mathrm{ab}}
\]
is the abelianization. Thus the representations of $G$ factoring through the abelianization have common kernel exactly
\[
[G,G].
\]
Over $\CC$, since a finite abelian group has only one-dimensional irreducible representations, this can be stated as
\[
[G,G]
=
\bigcap_{\chi:G\to\CC^\times}\ker\chi,
\]
where the intersection runs over all complex linear characters of $G$.
:::
:::
