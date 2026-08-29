---
schema: qual/card@1
id: P-2JEMA
kind: problem
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
  date: 2026-08-30
---

::: problem
Let $G$ be a group. Show that the group of inner automorphisms $\operatorname{Inn}(G)$ is isomorphic to the quotient group $G / Z(G)$, where $Z(G)$ is the center of $G$.
:::

::: solution
**Goal:** Prove that $\operatorname{Inn}(G) \cong G / Z(G)$ via the First Isomorphism Theorem for groups.

<1>1. Definition of the Conjugation Homomorphism:
    *Proof:*
    <2>1. For each element $g \in G$, define the conjugation (inner automorphism) map $\phi_g: G \to G$ by:
        $$\phi_g(x) = g x g^{-1} \quad \text{for all } x \in G.$$
    <2>2. $\phi_g$ is an automorphism of $G$ with inverse $\phi_{g^{-1}}$, so $\phi_g \in \operatorname{Aut}(G)$.
    <2>3. By definition, the group of inner automorphisms is:
        $$\operatorname{Inn}(G) = \{\phi_g \mid g \in G\} \le \operatorname{Aut}(G).$$
    <2>4. Define the map $\Phi: G \to \operatorname{Aut}(G)$ by $\Phi(g) = \phi_g$.

<1>2. Proof that $\Phi$ is a group homomorphism:
    *Proof:*
    <2>1. For any $g, h \in G$ and any $x \in G$:
        $$\Phi(gh)(x) = \phi_{gh}(x) = (gh) x (gh)^{-1} = g (h x h^{-1}) g^{-1} = \phi_g(\phi_h(x)) = (\phi_g \circ \phi_h)(x) = (\Phi(g) \circ \Phi(h))(x).$$
    <2>2. Thus $\Phi(gh) = \Phi(g) \circ \Phi(h)$, so $\Phi$ is a homomorphism from $G$ to $\operatorname{Aut}(G)$.
    <2>3. The image of $\Phi$ is precisely $\operatorname{im}(\Phi) = \operatorname{Inn}(G)$.

<1>3. Computation of the Kernel $\ker\Phi$:
    *Proof:*
    <2>1. By definition, the kernel consists of elements $g \in G$ that map to the identity automorphism $\operatorname{id}_G$:
        $$\begin{aligned}
        g \in \ker\Phi &\iff \Phi(g) = \operatorname{id}_G \\
        &\iff \phi_g(x) = x \quad \forall x \in G \\
        &\iff g x g^{-1} = x \quad \forall x \in G \\
        &\iff g x = x g \quad \forall x \in G.
        \end{aligned}$$
    <2>2. The condition that $g$ commutes with every element $x \in G$ is the exact definition of the **center** $Z(G)$:
        $$\ker\Phi = \{g \in G \mid gx = xg \ \forall x \in G\} = Z(G).$$

<1>4. Application of the First Isomorphism Theorem:
    *Proof:*
    <2>1. By the First Isomorphism Theorem for groups:
        $$G / \ker\Phi \cong \operatorname{im}(\Phi).$$
    <2>2. Substituting $\ker\Phi = Z(G)$ and $\operatorname{im}(\Phi) = \operatorname{Inn}(G)$ yields:
        $$G / Z(G) \cong \operatorname{Inn}(G).$$

<1>5. Conclusion:
    $\operatorname{Inn}(G) \cong G / Z(G)$. Q.E.D.
:::
