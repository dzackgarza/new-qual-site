---
schema: qual/card@1
id: P-JX3FO
kind: problem
title: The kernel of a homomorphism is a normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
- Prove that the kernel of a homomorphism is a normal subgroup.
:::

::: solution
**Goal:** Prove that for any group homomorphism $\phi: G \to H$, the kernel $\ker \phi = \{g \in G \mid \phi(g) = e_H\}$ is a normal subgroup of $G$ ($\ker \phi \trianglelefteq G$).

<1>1. $\ker \phi$ is a subgroup of $G$:
    *Proof:*
    <2>1. **Identity:** Since homomorphisms preserve identities, $\phi(e_G) = e_H$, so $e_G \in \ker \phi$. Thus $\ker \phi \neq \varnothing$.
    <2>2. **Subgroup criterion:** Let $x, y \in \ker \phi$. Then $\phi(x) = e_H$ and $\phi(y) = e_H$.
    <2>3. Using the homomorphism property and properties of inverses:
        $$\phi(x y^{-1}) = \phi(x) \phi(y)^{-1} = e_H \cdot e_H^{-1} = e_H \cdot e_H = e_H.$$
    <2>4. Thus $x y^{-1} \in \ker \phi$, so $\ker \phi \le G$.

<1>2. $\ker \phi$ is invariant under conjugation (normality):
    *Proof:*
    <2>1. Let $g \in G$ and $k \in \ker \phi$.
    <2>2. Applying $\phi$ to the conjugate $g k g^{-1}$:
        $$\phi(g k g^{-1}) = \phi(g) \phi(k) \phi(g^{-1}) = \phi(g) e_H \phi(g)^{-1} = \phi(g) \phi(g)^{-1} = e_H.$$
    <2>3. Therefore $g k g^{-1} \in \ker \phi$.
    <2>4. Because $g (\ker \phi) g^{-1} \subseteq \ker \phi$ for all $g \in G$, $\ker \phi$ is normal in $G$.

<1>3. Conclusion:
    $\ker \phi$ is a normal subgroup of $G$ ($\ker \phi \trianglelefteq G$). Q.E.D.
:::
