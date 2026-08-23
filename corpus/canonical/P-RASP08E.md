---
schema: qual/card@1
id: P-RASP08E
kind: problem
title: "Contraction mapping principle for integral equation"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $F : \mathbb{C} \to \mathbb{C}$ be a bounded Borel measurable function, and $y_0 \in \mathbb{C}$. Define a sequence of functions $f_n : [0,1] \to \mathbb{C}$ by the recursion $f_0(x) \equiv y_0$ and
$$
f_{n+1}(x) := y_0 + \int_0^x F(f_n(t))\,dt.
$$
Show that $f_n \in C([0,1])$, and there are $f \in C([0,1])$ and a subsequence $f_{n_k}$ such that $f_{n_k} \to f$ in $C([0,1])$.
:::
