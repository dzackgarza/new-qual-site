---
schema: qual/card@1
id: D-T4LOC
kind: definition
title: Dual Norm
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Norms
relations: []
review: draft
---

:::{.definition}
For $X$ a normed vector space and $L \in X\dual$, the **dual norm** or **operator norm** is defined by
\[
\norm{L}_{X\dual} 
\da \sup_{ \substack{x\in X \\ \norm{x} = 1} } \abs{L(x)}
= \sup_{ \substack{x\in X \\ \norm{x} \leq  1} } \abs{L(x)}
.\]

:::
