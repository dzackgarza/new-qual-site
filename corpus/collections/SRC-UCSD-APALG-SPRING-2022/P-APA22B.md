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
---

::: {.problem}
Let $V$ be a finite-dimensional inner product space and write $n = \dim V$.
For the purposes of this question, the definition of a linear map $\phi \colon V \to V$ being unitary is that $\phi$ is invertible and $\phi^{-1} = \phi^*$ (where $\phi^*$ is the adjoint of $\phi$).

(a) Let $\phi \colon V \to V$ be a linear map, and write $\sigma_1, \ldots, \sigma_n$ for its singular values.
Prove that $\phi \colon V \to V$ is unitary if and only if $\sigma_i = 1$ for all $1 \leq i \leq n$.

Now let $W = \CC^{100}$, considered as an inner product space with its usual inner product (i.e., dot product).

(b) Suppose $\psi \colon W \to W$ is a linear map such that (a) $\|\psi\|_{\mathrm{Frob}} = 30$, and (b) $\|\psi\|_{\mathrm{op}} \leq 3$, where $\|\psi\|_{\mathrm{op}}$ denotes the operator norm with respect to the usual $\ell^2$-norm on $W$.
Using (a), or otherwise, prove that $\psi$ is diagonalizable.
:::


::: {.solution}
The singular values of a linear map $\phi$ are the square roots of the eigenvalues of the positive semidefinite operator $\phi^*\phi$.

::: pf

::: {.pf-step #unitary}

(a) $\phi$ is unitary if and only if $\sigma_i=1$ for every $i$.

::: pf-proof

If $\phi$ is unitary, then $\phi^*\phi=\phi^{-1}\phi=\operatorname{id}$, whose eigenvalues are all $1$. Conversely, if every $\sigma_i=1$, then the self-adjoint operator $\phi^*\phi$ has only the eigenvalue $1$; by the spectral theorem it is diagonalizable, so $\phi^*\phi=\operatorname{id}$. Then $\phi$ is injective, hence invertible since $V$ is finite-dimensional, and $\phi^*=\phi^*\phi\phi^{-1}=\phi^{-1}$.

:::

:::

::: {.pf-step #all-three}

(b) Every singular value of $\psi$ equals $3$.

::: pf-proof

The operator norm is the largest singular value, so $0\le\sigma_i\le3$ for $1\le i\le100$. The squared Frobenius norm is $\sum_{i=1}^{100}\sigma_i^2=900=100\cdot 9$, a sum of $100$ terms each at most $9$; so each term equals $9$.

:::

:::

::: pf-step

$\psi$ is diagonalizable.

::: pf-proof

By step [](#all-three){.pf-ref}, $\frac13\psi$ has all singular values $1$, so it is unitary by step [](#unitary){.pf-ref}. A unitary operator is normal, so by the spectral theorem there is a unitary $Q$ with $Q^*\bigl(\tfrac13\psi\bigr)Q$ diagonal; then $Q^*\psi Q$ is diagonal.

:::

:::

:::
:::
