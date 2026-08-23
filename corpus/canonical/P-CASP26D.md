---
schema: qual/card@1
id: P-CASP26D
kind: problem
title: "Holomorphic function on the upper half-plane with real boundary values and polynomial growth is a Laurent polynomial"
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Boundary Values
  - Reflection Principle
  - Growth Estimates
relations: []
review: draft
solved: false
---

::: problem
Let $f$ be holomorphic on the upper half-plane $H = \{z \in \mathbb{C} : \operatorname{Im} z > 0\}$. Assume that

(i) $f$ extends continuously to $H \setminus \{0\}$,

(ii) $f(x) \in \mathbb{R}$ for all $x \in \mathbb{R} \setminus \{0\}$,

(iii) there exists an integer $N > 0$ such that $|f(z)| \leq |z|^N + |z|^{-N}$ for all $z \in H$.

Prove that there are constants $a_k \in \mathbb{R}$ such that $f(z) = \sum_{k=-N}^{N} a_k z^k$.
:::