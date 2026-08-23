---
schema: qual/card@1
id: P-CASP04E
kind: problem
title: "Points connected to infinity outside a compact set are not in its polynomial hull"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $K$ be a compact subset of $\mathbb{C}$ and $\hat{K}$ its polynomial hull, i.e.
$$\hat{K} := \{z \in \mathbb{C} : |p(z)| \leq \sup_{w \in K} |p(w)|, \text{ for every polynomial } p\}.$$
Show that if $z \in \mathbb{C} \setminus K$ and there is a curve $\gamma \subset \mathbb{C}_\infty \setminus K$ connecting $z$ to $\infty$, then $z \notin \hat{K}$.
:::
