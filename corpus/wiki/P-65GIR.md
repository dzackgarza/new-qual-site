---
schema: qual/card@1
id: P-65GIR
kind: problem
title: Ascending chains of ideals in a PID stabilize
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Noetherian Rings
  - Ideals
relations: []
review: draft
---

Let $R$ be a PID and $(a_1) < (a_2) < \cdots$ be an ascending chain of ideals in $R$.
Prove that for some $n$, we have $(a_j) = (a_n)$ for all $j\geq n$.

::: {.solution}
\envlist

- Let $I\da \union Ra_i$ which is an ideal in a PID and thus $I = Rb$ for some $b$.

- Using that $b\in I$, which is a union, we have $Rb\in Ra_m$ for some $m$.

- Thus $I = R_b \subseteq Ra_m$, and $Ra_m \subseteq I$ by definition of $I$, so $Rb = Ra_m$.

- In particular, since $Ra_{m} \subseteq Ra_{m+1}$ by assumption, and $Ra_{m+1} \subseteq Rb \subseteq Ra_m$ since $Rb = I$, we have $Ra_m = Ra_{m+1}$.
  So inductively, the chain stabilizes at $m$.
:::
