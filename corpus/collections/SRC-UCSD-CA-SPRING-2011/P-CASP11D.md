---
schema: qual/card@1
id: P-CASP11D
kind: problem
title: "Subsequence convergence characterization and identity theorem for locally bounded analytic functions"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
(a) Let $(X, d)$ be a metric space, $\{x_n\}$ a sequence in $X$, and $x \in X$.
Suppose that every subsequence of $\{x_n\}$ has a subsequence which converges to $x$.
Show that $\{x_n\}$ converges to $x$.

(b) Let $\{f_n\}$ be a sequence of locally bounded analytic functions in an open region $G \subset \mathbb{C}$.
Let $A := \{z \in G : \lim_{n \to \infty} f_n(z) = 0\}$ and assume that $A$ has a limit point in $G$.
Show that $\{f_n\}$ converges uniformly on compact subsets of $G$ to $f \equiv 0$.
:::

::: solution
**Goal:** Prove the metric subsequence characterization of convergence in (a), and use Montel's Theorem and the Identity Theorem to prove compact convergence to 0 in (b).

<1>1. Part (a): Subsequence criterion for metric convergence.
    *Proof:*
    <2>1. Suppose for contradiction that the sequence $(x_n)_{n=1}^\infty$ does not converge to $x$.
    <2>2. By the negation of the definition of convergence, there exists $\varepsilon_0 > 0$ such that for every integer $N \ge 1$, there exists some $n \ge N$ satisfying $d(x_n, x) \ge \varepsilon_0$.
    <2>3. Inductively choosing indices $n_1 < n_2 < n_3 < \dots$ constructs a subsequence $(x_{n_k})_{k=1}^\infty$ such that
    $$d(x_{n_k}, x) \ge \varepsilon_0 \quad \text{for all } k \ge 1.$$
    <2>4. By hypothesis, the subsequence $(x_{n_k})$ must have a further subsequence $(x_{n_{k_j}})_{j=1}^\infty$ that converges to $x$.
    <2>5. Convergence implies $\lim_{j \to \infty} d(x_{n_{k_j}}, x) = 0$.
    <2>6. But $d(x_{n_{k_j}}, x) \ge \varepsilon_0 > 0$ for all $j \ge 1$, which gives the contradiction $0 \ge \varepsilon_0 > 0$.
    <2>7. Therefore $(x_n)$ converges to $x$.

<1>2. Part (b): Normality and sub-subsequence limit identification via the Identity Theorem.
    *Proof:*
    <2>1. Let $H(G)$ denote the space of holomorphic functions on the region $G$, equipped with the topology of uniform convergence on compact subsets (which is metrizable as a Fréchet space).
    <2>2. Since $\{f_n\}$ is locally bounded on the open region $G$, Montel's Theorem asserts that $\{f_n\}$ is a normal family in $H(G)$.
    <2>3. Let $(f_{n_k})_{k=1}^\infty$ be an arbitrary subsequence of $(f_n)$.
    <2>4. By normality, there exists a further sub-subsequence $(f_{n_{k_j}})_{j=1}^\infty$ that converges uniformly on every compact subset $K \subset G$ to a holomorphic function $g \in H(G)$.
    <2>5. For every point $z \in A$, $\lim_{n \to \infty} f_n(z) = 0$ by definition of $A$. Pointwise convergence of the sub-subsequence implies
    $$g(z) = \lim_{j \to \infty} f_{n_{k_j}}(z) = 0 \quad \text{for all } z \in A.$$
    <2>6. Thus $A \subseteq \{z \in G : g(z) = 0\}$.
    <2>7. Since $A$ has an accumulation point in the connected open region $G$, the Identity Theorem for holomorphic functions implies $g \equiv 0$ on all of $G$.

<1>3. Part (b): Conclusion of uniform convergence on compact sets.
    *Proof:*
    <2>1. By <1>2, every subsequence of $\{f_n\}$ possesses a further subsequence that converges in $H(G)$ to the zero function $f \equiv 0$.
    <2>2. Applying the result of part (a) (<1>1) to the metric space $H(G)$ and the target point $f \equiv 0$, the full sequence $\{f_n\}$ converges to $f \equiv 0$ in $H(G)$.
    <2>3. Therefore $\{f_n\}$ converges to $0$ uniformly on all compact subsets of $G$.
:::
