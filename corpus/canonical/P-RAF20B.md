---
schema: qual/card@1
id: P-RAF20B
kind: problem
title: "A bijective bounded operator with unbounded inverse on an incomplete space"
classification:
  areas:
  - real-analysis
  topics:
  - Bounded Operators
  - Normed Spaces
  - Bounded Inverse Theorem
relations: []
review: draft
solved: false
---

::: problem
Let $X$ denote the set of all sequences $a = (a_1, a_2, \ldots)$ with all $a_k$ ($k \geq 1$) real numbers but only finitely many of them nonzero.
$X$ is a real vector space with the usual component-wise addition and scalar multiplication.
It is a normed vector space with the norm $\|a\| = \sup_{k \geq 1} |a_k|$.
Define $T : X \to X$ by
$$
Ta = \left(a_1, \frac{a_2}{2}, \ldots, \frac{a_k}{k}, \ldots\right) \quad \text{if } a = (a_1, a_2, \ldots, a_k, \ldots) \in X.
$$

Prove that $T : X \to X$ is a bijective, linear, and bounded operator, but its inverse $T^{-1} : X \to X$ is unbounded.
:::
