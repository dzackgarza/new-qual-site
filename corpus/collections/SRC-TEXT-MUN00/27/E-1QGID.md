---
schema: qual/card@1
id: E-1QGID
kind: problem
title: Compactness, connectedness, and path connectedness of the K-topology line
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Recall that $\mathbb{R}_K$ denotes $\mathbb{R}$ in the $K$-topology.

(a) Show that $[0, 1]$ is not compact as a subspace of $\mathbb{R}_K$.

(b) Show that $\mathbb{R}_K$ is connected.
[Hint: $(-\infty, 0)$ and $(0, \infty)$ inherit their usual topologies as subspaces of $\mathbb{R}_K$.]

(c) Show that $\mathbb{R}_K$ is not path connected.
:::

::: solution
**Goal:** Analyze compactness of $[0, 1]$, connectedness of $\mathbb{R}_K$, and non-path-connectedness of $\mathbb{R}_K$.

<1>1. Part (a): $[0, 1]$ is not compact in $\mathbb{R}_K$.
    *Proof:*
    <2>1. The basis for $\mathbb{R}_K$ includes sets of the form $(a, b) \setminus K$, where $K = \{\frac{1}{n} : n \in \mathbb{Z}_+\}$.
    <2>2. Define the open cover $\mathcal{U}$ of $[0, 1]$ by:
        $$\mathcal{U} = \{(-1, 1) \setminus K\} \cup \left\{\left(\frac{1}{n+1}, \frac{1}{n-1}\right) : n \ge 2\right\} \cup \left\{\left(\frac{1}{2}, 2\right)\right\}.$$
    <2>3. $\mathcal{U}$ is an open cover: $(-1, 1) \setminus K$ contains $0$ and all points of $[0, 1] \setminus K$; each point $\frac{1}{n} \in K$ with $n \ge 2$ belongs to $(\frac{1}{n+1}, \frac{1}{n-1})$; and $1 \in (\frac{1}{2}, 2)$.
    <2>4. Any subcover must contain $(-1, 1) \setminus K$ to cover $0$.
    <2>5. Since $(-1, 1) \setminus K$ contains no point of $K$, and each interval $(\frac{1}{n+1}, \frac{1}{n-1})$ contains only the single point $\frac{1}{n} \in K$, any subcover must contain every interval $(\frac{1}{n+1}, \frac{1}{n-1})$ for all $n \ge 2$.
    <2>6. Thus no finite subcover exists, so $[0, 1]$ is not compact in $\mathbb{R}_K$.

<1>2. Part (b): $\mathbb{R}_K$ is connected.
    *Proof:*
    <2>1. The subspace topology on $(-\infty, 0)$ is the standard Euclidean topology since $(-\infty, 0) \cap K = \emptyset$, so $(-\infty, 0)$ is connected.
    <2>2. The subspace topology on $(0, \infty)$ is also the standard Euclidean topology because $K$ has no limit points in $(0, \infty)$, so $(0, \infty)$ is connected.
    <2>3. Suppose $\mathbb{R}_K = U \cup V$ is a separation of $\mathbb{R}_K$ into disjoint open sets. Without loss of generality, let $0 \in U$.
    <2>4. Since $0 \in U$ and $U$ is open, $U$ contains a basic neighborhood $(-\varepsilon, \varepsilon) \setminus K$ for some $\varepsilon > 0$.
    <2>5. Then $U \cap (-\infty, 0) \supseteq (-\varepsilon, 0) \neq \emptyset$. Since $(-\infty, 0)$ is connected, $(-\infty, 0) \subseteq U$.
    <2>6. Similarly, $U \cap (0, \infty) \supseteq ((0, \varepsilon) \setminus K) \neq \emptyset$. Since $(0, \infty)$ is connected, $(0, \infty) \subseteq U$.
    <2>7. Thus $\mathbb{R} = (-\infty, 0) \cup \{0\} \cup (0, \infty) \subseteq U$, so $V = \emptyset$.
    <2>8. Hence no separation exists, so $\mathbb{R}_K$ is connected.

<1>3. Part (c): $\mathbb{R}_K$ is not path connected.
    *Proof:*
    <2>1. Suppose there exists a continuous path $\gamma: [0, 1] \to \mathbb{R}_K$ with $\gamma(0) = 0$ and $\gamma(1) = 1$.
    <2>2. Since the topology of $\mathbb{R}_K$ is strictly finer than the standard topology on $\mathbb{R}$, $\gamma$ is also continuous as a map into the standard Euclidean space $\mathbb{R}$.
    <2>3. By the Intermediate Value Theorem, the image $\gamma([0, 1])$ is a connected subset of standard $\mathbb{R}$ containing $0$ and $1$, so $[0, 1] \subseteq \gamma([0, 1])$.
    <2>4. Since $[0, 1]$ is compact in standard $\mathbb{R}$ and $\gamma: [0, 1] \to \mathbb{R}_K$ is continuous, the image $\gamma([0, 1])$ is compact in $\mathbb{R}_K$.
    <2>5. The interval $[0, 1]$ is closed in $\mathbb{R}_K$ because $\mathbb{R}_K \setminus [0, 1] = (-\infty, 0) \cup (1, \infty)$ is open in $\mathbb{R}_K$.
    <2>6. As a closed subset of the compact space $\gamma([0, 1])$, $[0, 1]$ must be compact in $\mathbb{R}_K$.
    <2>7. This directly contradicts <1>1.
    <2>8. Thus no continuous path connects $0$ to $1$, so $\mathbb{R}_K$ is not path connected. Q.E.D.
:::
