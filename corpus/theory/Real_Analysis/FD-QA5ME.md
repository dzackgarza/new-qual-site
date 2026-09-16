---
schema: qual/card@1
id: FD-QA5ME
kind: definition
title: Lebesgue outer measure
prompts:
- How is the outer measure $m_*(E)$ defined?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
For a closed cube $Q=\prod_{i=1}^n[a_i,a_i+\ell]\subseteq\RR^n$, write $\abs{Q}\coloneqq\ell^n$ for its volume.
The \dfn{outer measure} of $E\subseteq\RR^n$ is
$$
m_*(E) \coloneqq \inf \theset{ \sum_{i=1}^\infty \abs{Q_i} \suchthat Q_1,Q_2,\ldots \text{ closed cubes with } E\subseteq\bigcup_{i=1}^\infty Q_i}.
$$
:::
