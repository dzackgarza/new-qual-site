---
schema: qual/card@1
id: E-M3CGY
kind: problem
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

::: {.exercise}
- Show that every open $U \subseteq \RR^n$ is a countable union of *almost* disjoint closed cubes.
:::

::: {.solution}
A \dfn{dyadic cube} of level $k \geq 0$ is a cube $\prod_{i=1}^n [m_i 2^{-k}, (m_i+1)2^{-k}]$ with $m_i \in \ZZ$. Its \dfn{parent} is the unique dyadic cube of level $k-1$ containing it, for $k \geq 1$. Closed cubes are \dfn{almost disjoint} if their interiors are pairwise disjoint. Let $U \subseteq \RR^n$ be open.

<1>1. The dyadic cubes of a fixed level are countably many, are almost disjoint, and cover $\RR^n$. Two dyadic cubes are either almost disjoint or one contains the other.

::: {.proof}
The cubes of level $k$ are indexed by $\ZZ^n$ and form the grid of side $2^{-k}$. If $Q$ has level $k$ and $Q'$ has level $k' \leq k$, then $Q$ lies in exactly one cube of level $k'$, its ancestor; either that ancestor is $Q'$, or it is almost disjoint from $Q'$ and hence so is $Q$.
:::

<1>2. If $U = \RR^n$, the level-$0$ dyadic cubes give the required union.

::: {.proof}
Step <1>1.
:::

<1>3. Assume $U \neq \RR^n$, and let $\mathcal F$ be the set of dyadic cubes $Q \subseteq U$ that are of level $0$ or whose parent is not contained in $U$. Then $U = \bigcup_{Q \in \mathcal F} Q$.

<2>1. Every $x \in U$ lies in some dyadic cube contained in $U$.

::: {.proof}
Choose $r > 0$ with $B(x,r) \subseteq U$. A dyadic cube containing $x$ of side $2^{-k} < r/\sqrt n$ has diameter less than $r$, so it lies in $B(x,r)$.
:::

<2>2. Every $x \in U$ lies in some $Q \in \mathcal F$.

::: {.proof}
For each $k$ choose a dyadic cube $Q_k(x) \ni x$ of level $k$ with $Q_{k+1}(x) \subseteq Q_k(x)$, starting from a level-$0$ cube containing $x$ and descending by children. By step <2>1 some $Q_k(x) \subseteq U$ for large $k$, since every level-$k$ cube containing $x$ has diameter $\sqrt n\,2^{-k}$. Let $k_0$ be the least $k$ with $Q_k(x) \subseteq U$. Then either $k_0 = 0$, or the parent $Q_{k_0-1}(x)$ is not contained in $U$; in both cases $Q_{k_0}(x) \in \mathcal F$.
:::

<2>3. Q.E.D.

::: {.proof}
Each $Q \in \mathcal F$ lies in $U$, and step <2>2 gives the reverse inclusion.
:::

<1>4. $\mathcal F$ is countable and almost disjoint.

::: {.proof}
$\mathcal F$ is a subset of the countable set of all dyadic cubes. Let $Q \neq Q'$ be in $\mathcal F$. By step <1>1 they are almost disjoint or one contains the other, say $Q \subsetneq Q'$. Then $Q$ has level at least $1$, and $Q'$ contains the parent of $Q$ by step <1>1. The parent is not contained in $U$ because $Q \in \mathcal F$, so $Q' \not\subseteq U$, a contradiction.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>2 handles $U = \RR^n$; otherwise steps <1>3 and <1>4 write $U$ as the countable almost disjoint union of the cubes in $\mathcal F$.
:::
:::
