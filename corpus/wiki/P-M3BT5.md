---
schema: qual/card@1
id: P-M3BT5
kind: problem
title: A radical extension is radical over any intermediate field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Solvable Groups
relations: []
review: draft
solved: false
---

::: problem
Suppose $F = K[\alpha_1, \cdots, \alpha_n]$ where $\alpha_1^{n_1} \in K$ for some $n_1$ and for each $i$ we have $\alpha_i^{n_i} \in K[\alpha_1, \cdots, \alpha_{i-1}]$ for some powers $n_i$.
We want to show that $F = E[\beta_1, \cdots \beta_m]$ where each $\beta_i$ satisfies a similar condition.

Let $A = \theset{\alpha_i \suchthat \alpha_i \not\in E}$.
Since $E \injects F$, adjoining all elements of $A$ to $E$ yields exactly $F$.
Using the order of $\alpha_i$ given by the definition of $F$ as a radical extension, let $\beta_1$ be the $\alpha_i \in A$ with the smallest index $i$.
Then by assumption, there is some $m_1$ such that $\beta_1^{m_1} \in K[\alpha_1, \cdots, \alpha_{i-1}] \subset F$, so we can construct $F_1 \definedas E[\beta_1]$ which will be a radical extension.

Inductively letting $A_2 = A \setminus\theset{\beta_1}$ and repeating this process to construct $F_2, F_3, \ldots$ will yield radical extensions at every step, and since $A$ is finite, there is some $N$ such that $F_N = F$.
But then $F$ is a radical extension over $E$ as desired.
:::
