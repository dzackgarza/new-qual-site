---
schema: qual/card@1
id: P-2HERP
kind: problem
title: Eigenvalues of skew-symmetric matrices
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Matrices
  - Bilinear Forms
relations: []
review: draft
---

::: problem
What can you say about the eigenvalues of a real skew-symmetric matrix?
:::


::: {.solution}
Let $A\in M_n(\RR)$ satisfy $A^t=-A$. Regard $A$ as a complex matrix. If $Av=\lambda v$ for $0\ne v\in\CC^n$, then
\[
\lambda\langle v,v\rangle
=\langle Av,v\rangle
=-\langle v,Av\rangle
=-\overline\lambda\langle v,v\rangle.
\]
Hence
\[
\lambda=-\overline\lambda,
\]
so every complex eigenvalue of $A$ is purely imaginary (possibly $0$).

Because $A$ has real coefficients, nonzero eigenvalues occur in conjugate pairs
\[
i\mu,-i\mu\qquad(\mu\in\RR).
\]
In particular the only possible **real** eigenvalue is $0$. Therefore an odd-dimensional real skew-symmetric matrix is singular: its nonzero eigenvalues pair off, leaving $0$ as an eigenvalue.

Equivalently, $iA$ is Hermitian, so the spectral theorem gives a unitary diagonalization of $A$ over $\CC$ with purely imaginary diagonal entries.
:::
