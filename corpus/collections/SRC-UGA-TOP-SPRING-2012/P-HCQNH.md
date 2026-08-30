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
**Goal:** Derive $\chi(X)=\chi(U)+\chi(V)-\chi(U\cap V)$.

<1> Use Mayer--Vietoris for reduced homology.
    *Proof:*
    <2>1. The long exact sequence yields alternating dimensions:
        $$
        \cdots\to H_n(U\cap V)\to H_n(U)\oplus H_n(V)\to H_n(X)\to H_{n-1}(U\cap V)\to\cdots
        $$
    <2>2. Summing alternating ranks over all $n$ in a finite-dimensional complex gives
        $$\chi(X)=\chi(U)+\chi(V)-\chi(U\cap V).$$

<1> Conclusion:
    This is exactly the stated Euler characteristic additivity formula for an open cover by two sets.

Authored by **Codex 5.3 Spark Extra High**.
:::
