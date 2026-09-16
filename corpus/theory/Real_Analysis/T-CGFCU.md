---
schema: qual/card@1
id: T-CGFCU
kind: theorem
title: Lusin's theorem
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Continuity
relations: []
review: draft
---

::: {.theorem}
Let $E\subseteq\RR^n$ be [[D-MDJII|Lebesgue measurable]] with $m(E)<\infty$, and let $f\colon E\to\RR$ be [[D-DHFN4|measurable]].
For every $\varepsilon>0$ there exists a closed set $F_\varepsilon\subseteq\RR^n$ with
$$
F_\varepsilon \subseteq E \quad\text{and}\quad m(E \setminus F_\varepsilon) \leq \varepsilon
$$
such that the restriction $\ro{f}{F_\varepsilon}\colon F_\varepsilon\to\RR$ is continuous.
:::

::: {.example}
Continuity of the restriction $\ro{f}{F_\varepsilon}$ does not make $f$ continuous at points of $F_\varepsilon$.
Let $E=[0,1]$ and $f=\chi_{\QQ\cap[0,1]}$, which is discontinuous at every point of $[0,1]$.
Enumerate $\QQ\cap[0,1]=\theset{q_1,q_2,\ldots}$ and put $F_\varepsilon\coloneqq[0,1]\setminus\bigcup_{k\geq1}(q_k-\varepsilon2^{-k-1},q_k+\varepsilon2^{-k-1})$.
Then $F_\varepsilon$ is closed, $F_\varepsilon\subseteq E$, $m(E\setminus F_\varepsilon)\leq\varepsilon$, and $\ro{f}{F_\varepsilon}=0$ is continuous.
:::
