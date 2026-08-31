---
schema: qual/card@1
id: P-YMOTZ
kind: problem
title: Abelian groups of order 36, and nonabelian groups of order 36
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Abelian Groups
relations: []
review: draft
---

::: problem
(a) Classify all abelian groups of order 36 up to isomorphism.

For the rest of the problem, assume that $G$ is a non-abelian group of order 36. You may assume that the only subgroup of order 12 in $S_4$ is $A_4$ and that $A_4$ has no subgroup of order 6.

(b) Prove that if the Sylow 2-subgroup of $G$ is normal, then $G$ has a normal subgroup $N$ such that $G/N \cong A_4$.

(c) Show that if $G$ has a normal subgroup $N$ such that $G/N \cong A_4$ and a subgroup $H \cong A_4$, then $G$ must be the direct product of $N$ and $H$.

(d) Show that the dihedral group of order 36 is a non-abelian group of order 36 whose Sylow 2-subgroup is not normal.
:::

::: solution
**Goal:** Classify abelian groups of order 36, prove that non-abelian groups with normal Sylow 2-subgroups admit an $A_4$ quotient, prove direct product decomposition, and exhibit $D_{18}$ as a non-abelian counterexample to Sylow 2 normality.

<1>1. Part (a): Classification of abelian groups of order 36.
::: {.proof}
    <2>1. The prime factorization of 36 is $36 = 2^2 \cdot 3^2$.
    <2>2. By the Fundamental Theorem of Finitely Generated Abelian Groups, any finite abelian group is isomorphic to a direct product of cyclic groups of prime power orders.
    <2>3. Partitions of the prime exponents:
        - For $p = 2$: the partitions of 2 are $2$ and $1 + 1$, corresponding to $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$.
        - For $p = 3$: the partitions of 2 are $2$ and $1 + 1$, corresponding to $\mathbb{Z}/9\mathbb{Z}$ and $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$.
    <2>4. There are $2 \times 2 = 4$ non-isomorphic abelian groups of order 36:
        1. $\mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/9\mathbb{Z} \cong \mathbb{Z}/36\mathbb{Z}$.
        2. $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/9\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/18\mathbb{Z}$.
        3. $\mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \cong \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/12\mathbb{Z}$.
        4. $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z} \times \mathbb{Z}/6\mathbb{Z}$.

:::

<1>2. Part (b): If $P \in \operatorname{Syl}_2(G)$ is normal, then $G/N \cong A_4$ for some normal subgroup $N \trianglelefteq G$.
::: {.proof}
    <2>1. Let $P \in \operatorname{Syl}_2(G)$ with $|P| = 4$ and $P \trianglelefteq G$.
    <2>2. Number of Sylow 3-subgroups: By Sylow's Theorems, $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 4$, so $n_3 \in \{1, 4\}$.
    <2>3. If $n_3 = 1$, let $Q \in \operatorname{Syl}_3(G)$ ($|Q| = 9$). Then $Q \trianglelefteq G$.
        - Since $P \trianglelefteq G$ and $Q \trianglelefteq G$ with $\gcd(|P|, |Q|) = \gcd(4, 9) = 1$, $P \cap Q = \{e\}$ and $G \cong P \times Q$.
        - Any group of order $p^2$ is abelian, so both $P$ and $Q$ are abelian.
        - The direct product of abelian groups is abelian, so $G$ is abelian, contradicting the hypothesis that $G$ is non-abelian.
    <2>4. Thus $n_3 = 4$.
    <2>5. Conjugation action on $\operatorname{Syl}_3(G)$:
        - $G$ acts transitively on the set $X = \operatorname{Syl}_3(G)$ of size 4 by conjugation.
        - This defines a permutation homomorphism $\rho: G \to \operatorname{Sym}(X) \cong S_4$.
    <2>6. Kernel and image of $\rho$:
        - Let $Q \in X$. The stabilizer is $\operatorname{Stab}_G(Q) = N_G(Q)$, which has index $[G : N_G(Q)] = n_3 = 4$, so $|N_G(Q)| = 36/4 = 9$, which forces $N_G(Q) = Q$.
        - The kernel $N = \ker(\rho) = \bigcap_{g \in G} g Q g^{-1} \subseteq Q$ is a 3-group, so $|N| \in \{1, 3, 9\}$.
        - The image $\operatorname{Im}(\rho) \cong G/N$ has order $\frac{36}{|N|}$ and is a subgroup of $S_4$, so $\frac{36}{|N|}$ divides $|S_4| = 24$.
        - Thus $\frac{36}{|N|}$ divides 24, which requires $3 \mid |N|$.
        - If $|N| = 9$, then $N = Q \trianglelefteq G$, which would mean $n_3 = 1$, a contradiction.
        - Hence $|N| = 3$.
    <2>7. Identification of the quotient:
        - $|\operatorname{Im}(\rho)| = \frac{36}{3} = 12$.
        - Since $\operatorname{Im}(\rho)$ is a subgroup of order 12 in $S_4$, by the given assumption $\operatorname{Im}(\rho) = A_4$.
        - Therefore $G/N \cong A_4$, where $N = \ker(\rho) \trianglelefteq G$ is of order 3.

