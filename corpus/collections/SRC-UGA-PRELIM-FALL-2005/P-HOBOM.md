---
schema: qual/card@1
id: P-HOBOM
kind: problem
title: Existence of nonabelian groups of order $5$ and $6$
classification:
  areas:
  - prelim
  topics:
  - Groups
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
For $n = 5, 6$, either give an example of a nonabelian group of order $n$, or prove that none exists.
:::

::: {.solution}
**Case $n = 5$:**

<1>1. Every group of prime order is cyclic, hence abelian.
<2>1. Let $G$ be a group with $|G| = 5$.
Proof: setup.
<2>2. Choose an element $g \in G \setminus \{e\}$.
Proof: $|G| = 5 > 1$.
<2>3. By Lagrange's theorem, the order of the subgroup $\langle g \rangle$ divides $|G| = 5$.
Proof: Lagrange's theorem.
<2>4. Since $g \neq e$, $|\langle g \rangle| > 1$, so $|\langle g \rangle| = 5$.
Proof: $5$ is prime, so its only positive divisors are $1$ and $5$.
<2>5. Therefore, $G = \langle g \rangle \cong \mathbb{Z}/5\mathbb{Z}$, which is cyclic and abelian.
Proof: <2>4. <2>6. No nonabelian group of order $5$ exists.
Proof: <2>5.

**Case $n = 6$:**

<1>2. The symmetric group $S_3$ is a nonabelian group of order $6$.
<2>1. The order of $S_3$ is $3! = 6$.
Proof: order formula for symmetric groups on $3$ elements.
<2>2. Let $\sigma = (1\ 2)$ and $\tau = (2\ 3)$ in $S_3$.
Proof: definitions of transpositions in $S_3$.
<2>3. $\sigma \tau = (1\ 2)(2\ 3) = (1\ 2\ 3)$.
Proof: direct cycle composition: $1 \mapsto 1 \mapsto 2$, $2 \mapsto 3 \mapsto 3$, $3 \mapsto 2 \mapsto 1$.
<2>4. $\tau \sigma = (2\ 3)(1\ 2) = (1\ 3\ 2)$.
Proof: direct cycle composition: $1 \mapsto 2 \mapsto 3$, $2 \mapsto 1 \mapsto 1$, $3 \mapsto 3 \mapsto 2$.
<2>5. Since $\sigma \tau \neq \tau \sigma$, $S_3$ is nonabelian.
Proof: $(1\ 2\ 3) \neq (1\ 3\ 2)$ (for example, they map $1$ to different elements).
<2>6. Hence $S_3$ (or equivalently the dihedral group $D_3$) is a nonabelian group of order $6$.
Proof: <2>1 and <2>5.

<1>3. Q.E.D. Proof: <1>1 and <1>2.
:::
