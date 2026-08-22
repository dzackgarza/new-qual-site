---
schema: qual/card@1
id: P-ALGS11F
kind: problem
title: Tensor product of linear maps and $\det(\phi \otimes \psi)$
classification:
  areas:
  - algebra
  topics:
  - Multilinear Algebra
  - Linear Algebra
relations: []
review: draft
solved: false
---

::: problem
Given vector spaces $V$ and $W$ over the complex numbers, suppose that $\phi \colon V \to V$ and $\psi \colon W \to W$ are $\mathbb{C}$-linear transformations.

(i) Show that there is a unique linear transformation
\[
\phi \otimes \psi \colon V \otimes_{\mathbb{C}} W \to V \otimes_{\mathbb{C}} W
\]
with the property that
\[
(\phi \otimes \psi)(v \otimes w) = \phi(v) \otimes \psi(w)
\]
for all $v \in V$, $w \in W$.

(ii) Let $V$ and $W$ be finite-dimensional of complex dimensions $m$ and $n$ respectively.
Prove that
\[
\det(\phi \otimes \psi) = \det(\phi)^n \det(\psi)^m.
\]

Hint: Choose $\mathbb{C}$-bases for $V$ and $W$ such that the matrices representing $\phi$ and $\psi$ have a special form.
:::
