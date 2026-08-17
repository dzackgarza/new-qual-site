---
schema: qual/card@1
id: E-FV5FI
kind: exercise
title: Compact subsets of metric spaces are bounded
classification:
  areas:
  - topology
  topics:
  - compactness
  - metric-spaces
relations: []
review: draft
solved: true
---

::: exercise
Show that if $X$ is a metric space and $A\subseteq X$ is compact then $A$ is bounded.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that if $X$ is a metric space and $A \subseteq X$ is compact, then $A$ is bounded.

<1>1. Fix a point $p \in X$; the open balls $\theset{B(p, n)}_{n \in \NN}$ form an open cover of $X$.
Proof: Every point of $X$ is at finite distance from $p$, so it lies in some $B(p, n)$; balls are open in a metric space.

<1>2. The restriction to $A$ is an open cover of $A$, so it has a finite subcover $B(p, n_1), \ldots, B(p, n_k)$.
Proof: $A$ is compact.

<1>3. Let $N := \max\theset{n_1, \ldots, n_k}$; then $A \subseteq B(p, N)$.
Proof: Each $a \in A$ lies in some $B(p, n_j) \subseteq B(p, N)$ since $n_j \leq N$.

<1>4. $A$ is bounded.
Proof: $A$ is contained in a ball of finite radius $N$ centered at $p$, which is the definition of boundedness in a metric space.

<1>5. Q.E.D. Proof: <1>2--<1>4 establish the claim.
:::
