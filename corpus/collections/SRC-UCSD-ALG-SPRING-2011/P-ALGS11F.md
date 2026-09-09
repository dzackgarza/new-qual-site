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

audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 6 of the official UCSD Spring 2011 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Used the tensor-product universal property for existence and Schur triangularization for the determinant formula.
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
\n\n::: {.solution}\n<1>1. There is a unique linear map\n\[\n\phi\otimes\psi:V\otimes_{\mathbb C}W\to V\otimes_{\mathbb C}W\n\]\nsatisfying\n\[\n(\phi\otimes\psi)(v\otimes w)=\phi(v)\otimes\psi(w).\n\]\n::: {.proof}\nDefine\n\[\nB:V\times W\longrightarrow V\otimes_{\mathbb C}W,\qquad\nB(v,w)=\phi(v)\otimes\psi(w).\n\]\nBecause $\phi$ and $\psi$ are linear, $B$ is bilinear.
By the universal property of $V\otimes W$, there is a unique linear map\n\[\nT:V\otimes W\to V\otimes W\n\]\nsuch that $T(v\otimes w)=B(v,w)$.
This map is, by definition, $\phi\otimes\psi$.\n:::\n\n<1>2. Assume now that $\dim V=m$ and $\dim W=n$.
Choose bases in which the matrices of $\phi$ and $\psi$ are upper triangular.\n::: {.proof}\nOver $\mathbb C$, every square matrix is triangularizable: equivalently, by Schur triangularization, there are bases in which\n\[\n[\phi]=A=(a_{ij}),\qquad [\psi]=B=(b_{rs})\n\]\nare upper triangular.
Let their diagonal entries be\n\[\n\lambda_1,\ldots,\lambda_m\quad\text{and}\quad\mu_1,\ldots,\mu_n.\n\]\nThen\n\[\n\det\phi=\prod_{i=1}^m\lambda_i,\qquad\det\psi=\prod_{j=1}^n\mu_j.\n\]\n:::\n\n<1>3. In the tensor-product basis $v_i\otimes w_j$, the matrix of $\phi\otimes\psi$ is the Kronecker product $A\otimes B$, which is upper triangular with diagonal entries\n\[\n\lambda_i\mu_j\qquad(1\le i\le m,\ 1\le j\le n).\n\]\n::: {.proof}\nFor basis vectors,\n\[\n(\phi\otimes\psi)(v_i\otimes w_j)=\phi(v_i)\otimes\psi(w_j).\n\]\nSince $A$ and $B$ are upper triangular, each factor is a linear combination only of basis vectors with index at least the original one, so with the lexicographically ordered tensor basis the resulting matrix is upper triangular.
The coefficient of $v_i\otimes w_j$ in the image of $v_i\otimes w_j$ is $\lambda_i\mu_j$.\n:::\n\n<1>4. Therefore\n\[\n\det(\phi\otimes\psi)=\det(\phi)^n\det(\psi)^m.\n\]\n::: {.proof}\nUsing <1>3,\n\[\n\det(\phi\otimes\psi)\n=\prod_{i=1}^m\prod_{j=1}^n(\lambda_i\mu_j)\n=\left(\prod_{i=1}^m\lambda_i\right)^n\left(\prod_{j=1}^n\mu_j\right)^m\n=\det(\phi)^n\det(\psi)^m.\n\]\n:::\n:::\n
