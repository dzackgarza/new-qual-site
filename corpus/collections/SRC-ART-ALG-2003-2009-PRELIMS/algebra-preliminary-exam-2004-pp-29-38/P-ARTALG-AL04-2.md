---
schema: qual/card@1
id: P-ARTALG-AL04-2
kind: problem
title: Every group of size 15 is cyclic
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Prove that any group of size 15 is cyclic.

::: {.solution}
<1>1. Sylow analysis of $G$:
<2>1. The order of $G$ is $|G| = 15 = 3 \cdot 5$.
By the Sylow Theorems, the number $n_3$ of Sylow 3-subgroups satisfies:
\[
n_3 \equiv 1 \pmod 3 \quad \text{and} \quad n_3 \mid 5 \implies n_3 = 1.
\]
Thus $G$ contains a unique Sylow 3-subgroup $P$, which is normal in $G$ ($P \triangleleft G$), with $P \cong \mathbb{Z}/3\mathbb{Z}$.
<2>2. Similarly, the number $n_5$ of Sylow 5-subgroups satisfies:
\[
n_5 \equiv 1 \pmod 5 \quad \text{and} \quad n_5 \mid 3 \implies n_5 = 1.
\]
Thus $G$ contains a unique Sylow 5-subgroup $Q$, which is normal in $G$ ($Q \triangleleft G$), with $Q \cong \mathbb{Z}/5\mathbb{Z}$.

<1>2. Internal direct product decomposition:
<2>1. Since $\gcd(|P|, |Q|) = \gcd(3, 5) = 1$, Lagrange's Theorem implies:
\[
P \cap Q = \{e\}.
\]
<2>2. For any $p \in P$ and $q \in Q$, consider the commutator $[p, q] = p q p^{-1} q^{-1}$:
- Since $Q \triangleleft G$, $(p q p^{-1}) q^{-1} \in Q$.
- Since $P \triangleleft G$, $p (q p^{-1} q^{-1}) \in P$.
Thus $[p, q] \in P \cap Q = \{e\}$, which means $pq = qp$ for all $p \in P, q \in Q$.
<2>3. The map $\varphi: P \times Q \to G$ defined by $\varphi(p, q) = pq$ is a group homomorphism.
Its kernel is $\operatorname{ker}(\varphi) = \{(p, q) \mid pq = e\} = \{(p, p^{-1}) \mid p \in P \cap Q\} = \{(e, e)\}$, so $\varphi$ is injective.
Since $|P \times Q| = 3 \cdot 5 = 15 = |G|$, $\varphi$ is an isomorphism:
\[
G \cong P \times Q \cong (\mathbb{Z}/3\mathbb{Z}) \times (\mathbb{Z}/5\mathbb{Z}).
\]

<1>3. Conclusion of cyclicity:
<2>1. By the Chinese Remainder Theorem, since $\gcd(3, 5) = 1$:
\[
(\mathbb{Z}/3\mathbb{Z}) \times (\mathbb{Z}/5\mathbb{Z}) \cong \mathbb{Z}/15\mathbb{Z}.
\]
(Equivalently, if $P = \langle a \rangle$ and $Q = \langle b \rangle$, the element $g = ab$ has order $\operatorname{lcm}(3, 5) = 15$, so $G = \langle ab \rangle$.)
Thus $G$ is cyclic.

<1>4. Conclusion:
Any group of order 15 is isomorphic to $\mathbb{Z}/15\mathbb{Z}$, hence cyclic. Q.E.D.
:::
