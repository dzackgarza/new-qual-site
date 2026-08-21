---
schema: qual/card@1
id: E-F46JG
kind: exercise
title: Every topological group is completely regular
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Separation Axioms
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §33.10"}


Prove the following.

Theorem. Every topological group is completely regular.

Proof. Let $V_0$ be a neighborhood of the identity element $e$, in the topological group $G$. In general, choose $V_n$ to be a neighborhood of $e$ such that $V_n \cdot V_n \subset V_{n-1}$. Consider the set of all dyadic rationals $p$, that is, all rational numbers of the form $k/2^n$, with $k$ and $n$ integers. For each dyadic rational $p$ in $(0, 1]$, define an open set $U(p)$ inductively as follows: $U(1) = V_0$ and $U(\tfrac{1}{2}) = V_1$. Given $n$, if $U(k/2^n)$ is defined for $0 < k/2^n \leq 1$, define

$$
U(1/2^{n+1}) = V_{n+1},
$$

$$
U((2k+1)/2^{n+1}) = V_{n+1} \cdot U(k/2^n)
$$

for $0 < k < 2^n$. For $p \leq 0$, let $U(p) = \varnothing$, and for $p > 1$, let $U(p) = G$. Show that

$$
V_n \cdot U(k/2^n) \subset U((k+1)/2^n)
$$

for all $k$ and $n$. Proceed as in the Urysohn lemma.

This exercise is adapted from [M-Z], to which the reader is referred for further results on topological groups.
:::
