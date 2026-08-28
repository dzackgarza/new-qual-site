---
schema: qual/card@1
id: E-6W4WA
kind: exercise
title: Dense subspace
classification:
  areas:
  - topology
  topics:
  - Density
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
- What does it mean for $E\subseteq X$ to be a **dense** subspace?
:::

::: solution
**Goal:** State the precise topological definition of a dense subspace $E \subseteq X$ and establish its standard equivalent characterizations.

<1>1. Primary Definition:
    A subset $E \subseteq X$ of a topological space $X$ is **dense** in $X$ if the topological closure of $E$ in $X$ is the entire space:
    $$\overline{E} = X.$$

<1>2. Equivalent Characterizations:
    Let $E \subseteq X$ be a subset. The following statements are logically equivalent:
    1. $\overline{E} = X$.
    2. Every non-empty open set $U \subseteq X$ intersects $E$ ($U \cap E \neq \varnothing$).
    3. For every point $x \in X$ and every open neighborhood $U$ of $x$, $U \cap E \neq \varnothing$.
    4. The only closed subset of $X$ containing $E$ is $X$ itself.
    5. The interior of the complement of $E$ is empty: $\operatorname{Int}(X \setminus E) = \varnothing$.

<1>3. Proof of equivalence of (1), (2), (3), and (5):
    *Proof:*
    <2>1. **(1) $\iff$ (3):** By the Kuratowski closure definition, $x \in \overline{E}$ if and only if every open neighborhood $U$ of $x$ intersects $E$. Thus $\overline{E} = X$ if and only if every point $x \in X$ satisfies this condition.
    <2>2. **(2) $\iff$ (3):** (3) implies (2) since any non-empty open set $U$ contains some point $x \in U$, and $U$ serves as an open neighborhood of $x$. Conversely, (2) implies (3) by applying (2) to the non-empty open neighborhood $U$.
    <2>3. **(1) $\iff$ (5):** By the duality between closure and interior:
        $$\operatorname{Int}(X \setminus E) = X \setminus \overline{E}.$$
        Hence $\operatorname{Int}(X \setminus E) = \varnothing \iff X \setminus \overline{E} = \varnothing \iff \overline{E} = X$.

<1>4. Metric/Convergence Characterization:
    If $X$ is a metric space (or more generally first-countable), $E \subseteq X$ is dense if and only if for every $x \in X$, there exists a sequence $(x_n)_{n=1}^\infty$ in $E$ such that $x_n \to x$. (For general topological spaces, this holds using nets or filters.) Q.E.D.
:::
