---
schema: qual/card@1
id: E-AMD-FAT34AQV
kind: exercise
title: Diagonalizable versus distinct eigenvalues
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Does diagonalizable imply distinct eigenvalues?
:::

::: solution
**Goal:** Determine whether diagonalizability of a linear operator or matrix implies that its eigenvalues are all distinct.

<1>1. Answer:
    **No**, diagonalizability does not imply that the eigenvalues are distinct.

<1>2. Counterexample:
    *Proof:*
    <2>1. Consider the $n \times n$ identity matrix $I_n$ for $n \ge 2$ (or any scalar matrix $c I_n$ with $c \in F$):
        $$I_n = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} \in M_n(F).$$
    <2>2. The matrix $I_n$ is already diagonal, hence trivially diagonalizable (with change-of-basis matrix $P = I_n$).
    <2>3. The characteristic polynomial is $p(x) = \det(x I_n - I_n) = (x - 1)^n$.
    <2>4. The unique eigenvalue of $I_n$ is $\lambda = 1$, which has algebraic multiplicity $n \ge 2$.
    <2>5. Because there is only 1 distinct eigenvalue for an $n \times n$ matrix with $n \ge 2$, the eigenvalues are not distinct.

<1>3. Distinction between the two implications:
    *Proof:*
    <2>1. **Distinct eigenvalues $\implies$ diagonalizable:** If an $n \times n$ matrix over a field $F$ has $n$ pairwise distinct eigenvalues in $F$, the corresponding eigenvectors are linearly independent, providing an eigenbasis for $F^n$, so the matrix is diagonalizable.
    <2>2. **Diagonalizable $\not\implies$ distinct eigenvalues:** Diagonalizability requires only that the algebraic multiplicity equals the geometric multiplicity for each eigenvalue (and that the characteristic polynomial splits), which permits repeated eigenvalues as long as each eigenspace $E_\lambda$ has $\dim(E_\lambda)$ equal to the algebraic multiplicity of $\lambda$.

<1>4. Conclusion:
    Diagonalizability does not imply distinct eigenvalues. Q.E.D.
:::
