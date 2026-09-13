---
schema: qual/card@1
id: P-AMH-ALG-SG16-08
kind: problem
title: Amherst algebra study guide problem 8
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(March 2013) Let $G$ be a group, let $N\subseteq G$ be a normal subgroup, and suppose that $[G:N]=42$, where $[G:N]$ denotes the index of $N$ in $G$.
Prove that $x^{42}\in N$ for every $x\in G$.
(Suggestion: Consider the quotient group $G/N$.)
:::

::: {.solution}
Proof.
The quotient groupG/N has order 42 since|G/N| = [G :N] = 42. Given any x∈G, consider the coset Nx∈ G/N. By Lagrange’s Theorem applied to the group G/N and the element Nx, we have (Nx)42 =Ne, since Ne is the identity element of G/N. Now (Nx)42 =N(x42) [by deﬁnition of the group operation in G/N], and therefore Nx 42 =Ne, and hence x42 =x42e−1∈N by the coset relation.
QED
:::
