---
schema: qual/card@1
id: D-5MX7E
kind: definition
title: Colimit
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition}
For a diagram $F: I \to \mathcal C$, the **colimit** is an object $X$ together with maps $\iota_i: F(i) \to X$ commuting with the diagram, universal with that property: any other such cocone $\ts{\psi_i: F(i) \to Y}$ factors through a unique $X \to Y$.
For a directed system $(X_i, f_{ij})$ this is the direct limit: the $\iota_i$ point **out of** the system and into $X$, and a compatible family of maps out of the system extends uniquely over $X$.
The dual notion, reversing all arrows, is a limit.
:::

::: {.example}
\envlist

- Coproducts

- Pushouts

- Direct / inductive limits

- The group $\ZZ[1/p]$, as the colimit of $\ZZ \mapsvia{p} \ZZ \mapsvia{p} \cdots$.
:::

::: {.concept}
See Weibel, *An Introduction to Homological Algebra*, 2.6.7 and Variation 2.6.9.
:::
