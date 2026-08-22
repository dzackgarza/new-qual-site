---
schema: qual/card@1
id: P-APAF21B
kind: problem
title: Rayleigh quotient minimum; unique Hermitian splitting and eigenvalue real/imaginary bounds
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
relations: []
review: draft
solved: false
---

::: problem
Assume that the eigenvalues of a Hermitian matrix $A\in M_n$ are arranged in the order
\[
\lambda_n(A)\le\cdots\le\lambda_2(A)\le\lambda_1(A).
\]

(a) Let $A\in M_n$ be Hermitian. Prove that
\[
\lambda_n=\min_{x\neq 0}\frac{x^HAx}{x^Hx}.
\]

(b) Prove that every $A\in M_n$ may be written uniquely as $A=S+iT$, where $S$ and $T$ are Hermitian.

(c) For any $A\in M_n$, consider the unique expansion $A=S+iT$, where $S$ and $T$ are Hermitian. Prove that for any $\lambda\in\operatorname{eig}(A)$, it holds that
\[
\lambda_n(S)\le\operatorname{Re}(\lambda)\le\lambda_1(S)
\quad\text{and}\quad
\lambda_n(T)\le\operatorname{Im}(\lambda)\le\lambda_1(T).
\]
:::
