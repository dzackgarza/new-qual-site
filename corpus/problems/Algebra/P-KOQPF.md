---
schema: qual/card@1
id: P-KOQPF
kind: problem
title: Infinite simple groups have no finite-index subgroups
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that if $G$ is an infinite simple group, then $G$ cannot have a proper subgroup of finite index.
:::

::: solution
**Goal:** Prove that an infinite simple group has no proper subgroup $H < G$ with $[G : H] < \infty$.

<1>1. Setting up the coset action:
    *Proof:*
    <2>1. Suppose, for contradiction, that $H \le G$ is a proper subgroup ($H \ne G$) of finite index $n = [G : H] < \infty$.
    <2>2. Since $H$ is a proper subgroup, $n = [G : H] \ge 2$.
    <2>3. Let $X = G/H = \{g_1 H, g_2 H, \dots, g_n H\}$ be the set of left cosets of $H$ in $G$, with $|X| = n$.
    <2>4. Define the action of $G$ on $X$ by left multiplication:
        $$\rho: G \to \operatorname{Sym}(X) \cong S_n, \qquad g \mapsto (xH \mapsto gxH).$$

<1>2. Properties of the permutation representation $\rho$:
    *Proof:*
    <2>1. The map $\rho: G \to S_n$ is a group homomorphism.
    <2>2. The kernel $K = \ker\rho$ is the normal core of $H$ in $G$:
        $$K = \ker\rho = \bigcap_{g \in G} g H g^{-1}.$$
    <2>3. As the kernel of a group homomorphism, $K \trianglelefteq G$ is a normal subgroup of $G$.

<1>3. Simplicity of $G$ forces $K$:
    *Proof:*
    <2>1. Because $G$ is a simple group, its only normal subgroups are $K = \{e\}$ or $K = G$.
    <2>2. **If $K = G$:** Then $G = \ker\rho \subseteq H \subsetneq G$, which forces $H = G$, contradicting that $H$ is a proper subgroup.
    <2>3. **If $K = \{e\}$:** Then $\rho: G \to S_n$ is an injective homomorphism (an embedding).

<1>4. Deriving the contradiction from injectivity:
    *Proof:*
    <2>1. If $\rho$ is injective, then $G \cong \rho(G) \le S_n$.
    <2>2. Thus $|G| \le |S_n| = n! < \infty$.
    <2>3. This contradicts the hypothesis that $G$ is an **infinite** group!

<1>5. Conclusion:
    Neither $K = G$ nor $K = \{e\}$ is possible. Therefore, no proper subgroup of finite index can exist in an infinite simple group. Q.E.D.
:::
