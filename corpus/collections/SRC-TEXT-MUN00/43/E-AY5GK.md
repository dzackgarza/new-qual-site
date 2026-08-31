---
schema: qual/card@1
id: E-AY5GK
kind: exercise
title: Topologically complete spaces
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

A space $X$ is said to be topologically complete if there exists a metric for the topology of $X$ relative to which $X$ is complete.

(a) Show that a closed subspace of a topologically complete space is topologically complete.

(b) Show that a countable product of topologically complete spaces is topologically complete (in the product topology).

(c) Show that an open subspace of a topologically complete space is topologically complete.
[Hint: If $U \subset X$ and $X$ is complete under the metric $d$, define $\phi: U \to \mathbb{R}$ by the equation

$$
\phi(x) = 1/d(x, X - U).
$$

Imbed $U$ in $X \times \mathbb{R}$ by setting $f(x) = x \times \phi(x)$.]

(d) Show that if $A$ is a $G_\delta$ set in a topologically complete space, then $A$ is topologically complete.
[Hint: Let $A$ be the intersection of the open sets $U_n$, for $n \in \mathbb{Z}_+$. Consider the diagonal imbedding $f(a) = (a, a, \ldots)$ of $A$ into $\prod U_n$.] Conclude that the irrationals are topologically complete.
:::

::: solution
**Goal:** Prove that topological completeness is preserved under closed subspaces, countable products, open subspaces, and $G_\delta$ subsets, and conclude that $\mathbb{R} \setminus \mathbb{Q}$ is topologically complete.

<1>1. Part (a): Closed subspaces of topologically complete spaces are topologically complete.
    *Proof:*
    <2>1. Let $X$ be topologically complete, so there is a metric $d$ on $X$ compatible with its topology such that $(X, d)$ is a complete metric space.
    <2>2. Let $A \subseteq X$ be a closed subspace, equipped with the subspace metric $d_A = d|_{A \times A}$.
    <2>3. Let $(x_n)_{n=1}^\infty$ be a Cauchy sequence in $(A, d_A)$.
    <2>4. Since $d_A(x_n, x_m) = d(x_n, x_m)$, $(x_n)$ is a Cauchy sequence in the complete space $(X, d)$.
    <2>5. Therefore $(x_n)$ converges to some limit point $x \in X$.
    <2>6. Since $A$ is closed in $X$, every limit of points in $A$ belongs to $A$, so $x \in A$.
    <2>7. Thus every Cauchy sequence in $(A, d_A)$ converges in $A$, so $(A, d_A)$ is complete.

<1>2. Part (b): Countable products of topologically complete spaces are topologically complete.
    *Proof:*
    <2>1. Let $\{X_n\}_{n=1}^\infty$ be a countable family of topologically complete spaces, with each $(X_n, d_n)$ being a complete metric space.
    <2>2. Define the bounded metrics $\bar{d}_n(x, y) = \min\{1, d_n(x, y)\}$ on each $X_n$.
    <2>3. On the product space $X = \prod_{n=1}^\infty X_n$, define the metric
    $$D(x, y) = \sum_{n=1}^\infty \frac{1}{2^n} \bar{d}_n(x_n, y_n).$$
    <2>4. The metric $D$ induces the product topology on $X$.
    <2>5. Let $(x^{(k)})_{k=1}^\infty$ be a Cauchy sequence in $(X, D)$.
    <2>6. For each fixed coordinate $n$, $\bar{d}_n(x_n^{(k)}, x_n^{(m)}) \le 2^n D(x^{(k)}, x^{(m)}) \to 0$ as $k, m \to \infty$, so the coordinate sequence $(x_n^{(k)})_{k=1}^\infty$ is Cauchy in $(X_n, d_n)$.
    <2>7. By completeness of each $(X_n, d_n)$, $x_n^{(k)} \to y_n \in X_n$ as $k \to \infty$.
    <2>8. Setting $y = (y_1, y_2, \dots) \in X$, $x^{(k)} \to y$ in the product topology, so $(X, D)$ is complete.

