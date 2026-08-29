---
schema: qual/card@1
id: P-MZJIA
kind: problem
title: $C_G(H)$ is normal in $N_G(H)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G$ be a group and $H \le G$ a subgroup. Show that the centralizer $C_G(H)$ is a normal subgroup of the normalizer $N_G(H)$ (i.e. $C_G(H) \trianglelefteq N_G(H)$), and that $N_G(H)/C_G(H)$ is isomorphic to a subgroup of $\operatorname{Aut}(H)$ (the $N/C$ Theorem).
:::

::: solution
**Goal:** Prove the $N/C$ Theorem: $C_G(H) \trianglelefteq N_G(H)$ and $N_G(H)/C_G(H) \hookrightarrow \operatorname{Aut}(H)$.

<1>1. Definitions and Conjugation Action:
    *Proof:*
    <2>1. By definition:
        $$N_G(H) = \{g \in G \mid g H g^{-1} = H\},$$
        $$C_G(H) = \{g \in G \mid gh = hg \ \forall h \in H\} = \{g \in G \mid g h g^{-1} = h \ \forall h \in H\}.$$
    <2>2. Since $gh = hg \implies g H g^{-1} = H$, we immediately have $C_G(H) \subseteq N_G(H)$.
    <2>3. For every $n \in N_G(H)$, define the conjugation map $\psi_n: H \to H$ by:
        $$\psi_n(h) = n h n^{-1}.$$
    <2>4. **$\psi_n \in \operatorname{Aut}(H)$:**
        - $\psi_n(h_1 h_2) = n h_1 h_2 n^{-1} = (n h_1 n^{-1})(n h_2 n^{-1}) = \psi_n(h_1)\psi_n(h_2)$.
        - $\psi_n$ is bijective with two-sided inverse $\psi_{n^{-1}}$ (since $n^{-1} \in N_G(H)$).
        - Thus $\psi_n \in \operatorname{Aut}(H)$.

<1>2. The Homomorphism $\Phi: N_G(H) \to \operatorname{Aut}(H)$:
    *Proof:*
    <2>1. Define $\Phi: N_G(H) \to \operatorname{Aut}(H)$ by $\Phi(n) = \psi_n$.
    <2>2. $\Phi$ is a group homomorphism:
        $$\Phi(n_1 n_2)(h) = (n_1 n_2) h (n_1 n_2)^{-1} = n_1 (n_2 h n_2^{-1}) n_1^{-1} = \psi_{n_1}(\psi_{n_2}(h)) = (\Phi(n_1) \circ \Phi(n_2))(h).$$

<1>3. Kernel of $\Phi$ and the First Isomorphism Theorem:
    *Proof:*
    <2>1. The kernel of $\Phi$ consists of all $n \in N_G(H)$ such that $\psi_n = \operatorname{id}_H$:
        $$\begin{aligned}
        n \in \ker\Phi &\iff \psi_n(h) = h \quad \forall h \in H \\
        &\iff n h n^{-1} = h \quad \forall h \in H \\
        &\iff nh = hn \quad \forall h \in H \\
        &\iff n \in C_G(H).
        \end{aligned}$$
    <2>2. Thus $\ker\Phi = C_G(H)$.
    <2>3. As the kernel of a group homomorphism, $C_G(H)$ is a **normal subgroup** of $N_G(H)$:
        $$C_G(H) \trianglelefteq N_G(H).$$
    <2>4. By the First Isomorphism Theorem for groups:
        $$N_G(H) / C_G(H) = N_G(H) / \ker\Phi \cong \operatorname{im}(\Phi) \le \operatorname{Aut}(H).$$

<1>4. Conclusion:
    $C_G(H) \trianglelefteq N_G(H)$, and $N_G(H)/C_G(H)$ embeds isomorphically into $\operatorname{Aut}(H)$. Q.E.D.
:::
