---
schema: qual/card@1
id: P-UCLAB12W-10
kind: problem
title: Determinant of the matrix exponential
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Let $A$ be a complex $n\times n$ matrix.
State and prove under which conditions on $A$ the identity
$$
\det(e^A)=\exp(\operatorname{tr}A)
$$
holds.
Here
$$
e^A=I+A+\frac{A^2}{2!}+\frac{A^3}{3!}+\cdots.
$$
You may assume that this series converges entrywise for every complex matrix $A$.
:::

::: {.solution}

The identity holds for every complex $n\times n$ matrix $A$; no additional condition is required.

::: pf

::: pf-step

There is an invertible matrix $S$ such that
$$
T=S^{-1}AS
$$
is upper triangular.


::: pf-proof

Proceed by induction on $n$. For $n=1$ the assertion is immediate. For $n>1$, the characteristic polynomial of $A$ has a root over $\CC$, so $A$ has a nonzero eigenvector. Extend it to a basis. In that basis, the matrix has block form
$$
\begin{pmatrix}
\lambda&*\\
0&C
\end{pmatrix}.
$$
By induction, after changing only the remaining $n-1$ basis vectors, the block $C$ becomes upper triangular. Hence the full matrix becomes upper triangular.

:::

:::

::: {.pf-step #s1-2}

Matrix exponentiation respects similarity:
$$
e^T=S^{-1}e^AS.
$$


::: pf-proof

Since $T=S^{-1}AS$, induction gives
$$
T^m=S^{-1}A^mS
$$
for every $m\ge0$. Therefore the convergent exponential series gives
$$
\begin{aligned}
e^T
&=\sum_{m=0}^{\infty}\frac{T^m}{m!}\\
&=\sum_{m=0}^{\infty}\frac{S^{-1}A^mS}{m!}\\
&=S^{-1}\left(\sum_{m=0}^{\infty}\frac{A^m}{m!}\right)S\\
&=S^{-1}e^AS.
\end{aligned}
$$
The entrywise convergence assumed in the problem permits multiplication by the fixed matrices $S^{-1}$ and $S$ term by term.

:::

:::

::: {.pf-step #s1-3}

If the diagonal entries of $T$ are
$$
\lambda_1,\ldots,\lambda_n,
$$
then $e^T$ is upper triangular with diagonal entries
$$
e^{\lambda_1},\ldots,e^{\lambda_n}.
$$


::: pf-proof

Every power $T^m$ is upper triangular. Its $j$-th diagonal entry is $\lambda_j^m$, because diagonal entries multiply under products of upper-triangular matrices. Hence the $j$-th diagonal entry of
$$
e^T=\sum_{m=0}^{\infty}\frac{T^m}{m!}
$$
is
$$
\sum_{m=0}^{\infty}\frac{\lambda_j^m}{m!}
=e^{\lambda_j}.
$$
A sum of upper-triangular matrices is upper triangular.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\det(e^T)=\exp(\operatorname{tr}T).
$$


::: pf-proof

By step [](#s1-3){.pf-ref} and the determinant formula for triangular matrices,
$$
\det(e^T)
=\prod_{j=1}^n e^{\lambda_j}
=e^{\lambda_1+\cdots+\lambda_n}.
$$
Since $T$ is upper triangular,
$$
\operatorname{tr}T=\lambda_1+\cdots+\lambda_n.
$$
Thus the displayed identity follows.

:::

:::

::: {.pf-step #s1-5}

Similarity preserves both determinant and trace, so
$$
\det(e^A)=\det(e^T)
\qquad\text{and}\qquad
\operatorname{tr}A=\operatorname{tr}T.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
e^T=S^{-1}e^AS,
$$
so multiplicativity of determinant gives
$$
\det(e^T)=\det(e^A).
$$
Also
$$
\operatorname{tr}(S^{-1}AS)
=\operatorname{tr}(ASS^{-1})
=\operatorname{tr}A,
$$
using $\operatorname{tr}(XY)=\operatorname{tr}(YX)$.

:::

:::

::: {.pf-step #s1-6}

Therefore, for every complex square matrix $A$,
$$
\boxed{\det(e^A)=\exp(\operatorname{tr}A)}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref}:
$$
\det(e^A)
=\det(e^T)
=\exp(\operatorname{tr}T)
=\exp(\operatorname{tr}A).
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the identity with no hypothesis beyond $A\in\Mat_n(\CC)$.

:::

:::

:::