<1>3. Part (c): Open subspaces of topologically complete spaces are topologically complete.
    *Proof:*
    <2>1. Let $(X, d)$ be a complete metric space and let $U \subseteq X$ be an open subset.
    <2>2. If $U = X$, $U$ is already complete. If $U \subsetneq X$, the closed set $F = X \setminus U$ is non-empty.
    <2>3. Define $\phi: U \to \mathbb{R}$ by $\phi(x) = \frac{1}{d(x, F)}$. Since the distance function $x \mapsto d(x, F)$ is continuous and non-zero on $U$, $\phi$ is continuous.
    <2>4. Define the embedding $f: U \to X \times \mathbb{R}$ by $f(x) = (x, \phi(x))$. The map $f$ is a homeomorphism of $U$ onto its image $f(U) \subset X \times \mathbb{R}$ (with inverse being the first projection $\pi_1$).
    <2>5. By parts (a) and (b), the product space $X \times \mathbb{R}$ is complete under the metric $D((x_1, t_1), (x_2, t_2)) = d(x_1, x_2) + |t_1 - t_2|$.
    <2>6. We claim that the graph $f(U) = \{(x, \phi(x)) : x \in U\}$ is a closed subset of $X \times \mathbb{R}$:
    Let $(x_k, \phi(x_k)) \to (x, t)$ in $X \times \mathbb{R}$ as $k \to \infty$. Then $x_k \to x$ in $X$ and $\phi(x_k) \to t$ in $\mathbb{R}$.
    If $x \in F$, then $d(x_k, F) \to d(x, F) = 0$, so $\phi(x_k) = \frac{1}{d(x_k, F)} \to \infty$, which contradicts $\phi(x_k) \to t \in \mathbb{R}$.
    Thus $x \in U$, and by continuity of $\phi$, $t = \lim \phi(x_k) = \phi(x)$.
    <2>7. Hence $(x, t) = (x, \phi(x)) \in f(U)$, proving that $f(U)$ is closed in $X \times \mathbb{R}$.
    <2>8. By part (a), $f(U)$ is complete, so $U \cong f(U)$ is topologically complete.

<1>4. Part (d): $G_\delta$ subsets are topologically complete.
    *Proof:*
    <2>1. Let $A \subseteq X$ be a $G_\delta$ subset in a topologically complete space $X$, so $A = \bigcap_{n=1}^\infty U_n$ for open sets $U_n \subseteq X$.
    <2>2. By part (c), each open set $U_n$ is topologically complete.
    <2>3. By part (b), the countable product $Y = \prod_{n=1}^\infty U_n$ is topologically complete.
    <2>4. Define the diagonal map $\Delta: A \to Y$ by $\Delta(a) = (a, a, a, \dots)$.
    <2>5. The map $\Delta$ is a homeomorphism of $A$ onto its image $\Delta(A) \subset Y$.
    <2>6. The image is $\Delta(A) = \left\{(u_1, u_2, \dots) \in \prod_{n=1}^\infty U_n : u_1 = u_2 = u_3 = \cdots \right\} = \bigcap_{n=1}^\infty \{(u_k) \in Y : u_n = u_{n+1}\}$.
    <2>7. Since each coordinate equality condition $\{ (u_k) \in Y : u_n = u_{n+1} \}$ is closed in the product topology (as $X$ is Hausdorff), $\Delta(A)$ is an intersection of closed sets, hence closed in $Y$.
    <2>8. By part (a), the closed subspace $\Delta(A) \subseteq Y$ is topologically complete, so $A \cong \Delta(A)$ is topologically complete.

<1>5. Application to the irrational numbers $\mathbb{R} \setminus \mathbb{Q}$:
    *Proof:*
    <2>1. The real line $\mathbb{R}$ with its standard metric is complete, hence topologically complete.
    <2>2. The rationals $\mathbb{Q} = \{q_1, q_2, q_3, \dots\}$ are countable, so $\mathbb{Q} = \bigcup_{n=1}^\infty \{q_n\}$ is an $F_\sigma$ set.
    <2>3. The irrational numbers are the complement $\mathbb{R} \setminus \mathbb{Q} = \bigcap_{n=1}^\infty (\mathbb{R} \setminus \{q_n\})$.
    <2>4. Since each $\mathbb{R} \setminus \{q_n\}$ is open in $\mathbb{R}$, $\mathbb{R} \setminus \mathbb{Q}$ is a $G_\delta$ set in $\mathbb{R}$.
    <2>5. By <1>4, the irrational numbers $\mathbb{R} \setminus \mathbb{Q}$ are topologically complete.
:::
