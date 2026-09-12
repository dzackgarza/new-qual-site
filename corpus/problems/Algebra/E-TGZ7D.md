---
schema: qual/card@1
id: E-TGZ7D
kind: problem
title: Common eigenvectors and simultaneous diagonalization of commuting endomorphisms
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used invariant eigenspaces for both the common-eigenvector and simultaneous-diagonalization statements.
---

::: {.exercise}
Let $\phi,\psi$ be commuting endomorphisms of a finite-dimensional vector space $E$ over a field $k$.

1. If $k$ is algebraically closed, prove that $\phi$ and $\psi$ have a common eigenvector.
2. If both operators are diagonalizable, prove that they are simultaneously diagonalizable.
:::

::: {.solution}
<1>1. Assume $k$ is algebraically closed. Then $\phi$ has an eigenvalue $\lambda$, and its nonzero eigenspace
\[
E_\lambda=\ker(\phi-\lambda I)
\]
is invariant under $\psi$, because for $v\in E_\lambda$,
\[
\phi(\psi v)=\psi(\phi v)=\lambda\psi v.
\]
The restriction $\psi|_{E_\lambda}$ has an eigenvector $0\ne v\in E_\lambda$ since $k$ is algebraically closed. Then $v$ is an eigenvector of both operators.

<1>2. Now suppose both $\phi$ and $\psi$ are diagonalizable. Decompose
\[
E=\bigoplus_\lambda E_\lambda
\]
into eigenspaces of $\phi$. As above, every $E_\lambda$ is $\psi$-invariant. Since $\psi$ is diagonalizable, its minimal polynomial splits into distinct linear factors; the minimal polynomial of each restriction $\psi|_{E_\lambda}$ divides it, so each restriction is diagonalizable. Choose an eigenbasis for $\psi$ inside each $E_\lambda$. The union of these bases is a basis of $E$ consisting of simultaneous eigenvectors of $\phi$ and $\psi$.
:::
