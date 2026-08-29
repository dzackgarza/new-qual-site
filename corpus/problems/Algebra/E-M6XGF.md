---
schema: qual/card@1
id: E-M6XGF
kind: exercise
title: Poincaré's theorem on finite-index subgroups
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Normal Subgroups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Prove Poincaré's theorem for groups: if $H \le G$ is a subgroup of finite index $n = [G : H]$, then there exists a normal subgroup $N \trianglelefteq G$ such that $N \subseteq H$ and the index $[G : N]$ divides $n!$ (so $[G : N] \le n!$).
:::

::: solution
**Goal:** Prove Poincaré's Theorem: the normal core $N = \operatorname{Core}_G(H) = \bigcap_{g \in G} g H g^{-1}$ is normal in $G$, contained in $H$, with $[G : N] \mid n!$.

<1>1. Constructing the coset action:
    *Proof:*
    <2>1. Let $X = G/H = \{g_1 H, g_2 H, \dots, g_n H\}$ be the set of left cosets of $H$ in $G$, where $|X| = n = [G : H]$.
    <2>2. Define the left translation action $\rho: G \to \operatorname{Sym}(X) \cong S_n$ by:
        $$\rho(g)(x H) = (gx) H \quad \text{for } x H \in X.$$
    <2>3. $\rho$ is a well-defined group homomorphism:
        $$\rho(g h)(x H) = (ghx) H = \rho(g)(hx H) = (\rho(g) \circ \rho(h))(x H).$$

<1>2. Kernel of the homomorphism (The Normal Core $N$):
    *Proof:*
    <2>1. Let $N = \ker\rho$. As the kernel of a group homomorphism, $N \trianglelefteq G$ is a normal subgroup of $G$.
    <2>2. By definition:
        $$\begin{aligned}
        g \in \ker\rho &\iff \rho(g)(x H) = x H \quad \forall x \in G \\
        &\iff gx H = x H \quad \forall x \in G \\
        &\iff x^{-1} g x \in H \quad \forall x \in G \\
        &\iff g \in x H x^{-1} \quad \forall x \in G.
        \end{aligned}$$
    <2>3. Thus $N = \bigcap_{x \in G} x H x^{-1}$ is the normal core of $H$ in $G$.
    <2>4. Setting $x = e$ shows $N \subseteq H$.

<1>3. Index and Divisibility:
    *Proof:*
    <2>1. By the First Isomorphism Theorem:
        $$G / N = G / \ker\rho \cong \operatorname{im}(\rho) \le S_n.$$
    <2>2. Thus $G/N$ is isomorphic to a subgroup of $S_n$.
    <2>3. By Lagrange's Theorem on $S_n$, the order $|G/N| = [G : N]$ divides $|S_n| = n!$.
    <2>4. In particular, $[G : N] \le n!$.
    <2>5. Furthermore, by the tower law:
        $$[G : N] = [G : H] \cdot [H : N] = n \cdot [H : N].$$
        Thus $[H : N] = \frac{[G : N]}{n} \le \frac{n!}{n} = (n-1)!$.

<1>4. Conclusion:
    There exists $N \trianglelefteq G$ with $N \subseteq H$ and $[G : N] \mid n!$. Q.E.D.
:::
