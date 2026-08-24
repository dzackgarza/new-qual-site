---
schema: qual/card@1
id: P-APAS13B
kind: problem
title: Unique Hermitian splitting $A=S+iT$ and eigenvalue real/imaginary bounds
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
---

::: problem
(a) Prove that every $A\in M_n$ may be written uniquely as $A=S+iT$, where $S$ and $T$ are Hermitian.

(b) For any $A\in M_n$, consider the unique expansion $A=S+iT$, where $S$ and $T$ are Hermitian.
Prove that for any $\lambda\in\operatorname{eig}(A)$, it holds that
\[
\lambda_n(S)\le\operatorname{Re}(\lambda)\le\lambda_1(S)
\quad\text{and}\quad
\lambda_n(T)\le\operatorname{Im}(\lambda)\le\lambda_1(T),
\]
where, by convention, the eigenvalues of a Hermitian matrix $C\in M_n$ are arranged in nonincreasing order, i.e.,
\[
\lambda_1(C)\ge\lambda_2(C)\ge\cdots\ge\lambda_n(C).
\]
:::
