---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-METRIC1
kind: problem
title: 'A closed and bounded noncompact subset of a metric space'
classification:
  areas:
  - real-analysis
  topics:
  - compactness
  - metric-spaces
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Find an example of a metric space $X$ and a subset $E\subseteq X$ such that $E$ is closed and bounded but not compact.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Find a metric space $X$ and a closed bounded subset $E \subseteq X$ that is not compact.

<1>1. Example: $X = \ell^2$ (or $\mathbb R^\infty$ with sup norm), $E = \{e_n : n \in \mathbb N\}$ where $e_n$ is the sequence with $1$ in the $n$-th slot and $0$ elsewhere.
Proof: $E$ is bounded: $\|e_n\|_2 = 1$ for all $n$.

<1>2. $E$ is closed in $X$.
Proof: $\|e_n - e_m\|_2 = \sqrt2$ for $n \neq m$, so $E$ has no accumulation points in $X$; a set with no accumulation points is closed (any convergent sequence in $E$ is eventually constant, so its limit lies in $E$).

<1>3. $E$ is not compact.
Proof: the open cover $\{B(e_n, 1/2)\}$ (or the cover by the balls of radius $\sqrt2/2$ around each $e_n$) has no finite subcover, since any finite subcover misses all but finitely many $e_n$'s. Equivalently, $\{e_n\}$ has no convergent subsequence ($\|e_n - e_m\| = \sqrt2$ for $n \neq m$).

<1>4. Q.E.D. Proof: <1>1–<1>3 exhibit the required example.
(Alternative: $X = \mathbb R$ with the discrete metric, $E = X$: $E$ is closed and bounded — bounded in the discrete metric since $d \le 1$ — but not compact, as the cover by singletons has no finite subcover.)
:::
