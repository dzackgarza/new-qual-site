---
schema: qual/card@1
id: FT-KXFMK
kind: theorem
title: Equivalent characterizations of measurability of a set
prompts:
- What conditions each characterise measurability of a set $E \subset \RR^n$?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $m_*$ be the [[D-3XE77|outer measure]] on $\RR^n$ and let $E\subseteq \RR^n$.
The following are equivalent:

1. $E$ is [[D-MDJII|Lebesgue measurable]]: for every $\varepsilon>0$ there exists an open set $G\supseteq E$ with $m_*(G\setminus E)<\varepsilon$.

2. For every $\varepsilon>0$ there exists a closed set $F\subseteq E$ with $m_*(E\setminus F) < \varepsilon$.

3. $E = H \cup Z$ with $H$ an [[D-RPOGQ|$F_\sigma$ set]] and $Z$ a [[FD-6HUIM|null]] set.

4. $E = V\setminus Z$ with $V$ a [[D-RPOGQ|$G_\delta$ set]] and $Z$ a null set.

If $m_*(E)<\infty$, these are also equivalent to:

5. For every $\varepsilon>0$ there exists a compact set $K\subseteq E$ with $m_*(E\setminus K) < \varepsilon$.
:::

::: {.example}
The finiteness hypothesis in (5) cannot be dropped: $E=\RR^n$ is measurable, but $m_*(\RR^n\setminus K)=\infty$ for every compact $K\subseteq\RR^n$.
:::
