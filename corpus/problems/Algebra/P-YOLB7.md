---
schema: qual/card@1
id: P-YOLB7
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
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
State and prove the Cayley–Hamilton Theorem for an $n \times n$ matrix $A$ over a commutative ring $R$.
:::

::: solution
Let
\[
p(t)=\det(tI-A)=t^n+c_{n-1}t^{n-1}+\cdots+c_0.
\]
Over the commutative ring $R[t]$, the adjugate identity gives
\[
(tI-A)\operatorname{adj}(tI-A)=p(t)I.
\]
Write
\[
\operatorname{adj}(tI-A)=B_{n-1}t^{n-1}+\cdots+B_0,
\qquad B_i\in M_n(R).
\]
Comparing coefficients of powers of $t$ yields
\[
B_{n-1}=I,
\]
\[
B_{k-1}-AB_k=c_kI\qquad(1\le k\le n-1),
\]
and
\[
-AB_0=c_0I.
\]
Multiply these identities successively by the appropriate powers of $A$ and add. All terms involving the $B_i$ telescope, leaving
\[
A^n+c_{n-1}A^{n-1}+\cdots+c_0I=0.
\]
Thus
\[
\boxed{p(A)=0},
\]
which is the Cayley--Hamilton theorem over any commutative ring.
:::
