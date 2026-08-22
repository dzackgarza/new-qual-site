---
schema: qual/card@1
id: P-APA22B
kind: problem
title: Unitary maps have singular values $1$; Frobenius and operator norms force diagonalizability
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Norms
  - Diagonalization
relations: []
review: draft
solved: false
---

::: problem
Let $V$ be a finite-dimensional inner product space and write $n = \dim V$.
For the purposes of this question, the definition of a linear map $\phi \colon V \to V$ being unitary is that $\phi$ is invertible and $\phi^{-1} = \phi^*$ (where $\phi^*$ is the adjoint of $\phi$).

(a) Let $\phi \colon V \to V$ be a linear map, and write $\sigma_1, \ldots, \sigma_n$ for its singular values.
Prove that $\phi \colon V \to V$ is unitary if and only if $\sigma_i = 1$ for all $1 \leq i \leq n$.

Now let $W = \mathbb{C}^{100}$, considered as an inner product space with its usual inner product (i.e., dot product).

(b) Suppose $\psi \colon W \to W$ is a linear map such that (a) $\|\psi\|_{\mathrm{Frob}} = 30$, and (b) $\|\psi\|_{\mathrm{op}} \leq 3$, where $\|\psi\|_{\mathrm{op}}$ denotes the operator norm with respect to the usual $\ell^2$-norm on $W$.
Using (a), or otherwise, prove that $\psi$ is diagonalizable.
:::
