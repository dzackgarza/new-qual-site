---
schema: qual/card@1
id: P-2GXZ2
kind: problem
title: "Let $R$ be a commutative ring and $a\\in R$."
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - localization
  - rings
relations: []
review: draft
---

Let $R$ be a commutative ring and $a\in R$.
Prove that $a$ is not nilpotent $\iff$ there exists a commutative ring $S$ and a ring homomorphism $\phi: R\to S$ such that $\phi(a)$ is a unit.

> Note: by definition, $a$ is nilpotent $\iff$ there is a natural number $n$ such that $a^n = 0$.

::: {.solution}
$\not A\implies \not B$:

- Suppose $a$ is nilpotent, so $a^m = 0_R$, and suppose $\phi: R\to S$ is a ring morphism.

- Ring morphisms send zero to zero, so $0_S = \phi(0_R) = \phi(a^m) = \phi(a)^m$ and $\phi(a)$ is nilpotent.

- But nontrivial rings can't contain nilpotent units: if $u$ is a unit and $ut= 1$ with $u^k=0$, then $1 = 1^k = (ut)^k = u^k t^k=0$ and $R=0$.

$A\implies B$:

- If $a$ is not nilpotent, localize at the infinite multiplicative subset $A \da \ts{1, a, a^2, \cdots}$ to obtain $R\localize{A}$.
  Since $0\not\in A$, this is not the zero ring.

- By the universal property, there is a map $\phi: R\to R\localize{A}$, and the claim is that $\phi(a)$ is a unit in $R\localize{A}$.

- More directly, $R\localize{A} = \ts{ [p/q] \st p\in R,\, q\in A }$ and $\phi(a) = [a/1]$, whose inverse is $[1/a]$: the product is $[a/a] = [1/1] = 1$.
:::
