---
schema: qual/card@1
id: P-RAF04H
kind: problem
title: "Iterated integral operators produce a uniformly convergent subsequence (Arzela-Ascoli)"
classification:
  areas:
  - real-analysis
  topics:
  - Arzela-Ascoli Theorem
  - Compact Operators
  - Uniform Convergence
relations: []
review: draft
---

::: problem
Let $G : \mathbb{R} \to \mathbb{R}$ be a bounded Borel measurable function.
Define $f_0(t) = 1$ and $f_n : [-1, 1] \to \mathbb{R}$ inductively by
$$
f_{n+1}(t) = 1 + \int_0^t G(f_n(\tau)) \, d\tau.
$$

Show:

(a) $f_n$ are well defined and $f_n \in C([-1, 1], \mathbb{R})$ for all $n$.

(b) The sequence $\{f_n\}_{n=1}^\infty$ has a uniformly convergent subsequence.
:::
