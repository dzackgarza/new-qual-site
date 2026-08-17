---
schema: qual/card@1
id: P-AWKNO
kind: problem
title: Use the Class Equation (equivalently, the conjugation action of a group...
classification:
  areas:
  - algebra
  topics:
  - class-equation
  - p-groups
  - abelian-groups
relations: []
review: draft
solved: true
---

::: problem
(a) Use the Class Equation (equivalently, the conjugation action of a group on itself) to prove that any $p\dash$group (a group whose order is a positive power of a prime integer $p$) has a nontrivial center.

(b) Prove that any group of order $p^2$ (where $p$ is prime) is abelian.

(c) Prove that any group of order $5^2 \cdot 7^2$ is abelian.

(d) Write down exactly one representative in each isomorphism class of groups of order $5^2 \cdot 7^2$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) Nontrivial center of a $p$-group:** Let $G$ be a group of order $|G| = p^n$ with $n \geq 1$.
The class equation for the conjugation action of $G$ on itself is:
$$
|G| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)],
$$
where $x_1, \ldots, x_k$ are representatives of the non-central conjugacy classes.
For each $x_i \notin Z(G)$, the centralizer $C_G(x_i)$ is a proper subgroup of $G$, so $[G : C_G(x_i)] = p^{d_i}$ for some integer $d_i \geq 1$.
Thus $p \mid [G : C_G(x_i)]$ for all $i$.
Since $p \mid |G|$ and $p \mid \sum_{i=1}^k [G : C_G(x_i)]$, it follows from the class equation that:
$$
p \mid |Z(G)|.
$$
Since $e \in Z(G)$, $|Z(G)| \geq 1$.
Because $p \mid |Z(G)|$, we must have $|Z(G)| \geq p > 1$, so $Z(G)$ is non-trivial.

**(b) Groups of order $p^2$ are abelian:** Let $|G| = p^2$.
By part (a), $|Z(G)| \in \{p, p^2\}$.

- If $|Z(G)| = p^2$, then $Z(G) = G$, so $G$ is abelian.

- If $|Z(G)| = p$, then the quotient group $G / Z(G)$ has order $|G| / |Z(G)| = p^2 / p = p$.
  Since any group of prime order is cyclic, $G / Z(G)$ is cyclic.
  A standard lemma states: *If $G/Z(G)$ is cyclic, then $G$ is abelian.* (Proof: If $G/Z(G) = \langle gZ(G) \rangle$, any element of $G$ can be written as $g^a z$ for $z \in Z(G)$.
  Two such elements $(g^a z_1)(g^b z_2) = g^{a+b} z_1 z_2 = (g^b z_2)(g^a z_1)$ commute.)
  Thus $G$ is abelian, which contradicts $|Z(G)| = p$.
  Hence $|Z(G)| = p^2$, and $G$ is abelian.

**(c) Groups of order $5^2 \cdot 7^2 = 1225$ are abelian:** Let $|G| = 5^2 \cdot 7^2$.
By Sylow's Theorems:

- The number $n_5$ of Sylow 5-subgroups satisfies $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 7^2 = 49$.
  The divisors of 49 are $1, 7, 49$.
  Modulo 5: $1 \equiv 1$, $7 \equiv 2$, $49 \equiv 4$.
  Thus $n_5 = 1$.

- The number $n_7$ of Sylow 7-subgroups satisfies $n_7 \equiv 1 \pmod 7$ and $n_7 \mid 5^2 = 25$.
  The divisors of 25 are $1, 5, 25$.
  Modulo 7: $1 \equiv 1$, $5 \equiv 5$, $25 \equiv 4$.
  Thus $n_7 = 1$.

Let $P$ be the unique Sylow 5-subgroup and $Q$ be the unique Sylow 7-subgroup.
Since $n_5 = 1$ and $n_7 = 1$, both $P \normal G$ and $Q \normal G$.
Moreover, $|P| = 25$ and $|Q| = 49$, so $\gcd(|P|, |Q|) = 1 \implies P \cap Q = \{e\}$.
Since $P \normal G$ and $Q \normal G$ with $P \cap Q = \{e\}$, elements of $P$ and $Q$ commute, and:
$$
G \cong P \times Q.
$$
By part (b), since $|P| = 5^2$ and $|Q| = 7^2$, both $P$ and $Q$ are abelian.
The direct product of two abelian groups is abelian, so $G$ is abelian.

**(d) Isomorphism classes of groups of order $5^2 \cdot 7^2$:** By part (b), the abelian groups of order $p^2$ up to isomorphism are $\ZZ_{p^2}$ and $\ZZ_p \times \ZZ_p$.
Thus:

- For $P$ (order 25): $P \cong \ZZ_{25}$ or $P \cong \ZZ_5 \times \ZZ_5$.

- For $Q$ (order 49): $Q \cong \ZZ_{49}$ or $Q \cong \ZZ_7 \times \ZZ_7$.

Since $G \cong P \times Q$, there are exactly $2 \times 2 = 4$ isomorphism classes:

1. $\ZZ_{25} \times \ZZ_{49} \cong \ZZ_{1225}$

2. $\ZZ_{25} \times \ZZ_7 \times \ZZ_7 \cong \ZZ_7 \times \ZZ_{175}$

3. $\ZZ_5 \times \ZZ_5 \times \ZZ_{49} \cong \ZZ_5 \times \ZZ_{245}$

4. $\ZZ_5 \times \ZZ_5 \times \ZZ_7 \times \ZZ_7 \cong \ZZ_{35} \times \ZZ_{35}$
:::
