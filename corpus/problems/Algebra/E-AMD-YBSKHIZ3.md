---
schema: qual/card@1
id: E-AMD-YBSKHIZ3
kind: problem
title: $C_G(H)\subseteq N_G(H)\leq G$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Let $G$ be a group and $H \le G$ a subgroup.
(1) Prove that the centralizer $C_G(H)$ and the normalizer $N_G(H)$ are subgroups of $G$, and that:
$$C_G(H) \subseteq N_G(H) \le G.$$
(2) Prove that $C_G(H)$ is a **normal subgroup** of $N_G(H)$, and state the $N/C$ Theorem for the quotient $N_G(H)/C_G(H)$.
:::

::: solution
**Goal:** Prove subgroup inclusions $C_G(H) \trianglelefteq N_G(H) \le G$ and the $N/C$ Theorem.

<1>1. Definitions:
    *Proof:*
    <2>1. The **centralizer** of $H$ in $G$ is the set of elements commuting with every element of $H$:
        $$C_G(H) \coloneqq \{g \in G \mid g h = h g \ \forall h \in H\} = \{g \in G \mid g h g^{-1} = h \ \forall h \in H\}.$$
    <2>2. The **normalizer** of $H$ in $G$ is the set of elements stabilizing $H$ setwise under conjugation:
        $$N_G(H) \coloneqq \{g \in G \mid g H g^{-1} = H\}.$$

<1>2. Proof that $C_G(H) \subseteq N_G(H)$:
    *Proof:*
    <2>1. Let $g \in C_G(H)$.
    <2>2. For every $h \in H$, $g h g^{-1} = h \in H$.
    <2>3. Thus $g H g^{-1} = \{g h g^{-1} \mid h \in H\} = \{h \mid h \in H\} = H$.
    <2>4. By definition of the normalizer, this means $g \in N_G(H)$.
    <2>5. Therefore, $C_G(H) \subseteq N_G(H)$.

<1>3. Proof that $N_G(H) \le G$ and $C_G(H) \le G$ are Subgroups:
    *Proof:*
    <2>1. **$N_G(H)$ is a subgroup:**
        - Identity: $e H e^{-1} = H \implies e \in N_G(H)$.
        - Products: If $x, y \in N_G(H)$, $(x y) H (x y)^{-1} = x (y H y^{-1}) x^{-1} = x H x^{-1} = H \implies x y \in N_G(H)$.
        - Inverses: If $x \in N_G(H)$, $x H x^{-1} = H \implies x^{-1}(x H x^{-1})x = x^{-1} H x \implies H = x^{-1} H (x^{-1})^{-1} \implies x^{-1} \in N_G(H)$.
    <2>2. **$C_G(H)$ is a subgroup:**
        - $e h e^{-1} = h \implies e \in C_G(H)$.
        - If $x, y \in C_G(H)$, $(x y) h (x y)^{-1} = x (y h y^{-1}) x^{-1} = x h x^{-1} = h \implies x y \in C_G(H)$.
        - If $x \in C_G(H)$, $x h x^{-1} = h \implies h = x^{-1} h x \implies x^{-1} h (x^{-1})^{-1} = h \implies x^{-1} \in C_G(H)$.

<1>4. Normality of $C_G(H)$ in $N_G(H)$ and the $N/C$ Theorem:
    *Proof:*
    <2>1. Conjugation defines a group homomorphism from the normalizer to the automorphism group of $H$:
        $$\Psi: N_G(H) \longrightarrow \operatorname{Aut}(H), \qquad n \longmapsto (c_n: h \mapsto n h n^{-1}).$$
    <2>2. The kernel of $\Psi$ is:
        $$\ker\Psi = \{n \in N_G(H) \mid n h n^{-1} = h \ \forall h \in H\} = C_G(H).$$
    <2>3. Being the kernel of a homomorphism, $C_G(H)$ is a **normal subgroup** of $N_G(H)$ ($C_G(H) \trianglelefteq N_G(H)$).
    <2>4. By the First Isomorphism Theorem, we obtain the **$N/C$ Theorem**:
        $$N_G(H) / C_G(H) \cong \operatorname{im}(\Psi) \le \operatorname{Aut}(H).$$

<1>5. Conclusion:
    $C_G(H) \trianglelefteq N_G(H) \le G$, and $N_G(H)/C_G(H)$ embeds into $\operatorname{Aut}(H)$. Q.E.D.
:::
