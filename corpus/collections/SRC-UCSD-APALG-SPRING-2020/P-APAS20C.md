---
schema: qual/card@1
id: P-APAS20C
kind: problem
title: Positive definiteness of $\phi-t\psi$ via the smallest eigenvalue of $\psi^{-1/2}\phi\psi^{-1/2}$
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Hermitian Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $V$ be an inner product space of dimension $n$, and $\phi,\psi\colon V\to V$ two positive definite Hermitian maps.
You may use without proof that $\psi$ has a unique positive definite square root $\psi^{1/2}$, and that $\psi$ and $\psi^{1/2}$ are non-singular.

Let $t\in\mathbb{R}$ be a real number.
Prove that $\phi-t\psi$ is positive definite if and only if $t<\lambda_n(\theta)$ (i.e., the smallest eigenvalue of $\theta$) where $\theta=\psi^{-1/2}\phi\psi^{-1/2}$.
:::

::: {.solution}
<1>1. $\phi - t\psi$ is positive definite iff $\psi^{-1/2}(\phi - t\psi)\psi^{-1/2}$ is positive definite.
::: {.proof}
conjugating by the invertible $\psi^{-1/2}$ preserves positive definiteness (it is a congruence).
:::

<1>2. $\psi^{-1/2}(\phi - t\psi)\psi^{-1/2} = \psi^{-1/2}\phi\psi^{-1/2} - t\psi^{-1/2}\psi\psi^{-1/2} = \theta - tI$.
::: {.proof}
<1>1, expanding.
:::

<1>3. $\theta$ is positive definite Hermitian (it is a congruence of the positive definite $\phi$), so it is diagonalizable with positive eigenvalues $\lambda_1 \ge \cdots \ge \lambda_n > 0$.
::: {.proof}
$\theta = \psi^{-1/2}\phi\psi^{-1/2}$ is Hermitian and positive definite.
:::

<1>4. $\theta - tI$ is positive definite iff all its eigenvalues are positive, i.e. iff $\lambda_i - t > 0$ for all $i$.
::: {.proof}
<1>3 (the eigenvalues of $\theta - tI$ are $\lambda_i - t$).
:::

<1>5. This holds iff $t < \lambda_i$ for all $i$, i.e. iff $t < \lambda_n$ (the smallest eigenvalue).
::: {.proof}
<1>4.
:::

<1>6. Hence $\phi - t\psi$ is positive definite iff $t < \lambda_n(\theta)$.
::: {.proof}
<1>1, <1>2, <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
