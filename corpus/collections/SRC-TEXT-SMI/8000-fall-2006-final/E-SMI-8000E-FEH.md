---
schema: qual/card@1
id: E-SMI-8000E-FEH
kind: problem
title: Proof choice — spectral theorem or Cayley-Hamilton
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both proof choices with Smith Math 8000 Fall 2006 final part H."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Chose Cayley--Hamilton over a commutative field and proved it from the adjugate identity by coefficient comparison."
---

::: {.exercise}
Prove one:

(i) Every real symmetric matrix is orthogonally diagonalizable;

or

(ii) The Cayley-Hamilton theorem.
Say what your hypotheses are.
:::

::: solution
We prove option (ii). Let $F$ be a commutative field and
$A\in M_n(F)$. Write
$$
\chi_A(t)=\det(tI-A)=t^n+c_{n-1}t^{n-1}+\cdots+c_0.
$$
The Cayley--Hamilton theorem asserts
$$
\boxed{\chi_A(A)=0.}
$$

<1>1. Expand the adjugate identity over $F[t]$.
::: proof
Write
$$
\operatorname{adj}(tI-A)=B_{n-1}t^{n-1}+\cdots+B_0.
$$
Then
$$
(tI-A)\operatorname{adj}(tI-A)=\chi_A(t)I.
$$
Comparing coefficients gives
$$
B_{n-1}=I,
$$
$$
B_{k-1}-AB_k=c_kI\qquad(1\le k\le n-1),
$$
and
$$
-AB_0=c_0I.
$$
:::

<1>2. Solve the recurrence and conclude.
::: proof
Starting from $B_{n-1}=I$ and descending through the recurrence gives
$$
B_0=A^{n-1}+c_{n-1}A^{n-2}+\cdots+c_1I.
$$
Substituting this into $-AB_0=c_0I$ yields
$$
A^n+c_{n-1}A^{n-1}+\cdots+c_1A+c_0I=0.
$$
This is exactly
$$
\boxed{\chi_A(A)=0.}
$$
:::
:::
