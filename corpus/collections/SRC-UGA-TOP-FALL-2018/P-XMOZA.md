---
schema: qual/card@1
id: P-XMOZA
kind: problem
title: Connectedness of $\{(x,y)\in\RR^2:x>0,\,y\geq 0,\,y/x\in\QQ\}$
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Subspace Topology
  - Euclidean Spaces
relations: []
review: draft
---

::: problem
Let
$$
X = \left\{(x, y) \in \mathbb{R}^2 : x > 0, \, y \ge 0, \text{ and } \frac{y}{x} \in \mathbb{Q}\right\}
$$
equipped with the subspace topology inherited from the standard Euclidean topology on $\mathbb{R}^2$. Prove or disprove that $X$ is connected.
:::

::: solution
**Goal:** Disprove that $X$ is connected by constructing an explicit separation of $X$ into two disjoint, non-empty open subsets.

<1>1. Strategy and definition of the separating open half-spaces:
    *Proof:*
    <2>1. Choose a positive irrational number, such as $\alpha = \sqrt{2} \in \mathbb{R} \setminus \mathbb{Q}$.
    <2>2. Define two open subsets of the plane $\mathbb{R}^2$:
    $$U = \{(x, y) \in \mathbb{R}^2 : y < \sqrt{2} x\}, \qquad V = \{(x, y) \in \mathbb{R}^2 : y > \sqrt{2} x\}.$$
    <2>3. The function $g(x, y) = y - \sqrt{2} x$ is continuous from $\mathbb{R}^2$ to $\mathbb{R}$.
    <2>4. The sets $U = g^{-1}((-\infty, 0))$ and $V = g^{-1}((0, \infty))$ are open in $\mathbb{R}^2$.
    <2>5. Define $A = X \cap U$ and $B = X \cap V$. By definition of the subspace topology, $A$ and $B$ are open in $X$.

<1>2. $A$ and $B$ are disjoint and cover $X$:
    *Proof:*
    <2>1. Disjointness: $U \cap V = \emptyset$, so $A \cap B = (X \cap U) \cap (X \cap V) = \emptyset$.
    <2>2. Union: Let $(x, y) \in X$. Since $x > 0$ and $y/x \in \mathbb{Q}$, while $\sqrt{2} \notin \mathbb{Q}$, we have $\frac{y}{x} \ne \sqrt{2}$.
    <2>3. Since $x > 0$, $\frac{y}{x} \ne \sqrt{2} \iff y \ne \sqrt{2} x$.
    <2>4. Therefore, either $y < \sqrt{2} x$ (so $(x, y) \in U$) or $y > \sqrt{2} x$ (so $(x, y) \in V$).
    <2>5. Thus every point of $X$ belongs to $A \cup B$, so $X = A \cup B$.

<1>3. $A$ and $B$ are both non-empty:
    *Proof:*
    <2>1. For the point $(1, 1) \in \mathbb{R}^2$: $x = 1 > 0$, $y = 1 \ge 0$, and $y/x = 1 \in \mathbb{Q}$, so $(1, 1) \in X$.
    <2>2. Since $1 < \sqrt{2} \cdot 1$, $(1, 1) \in U$, so $(1, 1) \in A$, proving $A \ne \emptyset$.
    <2>3. For the point $(1, 2) \in \mathbb{R}^2$: $x = 1 > 0$, $y = 2 \ge 0$, and $y/x = 2 \in \mathbb{Q}$, so $(1, 2) \in X$.
    <2>4. Since $2 > \sqrt{2} \cdot 1$, $(1, 2) \in V$, so $(1, 2) \in B$, proving $B \ne \emptyset$.

<1>4. Conclusion:
    *Proof:*
    The subsets $A$ and $B$ form a non-trivial separation of $X$ into disjoint, non-empty open sets in the subspace topology. Therefore $X$ is not connected (it is disconnected).
:::
