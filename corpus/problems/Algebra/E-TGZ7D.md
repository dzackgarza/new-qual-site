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

(a) If $k$ is algebraically closed, prove that $\phi$ and $\psi$ have a common eigenvector.

(b) If both operators are diagonalizable, prove that they are simultaneously diagonalizable.
:::

::: {.solution}
For a scalar $\lambda$, write $E_\lambda=\ker(\phi-\lambda I)$.

::: pf

::: {.pf-step #invariant}
Each $E_\lambda$ is $\psi$-invariant.

::: pf-proof
For $v\in E_\lambda$,
$$
\phi(\psi v)=\psi(\phi v)=\lambda\psi v,
$$
so $\psi v\in E_\lambda$.
:::

:::

::: pf-step
(a) If $k$ is algebraically closed, then $\phi$ and $\psi$ have a common eigenvector.

::: pf-proof
Since $k$ is algebraically closed, $\phi$ has an eigenvalue $\lambda$, so $E_\lambda\neq0$. By step [](#invariant){.pf-ref}, $\psi$ restricts to an endomorphism of $E_\lambda$, which has an eigenvector $0\ne v\in E_\lambda$ since $k$ is algebraically closed. Then $v$ is an eigenvector of both operators.
:::

:::

::: pf-step
(b) If $\phi$ and $\psi$ are diagonalizable, then they are simultaneously diagonalizable.

::: pf-proof
Since $\phi$ is diagonalizable,
$$
E=\bigoplus_\lambda E_\lambda.
$$
By step [](#invariant){.pf-ref}, every $E_\lambda$ is $\psi$-invariant. Since $\psi$ is diagonalizable, its minimal polynomial splits into distinct linear factors; the minimal polynomial of each restriction $\psi\restrict_{E_\lambda}$ divides it, so each restriction is diagonalizable. Choose an eigenbasis for $\psi$ inside each $E_\lambda$. The union of these bases is a basis of $E$ consisting of simultaneous eigenvectors of $\phi$ and $\psi$.
:::

:::

:::

:::
