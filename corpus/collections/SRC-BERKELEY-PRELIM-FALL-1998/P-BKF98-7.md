---
schema: qual/card@1
id: P-BKF98-7
kind: problem
title: $A$ is positive semidefinite iff $\operatorname{tr}(AB)\ge0$ for all positive semidefinite $B$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    In one direction diagonalized A and paired its nonnegative eigenvalues
    with nonnegative diagonal entries of an orthogonal conjugate of B. In
    the converse direction used rank-one tests B=xx^T.
---

::: {.problem}
A real symmetric $n\times n$ matrix $A$ is positive semidefinite if
\[
x^TAx\ge0
\qquad\text{for all }x\in\mathbb R^n.
\]
Prove that $A$ is positive semidefinite if and only if
\[
\operatorname{tr}(AB)\ge0
\]
for every real symmetric positive semidefinite $n\times n$ matrix $B$.
:::

::: {.solution}
<1>1. Suppose $A$ is positive semidefinite. Then there is an orthogonal
matrix $Q$ and nonnegative real numbers
$$
\lambda_1,\ldots,\lambda_n
$$
such that
$$
Q^TAQ
=
\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
$$

::: {.proof}
This is the spectral theorem for real symmetric matrices. Positive
semidefiniteness makes every eigenvalue nonnegative.
:::

<1>2. If $B$ is real symmetric positive semidefinite, then
$$
C\coloneqq Q^TBQ
$$
is positive semidefinite and
$$
c_{ii}\geq0
$$
for every $i$.

::: {.proof}
For every $y\in\RR^n$,
$$
y^TCy
=
(Qy)^TB(Qy)
\geq0.
$$
Thus $C$ is positive semidefinite. Taking $y=e_i$ gives
$$
c_{ii}=e_i^TCe_i\geq0.
$$
:::

<1>3. If $A$ and $B$ are positive semidefinite, then
$$
\operatorname{tr}(AB)\geq0.
$$

::: {.proof}
By cyclic invariance of trace and steps <1>1--<1>2,
$$
\begin{aligned}
\operatorname{tr}(AB)
&=
\operatorname{tr}(Q^TABQ)\\
&=
\operatorname{tr}
\left(
\operatorname{diag}(\lambda_1,\ldots,\lambda_n)C
\right)\\
&=
\sum_{i=1}^n\lambda_i c_{ii}.
\end{aligned}
$$
Every term is nonnegative by steps <1>1 and <1>2.
:::

<1>4. Conversely, suppose
$$
\operatorname{tr}(AB)\geq0
$$
for every real symmetric positive semidefinite matrix $B$. For each
$x\in\RR^n$, the matrix
$$
B_x\coloneqq xx^T
$$
is positive semidefinite.

::: {.proof}
The matrix $B_x$ is symmetric, and for every $y\in\RR^n$,
$$
y^TB_xy
=
y^Txx^Ty
=
(x^Ty)^2
\geq0.
$$
:::

<1>5. For every $x\in\RR^n$,
$$
\operatorname{tr}(AB_x)
=
x^TAx.
$$

::: {.proof}
Using cyclic invariance of trace,
$$
\operatorname{tr}(Axx^T)
=
\operatorname{tr}(x^TAx).
$$
The quantity $x^TAx$ is a $1\times1$ matrix, whose trace is itself.
:::

<1>6. The matrix $A$ is positive semidefinite.

::: {.proof}
By the hypothesis and step <1>4,
$$
\operatorname{tr}(AB_x)\geq0
$$
for every $x$. Step <1>5 therefore gives
$$
x^TAx\geq0
$$
for every $x\in\RR^n$, which is the definition of positive
semidefiniteness.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves the forward implication and step <1>6 proves the converse.
:::
:::
