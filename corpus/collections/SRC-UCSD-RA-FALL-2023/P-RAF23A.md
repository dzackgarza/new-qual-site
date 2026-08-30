---
schema: qual/card@1
id: P-RAF23A
kind: problem
title: "True/false on distributional derivative of monotone function and countable sets"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
TRUE or FALSE: Prove it if true and disprove it if false.

(i) Let $f(t)$ be a monotone non-increasing function on $\mathbb{R}$.
Then its distributional derivative is always a Radon measure.

(ii) Let $E \subset [0,1] \subset \mathbb{R}$ be a countable subset.
Then for any $\epsilon > 0$, there is a finite cover of $E$ by open intervals $\{I_k\}_{k=1}^{n}$ such that
$$
\sum_{k=1}^{n} m(I_k) < \epsilon.
$$
:::

::: solution
**Goal:** Evaluate each claim and give the correct proof.

<1>1. Statement (i): TRUE.
    <2>1. A monotone function on $\mathbb R$ has bounded variation on every compact interval.
    <2>2. The distributional derivative of a bounded-variation function is a signed Radon measure on $\mathbb R$.
    <2>3. Therefore the distributional derivative of monotone non-increasing $f$ is a Radon measure.

<1>2. Statement (ii): FALSE.
    <2>1. Let $E=\mathbb Q\cap[0,1]$, which is countable and dense in $[0,1]$.
    <2>2. If $\{I_k\}_{k=1}^n$ is a finite open cover of $E$, then
    $U=\bigcup_{k=1}^n I_k$ is an open set containing $E$.
    <2>3. Since $E$ is dense, $\overline{U}\supset [0,1]$, hence $m(U)\ge1$.
    <2>4. If the intervals are disjoint components $J_j$ of $U$, then
    $$m(U)=\sum_j m(J_j)\ge1.$$
    <2>5. This also equals $\sum_{k=1}^n m(I_k)$ after merging overlapping intervals, so it cannot be made smaller than $\epsilon<1$.
    <2>6. Therefore statement (ii) is false.
:::
