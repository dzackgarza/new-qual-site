---
schema: qual/card@1
id: FD-6HUIM
kind: definition
title: Null sets in $\RR^n$
prompts:
- What does it mean for a set to be null?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $m$ be Lebesgue measure on $\RR^n$.
A set $A\subseteq\RR^n$ is \dfn{null} if for every $\varepsilon>0$ there exist open sets $U_1,U_2,\ldots\subseteq\RR^n$ with $A\subseteq\bigcup_{j} U_j$ and $\sum_j m(U_j) < \varepsilon$.
:::

::: {.remark}
A set $A$ is null if and only if its [[D-3XE77|outer measure]] $m_*(A)$ is $0$.
Indeed, $m_*(A)\leq\sum_j m(U_j)$ for every such cover; conversely, if $m_*(A)=0$, a cover of $A$ by closed cubes of total volume less than $\varepsilon/2^{n+1}$ can be replaced by the open cubes with the same centers and twice the side lengths, of total volume less than $\varepsilon$.
:::
