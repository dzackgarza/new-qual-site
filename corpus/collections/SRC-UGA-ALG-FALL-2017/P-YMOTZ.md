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
::: {.problem}
(a) Classify all abelian groups of order 36 up to isomorphism.

For the rest of the problem, assume that $G$ is a non-abelian group of order 36. You may assume that the only subgroup of order 12 in $S_4$ is $A_4$ and that $A_4$ has no subgroup of order 6.

(b) Prove that if the Sylow 2-subgroup of $G$ is normal, then $G$ has a normal subgroup $N$ such that $G/N \cong A_4$.

(c) Show that if $G$ has a normal subgroup $N$ such that $G/N \cong A_4$ and a subgroup $H \cong A_4$, then $G$ must be the direct product of $N$ and $H$.

(d) Show that the dihedral group of order 36 is a non-abelian group of order 36 whose Sylow 2-subgroup is not normal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There are four abelian groups of order $36$, up to isomorphism, represented by $C_{36}$, $C_2\times C_{18}$, $C_3\times C_{12}$, and $C_6\times C_6$.

::: pf-proof

::: pf-step

The prime factorization of 36 is $36 = 2^2 \cdot 3^2$.

:::

::: pf-step

By the Fundamental Theorem of Finitely Generated Abelian Groups, any finite abelian group is isomorphic to a direct product of cyclic groups of prime power orders.

:::

::: pf-step

Partitions of the prime exponents:
        - For $p = 2$: the partitions of 2 are $2$ and $1 + 1$, corresponding to $\ZZ/4\ZZ$ and $\ZZ/2\ZZ \times \ZZ/2\ZZ$.
        - For $p = 3$: the partitions of 2 are $2$ and $1 + 1$, corresponding to $\ZZ/9\ZZ$ and $\ZZ/3\ZZ \times \ZZ/3\ZZ$.

:::

::: pf-step

There are $2 \times 2 = 4$ non-isomorphic abelian groups of order 36:

:::

1. $\ZZ/4\ZZ \times \ZZ/9\ZZ \cong \ZZ/36\ZZ$.
2. $\ZZ/2\ZZ \times \ZZ/2\ZZ \times \ZZ/9\ZZ \cong \ZZ/2\ZZ \times \ZZ/18\ZZ$.
3. $\ZZ/4\ZZ \times \ZZ/3\ZZ \times \ZZ/3\ZZ \cong \ZZ/3\ZZ \times \ZZ/12\ZZ$.
4. $\ZZ/2\ZZ \times \ZZ/2\ZZ \times \ZZ/3\ZZ \times \ZZ/3\ZZ \cong \ZZ/6\ZZ \times \ZZ/6\ZZ$.

:::

:::

