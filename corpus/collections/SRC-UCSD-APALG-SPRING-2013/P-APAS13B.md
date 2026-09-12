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

::: solution
For part (a), define
\[
S=\frac{A+A^H}{2},\qquad T=\frac{A-A^H}{2i}.
\]
Then
\[
S^H=\frac{A^H+A}{2}=S,
\]
and, since \(\overline{i}=-i\),
\[
T^H=\frac{A^H-A}{-2i}=\frac{A-A^H}{2i}=T.
\]
Thus both \(S\) and \(T\) are Hermitian, and
\[
S+iT
 =\frac{A+A^H}{2}+\frac{A-A^H}{2}
 =A.
\]

To prove uniqueness, suppose also \(A=S_1+iT_1\) with \(S_1,T_1\) Hermitian. Taking Hermitian transposes gives
\[
A^H=S_1-iT_1.
\]
Adding and subtracting the two identities yields
\[
S_1=\frac{A+A^H}{2}=S,
\qquad
T_1=\frac{A-A^H}{2i}=T.
\]
Hence the decomposition is unique.

For part (b), let \(Av=\lambda v\) with \(v\neq0\). Then
\[
v^HAv=\lambda\,v^Hv.
\]
Using \(A=S+iT\),
\[
\lambda
 =\frac{v^HSv}{v^Hv}+i\frac{v^HTv}{v^Hv}.
\]
Because \(S\) and \(T\) are Hermitian, the two Rayleigh quotients on the right are real. Therefore
\[
\operatorname{Re}(\lambda)=\frac{v^HSv}{v^Hv},
\qquad
\operatorname{Im}(\lambda)=\frac{v^HTv}{v^Hv}.
\]

If \(C\) is Hermitian with eigenvalues
\(\lambda_1(C)\ge\cdots\ge\lambda_n(C)\), the spectral theorem gives an orthonormal eigenbasis. Writing \(v=\sum_j c_j u_j\),
\[
\frac{v^HCv}{v^Hv}
 =\frac{\sum_j |c_j|^2\lambda_j(C)}{\sum_j |c_j|^2},
\]
which is a convex combination of the eigenvalues. Hence
\[
\lambda_n(C)\le \frac{v^HCv}{v^Hv}\le \lambda_1(C).
\]
Applying this first to \(C=S\) and then to \(C=T\) gives
\[
\lambda_n(S)\le\operatorname{Re}(\lambda)\le\lambda_1(S),
\qquad
\lambda_n(T)\le\operatorname{Im}(\lambda)\le\lambda_1(T).
\]
:::
