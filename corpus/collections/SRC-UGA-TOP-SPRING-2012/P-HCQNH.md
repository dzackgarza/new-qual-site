---
schema: qual/card@1
id: P-HCQNH
kind: problem
title: A formula for $\chi(X)$ in terms of $\chi(U)$, $\chi(V)$, and $\chi(U\cap V)$
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Mayer-Vietoris
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Suppose that $U$ and $V$ are open subsets of a space $X$, with $X = U \cup V$.
Find, with proof, a general formula relating the Euler characteristics of $X, U, V$, and $U \cap V$.

> You may assume that the homologies of $U, V, U \cap V, X$ are finite-dimensional so that their Euler characteristics are well defined.
:::

::: solution
**Goal:** Prove the inclusion-exclusion formula for the Euler characteristic $\chi(X) = \chi(U) + \chi(V) - \chi(U \cap V)$ using the Mayer–Vietoris sequence.

<1>1. Definition of the Euler characteristic:
    *Proof:*
    <2>1. For a topological space $Y$ whose homology groups with rational coefficients $H_n(Y; \mathbb{Q})$ are finite-dimensional and vanish for sufficiently large $n$, the Euler characteristic is defined by
    $$\chi(Y) = \sum_{n=0}^\infty (-1)^n \dim_\mathbb{Q} H_n(Y; \mathbb{Q}).$$

<1>2. The Mayer–Vietoris long exact sequence:
    *Proof:*
    <2>1. Since $X = U \cup V$ is covered by the open sets $U$ and $V$, the Mayer–Vietoris theorem yields a long exact sequence in singular homology with rational coefficients:
    $$\cdots \xrightarrow{\partial_{n+1}} H_n(U \cap V; \mathbb{Q}) \xrightarrow{i_n} H_n(U; \mathbb{Q}) \oplus H_n(V; \mathbb{Q}) \xrightarrow{j_n} H_n(X; \mathbb{Q}) \xrightarrow{\partial_n} H_{n-1}(U \cap V; \mathbb{Q}) \xrightarrow{i_{n-1}} \cdots \to 0.$$
    <2>2. The map $i_n$ is given by $i_n(x) = (j_{U*}(x), -j_{V*}(x))$, and $j_n$ is given by $j_n(u, v) = k_{U*}(u) + k_{V*}(v)$.
    <2>3. By the dimension formula for vector space direct sums:
    $$\dim_\mathbb{Q}(H_n(U; \mathbb{Q}) \oplus H_n(V; \mathbb{Q})) = \dim_\mathbb{Q} H_n(U; \mathbb{Q}) + \dim_\mathbb{Q} H_n(V; \mathbb{Q}).$$

<1>3. Alternating sum of dimensions in a long exact sequence:
    *Proof:*
    <2>1. In any exact sequence of finite-dimensional vector spaces $0 \to V_m \to V_{m-1} \to \cdots \to V_1 \to V_0 \to 0$, the alternating sum of dimensions vanishes: $\sum_{k=0}^m (-1)^k \dim V_k = 0$.
    <2>2. Grouping each degree $n$ into three terms:
    $$A_{3n+2} = H_n(U \cap V; \mathbb{Q}), \qquad A_{3n+1} = H_n(U; \mathbb{Q}) \oplus H_n(V; \mathbb{Q}), \qquad A_{3n} = H_n(X; \mathbb{Q}).$$
    <2>3. The alternating sum over the entire sequence is:
    $$\sum_{n=0}^\infty (-1)^n \left[ \dim_\mathbb{Q} H_n(X; \mathbb{Q}) - \dim_\mathbb{Q}(H_n(U; \mathbb{Q}) \oplus H_n(V; \mathbb{Q})) + \dim_\mathbb{Q} H_n(U \cap V; \mathbb{Q}) \right] = 0.$$
    <2>4. Distributing the sum:
    $$\sum_{n=0}^\infty (-1)^n \dim H_n(X) - \left(\sum_{n=0}^\infty (-1)^n \dim H_n(U) + \sum_{n=0}^\infty (-1)^n \dim H_n(V)\right) + \sum_{n=0}^\infty (-1)^n \dim H_n(U \cap V) = 0.$$
    <2>5. Substituting the definitions of the Euler characteristics:
    $$\chi(X) - (\chi(U) + \chi(V)) + \chi(U \cap V) = 0.$$

<1>4. Conclusion:
    *Proof:*
    Rearranging gives the general formula:
    $$\chi(X) = \chi(U) + \chi(V) - \chi(U \cap V).$$
:::