::: {.pf-step #s2}

If $G$ is nonabelian with a normal Sylow $2$-subgroup, there exists a normal subgroup $N$ of order three such that $G/N\cong A_4$.

::: pf-proof

::: pf-step

Let $P \in \operatorname{Syl}_2(G)$ with $\cardinality{P} = 4$ and $P \trianglelefteq G$.

:::

::: pf-step

Number of Sylow 3-subgroups: By Sylow's Theorems, $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 4$, so $n_3 \in \{1, 4\}$.

:::

::: pf-step

If $n_3 = 1$, let $Q \in \operatorname{Syl}_3(G)$ ($\cardinality{Q} = 9$). Then $Q \trianglelefteq G$.
        - Since $P \trianglelefteq G$ and $Q \trianglelefteq G$ with $\gcd(\cardinality{P}, \cardinality{Q}) = \gcd(4, 9) = 1$, $P \cap Q = \{e\}$ and $G \cong P \times Q$.
        - Any group of order $p^2$ is abelian, so both $P$ and $Q$ are abelian.
        - The direct product of abelian groups is abelian, so $G$ is abelian, contradicting the hypothesis that $G$ is non-abelian.

:::

::: pf-step

Thus $n_3 = 4$.

:::

::: pf-step

Conjugation action on $\operatorname{Syl}_3(G)$:
        - $G$ acts transitively on the set $X = \operatorname{Syl}_3(G)$ of size 4 by conjugation.
        - This defines a permutation homomorphism $\rho: G \to \operatorname{Sym}(X) \cong S_4$.

:::

::: pf-step

Kernel and image of $\rho$:
        - Let $Q \in X$. The stabilizer is $\operatorname{Stab}_G(Q) = N_G(Q)$, which has index $[G : N_G(Q)] = n_3 = 4$, so $\cardinality{N_G(Q)} = 36/4 = 9$, which forces $N_G(Q) = Q$.
        - The kernel $N = \ker(\rho) = \bigcap_{g \in G} g Q g^{-1} \subseteq Q$ is a 3-group, so $\cardinality{N} \in \{1, 3, 9\}$.
        - The image $\operatorname{Im}(\rho) \cong G/N$ has order $\frac{36}{\cardinality{N}}$ and is a subgroup of $S_4$, so $\frac{36}{\cardinality{N}}$ divides $\cardinality{S_4} = 24$.
        - Thus $\frac{36}{\cardinality{N}}$ divides 24, which requires $3 \mid \cardinality{N}$.
        - If $\cardinality{N} = 9$, then $N = Q \trianglelefteq G$, which would mean $n_3 = 1$, a contradiction.
        - Hence $\cardinality{N} = 3$.

:::

::: pf-step

Identification of the quotient:

:::

- $\cardinality{\operatorname{Im}(\rho)} = \frac{36}{3} = 12$.
- Since $\operatorname{Im}(\rho)$ is a subgroup of order 12 in $S_4$, by the given assumption $\operatorname{Im}(\rho) = A_4$.
- Therefore $G/N \cong A_4$, where $N = \ker(\rho) \trianglelefteq G$ is of order 3.

:::

:::

::: {.pf-step #s3}

If $N\trianglelefteq G$, $G/N\cong A_4$, and $H\leq G$ with $H\cong A_4$, then $G\cong N\times H$.

::: pf-proof

::: pf-step

We are given $N \trianglelefteq G$ with $G/N \cong A_4$ ($\cardinality{N} = 3$) and $H \le G$ with $H \cong A_4$ ($\cardinality{H} = 12$).

:::

::: pf-step

Trivial intersection $N \cap H = \{e\}$:
        - $N \cap H$ is a normal subgroup of $H \cong A_4$ whose order divides $\cardinality{N} = 3$.
        - The normal subgroups of $A_4$ are $\{e\}$, $V_4$ (order 4), and $A_4$ (order 12); $A_4$ has no normal subgroup of order 3.
        - Thus $N \cap H = \{e\}$.

:::

::: pf-step

Full group product:
        - $\cardinality{N H} = \frac{\cardinality{N} \cardinality{H}}{\cardinality{N \cap H}} = \frac{3 \cdot 12}{1} = 36 = \cardinality{G}$.
        - Therefore $G = N H$.

:::

::: pf-step

Commutativity of elements:
        - Conjugation defines a homomorphism $\psi: H \to \operatorname{Aut}(N)$.
        - Since $\cardinality{N} = 3$, $\operatorname{Aut}(N) \cong (\ZZ/3\ZZ)^\times \cong \ZZ/2\ZZ$.
        - The commutator subgroup $[H, H] = [A_4, A_4] = V_4$, so the abelianization of $H$ is $H^{\text{ab}} \cong A_4/V_4 \cong \ZZ/3\ZZ$.
        - Since $\gcd(3, 2) = 1$, there are no non-trivial homomorphisms from $A_4$ to $\ZZ/2\ZZ$, so $\psi$ is trivial.
        - Thus $h n h^{-1} = n$, i.e., $n h = h n$ for all $n \in N$ and $h \in H$.

:::

::: pf-step

Hence $G$ is the internal direct product $G \cong N \times H \cong \ZZ/3\ZZ \times A_4$.

:::

:::

:::

::: {.pf-step #s4}

The dihedral group $D_{18}$ has order $36$, is nonabelian, and has a nonnormal Sylow $2$-subgroup.

::: pf-proof

::: pf-step

The dihedral group of order 36 has presentation:
    $$D_{18} = \langle r, s \mid r^{18} = 1, s^2 = 1, s r s = r^{-1} \rangle.$$

:::

::: pf-step

$\cardinality{D_{18}} = 36$. Since $s r = r^{17} s \ne r s$, $D_{18}$ is non-abelian.

:::

::: pf-step

A Sylow 2-subgroup has order 4.

:::

::: pf-step

Consider the subgroup $P = \{e, r^9, s, s r^9\} \le D_{18}$, which has order 4.

:::

::: pf-step

Conjugate $P$ by $r$:
    $$r s r^{-1} = s r^{-2} = s r^{16}.$$

:::

::: pf-step

Since $s r^{16} \notin P$ ($16 \not\equiv 0, 9 \pmod{18}$), $r P r^{-1} \ne P$.

:::

::: pf-step

Thus the Sylow 2-subgroup $P$ is not normal in $D_{18}$.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove parts (a)--(d), respectively.

:::

:::

:::
