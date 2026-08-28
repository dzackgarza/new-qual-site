---
schema: qual/card@1
id: FD-D4S7E
kind: definition
title: 'Definition: Measurability of a Set'
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
A set $E\subseteq \RR^n$ is *measurable* iff for every $\varepsilon>0$ there exists an open $G(\varepsilon) \supset E$ with $m_*(G(\varepsilon)\setminus E)<\varepsilon \to 0$ (outer regular).
:::
