---
schema: qual/card@1
id: P-DXHST
kind: problem
title: 'Faithful transitive actions: trivial core of a stabilizer, and abelian transitive
  subgroups of $S_n$'
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Suppose the group $G$ acts on the non-empty set $A$.
Assume this action is **faithful** ($\ker(G \to \operatorname{Sym}(A)) = \{1\}$) and **transitive** (for all $a, b \in A$, there exists $g \in G$ such that $g \cdot a = b$).

(a) For $a \in A$, let $G_a = \operatorname{Stab}_G(a)$ denote the stabilizer of $a$. Prove that:
$$
\bigcap_{\sigma \in G} \sigma G_a \sigma^{-1} = \{1\}.
$$

(b) Suppose that $G$ is **abelian**. Prove that $|G| = |A|$, and deduce that every abelian transitive subgroup of the symmetric group $S_n$ has order exactly $n$.
:::

::: solution
**Goal:** Prove that the kernel of a transitive action is the normal core $\bigcap_{g \in G} g G_a g^{-1} = \{1\}$, and show that transitive faithful abelian actions are regular ($G_a = \{1\}$ and $|G| = |A|$).

<1>1. Part (a): Proof that the Normal Core $\bigcap_{\sigma \in G} \sigma G_a \sigma^{-1} = \{1\}$:
    *Proof:*
    <2>1. The action of $G$ on $A$ is given by a group homomorphism $\rho: G \to \operatorname{Sym}(A)$, where $\rho(g)(x) = g \cdot x$.
    <2>2. The kernel of the action is defined as:
        $$\ker(\rho) = \{ g \in G \mid g \cdot x = x \text{ for all } x \in A \} = \bigcap_{x \in A} G_x.$$
    <2>3. Since the action is transitive, every element $x \in A$ can be written as $x = \sigma \cdot a$ for some $\sigma \in G$.
    <2>4. The stabilizer of $x = \sigma \cdot a$ is the conjugate subgroup:
        $$G_x = G_{\sigma \cdot a} = \sigma G_a \sigma^{-1}.$$
    <2>5. Therefore, the intersection of all stabilizers over all points in $A$ is:
        $$\bigcap_{x \in A} G_x = \bigcap_{\sigma \in G} \sigma G_a \sigma^{-1}.$$
    <2>6. Since the action is faithful by hypothesis, $\ker(\rho) = \{1\}$.
    <2>7. Thus:
        $$\bigcap_{\sigma \in G} \sigma G_a \sigma^{-1} = \ker(\rho) = \{1\}.$$

<1>2. Part (b): Faithful Transitive Actions of Abelian Groups are Regular:
    *Proof:*
    <2>1. Now assume that $G$ is **abelian**.
    <2>2. Since $G$ is abelian, every subgroup of $G$ is normal.
    <2>3. In particular, the stabilizer subgroup $G_a$ is normal in $G$:
        $$\sigma G_a \sigma^{-1} = G_a \quad \text{for all } \sigma \in G.$$
    <2>4. Substituting this into the intersection formula from Part (a):
        $$\bigcap_{\sigma \in G} \sigma G_a \sigma^{-1} = \bigcap_{\sigma \in G} G_a = G_a.$$
    <2>5. By Part (a), this intersection is trivial:
        $$G_a = \{1\}.$$
    <2>6. By the **Orbit-Stabilizer Theorem**, since the action is transitive, the single orbit is the entire set $A = G \cdot a$:
        $$|A| = [G : G_a] = \frac{|G|}{|G_a|} = \frac{|G|}{1} = |G|.$$
    <2>7. Thus $|G| = |A|$ (the action is free and transitive, i.e., **simply transitive / regular**).

<1>3. Application to Abelian Transitive Subgroups of $S_n$:
    *Proof:*
    <2>1. Let $G \le S_n$ be an abelian transitive subgroup acting on $A = \{1, 2, \dots, n\}$.
    <2>2. Since $G$ is a subgroup of $S_n = \operatorname{Sym}(A)$, the permutation action of $G$ on $A$ is faithful by definition ($\rho: G \hookrightarrow S_n$ is an inclusion).
    <2>3. Since $G$ is abelian and transitive, by Step 2 we have:
        $$|G| = |A| = n.$$

<1>4. Conclusion:
    (a) $\bigcap_{\sigma \in G} \sigma G_a \sigma^{-1} = \ker(\rho) = \{1\}$;
    (b) $G_a = \{1\} \implies |G| = |A| = n$. Q.E.D.
:::
