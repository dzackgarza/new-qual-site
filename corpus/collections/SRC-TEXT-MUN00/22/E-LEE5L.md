---
schema: qual/card@1
id: E-LEE5L
kind: exercise
title: A quotient map that is neither open nor closed
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $\pi_1: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ be projection on the first coordinate.
Let $A$ be the subspace of $\mathbb{R} \times \mathbb{R}$ consisting of all points $x \times y$ for which either $x \geq 0$ or $y = 0$ (or both); let $q: A \to \mathbb{R}$ be obtained by restricting $\pi_1$.
Show that $q$ is a quotient map that is neither open nor closed.
:::

::: {.solution}
<1>1. $q: A \to \mathbb{R}$ is continuous and surjective.
<2>1. $q = \pi_1|_A$ is the restriction of the continuous projection $\pi_1: \mathbb{R}^2 \to \mathbb{R}$, hence continuous.
Proof: restriction of a continuous map is continuous.
<2>2. For every $x \in \mathbb{R}$, $(x, 0) \in A$ (since $y = 0$) and $q(x, 0) = x$.
Proof: definition of $A$ and $q$.
<2>3. Thus $q$ is surjective.
Proof: <2>2.

<1>2. $q$ is a quotient map: $U \subseteq \mathbb{R}$ is open in $\mathbb{R}$ if and only if $q^{-1}(U)$ is open in $A$.
<2>1. If $U \subseteq \mathbb{R}$ is open, then $q^{-1}(U)$ is open in $A$ by continuity of $q$.
Proof: <1>1. <2>2. Conversely, suppose $q^{-1}(U)$ is open in $A$.
Proof: hypothesis.
<2>3. For every $x_0 \in U$, the point $(x_0, 0) \in q^{-1}(U) \subseteq A$.
Proof: $q(x_0, 0) = x_0 \in U$.
<2>4. Since $q^{-1}(U)$ is open in $A$, there exists an open box $B = (a, b) \times (-\varepsilon, \varepsilon) \subseteq \mathbb{R}^2$ containing $(x_0, 0)$ such that $B \cap A \subseteq q^{-1}(U)$.
Proof: definition of the subspace topology on $A$.
<2>5. For any $t \in (a, b)$, the point $(t, 0) \in B \cap A \subseteq q^{-1}(U)$, so $q(t, 0) = t \in U$.
Proof: $(t, 0) \in A$ for all $t \in \mathbb{R}$.
<2>6. Thus $(a, b) \subseteq U$, so $x_0 \in (a, b) \subseteq U$.
Proof: <2>5 and $x_0 \in (a, b)$.
<2>7. Since every point $x_0 \in U$ has an open interval neighborhood in $U$, $U$ is open in $\mathbb{R}$.
Proof: <2>6. <2>8. Therefore $q$ is a quotient map.
Proof: <2>1 and <2>7.

<1>3. $q$ is not an open map.
<2>1. The set $U = [0, \infty) \times (0, \infty)$ is open in $A$, because $U = (\mathbb{R} \times (0, \infty)) \cap A$.
Proof: $\mathbb{R} \times (0, \infty)$ is open in $\mathbb{R}^2$.
<2>2. The image $q(U) = [0, \infty)$.
Proof: projection of $[0, \infty) \times (0, \infty)$ on the first factor.
<2>3. $[0, \infty)$ is not open in $\mathbb{R}$ (it contains $0$ but no open ball $(-\delta, \delta) \subseteq [0, \infty)$). Proof: negative reals do not belong to $[0, \infty)$.
<2>4. Hence $q$ is not an open map.
Proof: <2>1, <2>2, and <2>3.

<1>4. $q$ is not a closed map.
<2>1. Consider the set $C = \{(x, y) \in \mathbb{R}^2 : x > 0, y > 0, xy = 1\}$.
Proof: definition of the hyperbola branch.
<2>2. $C \subset [0, \infty) \times [0, \infty) \subseteq A$.
Proof: $x > 0 \implies (x, y) \in A$.
<2>3. $C$ is closed in $\mathbb{R}^2$ as the intersection of the closed half-plane $[0, \infty)^2$ and the level set of the continuous function $(x, y) \mapsto xy$.
Proof: closed subset of $\mathbb{R}^2$.
<2>4. Hence $C = C \cap A$ is closed in $A$.
Proof: subspace topology.
<2>5. The image $q(C) = (0, \infty)$.
Proof: for every $x > 0$, $(x, 1/x) \in C$, so $q(x, 1/x) = x \in (0, \infty)$.
<2>6. $(0, \infty)$ is not closed in $\mathbb{R}$ (it contains the sequence $1/n \to 0$ whose limit $0 \notin (0, \infty)$). Proof: $0$ is a limit point of $(0, \infty)$ not contained in $(0, \infty)$.
<2>7. Hence $q$ is not a closed map.
Proof: <2>4, <2>5, and <2>6.

<1>5. Conclusion: $q$ is a quotient map that is neither open nor closed.
Q.E.D. Proof: <1>2, <1>3, and <1>4.
:::
