---
schema: qual/card@1
id: P-5SNWD
kind: problem
title: $H\operatorname{char} K\operatorname{char} G$ implies $H\operatorname{char}
  G$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Subgroups
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G$ be a group, and let $H \le K \le G$ be subgroups.
Prove that if $H$ is a characteristic subgroup of $K$ ($H \operatorname{char} K$) and $K$ is a characteristic subgroup of $G$ ($K \operatorname{char} G$), then $H$ is a characteristic subgroup of $G$ ($H \operatorname{char} G$).
:::

::: solution
**Goal:** Prove the transitivity of the characteristic subgroup relation: $H \operatorname{char} K \text{ and } K \operatorname{char} G \implies H \operatorname{char} G$.

<1>1. Definition of a Characteristic Subgroup:
    *Proof:*
    <2>1. A subgroup $A \le B$ is **characteristic** in $B$ (denoted $A \operatorname{char} B$) if for every automorphism $\sigma \in \operatorname{Aut}(B)$, the image of $A$ under $\sigma$ is contained in $A$:
        $$\sigma(A) = A \quad \text{for all } \sigma \in \operatorname{Aut}(B).$$

<1>2. Restricting an Automorphism of $G$ to $K$:
    *Proof:*
    <2>1. Let $\phi \in \operatorname{Aut}(G)$ be an arbitrary automorphism of the whole group $G$.
    <2>2. Since $K \operatorname{char} G$, by definition of characteristic subgroup, $\phi(K) = K$.
    <2>3. Consider the restriction of the map $\phi$ to the subgroup $K$, denoted $\psi \coloneqq \phi|_K: K \to K$.
    <2>4. We verify that $\psi$ is an automorphism of $K$ ($\psi \in \operatorname{Aut}(K)$):
        - **Homomorphism:** For any $x, y \in K$, $\psi(xy) = \phi(xy) = \phi(x)\phi(y) = \psi(x)\psi(y)$ because $\phi$ is a homomorphism.
        - **Injective:** $\ker(\psi) = \ker(\phi) \cap K = \{e\} \cap K = \{e\}$.
        - **Surjective:** The image $\psi(K) = \phi(K) = K$.
    <2>5. Therefore, $\psi = \phi|_K \in \operatorname{Aut}(K)$ is an automorphism of $K$.

<1>3. Invariance of $H$ under $\phi$:
    *Proof:*
    <2>1. Since $H \operatorname{char} K$, the subgroup $H$ is invariant under every automorphism of $K$.
    <2>2. In particular, applying the automorphism $\psi \in \operatorname{Aut}(K)$ to $H$:
        $$\psi(H) = H.$$
    <2>3. Since $\psi(h) = \phi(h)$ for all $h \in H \subseteq K$, we have:
        $$\phi(H) = \psi(H) = H.$$
    <2>4. Since $\phi \in \operatorname{Aut}(G)$ was arbitrary, this holds for all automorphisms $\phi \in \operatorname{Aut}(G)$.
    <2>5. Thus, $H \operatorname{char} G$.

<1>4. Contrast with Normality (Non-transitivity of normal subgroups):
    *Proof:*
    <2>1. While $H \trianglelefteq K \trianglelefteq G$ does not generally imply $H \trianglelefteq G$ (e.g. $H = \langle (12)(34) \rangle \trianglelefteq V_4 \trianglelefteq A_4$, but $H \not\trianglelefteq A_4$), the stronger relation $H \operatorname{char} K \trianglelefteq G$ *does* imply $H \trianglelefteq G$.

<1>5. Conclusion:
    $H \operatorname{char} K \operatorname{char} G \implies H \operatorname{char} G$. Q.E.D.
:::
