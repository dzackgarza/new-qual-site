---
schema: qual/card@1
id: PR-UHWNM
kind: proposition
title: Borel measures finite on balls are outer regular by open sets and inner regular by closed sets
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $X$ be a metric space with Borel $\sigma$-algebra $\mcb$, and let $\mu$ be a measure on $\mcb$ with $\mu(B)<\infty$ for every open ball $B$ of finite radius.
Then for every $E \in \mcb$ and every $\varepsilon>0$:

- there exists an open set $O\subseteq X$ with $E \subseteq O$ and $\mu(O\setminus E) < \varepsilon$;

- there exists a closed set $F\subseteq X$ with $F\subseteq E$ and $\mu(E\setminus F) < \varepsilon$.
:::
