---
schema: qual/card@1
id: E-AMD-FN5JCFZP
kind: problem
title: Cayley-Hamilton theorem
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove the Cayley-Hamilton theorem.
:::

::: {.solution}
Let
\[
p(t)=\det(tI-A)=c_0+c_1t+\cdots+c_nt^n.
\]
Over the polynomial ring \(R[t]\), the adjugate identity gives
\[
(tI-A)\operatorname{adj}(tI-A)=p(t)I.
\]
Write
\[
\operatorname{adj}(tI-A)=B_0+B_1t+\cdots+B_{n-1}t^{n-1},
\qquad B_i\in M_n(R).
\]
Comparing coefficients of powers of \(t\) yields
\[
-AB_0=c_0I,
\]
\[
B_{k-1}-AB_k=c_kI\qquad(1\le k\le n-1),
\]
and
\[
B_{n-1}=c_nI.
\]
Multiply these equations respectively by
\[
I,A,A^2,\ldots,A^{n-1},A^n
\]
on the left and add them. The terms involving the \(B_i\) telescope, leaving
\[
0=c_0I+c_1A+\cdots+c_nA^n=p(A).
\]
Therefore
\[
\boxed{p(A)=0},
\]
which is the Cayley--Hamilton theorem.
:::
