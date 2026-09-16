---
schema: qual/card@1
id: D-S2YWR
kind: definition
title: Limit superior of a function at a point
classification:
  areas:
  - real-analysis
  topics:
  - Limits
relations: []
review: draft
---

::: {.definition}
Let $A\subseteq\RR^n$, let $f\colon A\to \RR$, and let $y\in\RR^n$ be a [[D-Y6JAS|limit point]] of $A$.
The \dfn{limit superior} of $f$ at $y$ is
$$
\limsup_{x\to y} f(x) \coloneqq \lim_{\varepsilon\to 0^+} \sup f\qty{A \cap B_\varepsilon(y) \setminus\theset{y}} \in [-\infty,\infty],
$$
where $B_\varepsilon(y)$ is the open ball of radius $\varepsilon$ about $y$; the limit exists because the supremum is nonincreasing as $\varepsilon$ decreases.
:::
