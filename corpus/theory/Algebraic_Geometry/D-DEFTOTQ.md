---
schema: qual/card@1
id: D-DEFTOTQ
kind: definition
title: The total quotient ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Localization
relations: []
review: draft
prompts:
- What is the total quotient ring of a ring, and how does it generalise the fraction field?
- What plays the role of the function field on a non-integral scheme?
---

::: {.definition title="total quotient ring"}
Let $A$ be a ring and $S$ the multiplicative set of elements which are not zero divisors.
The \dfn{total quotient ring} of $A$ is the localisation $\inverseof{S} A$.
:::

::: {.definition title="Sheaf of total quotient rings"}
For $X$ a scheme and $U$ open, let $S(U) \subseteq \Gamma(U,\OO_X)$ be the set of sections whose germ at every $p \in U$ is not a zero divisor in $\OO_{X,p}$.
The sheafification $\mck_X$ of $U \mapsto \inverseof{S(U)}\Gamma(U,\OO_X)$ is the \dfn{sheaf of total quotient rings} of $X$.
:::

::: {.remark}
For a multiplicative subset $T\subseteq A$, the map $A\to \inverseof{T} A$ is injective if and only if $T$ contains no zero divisors; so $S$ is the largest multiplicative subset with $A\to \inverseof{S} A$ injective.
When $A$ is a domain, $S = A \smz$ and $\inverseof{S} A$ is the fraction field.

For $X$ integral with function field $K(X)$, $\mck_X$ is the constant sheaf $K(X)$.
A Cartier divisor on $X$ is a global section of $\unitsof{\mck_X}/\unitsof{\OO_X}$ ([[D-5PQ5W]]).
:::
