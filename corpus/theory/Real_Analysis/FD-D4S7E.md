---
schema: qual/card@1
id: FD-D4S7E
kind: definition
title: Lebesgue measurability of a set
prompts:
- When is a set $E \subseteq \RR^n$ measurable?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $m_*$ be the [[D-3XE77|outer measure]] on $\RR^n$.
A set $E\subseteq \RR^n$ is \dfn{measurable} if for every $\varepsilon>0$ there exists an open set $G \supseteq E$ with $m_*(G\setminus E)<\varepsilon$.
:::
