---
schema: qual/card@1
id: P-QYRBQ
kind: problem
title: No group of order 36 is simple
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that no group of order 36 is simple.
:::

::: solution
**Goal:** Prove that every group $G$ of order $|G| = 36 = 2^2 \cdot 3^2$ has a non-trivial proper normal subgroup.

<1>1. Sylow 3-Subgroups and Sylow's Theorems:
    *Proof:*
    <2>1. Let $|G| = 36 = 4 \cdot 9 = 2^2 \cdot 3^2$.
    <2>2. Let $P \in \operatorname{Syl}_3(G)$ be a Sylow 3-subgroup of $G$, so $|P| = 3^2 = 9$.
    <2>3. By Sylow's Third Theorem, the number $n_3$ of Sylow 3-subgroups satisfies:
        - $n_3 \mid [G : P] = 4 \implies n_3 \in \{1, 2, 4\}$.
        - $n_3 \equiv 1 \pmod 3$.
    <2>4. The only positive divisors of 4 congruent to $1 \pmod 3$ are:
        $$n_3 \in \{1, 4\}.$$

<1>2. Case 1: $n_3 = 1$:
    *Proof:*
    <2>1. If $n_3 = 1$, the unique Sylow 3-subgroup $P$ of order 9 is **normal** in $G$ ($P \trianglelefteq G$).
    <2>2. Since $1 < |P| = 9 < 36$, $P$ is a non-trivial proper normal subgroup.
    <2>3. Thus $G$ is not simple.

<1>3. Case 2: $n_3 = 4$ (Action on Sylow 3-Subgroups):
    *Proof:*
    <2>1. Suppose $n_3 = 4$. Let $X = \operatorname{Syl}_3(G) = \{P_1, P_2, P_3, P_4\}$ be the set of four Sylow 3-subgroups.
    <2>2. $G$ acts on $X$ by conjugation:
        $$g \cdot P_i = g P_i g^{-1}.$$
    <2>3. This group action induces a group homomorphism:
        $$\rho: G \longrightarrow S_4 = \operatorname{Sym}(X).$$
    <2>4. Let $K = \ker\rho \trianglelefteq G$ be the kernel of this action.
    <2>5. We examine the size of the kernel $K$:
        - By the First Isomorphism Theorem, $G / K \cong \operatorname{im}(\rho) \le S_4$.
        - Therefore, $|G/K| = [G : K]$ divides $|S_4| = 24$.
    <2>6. If $K = \{e\}$ (meaning $\rho$ were injective):
        - Then $G \cong \operatorname{im}(\rho) \le S_4$.
        - But by Lagrange's Theorem, this would force $|G| = 36$ to divide $|S_4| = 24$, which is impossible ($36 \nmid 24$)!
    <2>7. Therefore, $K \ne \{e\}$.
    <2>8. Furthermore, since the action by conjugation on Sylow subgroups is transitive (Sylow's Second Theorem), the image $\operatorname{im}(\rho)$ acts transitively on 4 elements, so $|\operatorname{im}(\rho)| \ge 4$.
    <2>9. Thus $|K| = |G| / |\operatorname{im}(\rho)| \le 36/4 = 9 < 36$, so $K \subsetneq G$.
    <2>10. Therefore, $K$ is a **non-trivial proper normal subgroup** of $G$.

<1>4. Conclusion:
    In all cases ($n_3 = 1$ or $n_3 = 4$), $G$ contains a non-trivial proper normal subgroup ($P$ or $K = \ker\rho$). Thus no group of order 36 is simple. Q.E.D.
:::
