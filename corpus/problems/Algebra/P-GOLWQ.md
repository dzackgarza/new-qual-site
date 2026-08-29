---
schema: qual/card@1
id: P-GOLWQ
kind: problem
title: A field homomorphism is zero or injective
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
- Show that any field morphism is either 0 or injective.
:::

::: solution
**Goal:** Prove that for any ring homomorphism $\phi: F \to R$ from a field $F$ to a ring $R$, $\phi$ is either the zero map or injective.

<1>1. The kernel of $\phi$ is an ideal of $F$:
    *Proof:*
    <2>1. By the First Isomorphism Theorem for rings, the kernel $\ker \phi = \{x \in F \mid \phi(x) = 0_R\}$ is an ideal of the field $F$.

<1>2. Classification of ideals in a field:
    *Proof:*
    <2>1. Let $I \subseteq F$ be an ideal of $F$.
    <2>2. If $I \neq (0)$, there exists some non-zero element $a \in I \setminus \{0\}$.
    <2>3. Because $F$ is a field, every non-zero element is a unit, so $a^{-1} \in F$ exists.
    <2>4. By the absorption property of ideals, $1_F = a^{-1} \cdot a \in I$.
    <2>5. For any $x \in F$, $x = x \cdot 1_F \in I$, which proves $I = F$.
    <2>6. Thus the only ideals in $F$ are the trivial ideal $(0)$ and the improper ideal $F$.

<1>3. Dichotomy for $\phi$:
    *Proof:*
    <2>1. Applying <1>2 to $I = \ker \phi$, either $\ker \phi = F$ or $\ker \phi = (0)$.
    <2>2. **If $\ker \phi = F$:** Then $\phi(x) = 0_R$ for all $x \in F$, so $\phi$ is the zero homomorphism.
    <2>3. **If $\ker \phi = (0)$:** For any $x, y \in F$:
        $$\phi(x) = \phi(y) \implies \phi(x - y) = 0_R \implies x - y \in \ker \phi = (0) \implies x = y.$$
        Thus $\phi$ is injective.

<1>4. Conclusion:
    Every ring homomorphism from a field is either identically $0$ or injective. Q.E.D.
:::
