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
---

::: problem
Suppose that $\phi$ and $\psi$ are commuting endomorphisms of a finite dimensional vector space $E$ over a field $k$, so $\phi \psi=\psi \phi$.

- Prove that if $k$ is algebraically closed, then $\phi$ and $\psi$ have a common eigenvector.

- Prove that if $E$ has a basis consisting of eigenvectors of $\phi$ and $E$ has a basis consisting of eigenvectors of $\psi$, then $E$ has a basis consisting of vectors that are eigenvectors for both $\phi$ and $\psi$ simultaneously.
:::

::: solution
**Goal:** Prove that commuting endomorphisms have a common eigenvector over an algebraically closed field, and are simultaneously diagonalizable if each is diagonalizable.

<1>1. Part 1: Common eigenvector over an algebraically closed field:
::: {.proof}
<2>1. Since $k$ is algebraically closed and $\dim E < \infty$, the characteristic polynomial of $\phi$ splits completely into linear factors over $k$.
<2>2. Thus $\phi$ has at least one eigenvalue $\lambda \in k$.
<2>3. Let $V_\lambda = \ker(\phi - \lambda I) \subseteq E$ be the eigenspace of $\phi$ for eigenvalue $\lambda$. Since $\lambda$ is an eigenvalue, $V_\lambda \ne \{0\}$.
<2>4. **$V_\lambda$ is $\psi$-invariant:** For any $v \in V_\lambda$:
$$\phi(\psi(v)) = (\phi \psi)(v) = (\psi \phi)(v) = \psi(\phi(v)) = \psi(\lambda v) = \lambda \psi(v).$$
Thus $\psi(v) \in V_\lambda$, so $\psi(V_\lambda) \subseteq V_\lambda$.
<2>5. The restriction $\psi|_{V_\lambda}: V_\lambda \to V_\lambda$ is an endomorphism of the non-zero, finite-dimensional vector space $V_\lambda$.
<2>6. Because $k$ is algebraically closed, the characteristic polynomial of $\psi|_{V_\lambda}$ has a root $\mu \in k$, which is an eigenvalue of $\psi|_{V_\lambda}$.
<2>7. Let $v_0 \in V_\lambda \setminus \{0\}$ be an eigenvector of $\psi|_{V_\lambda}$ for eigenvalue $\mu$.
<2>8. Then:
- $v_0 \in V_\lambda \implies \phi(v_0) = \lambda v_0$ (eigenvector of $\phi$).
- $\psi(v_0) = \mu v_0$ (eigenvector of $\psi$).
<2>9. Thus $v_0$ is a non-zero common eigenvector for both $\phi$ and $\psi$.
:::

<1>2. Part 2: Simultaneous diagonalizability:
::: {.proof}
<2>1. Since $\phi$ is diagonalizable, $E$ decomposes into a direct sum of distinct eigenspaces of $\phi$:
$$E = \bigoplus_{i=1}^m E_\phi(\lambda_i), \qquad \text{where } E_\phi(\lambda_i) = \ker(\phi - \lambda_i I).$$
<2>2. As shown in step <1>1.4, each eigenspace $E_\phi(\lambda_i)$ is invariant under $\psi$.
<2>3. **Restriction of a diagonalizable operator to an invariant subspace is diagonalizable:**
- Since $\psi$ is diagonalizable on $E$, its minimal polynomial $m_\psi(x)$ factors into distinct linear factors over $k$.
- The minimal polynomial of the restriction $\psi|_{E_\phi(\lambda_i)}$ divides $m_\psi(x)$, hence also factors into distinct linear factors over $k$.
- Therefore, $\psi|_{E_\phi(\lambda_i)}$ is diagonalizable on $E_\phi(\lambda_i)$.
<2>4. For each $i \in \{1, \dots, m\}$, choose a basis $\mathcal{B}_i$ of $E_\phi(\lambda_i)$ consisting of eigenvectors of $\psi|_{E_\phi(\lambda_i)}$.
<2>5. Every vector $v \in \mathcal{B}_i$ satisfies:
- $\phi(v) = \lambda_i v$ (since $v \in E_\phi(\lambda_i)$),
- $\psi(v) = \mu v$ for some $\mu \in k$ (since $v$ is an eigenvector of $\psi|_{E_\phi(\lambda_i)}$).
<2>6. Thus every vector in $\mathcal{B}_i$ is an eigenvector for both $\phi$ and $\psi$.
<2>7. The union $\mathcal{B} = \bigcup_{i=1}^m \mathcal{B}_i$ is a basis for $E = \bigoplus_{i=1}^m E_\phi(\lambda_i)$ consisting of simultaneous eigenvectors.
:::

<1>3. Conclusion:
::: {.proof}
Commuting operators on finite-dimensional spaces have a common eigenvector over algebraically closed fields, and are simultaneously diagonalizable if individually diagonalizable.
:::
:::
