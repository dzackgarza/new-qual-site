---
schema: qual/card@1
id: P-PERUTZ08-4.1
kind: problem
title: Fundamental groups of connected sums and realization of finitely presented groups
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 4.1 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
---

::: {.problem}
An $n$-dimensional manifold is a Hausdorff space covered by open sets homeomorphic to $\mathbb R^n$.
Let $X_1$ and $X_2$ be connected $n$-manifolds.
Form their connected sum by choosing embeddings $i_j:D^n\to X_j$, putting $D'=\tfrac12D^n$, and identifying $i_1(x)$ with $i_2(x)$ for $x\in\partial D'=S^{n-1}$ after removing the two copies of $\operatorname{int}D'$.

1. Prove that if $n>2$, then
   \[
   \pi_1(X_1\#X_2)\cong \pi_1(X_1)*\pi_1(X_2).
   \]

2. Let $X$ be an iterated connected sum of $r$ copies of $S^1\times S^{n-1}$, with $n\ge3$.
   Compute $\pi_1(X)$.

3. Given a finitely presented group
   \[
   G=\langle g_1,\dots,g_k\mid r_1,\dots,r_\ell\rangle,
   \]
   construct a connected compact $4$-manifold $M$ with $\pi_1(M)\cong G$.

For the last part, the source suggests starting with the case of no relations and using
\[
\partial(S^1\times D^3)=S^1\times S^2=\partial(D^2\times S^2).
\]
:::
