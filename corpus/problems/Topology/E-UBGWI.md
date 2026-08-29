---
schema: qual/card@1
id: E-UBGWI
kind: exercise
title: The closure is the smallest closed set containing $A$
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Let $X$ be a topological space and $A \subseteq X$ an arbitrary subset.
Prove that the topological closure $\operatorname{cl}_X(A)$ (or $\overline{A}$) is the smallest closed subset of $X$ containing $A$:
$$\overline{A} = \bigcap \{F \subseteq X \mid F \text{ is closed and } A \subseteq F\}.$$
:::

::: solution
**Goal:** Prove that $\overline{A}$ equals the intersection $\mathcal{C}_A \coloneqq \bigcap \{F \text{ closed} \mid A \subseteq F\}$ and is the unique smallest closed set containing $A$.

<1>1. Definition of the Closure and the Intersection of Closed Supersets:
    *Proof:*
    <2>1. In point-set topology, the closure $\overline{A}$ of a set $A \subseteq X$ is defined as the set of all points $x \in X$ such that every open neighborhood $U$ of $x$ intersects $A$ ($U \cap A \ne \varnothing$).
    <2>2. Let $\mathcal{F} = \{F \subseteq X \mid F \text{ is closed in } X \text{ and } A \subseteq F\}$ be the family of all closed subsets containing $A$.
    <2>3. Let $K = \bigcap_{F \in \mathcal{F}} F$.
    <2>4. Since an arbitrary intersection of closed sets is closed, $K$ is a **closed subset** of $X$.
    <2>5. Since $A \subseteq F$ for every $F \in \mathcal{F}$, we have $A \subseteq \bigcap_{F \in \mathcal{F}} F = K$.

<1>2. Proof that $\overline{A} \subseteq K$:
    *Proof:*
    <2>1. Let $F \in \mathcal{F}$ be any closed set containing $A$ ($A \subseteq F$).
    <2>2. We claim that $\overline{A} \subseteq F$.
    <2>3. Let $x \in X \setminus F$. Since $F$ is closed, $U \coloneqq X \setminus F$ is an open neighborhood of $x$.
    <2>4. Since $A \subseteq F$, we have $U \cap A \subseteq (X \setminus F) \cap F = \varnothing$.
    <2>5. Thus $U$ is an open neighborhood of $x$ disjoint from $A$, which means $x \notin \overline{A}$.
    <2>6. By contrapositive, $x \in \overline{A} \implies x \in F$.
    <2>7. Since this holds for all $F \in \mathcal{F}$, we have:
        $$\overline{A} \subseteq \bigcap_{F \in \mathcal{F}} F = K.$$

<1>3. Proof that $K \subseteq \overline{A}$:
    *Proof:*
    <2>1. We show that $\overline{A}$ itself is a closed set containing $A$.
    <2>2. Clearly $A \subseteq \overline{A}$ (since if $a \in A$, any neighborhood $U \ni a$ contains $a \in U \cap A$).
    <2>3. To see that $\overline{A}$ is closed, consider its complement $X \setminus \overline{A}$.
        If $y \in X \setminus \overline{A}$, there exists an open set $V \ni y$ such that $V \cap A = \varnothing$.
        For any $z \in V$, $V$ is an open neighborhood of $z$ disjoint from $A$, so $z \notin \overline{A}$.
        Thus $V \subseteq X \setminus \overline{A}$, proving $X \setminus \overline{A}$ is open, so $\overline{A}$ is **closed**.
    <2>4. Since $\overline{A}$ is closed and $A \subseteq \overline{A}$, $\overline{A} \in \mathcal{F}$.
    <2>5. Therefore, the intersection of all members of $\mathcal{F}$ is contained in $\overline{A}$:
        $$K = \bigcap_{F \in \mathcal{F}} F \subseteq \overline{A}.$$

<1>4. Conclusion:
    Combining Steps <1>2 and <1>3 gives $\overline{A} = K = \bigcap_{A \subseteq F \text{ closed}} F$. Thus $\overline{A}$ is the unique smallest closed set containing $A$ with respect to inclusion. Q.E.D.
:::
