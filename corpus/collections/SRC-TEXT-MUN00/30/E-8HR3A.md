---
schema: qual/card@1
id: E-8HR3A
kind: problem
title: Every basis of a second-countable space contains a countable basis
classification:
  areas:
  - topology
  topics:
  - Countability
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $X$ has a countable basis $\ts{B_n}$, then every basis $\mathcal{C}$ for $X$ contains a countable basis for $X$.
[Hint: For every pair of indices $n, m$ for which it is possible, choose $C_{n,m} \in \mathcal{C}$ such that $B_n \subset C_{n,m} \subset B_m$.]
:::

::: solution
**Goal:** Prove that if a topological space $X$ has a countable basis $\mathcal{B} = \{B_n\}_{n \in \mathbb{Z}_+}$, then every basis $\mathcal{C}$ for $X$ contains a countable subcollection $\mathcal{C}' \subseteq \mathcal{C}$ that is also a basis for $X$.

<1>1. Selection of a countable subcollection $\mathcal{C}' \subseteq \mathcal{C}$:
    *Proof:*
    <2>1. Define the index set of pairs:
        $$J = \{(n, m) \in \mathbb{Z}_+ \times \mathbb{Z}_+ \mid \exists C \in \mathcal{C} \text{ such that } B_n \subseteq C \subseteq B_m\}.$$
    <2>2. For each pair $(n, m) \in J$, choose one basis element $C_{n, m} \in \mathcal{C}$ satisfying $B_n \subseteq C_{n, m} \subseteq B_m$.
    <2>3. Define the subcollection:
        $$\mathcal{C}' = \{C_{n, m} \mid (n, m) \in J\} \subseteq \mathcal{C}.$$
    <2>4. Because $J \subseteq \mathbb{Z}_+ \times \mathbb{Z}_+$, $J$ is at most countable, and hence $\mathcal{C}'$ is a countable collection.

<1>2. Verification that $\mathcal{C}'$ is a basis for $X$:
    *Proof:*
    <2>1. Let $U \subseteq X$ be an arbitrary open set, and let $x \in U$.
    <2>2. Since $\mathcal{B} = \{B_n\}$ is a basis and $U$ is open, there exists $m \in \mathbb{Z}_+$ such that $x \in B_m \subseteq U$.
    <2>3. Since $\mathcal{C}$ is a basis and $B_m$ is open, there exists $C \in \mathcal{C}$ such that $x \in C \subseteq B_m$.
    <2>4. Since $\mathcal{B}$ is a basis and $C$ is open, there exists $n \in \mathbb{Z}_+$ such that $x \in B_n \subseteq C$.
    <2>5. Thus we have $B_n \subseteq C \subseteq B_m$, which implies that the pair $(n, m)$ belongs to $J$.
    <2>6. By definition of $\mathcal{C}'$, there is an element $C_{n, m} \in \mathcal{C}'$ satisfying $B_n \subseteq C_{n, m} \subseteq B_m$.
    <2>7. Consequently:
        $$x \in B_n \subseteq C_{n, m} \subseteq B_m \subseteq U.$$
    <2>8. Thus $x \in C_{n, m} \subseteq U$ with $C_{n, m} \in \mathcal{C}'$.

<1>3. Conclusion:
    $\mathcal{C}'$ is a countable subset of $\mathcal{C}$ that forms a basis for the topology of $X$. Q.E.D.
:::
