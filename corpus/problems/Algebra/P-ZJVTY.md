---
schema: qual/card@1
id: P-ZJVTY
kind: problem
title: $R^n/\im A$ is torsion iff $\operatorname{rank} A=n$ iff the Smith form of
  $A$ has $n$ nonzero invariant factors
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Smith Normal Form
  - Torsion
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
Let $R$ be a Principal Ideal Domain (PID) and let $A \in M_n(R)$ be an $n \times n$ matrix representing an $R$-module homomorphism $A: R^n \to R^n$.
Let $M = R^n / \operatorname{im}(A)$ be the cokernel module.
Prove that the following three conditions are equivalent:
(1) $M = R^n / \operatorname{im}(A)$ is a **torsion module** (every element of $M$ is annihilated by some non-zero $r \in R$).
(2) The matrix rank of $A$ is $\operatorname{rank}_R(A) = n$ (equivalently, $\det(A) \ne 0$).
(3) The Smith Normal Form of $A$ has exactly $n$ non-zero invariant factors $d_1, d_2, \dots, d_n \ne 0$.
:::

::: {.solution}
Take Smith normal form
\[
PAQ=\operatorname{diag}(d_1,\dots,d_n),
\qquad P,Q\in\operatorname{GL}_n(R),
\]
with $d_1\mid\cdots\mid d_n$, allowing some $d_i=0$. Then
\[
M=R^n/\operatorname{im}A
\cong\bigoplus_{i=1}^n R/(d_i),
\]
where $R/(0)=R$.

The module $R/(d_i)$ is torsion exactly when $d_i\ne0$: if $d_i\ne0$, the element $d_i$ annihilates the whole quotient; if $d_i=0$, the summand is a copy of the torsion-free module $R$. Hence
\[
M\text{ is torsion}
\iff d_i\ne0\text{ for every }i.
\]

Let $K=\operatorname{Frac}(R)$. Since $P,Q$ remain invertible over $K$,
\[
\operatorname{rank}A
=\operatorname{rank}_K\operatorname{diag}(d_1,\dots,d_n),
\]
which is the number of nonzero $d_i$. Therefore
\[
\operatorname{rank}A=n
\iff d_i\ne0\text{ for every }i.
\]
Because $R$ is a domain,
\[
\det A\ne0
\iff \prod_i d_i\ne0
\iff d_i\ne0\text{ for every }i.
\]
Thus the three conditions are equivalent.
:::
