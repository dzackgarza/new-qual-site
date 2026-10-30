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
(i) State the Cayley--Hamilton theorem for matrices $A\in M_n(\CC)$.

(ii) Prove the theorem directly for diagonalizable matrices.

(iii) Identify $M_n(\CC)$ with $\CC^{n^2}$ via a fixed linear isomorphism and give it the Euclidean metric.

Using the fact that the diagonalizable matrices are dense in $M_n(\CC)$, together with (ii), prove the Cayley--Hamilton theorem for arbitrary complex matrices.
:::

::: {.solution}
For $A\in M_n(\CC)$, write
$$
\chi_A(t)=\det(tI-A)
$$
for its characteristic polynomial.

::: pf

::: {.pf-step #p2-s1}

The Cayley--Hamilton theorem states that
$$
\boxed{\chi_A(A)=0}
$$
for every $A\in M_n(\CC)$.

::: pf-proof

This is the theorem to be proved.

:::

:::

::: {.pf-step #p2-s2}

Suppose $A$ is diagonalizable. Then there are an invertible matrix $S$ and a diagonal matrix
$$
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
$$
such that
$$
A=SDS^{-1}.
$$

::: pf-proof

This is the definition of diagonalizability over $\CC$.

:::

:::

::: {.pf-step #p2-s3}

If $A$ is diagonalizable as in step [](#p2-s2){.pf-ref}, then
$$
\chi_A(t)=\prod_{j=1}^n(t-\lambda_j).
$$

::: pf-proof

Similarity preserves the characteristic polynomial:
$$
\begin{aligned}
\chi_A(t)
&=
\det(tI-SDS^{-1})\\
&=
\det\bigl(S(tI-D)S^{-1}\bigr)\\
&=
\det(tI-D).
\end{aligned}
$$
Since $D$ is diagonal,
$$
\det(tI-D)
=
\prod_{j=1}^n(t-\lambda_j).
$$

:::

:::

::: {.pf-step #p2-s4}

If $A$ is diagonalizable, then
$$
\chi_A(A)=0.
$$

::: pf-proof

By step [](#p2-s3){.pf-ref}, every diagonal entry $\lambda_j$ of $D$ is a root of $\chi_A$. Therefore
$$
\chi_A(D)
=
\operatorname{diag}\bigl(
\chi_A(\lambda_1),\ldots,\chi_A(\lambda_n)
\bigr)
=0.
$$
For every polynomial $p$,
$$
p(SDS^{-1})
=
Sp(D)S^{-1}.
$$
Applying this with $p=\chi_A$ gives
$$
\chi_A(A)
=
S\chi_A(D)S^{-1}
=0.
$$
This proves Cayley--Hamilton for diagonalizable matrices.

:::

:::

::: {.pf-step #p2-s5}

Under the standard identification
$$
M_n(\CC)\cong\CC^{n^2},
$$
the coefficients of $\chi_A(t)$ depend continuously on the entries of $A$.

::: pf-proof

Expanding
$$
\det(tI-A)
$$
by the Leibniz formula expresses every coefficient of $t^k$ as a polynomial in the entries of $A$. Polynomial functions on $\CC^{n^2}$ are continuous.

:::

:::

::: {.pf-step #p2-s6}

The map
$$
F:M_n(\CC)\to M_n(\CC),
\qquad
F(A)=\chi_A(A),
$$
is continuous.

::: pf-proof

Write
$$
\chi_A(t)
=
t^n+c_{n-1}(A)t^{n-1}+\cdots+c_0(A),
$$
where each coefficient function $c_j(A)$ is continuous by step [](#p2-s5){.pf-ref}.
Then
$$
F(A)
=
A^n+c_{n-1}(A)A^{n-1}+\cdots+c_0(A)I.
$$
Matrix multiplication, matrix addition, and scalar multiplication are polynomial, hence continuous, operations on the finite-dimensional vector space $M_n(\CC)$. Therefore $F$ is continuous.

:::

:::

::: {.pf-step #p2-s7}

Let $A\in M_n(\CC)$. There is a sequence of diagonalizable matrices $(A_m)$ such that
$$
A_m\to A.
$$

::: pf-proof

This is exactly the density hypothesis supplied in the problem: the set of diagonalizable matrices is dense in $M_n(\CC)$ with its Euclidean metric.

:::

:::

::: {.pf-step #p2-s8}

For every $m$,
$$
F(A_m)=0.
$$

::: pf-proof

Each $A_m$ is diagonalizable, so step [](#p2-s4){.pf-ref} gives
$$
\chi_{A_m}(A_m)=0.
$$
By definition, this is $F(A_m)=0$.

:::

:::

::: {.pf-step #p2-s9}

For the arbitrary matrix $A$ from step [](#p2-s7){.pf-ref},
$$
F(A)=0.
$$

::: pf-proof

By continuity of $F$ from step [](#p2-s6){.pf-ref} and convergence $A_m\to A$,
$$
F(A)
=
F\left(\lim_{m\to\infty}A_m\right)
=
\lim_{m\to\infty}F(A_m).
$$
By step [](#p2-s8){.pf-ref}, every term on the right is zero. Hence
$$
F(A)=0.
$$

:::

:::

::: {.pf-step #p2-s10}

Therefore every complex matrix satisfies its characteristic polynomial:
$$
\boxed{\chi_A(A)=0}.
$$

::: pf-proof

The matrix $A$ in steps [](#p2-s7){.pf-ref}, [](#p2-s8){.pf-ref} and [](#p2-s9){.pf-ref} was arbitrary. Thus step [](#p2-s9){.pf-ref} proves the Cayley--Hamilton theorem for all $A\in M_n(\CC)$.

:::

:::

::: pf-qed

Step [](#p2-s1){.pf-ref} states the theorem, step [](#p2-s4){.pf-ref} proves it for diagonalizable matrices, and steps [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref}, [](#p2-s7){.pf-ref}, [](#p2-s8){.pf-ref}, [](#p2-s9){.pf-ref} and [](#p2-s10){.pf-ref} extend it to all matrices using density and continuity.

:::

:::

:::
