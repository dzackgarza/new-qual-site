---
schema: qual/card@1
id: P-RASP22B
kind: problem
title: "Bounded sequence with vanishing local integrals against L^1 functions"
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
Let $(f_n)_{n \in \mathbb{N}}$ be a sequence of Lebesgue measurable functions defined on $[0,1]$. Assume there is a $C > 0$ such that $|f_n(x)| \leq C$ for almost every $x \in [0,1]$ and every $n$, and assume that $\lim_{n \to \infty} \int_0^a f_n(x)\,dx = 0$ for every $a \in (0,1)$. Prove that
$$
\lim_{n \to \infty} \int_0^1 g(x) f_n(x)\,dx = 0
$$
for every function $g \in L^1([0,1])$.
:::
