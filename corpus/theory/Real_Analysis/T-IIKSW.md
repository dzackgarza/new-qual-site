---
schema: qual/card@1
id: T-IIKSW
kind: theorem
title: Approximation of measurable sets by open, closed, and compact sets
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $E\subseteq\RR^n$ be [[D-MDJII|Lebesgue measurable]] and let $\varepsilon>0$.

1. There exists an open set $O\supseteq E$ with $m(O\setminus E) < \varepsilon$.

2. There exists a closed set $F\subseteq E$ with $m(E\setminus F) < \varepsilon$.

3. If $m(E)<\infty$, there exists a compact set $K\subseteq E$ with $m(E\setminus K) < \varepsilon$ [@Fol13].
:::

::: {.example}
The finiteness hypothesis in (3) cannot be dropped.
For $E=\RR^n$, every compact $K\subseteq\RR^n$ is bounded, hence has finite measure, so $m(\RR^n\setminus K)=\infty$.
:::
