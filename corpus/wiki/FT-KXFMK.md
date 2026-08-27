---
schema: qual/card@1
id: FT-KXFMK
kind: theorem
title: Equivalent characterizations of measurability of a set
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
$E\subset \RR^n$ is measurable iff any of these conditions hold

- There exist closed $F\subseteq E$ with $m_*(E\setminus F) < \varepsilon \to 0$.

- There exist *compact* $K\subseteq E$ with $m_*(E\setminus K) < \varepsilon \to 0$.

- There exist open $G\supset E$ with $m_*(G\setminus E)<\varepsilon \to 0$ (outer regular)

- $E = H \union Z$ with $H\in F_\sigma$ and $Z$ null

- $E = V\setminus Z$ with $V\in G_\delta$ and $Z$ null
:::
