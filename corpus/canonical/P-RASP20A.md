---
schema: qual/card@1
id: P-RASP20A
kind: problem
title: "True or false: neighborhoods of measurable sets, Borel measurability of derivatives, averaging covering argument, C([0,1]) in L^1"
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Measure
  - Regularity
  - Borel Measurable Functions
  - Covering Arguments
  - L1 Spaces
relations: []
review: draft
solved: false
---

::: problem
Determine if each of the following statements is true or false.
If true, give a brief proof.
If false, give a counterexample.

(1) Let $E$ be a Lebesgue-measurable subset of $\mathbb{R}$.
For each $k \in \mathbb{N}$, let $E_k = \{x \in \mathbb{R} : \operatorname{dist}(x, E) < 1/k\}$, where $\operatorname{dist}(x, E) = \inf\{|y - x| : y \in E\}$.
Then $\lim_{k \to \infty} m(E_k) = m(E)$.

(2) If $f : (0, 1) \to \mathbb{R}$ is differentiable at each point $x \in (0, 1)$, then the derivative $f' : (0, 1) \to \mathbb{R}$ is Borel-measurable on $(0, 1)$.

(3) Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) = 1$.
Let $E_j \in \mathcal{M}$ ($j = 1, \ldots, n$). Let $q$ be an integer such that $1 \leq q \leq n$.
Assume that any $x \in X$ belongs to at least $q$ of these subsets $E_1, \ldots, E_n$.
Then there exists $j_0$ such that $\mu(E_{j_0}) \geq q/n$.

(4) The space $C([0, 1])$ is a closed subspace of $L^1([0, 1], m)$ with respect to the $L^1$-norm.
:::
