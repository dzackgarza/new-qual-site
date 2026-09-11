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
The **total quotient ring** of $A$ is the localisation $S\inv A$.
This is the closest thing to a field of fractions when $A$ is not a domain.
:::

::: {.remark}
One cannot simply invert all nonzero elements when zero divisors are present, since doing so collapses the ring; excluding the zero divisors is the largest choice for which $A \to S\inv A$ stays injective.
When $A$ is a domain, $S = A \smz$ and this is the fraction field.

The sheaf version is what Cartier divisors are defined against.
For $X$ a scheme and $U$ open, let $S(U) \subseteq \Gamma(U,\OO_X)$ be the elements which are not zero divisors in $\OO_{X,p}$ for all $p \in U$; the sheafification of $U \mapsto S(U)\inv\Gamma(U,\OO_X)$ is the **sheaf of total quotient rings** $\mck_X$, the analogue of the function field for a non-integral scheme.
A Cartier divisor is then a global section of $\mck_X\units/\OO_X\units$.
:::
