---
schema: qual/card@1
id: P-HH3JN
kind: problem
title: Spectral theorem for real symmetric matrices
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}

Prove that every real symmetric matrix $A \in M_n(\RR)$ has real eigenvalues and can be orthogonally diagonalized: there exists an orthogonal matrix $Q \in O(n)$ such that $Q^T A Q = \diag(\lambda_1, \ldots, \lambda_n)$ (the real spectral theorem).

:::

::: {.solution}

Let $A=A^T\in M_n(\RR)$, and let $\inner{v}{w}=v^Tw$ be the standard inner product on $\RR^n$.

::: pf

::: {.pf-step #real}

Every eigenvalue of $A$ is real.

::: pf-proof

Regard $A$ as a complex matrix, and let $Av=\lambda v$ with $\lambda\in\CC$ and $0\ne v\in\CC^n$. Then $v^*Av=\lambda v^*v$. Because $A^*=A$, the scalar $v^*Av$ is real: $\overline{v^*Av}=v^*A^*v=v^*Av$. Since $v^*v>0$, $\lambda$ is real.

:::

:::

::: {.pf-step #eigenvector}

If $n\ge1$, then $A$ has a unit eigenvector $u_1\in\RR^n$.

::: pf-proof

The characteristic polynomial of $A$ has a root $\lambda_1\in\CC$, which is real by step [](#real){.pf-ref}. Then $A-\lambda_1I$ is a singular real matrix, so it has a nonzero kernel vector in $\RR^n$; normalize it.

:::

:::

::: {.pf-step #invariant}

If $Au_1=\lambda_1u_1$, then $W=u_1^\perp$ is $A$-invariant, and $A$ restricted to $W$ is symmetric with respect to $\inner{\cdot}{\cdot}$.

::: pf-proof

For $w\in W$,
$$
\inner{Aw}{u_1}=\inner{w}{Au_1}=\lambda_1\inner{w}{u_1}=0,
$$
so $Aw\in W$. The identity $\inner{Aw}{w'}=\inner{w}{Aw'}$ holds for all $w,w'\in\RR^n$, in particular on $W$.

:::

:::

::: pf-step

$\RR^n$ has an orthonormal basis $u_1,\ldots,u_n$ of eigenvectors of $A$, and with $Q=[u_1\ \cdots\ u_n]$ we have $Q^TQ=I$ and $Q^TAQ=\diag(\lambda_1,\ldots,\lambda_n)$.

::: pf-proof

We argue by induction on $n$; the case $n=1$ is immediate. For $n>1$, take $u_1$ from step [](#eigenvector){.pf-ref}. By step [](#invariant){.pf-ref} and induction applied to the symmetric operator $A|_W$ on the $(n-1)$-dimensional inner product space $W$, $W$ has an orthonormal basis $u_2,\ldots,u_n$ of eigenvectors of $A$. Together with $u_1$ this is an orthonormal eigenbasis of $\RR^n$. Orthonormality gives $Q^TQ=I$, and $AQ=Q\diag(\lambda_1,\ldots,\lambda_n)$ gives the diagonalization.

:::

:::

:::

:::
