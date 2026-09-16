---
schema: qual/card@1
id: FT-O4DRR
kind: theorem
title: Carathéodory's criterion for Lebesgue measurability
prompts:
- State the Caratheodory characterization of measurability.
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $m_*$ be the [[D-3XE77|outer measure]] on $\RR^n$.
A set $E\subseteq \RR^n$ is [[D-MDJII|Lebesgue measurable]] if and only if for every $A\subseteq \RR^n$,
$$
m_*(A) = m_*(A\cap E) + m_*(A\cap E^c).
$$
:::
