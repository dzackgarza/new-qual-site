---
schema: qual/card@1
id: P-AMD-AF6CJFKN
kind: problem
title: Cauchy's theorem
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - p-Groups
  - Orbit-Stabilizer
relations: []
review: draft
solved: false
---

::: {.problem}
Prove Cauchy's Theorem.
Given $p\divides o(G) <\infty$
$$
X = \theset{ (a_{i})_{i=1}^p \in G^p \suchthat \prod_{i=1}^p a_i = e} \\
$$

- Show: $(a_1 a_2\cdots a_p) = e \implies (a_2 a_3 \cdots a_p a_1) = e$

- Show: $(\ZZ_p, +) \actson X$ and $\bar 1 \actson (a_1 a_2 \cdots a_p) = (a_2 a_3 \cdots a_p a_1)$

- Show: $|X| = |G|^{p-1}$

- Show: $\{ \mathcal{O}_x : |\mathcal{O}_x| = 1 \} > 1$ and $\exists a \in G \ni a^p = e$
:::
