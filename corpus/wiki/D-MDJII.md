---
schema: qual/card@1
id: D-MDJII
kind: definition
title: "Lebesgue Measurable Sets"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
---

::: {.definition title="Lebesgue Measurable Sets"}
A subset $E\subseteq \RR^n$ is **Lebesgue measurable** iff for every $\eps> 0$ there exists an open set $O \supseteq E$ such that $m_*(O\setminus E) < \eps$.
In this case, we define $m(E) \da m_*(E)$.
:::
