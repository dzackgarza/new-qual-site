---
schema: qual/card@1
id: P-Z4O2M
kind: problem
title: Every nonzero homomorphism from a field is injective, and whether the same
  holds for domains
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Homomorphisms
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $R$ and $S$ be commutative rings with multiplicative identity.

1. Prove that when $R$ is a field, every non-zero ring homomorphism $\phi: R\to S$ is injective.

2. Does (a) still hold if we only assume that $R$ is a domain?
   If so, prove it, and if not provide a counterexample.
:::

::: {.solution}
**Part 1.**

<1>1. $\ker \phi$ is an ideal of $R$.
Proof: the kernel of a ring homomorphism is always an ideal.

<1>2. Since $R$ is a field, its only ideals are $(0)$ and $R$.
Proof: a field has no nontrivial ideals.

<1>3. $\ker \phi \neq R$.
Proof: $\phi$ is nonzero, so $\phi(1) = 1 \neq 0$ (a nonzero homomorphism of unital rings sends $1$ to $1$), hence $1 \notin \ker \phi$.

<1>4. Hence $\ker \phi = (0)$, so $\phi$ is injective.
Proof: <1>2 and <1>3.

**Part 2.**

<1>1. No, the statement fails if $R$ is only assumed to be a domain.
Proof: exhibit a counterexample.

<1>2. Counterexample: $R = \ZZ$ (a domain) and $S = \ZZ/2\ZZ$, with $\phi: \ZZ \to \ZZ/2\ZZ$ the reduction mod $2$.
Proof: $\phi$ is a nonzero ring homomorphism.

<1>3. $\phi$ is not injective.
Proof: $\phi(2) = 0$ but $2 \neq 0$, so $\ker \phi = 2\ZZ \neq 0$.

<1>4. Q.E.D.
Proof: <1>4 (part 1) and <1>2–<1>3 (part 2).
:::
