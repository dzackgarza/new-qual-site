---
schema: qual/card@1
id: D-PPYCK
kind: definition
title: Equicontinuity on a set
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Normal Families
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open, let $K\subseteq\Omega$, and let $\mathcal F$ be a family of [[D-E7A5W|holomorphic]] functions on $\Omega$.
The family $\mathcal F$ is \dfn{equicontinuous} on $K$ if for every $\varepsilon>0$ there exists $\delta>0$ such that
$$
\abs{f(z)-f(w)}<\varepsilon\qquad\text{for all } f\in\mathcal F \text{ and all } z,w\in K \text{ with } \abs{z-w}<\delta.
$$
:::
