---
schema: qual/card@1
id: P-APAF04A
kind: problem
title: 'Cayley–Hamilton theorem'
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Minimal and Characteristic Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
State and prove the Cayley-Hamilton Theorem.
(You may use the Schur Decomposition Theorem.)
:::

::: {.solution}
<1>1. **Cayley--Hamilton Theorem.** Let $A\in M_n(\mathbb C)$ and let
\[
p_A(t)=\det(tI_n-A)
\]
be its characteristic polynomial. Then
\[
p_A(A)=0.
\]
::: {.proof}
We prove this using Schur decomposition, as allowed by the problem.
:::

<1>2. By Schur decomposition there is a unitary matrix $U$ such that
\[
T=U^*AU
\]
is upper triangular. If its diagonal entries are $\lambda_1,\ldots,\lambda_n$, then
\[
p_A(t)=p_T(t)=\prod_{j=1}^n(t-\lambda_j).
\]
::: {.proof}
Similarity preserves characteristic polynomials:
\[
\det(tI-U^*AU)
=\det\bigl(U^*(tI-A)U\bigr)
=\det(tI-A).
\]
For an upper-triangular matrix, the determinant is the product of the diagonal entries, so
\[
\det(tI-T)=\prod_{j=1}^n(t-\lambda_j).
\]
:::

<1>3. Let
\[
V_j=\operatorname{span}\{e_1,\ldots,e_j\},
\qquad V_0=0.
\]
Then $T(V_j)\subseteq V_j$, and
\[
(T-\lambda_j I)V_j\subseteq V_{j-1}
\qquad(1\le j\le n).
\]
::: {.proof}
Upper triangularity means that for each $j$,
\[
Te_j\in \operatorname{span}\{e_1,\ldots,e_j\}=V_j,
\]
so every $V_j$ is $T$-invariant.
Moreover the coefficient of $e_j$ in $Te_j$ is the diagonal entry $\lambda_j$, hence
\[
(T-\lambda_jI)e_j\in V_{j-1}.
\]
For $i<j$, both $Te_i$ and $\lambda_j e_i$ lie in $V_{j-1}$, so
\[
(T-\lambda_jI)V_{j-1}\subseteq V_{j-1}.
\]
Together these statements give $(T-\lambda_jI)V_j\subseteq V_{j-1}$.
:::

<1>4. The operator
\[
\prod_{j=1}^n(T-\lambda_jI)
\]
is zero.
::: {.proof}
All factors are polynomials in $T$, hence commute. We may therefore apply them in the order
\[
(T-\lambda_nI),\ (T-\lambda_{n-1}I),\ldots,(T-\lambda_1I).
\]
Starting with $V_n=\mathbb C^n$, <1>3 gives successively
\[
V_n\xrightarrow{T-\lambda_nI}V_{n-1}
\xrightarrow{T-\lambda_{n-1}I}V_{n-2}
\longrightarrow\cdots\longrightarrow
V_1\xrightarrow{T-\lambda_1I}V_0=0.
\]
Thus the product annihilates every vector in $\mathbb C^n$.
:::

<1>5. Hence $p_T(T)=0$, and therefore $p_A(A)=0$.
::: {.proof}
By <1>2 and <1>4,
\[
p_T(T)=\prod_{j=1}^n(T-\lambda_jI)=0.
\]
Since $A=UTU^*$, polynomial evaluation commutes with similarity:
\[
p_A(A)=p_T(A)=U\,p_T(T)\,U^*=0.
\]
This proves the Cayley--Hamilton theorem.
:::
:::
