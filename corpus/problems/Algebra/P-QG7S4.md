---
schema: qual/card@1
id: P-QG7S4
kind: problem
title: $N/C$ theorem
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Automorphisms
  - Isomorphism Theorems
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that $N_G(H) / C_G(H)$ is isomorphic to a subgroup of $\operatorname{Aut}(H)$.
:::

::: solution
**Goal:** Prove the $N/C$ Theorem: for any subgroup $H \le G$, $N_G(H)/C_G(H) \cong A \le \operatorname{Aut}(H)$.

<1>1. Definition of the conjugation homomorphism:
    *Proof:*
    <2>1. For each $g \in N_G(H)$, conjugation by $g$ maps $H$ to $H$ (since $gHg^{-1} = H$ by definition of the normalizer).
    <2>2. Define $\phi_g: H \to H$ by $\phi_g(h) = g h g^{-1}$.
    <2>3. $\phi_g$ is an automorphism of $H$: it is a homomorphism ($\phi_g(hk) = ghkg^{-1} = ghg^{-1} gkg^{-1} = \phi_g(h)\phi_g(k)$), and it is bijective with inverse $\phi_{g^{-1}}$.
    <2>4. Define the map $\Phi: N_G(H) \to \operatorname{Aut}(H)$ by $\Phi(g) = \phi_g$.

<1>2. $\Phi$ is a group homomorphism:
    *Proof:*
    <2>1. For $g_1, g_2 \in N_G(H)$ and $h \in H$:
        $$\Phi(g_1 g_2)(h) = (g_1 g_2) h (g_1 g_2)^{-1} = g_1 (g_2 h g_2^{-1}) g_1^{-1} = \phi_{g_1}(\phi_{g_2}(h)) = (\Phi(g_1) \circ \Phi(g_2))(h).$$
    <2>2. Thus $\Phi(g_1 g_2) = \Phi(g_1) \circ \Phi(g_2)$.

<1>3. Computation of the kernel:
    *Proof:*
    <2>1. By definition, $g \in \ker\Phi$ if and only if $\Phi(g) = \operatorname{id}_H$.
    <2>2. $\Phi(g) = \operatorname{id}_H \iff \phi_g(h) = h$ for all $h \in H \iff ghg^{-1} = h$ for all $h \in H \iff gh = hg$ for all $h \in H$.
    <2>3. This is precisely the condition that $g \in C_G(H)$ (the centralizer of $H$ in $G$).
    <2>4. Since $C_G(H) \subseteq N_G(H)$, we have $\ker\Phi = C_G(H)$.

<1>4. First Isomorphism Theorem:
    *Proof:*
    <2>1. By the First Isomorphism Theorem for groups, $N_G(H) / \ker\Phi \cong \operatorname{im}\Phi$.
    <2>2. Since $\ker\Phi = C_G(H)$ and $\operatorname{im}\Phi \le \operatorname{Aut}(H)$, we obtain $N_G(H) / C_G(H) \cong \operatorname{im}\Phi \le \operatorname{Aut}(H)$.

<1>5. Conclusion:
    $N_G(H)/C_G(H)$ is isomorphic to a subgroup of $\operatorname{Aut}(H)$. Q.E.D.
:::
