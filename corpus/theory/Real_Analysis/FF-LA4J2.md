---
schema: qual/card@1
id: FF-LA4J2
kind: fact
title: Carathéodory criterion for Lebesgue measurability
slogan: 'A set $E$ is measurable exactly when, for every set $A$, the outer measure of $A$ is additive over $A\cap E$ and $A\setminus E$.'
prompts:
- What is the Carathéodory criterion for Lebesgue measurability?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.fact}
Let $m_*$ be the [[D-3XE77|outer measure]] on $\RR^n$.
A set $E\subseteq \RR^n$ is [[D-MDJII|Lebesgue measurable]] if and only if for every $A\subseteq \RR^n$,
$$
m_*(A) = m_*(A\cap E) + m_*(A\setminus E).
$$
:::
