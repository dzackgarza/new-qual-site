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

::: {.problem}
(a) Let $(X, d)$ be a metric space, $\{x_n\}$ a sequence in $X$, and $x \in X$.
Suppose that every subsequence of $\{x_n\}$ has a subsequence which converges to $x$.
Show that $\{x_n\}$ converges to $x$.

(b) Let $\{f_n\}$ be a sequence of locally bounded analytic functions in an open region $G \subset \mathbb{C}$.
Let $A := \{z \in G : \lim_{n \to \infty} f_n(z) = 0\}$ and assume that $A$ has a limit point in $G$.
Show that $\{f_n\}$ converges uniformly on compact subsets of $G$ to $f \equiv 0$.
:::

::: {.solution}
**Goal:** Prove the metric subsequence characterization of convergence in (a), and use Montel's Theorem and the Identity Theorem to prove compact convergence to 0 in (b).

::: pf

::: {.pf-step #s1}

Part (a): Subsequence criterion for metric convergence.
    *Proof:*

::: pf-proof

::: pf-step

Suppose for contradiction that the sequence $(x_n)_{n=1}^\infty$ does not converge to $x$.

:::

::: pf-step

By the negation of the definition of convergence, there exists $\varepsilon_0 > 0$ such that for every integer $N \ge 1$, there exists some $n \ge N$ satisfying $d(x_n, x) \ge \varepsilon_0$.

:::

::: pf-step

Inductively choosing indices $n_1 < n_2 < n_3 < \dots$ constructs a subsequence $(x_{n_k})_{k=1}^\infty$ such that
    $$d(x_{n_k}, x) \ge \varepsilon_0 \quad \text{for all } k \ge 1.$$

:::

::: pf-step

By hypothesis, the subsequence $(x_{n_k})$ must have a further subsequence $(x_{n_{k_j}})_{j=1}^\infty$ that converges to $x$.

:::

::: pf-step

Convergence implies $\lim_{j \to \infty} d(x_{n_{k_j}}, x) = 0$.

:::

::: pf-step

But $d(x_{n_{k_j}}, x) \ge \varepsilon_0 > 0$ for all $j \ge 1$, which gives the contradiction $0 \ge \varepsilon_0 > 0$.

:::

::: pf-step

Therefore $(x_n)$ converges to $x$.

:::

:::

:::

::: {.pf-step #s2}

Part (b): Normality and sub-subsequence limit identification via the Identity Theorem.
    *Proof:*

::: pf-proof

::: pf-step

Let $H(G)$ denote the space of holomorphic functions on the region $G$, equipped with the topology of uniform convergence on compact subsets (which is metrizable as a Fréchet space).

:::

::: pf-step

Since $\{f_n\}$ is locally bounded on the open region $G$, Montel's Theorem asserts that $\{f_n\}$ is a normal family in $H(G)$.

:::

::: pf-step

Let $(f_{n_k})_{k=1}^\infty$ be an arbitrary subsequence of $(f_n)$.

:::

::: pf-step

By normality, there exists a further sub-subsequence $(f_{n_{k_j}})_{j=1}^\infty$ that converges uniformly on every compact subset $K \subset G$ to a holomorphic function $g \in H(G)$.

:::

::: pf-step

For every point $z \in A$, $\lim_{n \to \infty} f_n(z) = 0$ by definition of $A$. Pointwise convergence of the sub-subsequence implies
    $$g(z) = \lim_{j \to \infty} f_{n_{k_j}}(z) = 0 \quad \text{for all } z \in A.$$

:::

::: pf-step

Thus $A \subseteq \{z \in G : g(z) = 0\}$.

:::

::: pf-step

Since $A$ has an accumulation point in the connected open region $G$, the Identity Theorem for holomorphic functions implies $g \equiv 0$ on all of $G$.

:::

:::

:::

::: pf-step

Part (b): Conclusion of uniform convergence on compact sets.
    *Proof:*

::: pf-proof

::: pf-step

By step [](#s2){.pf-ref}, every subsequence of $\{f_n\}$ possesses a further subsequence that converges in $H(G)$ to the zero function $f \equiv 0$.

:::

::: pf-step

Applying the result of part (a) (step [](#s1){.pf-ref}) to the metric space $H(G)$ and the target point $f \equiv 0$, the full sequence $\{f_n\}$ converges to $f \equiv 0$ in $H(G)$.

:::

::: pf-step

Therefore $\{f_n\}$ converges to $0$ uniformly on all compact subsets of $G$.

:::

:::

:::

:::

:::