:::

<1>3. Part (c): Direct product decomposition $G \cong N \times H$.
::: {.proof}
    <2>1. We are given $N \trianglelefteq G$ with $G/N \cong A_4$ ($|N| = 3$) and $H \le G$ with $H \cong A_4$ ($|H| = 12$).
    <2>2. Trivial intersection $N \cap H = \{e\}$:
        - $N \cap H$ is a normal subgroup of $H \cong A_4$ whose order divides $|N| = 3$.
        - The normal subgroups of $A_4$ are $\{e\}$, $V_4$ (order 4), and $A_4$ (order 12); $A_4$ has no normal subgroup of order 3.
        - Thus $N \cap H = \{e\}$.
    <2>3. Full group product:
        - $|N H| = \frac{|N| |H|}{|N \cap H|} = \frac{3 \cdot 12}{1} = 36 = |G|$.
        - Therefore $G = N H$.
    <2>4. Commutativity of elements:
        - Conjugation defines a homomorphism $\psi: H \to \operatorname{Aut}(N)$.
        - Since $|N| = 3$, $\operatorname{Aut}(N) \cong (\mathbb{Z}/3\mathbb{Z})^\times \cong \mathbb{Z}/2\mathbb{Z}$.
        - The commutator subgroup $[H, H] = [A_4, A_4] = V_4$, so the abelianization of $H$ is $H^{\text{ab}} \cong A_4/V_4 \cong \mathbb{Z}/3\mathbb{Z}$.
        - Since $\gcd(3, 2) = 1$, there are no non-trivial homomorphisms from $A_4$ to $\mathbb{Z}/2\mathbb{Z}$, so $\psi$ is trivial.
        - Thus $h n h^{-1} = n$, i.e., $n h = h n$ for all $n \in N$ and $h \in H$.
    <2>5. Hence $G$ is the internal direct product $G \cong N \times H \cong \mathbb{Z}/3\mathbb{Z} \times A_4$.

:::

<1>4. Part (d): $D_{18}$ is non-abelian of order 36 with non-normal Sylow 2-subgroups.
::: {.proof}
    <2>1. The dihedral group of order 36 has presentation:
    $$D_{18} = \langle r, s \mid r^{18} = 1, s^2 = 1, s r s = r^{-1} \rangle.$$
    <2>2. $|D_{18}| = 36$. Since $s r = r^{17} s \ne r s$, $D_{18}$ is non-abelian.
    <2>3. A Sylow 2-subgroup has order 4.
    <2>4. Consider the subgroup $P = \{e, r^9, s, s r^9\} \le D_{18}$, which has order 4.
    <2>5. Conjugate $P$ by $r$:
    $$r s r^{-1} = s r^{-2} = s r^{16}.$$
    <2>6. Since $s r^{16} \notin P$ ($16 \not\equiv 0, 9 \pmod{18}$), $r P r^{-1} \ne P$.
    <2>7. Thus the Sylow 2-subgroup $P$ is not normal in $D_{18}$.

:::

<1>5. Conclusion:
::: {.proof}
    Abelian groups of order 36 are classified by integer partitions, normal Sylow 2-subgroups yield an $A_4$ quotient via conjugation on $\operatorname{Syl}_3(G)$, subgroups isomorphic to $A_4$ decompose $G$ as a direct product $\mathbb{Z}/3\mathbb{Z} \times A_4$, and $D_{18}$ has non-normal Sylow 2-subgroups.
:::
:::
