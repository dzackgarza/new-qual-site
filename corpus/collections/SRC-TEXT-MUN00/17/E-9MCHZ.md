---
schema: qual/card@1
id: E-9MCHZ
kind: problem
title: Closures and separation under five topologies on the line
classification:
  areas:
  - topology
  topics:
  - Closure
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the five topologies on $\mathbb{R}$ given in Exercise 7 of §13.

(a) Determine the closure of the set $K = \ts{1/n \mid n \in \mathbb{Z}_+}$ under each of these topologies.

(b) Which of these topologies satisfy the Hausdorff axiom?
the $T_1$ axiom?
:::

::: solution
**Goal:** Determine the closure of $K = \{1/n \mid n \in \mathbb{Z}_+\}$ and analyze the $T_1$ and Hausdorff axioms for the five topologies on $\mathbb{R}$:
1. $\mathcal{T}_1$: Standard Euclidean topology (basis $(a, b)$).
2. $\mathcal{T}_2$: $K$-topology $\mathbb{R}_K$ (basis $(a, b)$ and $(a, b) \setminus K$).
3. $\mathcal{T}_3$: Finite complement (cofinite) topology.
4. $\mathcal{T}_4$: Upper limit topology (basis $(a, b]$).
5. $\mathcal{T}_5$: Lower ray topology (basis $(-\infty, a)$).

<1>1. Part (a): Closure of $K = \{1/n \mid n \in \mathbb{Z}_+\}$:
    *Proof:*
    <2>1. **Under $\mathcal{T}_1$ (Standard):**
        In the Euclidean metric, $1/n \to 0$, so $0$ is the unique limit point of $K$ not in $K$. Thus $\overline{K} = K \cup \{0\}$.
    <2>2. **Under $\mathcal{T}_2$ ($\mathbb{R}_K$):**
        The set $(-1, 1) \setminus K$ is an open neighborhood of $0$ disjoint from $K$, so $0 \notin \overline{K}$. For any other $x \notin K$, standard Euclidean neighborhoods disjoint from $K$ isolate $x$. Thus $K$ is closed in $\mathbb{R}_K$, so $\overline{K} = K$.
    <2>3. **Under $\mathcal{T}_3$ (Cofinite):**
        The only closed sets are finite sets and $\mathbb{R}$. Since $K$ is infinite, the smallest closed set containing $K$ is $\mathbb{R}$. Thus $\overline{K} = \mathbb{R}$.
    <2>4. **Under $\mathcal{T}_4$ (Upper limit):**
        For the point $0$, the basic open set $(-1, 0]$ contains $0$ and contains no points of $K$, so $0 \notin \overline{K}$. For any $x \in (1/(n+1), 1/n)$, the interval $(1/(n+1), x]$ contains $x$ and misses $K$. Thus $K$ is closed in $\mathcal{T}_4$, so $\overline{K} = K$.
    <2>5. **Under $\mathcal{T}_5$ (Lower rays):**
        The closed sets of $\mathcal{T}_5$ are $\varnothing, \mathbb{R}$, and rays of the form $[a, \infty)$ for $a \in \mathbb{R}$. The smallest ray $[a, \infty)$ containing $K$ must have $a \le 1/n$ for all $n \ge 1$, which forces $a \le 0$. The smallest such set is $[0, \infty)$. Thus $\overline{K} = [0, \infty)$.

<1>2. Part (b): Verification of $T_1$ and Hausdorff axioms:
    *Proof:*
    <2>1. **$\mathcal{T}_1$ (Standard):** Satisfies $T_1$ and Hausdorff (standard metric space).
    <2>2. **$\mathcal{T}_2$ ($\mathbb{R}_K$):** Finer than $\mathcal{T}_1$, hence satisfies $T_1$ and Hausdorff.
    <2>3. **$\mathcal{T}_3$ (Cofinite):**
        - **$T_1$:** Satisfied, because every singleton $\{x\}$ is finite, hence closed.
        - **Hausdorff:** Not satisfied, because any two non-empty open sets have finite complements, so their intersection is non-empty on the infinite set $\mathbb{R}$.
    <2>4. **$\mathcal{T}_4$ (Upper limit):** Finer than $\mathcal{T}_1$, hence satisfies $T_1$ and Hausdorff.
    <2>5. **$\mathcal{T}_5$ (Lower rays):**
        - **$T_1$:** Not satisfied, because the closure of $\{x\}$ is $[x, \infty) \neq \{x\}$.
        - **Hausdorff:** Not satisfied (since Hausdorff implies $T_1$).

<1>3. Conclusion / Summary Table:
    - **$\mathcal{T}_1$:** $\overline{K} = K \cup \{0\}$; $T_1$: Yes; Hausdorff: Yes.
    - **$\mathcal{T}_2$:** $\overline{K} = K$; $T_1$: Yes; Hausdorff: Yes.
    - **$\mathcal{T}_3$:** $\overline{K} = \mathbb{R}$; $T_1$: Yes; Hausdorff: No.
    - **$\mathcal{T}_4$:** $\overline{K} = K$; $T_1$: Yes; Hausdorff: Yes.
    - **$\mathcal{T}_5$:** $\overline{K} = [0, \infty)$; $T_1$: No; Hausdorff: No.
    Q.E.D.
:::
