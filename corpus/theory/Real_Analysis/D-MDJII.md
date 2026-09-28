---
schema: qual/card@1
id: D-MDJII
kind: definition
title: Lebesgue measurable sets
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
A subset $E\subseteq \RR^n$ is \dfn{Lebesgue measurable} if for every $\varepsilon> 0$ there exists an open set $O \supseteq E$ such that $m_*(O\setminus E) < \varepsilon$.
For a Lebesgue measurable set $E$, its \dfn{Lebesgue measure} is $m(E) \coloneqq m_*(E)$.
:::
