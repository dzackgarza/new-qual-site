---
schema: qual/card@1
id: P-TX3CN
kind: problem
title: A finite-index subgroup contains a finite-index normal subgroup contained in
  every conjugate
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
---

::: problem
Let $G$ be a group containing a proper subgroup $H \lneq G$ of finite index $[G : H] < \infty$.

Prove that $G$ contains a normal subgroup $N \trianglelefteq G$ of finite index that is contained in every conjugate of $H$.
:::

::: solution
**Goal:** Prove the existence of the normal core $N = \operatorname{Core}_G(H) = \bigcap_{g \in G} g H g^{-1}$ using the left regular action of $G$ on the coset space $G/H$.

<1>1. Permutation action on cosets:
    *Proof:*
    <2>1. Let $n = [G : H] < \infty$, and let $X = G/H = \{g H \mid g \in G\}$ be the set of left cosets of $H$ in $G$, so $|X| = n$.
    <2>2. $G$ acts on $X$ by left multiplication:
    $$g \cdot (x H) = (g x) H \quad \text{for all } g \in G \text{ and } x H \in X.$$
    <2>3. This group action defines a permutation homomorphism $\rho: G \to \operatorname{Sym}(X) \cong S_n$.

<1>2. Kernel characterization and containment in all conjugates:
    *Proof:*
    <2>1. Define $N = \ker(\rho)$.
    <2>2. An element $g \in G$ belongs to $\ker(\rho)$ if and only if $g \cdot (x H) = x H$ for all $x \in G$.
    <2>3. Equivalence of condition:
    $$g x H = x H \iff x^{-1} g x H = H \iff x^{-1} g x \in H \iff g \in x H x^{-1}.$$
    <2>4. Thus the kernel is precisely the intersection of all conjugates of $H$:
    $$N = \ker(\rho) = \bigcap_{x \in G} x H x^{-1}.$$
    <2>5. Consequently, $N \subseteq g H g^{-1}$ for every $g \in G$, so $N$ is contained in every conjugate of $H$.

<1>3. Normality and finite index:
    *Proof:*
    <2>1. As the kernel of a group homomorphism $\rho: G \to \operatorname{Sym}(X)$, $N \trianglelefteq G$.
    <2>2. By the First Isomorphism Theorem:
    $$G/N \cong \operatorname{Im}(\rho) \le \operatorname{Sym}(X) \cong S_n.$$
    <2>3. Therefore, the index of $N$ in $G$ is
    $$[G : N] = |G/N| = |\operatorname{Im}(\rho)|.$$
    <2>4. By Lagrange's Theorem, $[G : N]$ divides $|\operatorname{Sym}(X)| = n! = [G : H]!$.
    <2>5. Since $n < \infty$, $[G : N] \le n! < \infty$, so $N$ is of finite index in $G$.

<1>4. Conclusion:
    *Proof:*
    $N = \bigcap_{x \in G} x H x^{-1}$ is a normal subgroup of finite index $[G : N] \le [G : H]!$ contained in every conjugate of $H$.
:::
