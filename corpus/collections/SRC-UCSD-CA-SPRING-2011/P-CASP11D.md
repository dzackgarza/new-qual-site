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
**Goal:** Prove (a) via subsequence contradiction and (b) via normality plus identity theorem.

<1> Part (a): assume $x_n\nrightarrow x$.
    Then there is $\varepsilon>0$ and a subsequence $x_{n_k}$ with $d(x_{n_k},x)\ge\varepsilon$ for all $k$.
    Any further subsequence has all terms outside $B(x,\varepsilon)$, so none can converge to $x$.
    This contradicts the hypothesis. Hence $x_n\to x$.

<1> Part (b): local boundedness gives normality of $\{f_n\}$ on $G$ (Montel), so every subsequence has a subsequence converging uniformly on compacta to a holomorphic function.
    Let $f_{n_k}\to f$ uniformly on compact subsets.

<1> For any $z\in A$, by definition $f_n(z)\to 0$ and by convergence of the subsequence we also have $f_{n_k}(z)\to f(z)$.
    Therefore $f(z)=0$ for all $z\in A$.
    The set $A$ has a limit point in $G$, so by the identity theorem $f\equiv 0$ on $G$.

<1> Every subsequence of $\{f_n\}$ has a further subsequence converging to $0$ on compact sets.
    A sequence in a metric space is convergent iff every subsequence has such a convergent further subsequence with unique limit.
    Therefore $f_n\to 0$ uniformly on compact subsets of $G$.

Authored by **Codex 5.3 Spark Extra High**.
:::
