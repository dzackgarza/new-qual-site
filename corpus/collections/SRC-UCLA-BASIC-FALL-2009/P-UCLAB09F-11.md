---
schema: qual/card@1
id: P-UCLAB09F-11
kind: problem
title: Cayley-Hamilton from the dense diagonalizable locus
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
<1>1. State the Cayley--Hamilton theorem for matrices $A\in M_n(\mathbb C)$.

<1>2. Prove the theorem directly for diagonalizable matrices.

<1>3. Identify $M_n(\mathbb C)$ with $\mathbb C^{n^2}$ via a fixed linear isomorphism and give it the Euclidean metric.
Using the fact that the diagonalizable matrices are dense in $M_n(\mathbb C)$, together with <1>2, prove the Cayley--Hamilton theorem for arbitrary complex matrices.
:::

::: {.solution}
For $A\in M_n(\mathbb C)$, write
\[
\chi_A(t)=\det(tI-A)
\]
for its characteristic polynomial.

<1>1. The Cayley--Hamilton theorem states that
\[
\boxed{\chi_A(A)=0}
\]
for every $A\in M_n(\mathbb C)$.

::: {.proof}
This is the theorem to be proved.
:::

<1>2. Suppose $A$ is diagonalizable. Then there are an invertible matrix $S$ and a diagonal matrix
\[
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
\]
such that
\[
A=SDS^{-1}.
\]

::: {.proof}
This is the definition of diagonalizability over $\mathbb C$.
:::

<1>3. If $A$ is diagonalizable as in step <1>2, then
\[
\chi_A(t)=\prod_{j=1}^n(t-\lambda_j).
\]

::: {.proof}
Similarity preserves the characteristic polynomial:
\[
\begin{aligned}
\chi_A(t)
&=
\det(tI-SDS^{-1})\\
&=
\det\bigl(S(tI-D)S^{-1}\bigr)\\
&=
\det(tI-D).
\end{aligned}
\]
Since $D$ is diagonal,
\[
\det(tI-D)
=
\prod_{j=1}^n(t-\lambda_j).
\]
:::

<1>4. If $A$ is diagonalizable, then
\[
\chi_A(A)=0.
\]

::: {.proof}
By step <1>3, every diagonal entry $\lambda_j$ of $D$ is a root of $\chi_A$. Therefore
\[
\chi_A(D)
=
\operatorname{diag}\bigl(
\chi_A(\lambda_1),\ldots,\chi_A(\lambda_n)
\bigr)
=0.
\]
For every polynomial $p$,
\[
p(SDS^{-1})
=
Sp(D)S^{-1}.
\]
Applying this with $p=\chi_A$ gives
\[
\chi_A(A)
=
S\chi_A(D)S^{-1}
=0.
\]
This proves Cayley--Hamilton for diagonalizable matrices.
:::

<1>5. Under the standard identification
\[
M_n(\mathbb C)\cong\mathbb C^{n^2},
\]
the coefficients of $\chi_A(t)$ depend continuously on the entries of $A$.

::: {.proof}
Expanding
\[
\det(tI-A)
\]
by the Leibniz formula expresses every coefficient of $t^k$ as a polynomial in the entries of $A$. Polynomial functions on $\mathbb C^{n^2}$ are continuous.
:::

<1>6. The map
\[
F:M_n(\mathbb C)\to M_n(\mathbb C),
\qquad
F(A)=\chi_A(A),
\]
is continuous.

::: {.proof}
Write
\[
\chi_A(t)
=
t^n+c_{n-1}(A)t^{n-1}+\cdots+c_0(A),
\]
where each coefficient function $c_j(A)$ is continuous by step <1>5.
Then
\[
F(A)
=
A^n+c_{n-1}(A)A^{n-1}+\cdots+c_0(A)I.
\]
Matrix multiplication, matrix addition, and scalar multiplication are polynomial, hence continuous, operations on the finite-dimensional vector space $M_n(\mathbb C)$. Therefore $F$ is continuous.
:::

<1>7. Let $A\in M_n(\mathbb C)$. There is a sequence of diagonalizable matrices $(A_m)$ such that
\[
A_m\to A.
\]

::: {.proof}
This is exactly the density hypothesis supplied in the problem: the set of diagonalizable matrices is dense in $M_n(\mathbb C)$ with its Euclidean metric.
:::

<1>8. For every $m$,
\[
F(A_m)=0.
\]

::: {.proof}
Each $A_m$ is diagonalizable, so step <1>4 gives
\[
\chi_{A_m}(A_m)=0.
\]
By definition, this is $F(A_m)=0$.
:::

<1>9. For the arbitrary matrix $A$ from step <1>7,
\[
F(A)=0.
\]

::: {.proof}
By continuity of $F$ from step <1>6 and convergence $A_m\to A$,
\[
F(A)
=
F\left(\lim_{m\to\infty}A_m\right)
=
\lim_{m\to\infty}F(A_m).
\]
By step <1>8, every term on the right is zero. Hence
\[
F(A)=0.
\]
:::

<1>10. Therefore every complex matrix satisfies its characteristic polynomial:
\[
\boxed{\chi_A(A)=0}.
\]

::: {.proof}
The matrix $A$ in steps <1>7--<1>9 was arbitrary. Thus step <1>9 proves the Cayley--Hamilton theorem for all $A\in M_n(\mathbb C)$.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>1 states the theorem, step <1>4 proves it for diagonalizable matrices, and steps <1>5--<1>10 extend it to all matrices using density and continuity.
:::
:::
