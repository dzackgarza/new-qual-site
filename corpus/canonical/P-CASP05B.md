---
schema: qual/card@1
id: P-CASP05B
kind: problem
title: "Jensen-type inequality for bounded analytic functions with prescribed zeros"
classification:
  areas:
  - complex-analysis
topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $f \in H(\mathbb{D})$, and $c_1, \ldots, c_n \in \mathbb{D} \setminus \{0\}$ with $f(c_j) = 0$ for $j = 1, \ldots, n$. Show that if $|f(z)| \leq M$ for $|z| < 1$, then
$$|f(0)| \leq M \prod_{j=1}^{n} |c_j|.$$

Hint: Consider the function $g(z) = f(z) / \prod_j \phi_{c_j}(z)$, where $\phi_{c_j}$ is a one-to-one analytic map of $\mathbb{D}$ onto itself vanishing at $c_j$.
:::
