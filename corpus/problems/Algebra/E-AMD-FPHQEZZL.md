---
schema: qual/card@1
id: E-AMD-FPHQEZZL
kind: exercise
title: $\Inn(G)\cong G/Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Isomorphism Theorems
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that $\operatorname{Inn}(G) \cong G / Z(G)$.
:::

::: solution
**Goal:** Prove that the group of inner automorphisms $\operatorname{Inn}(G)$ is isomorphic to the quotient $G / Z(G)$.

<1>1. Definition of the conjugation homomorphism:
    *Proof:*
    <2>1. For each $g \in G$, define the inner automorphism $\iota_g: G \to G$ by:
        $$\iota_g(x) = g x g^{-1} \quad \text{for all } x \in G.$$
    <2>2. The inner automorphism group is $\operatorname{Inn}(G) = \{\iota_g \mid g \in G\} \le \operatorname{Aut}(G)$.
    <2>3. Define the map $\Phi: G \to \operatorname{Aut}(G)$ by $\Phi(g) = \iota_g$.
    <2>4. For any $g, h, x \in G$:
        $$\iota_{gh}(x) = (gh) x (gh)^{-1} = g (h x h^{-1}) g^{-1} = \iota_g(\iota_h(x)) = (\iota_g \circ \iota_h)(x).$$
    <2>5. Thus $\Phi(gh) = \Phi(g) \circ \Phi(h)$, so $\Phi$ is a group homomorphism.

<1>2. Determination of the image and kernel:
    *Proof:*
    <2>1. **Image:** By definition of $\operatorname{Inn}(G)$, the image is $\operatorname{im}(\Phi) = \operatorname{Inn}(G)$.
    <2>2. **Kernel:** An element $g \in G$ lies in $\ker \Phi$ if and only if $\Phi(g) = \operatorname{id}_G$:
        $$\begin{aligned}
        g \in \ker \Phi &\iff \iota_g(x) = x \quad \forall x \in G \\
        &\iff g x g^{-1} = x \quad \forall x \in G \\
        &\iff g x = x g \quad \forall x \in G \\
        &\iff g \in Z(G).
        \end{aligned}$$
    <2>3. Thus $\ker \Phi = Z(G)$, the center of $G$.

<1>3. Application of the First Isomorphism Theorem:
    *Proof:*
    <2>1. By the First Isomorphism Theorem for groups applied to $\Phi: G \to \operatorname{Aut}(G)$:
        $$G / \ker \Phi \cong \operatorname{im}(\Phi).$$
    <2>2. Substituting $\ker \Phi = Z(G)$ and $\operatorname{im}(\Phi) = \operatorname{Inn}(G)$:
        $$G / Z(G) \cong \operatorname{Inn}(G).$$

<1>4. Conclusion:
    $\operatorname{Inn}(G) \cong G / Z(G)$. Q.E.D.
:::
