---
schema: qual/card@1
id: P-AMD-DIHC4KCK
kind: problem
title: Let $\{f_k\}$ be any sequence of functions in $L^2([0, 1])$…
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\{f_k\}$ be any sequence of functions in $L^2([0, 1])$ satisfying $\norm{f_k}_2 \leq M$ for all $k ∈ \NN$.

Prove that if $f_k \to f$ almost everywhere, then $f ∈ L^2([0, 1])$ with $\norm{f}_2 \leq M$ and
$$
\lim _{k \rightarrow \infty} \int_{0}^{1} f_{k}(x) dx = \int_{0}^{1} f(x) d x
$$

> Hint: Try using Fatou’s Lemma to show that $\norm{f}_2 \leq M$ and then try applying Egorov’s Theorem.
:::
