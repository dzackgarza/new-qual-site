---
schema: qual/card@1
id: E-SA3HI
kind: exercise
title: "- Show that if $K$ is compact and $F$ is closed with $K, F$ disjoint t\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - compactness
  - metric-spaces
relations: []
review: draft
solved: true
---

::: exercise
- Show that if $K$ is compact and $F$ is closed with $K, F$ disjoint then $\dist(K, F) > 0$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The function $x \mapsto \dist(x, F)$ is continuous (indeed $1$-Lipschitz).
Proof: $|\dist(x, F) - \dist(y, F)| \le |x - y|$ by the triangle inequality, since any point of $F$ within $\dist(x,F)$ of $x$ is within $\dist(x,F) + |x-y|$ of $y$ and vice versa.

<1>2. $\dist(\cdot, F)$ attains its minimum on $K$: there is $k_0 \in K$ with $\dist(k_0, F) = \dist(K, F)$.
Proof: a continuous function on a compact set attains its extrema — take a minimizing sequence $(k_m) \subseteq K$ with $\dist(k_m, F) \to \dist(K, F)$; by compactness a subsequence converges to $k_0 \in K$, and continuity of $\dist(\cdot, F)$ gives $\dist(k_0, F) = \dist(K, F)$.

<1>3. $\dist(K, F) > 0$.
Proof: if $\dist(k_0, F) = 0$, then $k_0$ is a limit point of $F$; since $F$ is closed, $k_0 \in F$, contradicting $K \cap F = \emptyset$.

<1>4. Q.E.D. Proof: <1>2 and <1>3.

<1>5. Remark: the hypothesis that $K$ is compact cannot be weakened to closed.
In $\RR$, take $K = \NN$ and $F = \{n + 2^{-n} : n \in \NN\}$: both are closed and disjoint, yet $\dist(K, F) = \inf_n 2^{-n} = 0$.
:::
