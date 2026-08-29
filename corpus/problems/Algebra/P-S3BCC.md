---
schema: qual/card@1
id: P-S3BCC
kind: problem
title: The kernel of the conjugation homomorphism $G\to\mathrm{Aut}(G)$ is $Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G$ be a group and let $\gamma: G \to \operatorname{Aut}(G)$ be the conjugation homomorphism defined by $\gamma(g) = c_g$, where $c_g(h) = g h g^{-1}$ for all $h \in G$.
Show that the kernel of $\gamma$ is the center of $G$:
$$\ker(\gamma) = Z(G).$$
:::

::: solution
**Goal:** Prove that the kernel of the inner automorphism homomorphism $\gamma: G \to \operatorname{Aut}(G)$ is the center $Z(G) = \{g \in G \mid gh = hg \text{ for all } h \in G\}$.

<1>1. Definition of the Kernel:
    *Proof:*
    <2>1. The identity element in the group $\operatorname{Aut}(G)$ is the identity automorphism $\operatorname{id}_G: G \to G$, where $\operatorname{id}_G(h) = h$ for all $h \in G$.
    <2>2. By definition of the kernel of a group homomorphism:
        $$\ker(\gamma) = \{ g \in G \mid \gamma(g) = \operatorname{id}_G \}.$$

<1>2. Equivalence of Conditions:
    *Proof:*
    <2>1. For any element $g \in G$:
        $$\gamma(g) = \operatorname{id}_G \iff c_g(h) = h \quad \text{for all } h \in G.$$
    <2>2. Using the definition $c_g(h) = g h g^{-1}$:
        $$g h g^{-1} = h \quad \text{for all } h \in G.$$
    <2>3. Right-multiplying both sides of $g h g^{-1} = h$ by $g$:
        $$g h = h g \quad \text{for all } h \in G.$$
    <2>4. The condition that $g h = h g$ for all $h \in G$ is precisely the definition of the **center** $Z(G)$.

<1>3. Conclusion:
    $$\ker(\gamma) = \{ g \in G \mid gh = hg \text{ for all } h \in G \} = Z(G).$$
    This also gives the First Isomorphism Theorem identification $\operatorname{Inn}(G) \cong G / Z(G)$. Q.E.D.
:::
