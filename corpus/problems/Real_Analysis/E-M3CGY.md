---
schema: qual/card@1
id: E-M3CGY
kind: exercise
title: Every open set in $\RR^n$ is a countable union of almost disjoint closed cubes
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- Show that every open $U \subseteq \RR^n$ is a countable union of *almost* disjoint closed cubes.
:::

::: {.solution}
<1>1. The case $U = \RR^n$ is immediate: the unit cubes $\prod_{i=1}^n [m_i, m_i+1]$ ($m_i \in \ZZ$) are closed, countable, cover $\RR^n$, and have pairwise disjoint interiors (almost disjoint).
Henceforth assume $U \neq \RR^n$.

<1>2. Call a cube *dyadic* if it has the form $\prod_{i=1}^n [m_i 2^{-k}, (m_i+1)2^{-k}]$ for integers $m_i$ and $k \ge 0$.
<2>1. The dyadic cubes of a fixed level $k$ have pairwise disjoint interiors and cover $\RR^n$.
Proof: they form the standard grid of side $2^{-k}$.
<2>2. Any two dyadic cubes have either disjoint interiors or a containment relation.
Proof: each dyadic cube is contained in exactly one dyadic cube of the next coarser level (its parent), so two cubes of the same level have disjoint interiors, while two cubes of different levels are disjoint or nested.

<1>3. Every point $x \in U$ lies in a dyadic cube contained in $U$.
<2>1. There is an open ball $B(x,r) \subseteq U$.
Proof: $U$ is open.
<2>2. Any dyadic cube containing $x$ with side length $s < r/\sqrt n$ is contained in $B(x,r)$, hence in $U$.
Proof: a cube of side $s$ containing $x$ lies inside the ball of radius $\sqrt n\, s$ about $x$ (its diameter is $\sqrt n \, s$). <2>3. Q.E.D. Proof: <2>1 and <2>2.

<1>4. Every point $x \in U$ lies in a *maximal* dyadic cube contained in $U$ (one whose parent is not contained in $U$). <2>1. Let $Q_k(x)$ be the unique dyadic cube of side $2^{-k}$ containing $x$.
Then $\bigcup_{k \ge 0} Q_k(x) = \RR^n$.
Proof: the cubes $Q_k(x)$ are nested and grow with decreasing $k$: given $z \in \RR^n$, once $2^{-k} > \max_i |x_i - z_i|$, the point $z$ shares a dyadic cube of level $k$ with $x$.
<2>2. Since $U \ne \RR^n$, some $Q_k(x)$ is not contained in $U$.
Proof: otherwise $U \supseteq \bigcup_k Q_k(x) = \RR^n$ by <2>1. <2>3. The set $\{k : Q_k(x) \subseteq U\}$ is nonempty and finite, hence has a largest element $k_0$.
Proof: nonempty by <1>3; finite by <2>2. <2>4. $Q_{k_0}(x)$ is a dyadic cube contained in $U$ whose parent is not contained in $U$.
Proof: maximality of $k_0$ in <2>3. <2>5. Q.E.D. Proof: <2>3 and <2>4.

<1>5. Let $\mathcal F$ be the family of all dyadic cubes contained in $U$ whose parent is not contained in $U$.
Then $U = \bigcup_{Q \in \mathcal F} Q$.
Proof: $\bigcup \mathcal F \subseteq U$ by definition; conversely, every $x \in U$ lies in such a cube by <1>4.

<1>6. The family $\mathcal F$ is countable and almost disjoint.
<2>1. $\mathcal F$ is countable.
Proof: level $k$ has exactly $2^{nk}$ dyadic cubes, so $\mathcal F$ is a subset of a countable union of finite sets.
<2>2. The members of $\mathcal F$ have pairwise disjoint interiors.
Proof: by <1>2<2>2, two distinct dyadic cubes have disjoint interiors or one strictly contains the other.
Strict containment $Q \subsetneq Q'$ is impossible in $\mathcal F$: then $Q'$ contains the parent of $Q$, and since the parent is not contained in $U$ (by maximality of $Q$), neither is $Q'$, contradicting $Q' \in \mathcal F$.
<2>3. Q.E.D. Proof: <2>1 and <2>2.

<1>7. Q.E.D. Proof: <1>5 gives the covering, <1>6 gives countability and almost disjointness, and <1>1 handles $U = \RR^n$.
:::
