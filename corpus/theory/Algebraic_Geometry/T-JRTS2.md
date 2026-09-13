---
schema: qual/card@1
id: T-JRTS2
kind: theorem
title: Hilbert's Nullstellensatz
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nullstellensatz
  - Varieties
relations: []
review: draft
prompts:
- State the Nullstellensatz.
- What is $I(V(J))$?
- Where does the Nullstellensatz use that $k$ is algebraically closed?
---

::: {.theorem title="Hilbert's Nullstellensatz"}
Let $k$ be algebraically closed and let $J \subseteq k[x_1, \ldots, x_n]$ be an ideal.
Then
\[
I(V(J)) = \sqrt{J} .
\]
:::

::: {.remark}
The weak form is the case $J \neq k[x_1,\ldots,x_n] \implies V(J) \neq \emptyset$, and it is equivalent: the strong form follows from the weak one by the Rabinowitsch trick, adjoining a variable $y$ and the polynomial $1 - yf$.

Algebraic closure is not a convenience here.
Over $\RR$ the ideal $(x^2+1)$ is prime, hence radical, but $V(x^2+1) = \emptyset$ in $\AA^1_\RR$, so $I(V(J)) = (1) \neq \sqrt{J}$.
:::
