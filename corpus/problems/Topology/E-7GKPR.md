---
schema: qual/card@1
id: E-7GKPR
kind: problem
title: Compact subsets of metric spaces are bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that if $X$ is a metric space and $A\subseteq X$ is compact then $A$ is bounded.
:::

::: solution
**Goal:** Prove that every compact subset $A$ of a metric space $(X, d)$ is bounded, meaning $\operatorname{diam}(A) = \sup_{x, y \in A} d(x, y) < \infty$.

<1>1. Trivial case: If $A = \varnothing$, then $\operatorname{diam}(A) = 0 < \infty$, so $A$ is bounded.

<1>2. Non-empty case: Assume $A \neq \varnothing$, and fix a basepoint $x_0 \in A$.
*Proof:* <2>1. For each integer $n \ge 1$, let $B(x_0, n) = \{x \in X \mid d(x, x_0) < n\}$ be the open ball of radius $n$ centered at $x_0$.
<2>2. For every $x \in A$, the distance $d(x, x_0)$ is a finite real number, so $x \in B(x_0, n)$ for any $n > d(x, x_0)$.
<2>3. Hence the collection $\{B(x_0, n) \mid n \in \mathbb{Z}_+\}$ forms an open covering of $A$: $$A \subseteq \bigcup_{n=1}^\infty B(x_0, n).$$ <2>4. Because $A$ is compact, there exists a finite subcover $\{B(x_0, n_1), \dots, B(x_0, n_k)\}$.
<2>5. Let $N = \max\{n_1, n_2, \dots, n_k\}$.
Since the concentric balls are nested, $$A \subseteq \bigcup_{j=1}^k B(x_0, n_j) = B(x_0, N).$$ <2>6. For any pair of points $x, y \in A$, both $d(x, x_0) < N$ and $d(y, x_0) < N$.
<2>7. By the triangle inequality: $$d(x, y) \le d(x, x_0) + d(x_0, y) < N + N = 2N.$$ <2>8. Therefore $\operatorname{diam}(A) = \sup_{x, y \in A} d(x, y) \le 2N < \infty$.

<1>3. Conclusion: $A$ is bounded in the metric $d$.
Q.E.D.
:::
