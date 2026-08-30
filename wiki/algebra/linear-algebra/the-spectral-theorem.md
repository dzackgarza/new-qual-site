---
title: The spectral theorem
order: 60
problems:
  topics:
  - Diagonalization
  - Spectral Theorem
  - Inner Product Spaces
  - Bilinear Forms
  - Quadratic Forms
  - Dual Spaces
  - Functional Analysis
---

# The spectral theorem

Diagonalizability with the extra structure of an inner product: not just a basis of eigenvectors, but an *orthonormal* one.

:::{.remark title="Notation"}
$A^t$ is the transpose and $A^{\dagger}$ the conjugate transpose.

- $A^{\dagger}$ is **adjoint** to $A$ when $\inner{A\vector x}{\vector y} = \inner{\vector x}{A^{\dagger} \vector y}$, and $A$ is **self-adjoint** when it is its own adjoint.
- $A$ is **symmetric** when $A = A^t$, and **orthogonal** when $A^tA = AA^t = I$.
- $A$ is **Hermitian** when $A^{\dagger} = A$, **normal** when $AA^{\dagger} = A^{\dagger}A$, and **unitary** when $A^{\dagger}A = AA^{\dagger} = I$.

:::

## Diagonalizability first

[[FD-K6FVX]]

[[L-C5DDK]]

[[T-6ABNR]]

[[FT-BC6S2]]

:::{.proof}
$\implies$: if $\min_A$ splits into linear factors then so does every invariant factor, so every elementary divisor is linear and the Jordan form is diagonal.

:::

:::{.remark title="The test to remember"}
$A$ is diagonalizable over $F$ exactly when $\min_A$ is a product of *distinct* linear factors over $F$.
Squarefree is the whole criterion, which is why hypotheses like $A^2 = A$ or $A^k=I$ settle diagonalizability immediately -- see [[Algebra/linear-algebra/find-the-canonical-form|Find the canonical form]].

:::

## The theorem

[[T-WQHMA]]

:::{.remark}
$A$ is symmetric exactly when the spectrum provides an orthonormal basis.

:::

:::{.proof title="of the spectral theorem"}
\envlist

- Suppose $A$ is Hermitian.
  $V$ is an invariant subspace, so $A$ has an eigenvector $\vector v_1$.
  Let $W_1 = \spanof_k\ts{\vector v_1}^\perp$; for $\vector w_1 \in W_1$,
$$
\inner{\vector v_1}{ A \vector w_1} =
\inner{A \vector v_1}{\vector w_1} =
\lambda \inner{\vector v_1}{\vector w_1} = 0,
$$
so $A(W_1)\subseteq W_1$ and the argument repeats on $W_1$.

- Suppose $A$ is symmetric, and take a unit eigenvector $\vector v$.
  Then
\[
\lambda = \lambda\inner{\vector v}{\vector v} = \inner{A\vector v}{\vector v} = \inner{\vector v}{A\vector v} = \overline{\lambda} \implies \lambda \in \RR
,\]
which is the statement that a real symmetric matrix has real eigenvalues.

:::

## Simultaneous diagonalization

[[PR-GV5CF]]

:::{.proof}
By induction on the number of operators.

- $A_n$ is diagonalizable, so $V = \bigoplus E_i$ splits into eigenspaces.
- Restrict the other $n-1$ operators to $E_n$; they commute on $V$ so they commute on $E_n$, and a diagonalizable operator restricted to an invariant subspace is diagonalizable.
- By induction they are simultaneously diagonalizable on $E_n$, and their eigenvectors there are also eigenvectors of $A_n$.
- Repeat for each eigenspace.

> [Full details](https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf#page=9)

:::

:::{.remark title="Why commuting is the hypothesis"}
Commuting operators preserve each other's eigenspaces, which is what lets the induction descend.
Without it the eigenspaces of one operator are not invariant under the other and there is no basis to build.

:::
