---
schema: qual/card@1
id: E-HOJKE
kind: exercise
title: $A$ is a field iff $A$ is a simple ring iff every homomorphism from $A$ to
  a nonzero field is injective
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Ideals
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that TFAE:

- $A\in \Field$

- $A$ is a simple ring, so $\Id(A) = \ts{ 0, A }$.

- If $B\in \Field$ is nonzero then every ring morphism $A\to B$ is injective.
:::

::: solution
**Goal:** Prove that for a non-trivial commutative ring $A$ with unity $1 \neq 0$, the following statements are equivalent:
(1) $A$ is a field.
(2) $A$ is a simple ring (the only ideals of $A$ are $(0)$ and $A$).
(3) Every ring homomorphism from $A$ to a field $B$ is injective.

<1>1. Statement (1) implies Statement (2):
    *Proof:*
    <2>1. Assume $A$ is a field. Let $I \subseteq A$ be an ideal of $A$.
    <2>2. If $I \neq (0)$, there exists a non-zero element $x \in I$.
    <2>3. Since $A$ is a field, $x$ has a multiplicative inverse $x^{-1} \in A$.
    <2>4. By the ideal absorption property, $1 = x^{-1} x \in I$.
    <2>5. Since $1 \in I$, for any $a \in A$ we have $a = a \cdot 1 \in I$, so $I = A$.
    <2>6. Thus the only ideals of $A$ are $(0)$ and $A$, which means $A$ is a simple ring.

<1>2. Statement (2) implies Statement (3):
    *Proof:*
    <2>1. Assume $A$ is simple, and let $\varphi: A \to B$ be a ring homomorphism to a field $B$ (with $\varphi(1_A) = 1_B \neq 0_B$).
    <2>2. The kernel $\ker \varphi = \{a \in A : \varphi(a) = 0_B\}$ is an ideal of $A$.
    <2>3. Because $\varphi(1_A) = 1_B \neq 0_B$, $1_A \notin \ker \varphi$, so $\ker \varphi \neq A$.
    <2>4. Since $A$ is simple, the only other possibility is $\ker \varphi = (0)$.
    <2>5. Therefore $\varphi$ is injective.

<1>3. Statement (3) implies Statement (1):
    *Proof:*
    <2>1. Assume every ring homomorphism from $A$ to a field is injective.
    <2>2. Let $x \in A$ be any non-zero element. We want to show that $x$ is a unit in $A$.
    <2>3. Suppose for contradiction that the principal ideal $(x)$ is proper ($(x) \neq A$).
    <2>4. By Krull's Theorem, every proper ideal is contained in a maximal ideal, so there exists a maximal ideal $\mathfrak{m} \subset A$ with $(x) \subseteq \mathfrak{m}$.
    <2>5. The quotient $B = A/\mathfrak{m}$ is a field, and the canonical projection $\pi: A \to A/\mathfrak{m}$ is a ring homomorphism.
    <2>6. By hypothesis (3), $\pi$ must be injective, which implies $\ker \pi = \mathfrak{m} = (0)$.
    <2>7. But $x \in (x) \subseteq \mathfrak{m} = (0)$, so $x = 0$, contradicting $x \neq 0$.
    <2>8. Thus $(x) = A$, which means there exists $y \in A$ such that $xy = 1$.
    <2>9. Therefore every non-zero element of $A$ is invertible, so $A$ is a field.

<1>4. Conclusion:
    *Proof:*
    By <1>1, <1>2, and <1>3, the circular chain of implications $(1) \implies (2) \implies (3) \implies (1)$ holds, establishing equivalence.
:::
