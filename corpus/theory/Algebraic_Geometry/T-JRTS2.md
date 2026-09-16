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
- How is the Nullstellensatz proved?
- If $L/k$ is a field extension and $L$ is a finitely generated $k$-algebra, show that $L/k$ is algebraic.
- State the weak Nullstellensatz in terms of maximal ideals and in terms of systems of polynomial equations, and deduce the strong form by the Rabinowitsch trick.
---

::: {.theorem title="Hilbert's Nullstellensatz"}
Let $k$ be algebraically closed and let $J \subseteq k[x_1, \ldots, x_n]$ be an ideal.
Then
\[
I(V(J)) = \sqrt{J} .
\]
[@Har10a, Theorem I.1.3A]
:::

::: {.remark}
The weak form is the case $J \neq k[x_1,\ldots,x_n] \implies V(J) \neq \emptyset$, and it is equivalent: the strong form follows from the weak one by the Rabinowitsch trick, adjoining a variable $y$ and the polynomial $1 - yf$.

Algebraic closure is not a convenience here.
Over $\RR$ the ideal $(x^2+1)$ is prime, hence radical, but $V(x^2+1) = \emptyset$ in $\AA^1_\RR$, so $I(V(J)) = (1) \neq \sqrt{J}$.
:::
