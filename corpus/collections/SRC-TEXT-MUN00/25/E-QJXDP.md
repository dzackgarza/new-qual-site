---
schema: qual/card@1
id: E-QJXDP
kind: exercise
title: Weak local connectedness at a point without local connectedness
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Consider the "infinite broom" $X$ pictured in Figure 25.1 of the text.
Show that $X$ is not locally connected at $p$, but is weakly locally connected at $p$.
[Hint: Any connected neighborhood of $p$ must contain all the points $a_i$.]
:::

::: {.solution}
<1>1. Definition of the space $X$ (the infinite broom): <2>1. In $\mathbb{R}^2$, let $a_n = (1, 1/n)$ for $n \in \mathbb{Z}_+$, let $L_n$ be the closed line segment from the origin $(0, 0)$ to $a_n$, and let $p = (1, 0)$.
Proof: definition of the infinite broom in Munkres Figure 25.1. <2>2. The space $X = \left(\bigcup_{n=1}^\infty L_n\right) \cup \{p\}$ is equipped with the subspace topology from $\mathbb{R}^2$.
Proof: definition of $X$.
<2>3. $X$ is a connected topological space: The union $\bigcup_{n=1}^\infty L_n$ is path-connected (every segment contains $(0, 0)$), and $a_n \to p$ as $n \to \infty$, so $p \in \overline{\bigcup_{n=1}^\infty L_n}$.
The closure of a connected space is connected, so $X$ is connected.
Proof: standard property of closures of connected sets.

<1>2. Show that $X$ is **not locally connected** at $p$: <2>1. A space $X$ is locally connected at $p$ if every open neighborhood $U$ of $p$ contains a connected open neighborhood $V$ of $p$.
Proof: definition of local connectedness at a point.
<2>2. Consider the open neighborhood $U = B(p, 1/2) \cap X$.
Proof: $B(p, 1/2)$ is an open ball in $\mathbb{R}^2$ disjoint from the origin $(0, 0)$.
<2>3. Let $V \subseteq U$ be any open neighborhood of $p$ in $X$.
Proof: setup.
<2>4. Since $V$ is open in $X$, $V = W \cap X$ for some open set $W \subseteq \mathbb{R}^2$ containing $p = (1, 0)$.
Proof: subspace topology.
<2>5. Since $a_n = (1, 1/n) \to p$, $W$ contains $a_n$ for all sufficiently large $n \ge N$.
Proof: definition of limit in $\mathbb{R}^2$.
<2>6. For each $n \ge N$, $V$ contains a non-empty open subsegment of $L_n$ near $a_n$.
Proof: $W$ is open and contains $a_n \in L_n$.
<2>7. Since $V \subseteq U \subseteq B(p, 1/2)$, the origin $(0, 0) \notin V$.
Proof: $\operatorname{dist}(p, (0, 0)) = 1 > 1/2$.
<2>8. The subsegments $V \cap L_n$ for distinct $n$ do not meet each other or $p$ in $V$, so they are clopen in $V \setminus \{p\}$.
Thus $V$ is disconnected.
Proof: the segments $L_n$ are pairwise disjoint away from $(0, 0)$.
<2>9. Hence no connected open neighborhood $V \subseteq U$ of $p$ exists, so $X$ is not locally connected at $p$.
Proof: <2>3 and <2>8.

<1>3. Show that $X$ is **weakly locally connected** at $p$: <2>1. A space $X$ is weakly locally connected at $p$ if every neighborhood $U$ of $p$ contains a connected subspace $C$ of $X$ such that $p \in \operatorname{int}(C)$ (or $C$ is a connected neighborhood of $p$). Proof: Munkres §25 definition of weak local connectedness.
<2>2. The space $C = X$ is connected by <1>1. Proof: <1>1. <2>3. $X$ is an open neighborhood of $p$ in $X$, so $p \in \operatorname{int}(X) = X$.
Proof: the whole space is open in itself.
<2>4. Thus $C = X$ is a connected neighborhood of $p$, so $X$ is weakly locally connected at $p$.
Proof: <2>2 and <2>3.

<1>4. Conclusion: $X$ is weakly locally connected at $p$, but not locally connected at $p$.
Q.E.D. Proof: <1>2 and <1>3.
:::
