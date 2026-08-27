---
schema: qual/card@1
id: D-NJ2Y6
kind: definition
title: Simplicial Complex
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
relations: []
review: draft
---

::: {.definition}
Given a simplex $\sigma = [v_1 \cdots v_n]$, define the **face map**
\[
\del_i:\Delta^n &\to \Delta^{n-1} \\ 
\sigma &\mapsto  [v_1 \cdots \hat v_i \cdots v_n]
\]

A **simplicial complex** is a set $K$ satisfying

1. $\sigma \in K \implies \del_i\sigma \in K$.

2. $\sigma,\tau\in K \implies \sigma\intersect\tau = \emptyset,~ \del_i\sigma,~\text{or}~\del_i\tau$.

This amounts to saying that any collection of $(n-1)$-simplices uniquely determines an $n$-simplex (or its lack thereof), or that that map $\Delta^k \into X$ is a continuous injection from the standard simplex in $\RR^n$.

3. $\abs{K\intersect B_\varepsilon(\sigma)} < \infty$ for every $\sigma\in K$, identifying $\sigma \subseteq \RR^n$.
:::
