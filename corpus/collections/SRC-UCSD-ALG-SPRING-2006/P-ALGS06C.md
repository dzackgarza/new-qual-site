---
schema: qual/card@1
id: P-ALGS06C
kind: problem
title: "Order of 1+p in (Z/p²Z)* and construction of a non-abelian group of order p³"
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

::: problem
Let $p$ be a prime number.

(a) Show that the order of $1 + p$ in $(\mathbb{Z}/p^2\mathbb{Z})^\times$ is equal to $p$.

(b) Use (a) above to construct a non-abelian group of order $p^3$.

(c) Describe the non-abelian group you have constructed in (b) above via generators and relations.
:::

::: {.solution}
<1>1. Part (a): Order of $1 + p$ in $(\mathbb{Z}/p^2\mathbb{Z})^\times$:
<2>1. By the Binomial Theorem:
\[
(1 + p)^p = \sum_{k=0}^p \binom{p}{k} p^k = 1 + \binom{p}{1} p + \sum_{k=2}^p \binom{p}{k} p^k = 1 + p^2 + \sum_{k=2}^p \binom{p}{k} p^k.
\]
Proof: Binomial Theorem.
<2>2. For every $k \ge 2$, the power $p^k$ is a multiple of $p^2$, so:
\[
(1 + p)^p \equiv 1 + p^2 \equiv 1 \pmod{p^2}.
\]
Proof: congruence modulo $p^2$.
<2>3. Since $p \ge 2$, $1 + p \not\equiv 1 \pmod{p^2}$, so the order of $1 + p$ is strictly greater than 1.
Because the order of $1 + p$ divides the prime $p$, the order must be exactly $p$:
\[
o(1 + p) = p \quad \text{in } (\mathbb{Z}/p^2\mathbb{Z})^\times.
\]
Proof: prime order divisibility.

<1>2. Part (b): Construction of a non-abelian group of order $p^3$:
<2>1. Consider the cyclic group $N = \mathbb{Z}/p^2\mathbb{Z}$ and $H = \mathbb{Z}/p\mathbb{Z}$.
The automorphism group of $N$ is $\operatorname{Aut}(N) \cong (\mathbb{Z}/p^2\mathbb{Z})^\times$.
Proof: automorphism group of cyclic groups.
<2>2. By Part (a), the element $1 + p$ has order $p$ in $(\mathbb{Z}/p^2\mathbb{Z})^\times$.
Therefore, there exists a non-trivial group homomorphism $\theta: H \to \operatorname{Aut}(N)$ defined on the generator $1 \in \mathbb{Z}/p\mathbb{Z}$ by:
\[
\theta(1)(x) = (1 + p)x \pmod{p^2}.
\]
Proof: homomorphism from a cyclic group to a group containing an element of order $p$.
<2>3. Define $G$ as the semidirect product $G = N \rtimes_\theta H = (\mathbb{Z}/p^2\mathbb{Z}) \rtimes_\theta (\mathbb{Z}/p\mathbb{Z})$.
The order of $G$ is:
\[
|G| = |N| \cdot |H| = p^2 \cdot p = p^3.
\]
Since $\theta$ is non-trivial ($1 + p \not\equiv 1 \pmod{p^2}$), $G$ is a non-abelian group of order $p^3$.
Proof: definition of semidirect product.

<1>3. Part (c): Generators and relations presentation:
<2>1. Let $a = (1, 0) \in G$ and $b = (0, 1) \in G$.
Then $a$ generates $N \cong \mathbb{Z}/p^2\mathbb{Z}$ (so $a^{p^2} = e$) and $b$ generates $H \cong \mathbb{Z}/p\mathbb{Z}$ (so $b^p = e$).
The semidirect product action gives $b a b^{-1} = \theta(1)(a) = a^{1 + p}$.
Proof: semidirect product conjugation relation.
<2>2. Thus $G$ has the presentation:
\[
G = \langle a, b \mid a^{p^2} = e, \; b^p = e, \; b a b^{-1} = a^{1 + p} \rangle.
\]
Proof: presentation of semidirect product of two cyclic groups.

<1>4. Conclusion:
Parts (a), (b), and (c) are fully established. Q.E.D.
Proof: <1>1 through <1>3.
:::
