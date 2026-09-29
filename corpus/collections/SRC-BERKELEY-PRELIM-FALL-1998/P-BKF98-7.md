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

::: pf

::: {.pf-step #A-diagonalization}
Suppose $A$ is positive semidefinite. Then there is an orthogonal
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

::: pf-proof
This is the spectral theorem for real symmetric matrices. Positive
semidefiniteness makes every eigenvalue nonnegative.
:::

:::

::: {.pf-step #C-psd-nonneg-diagonal}
If $B$ is real symmetric positive semidefinite, then
$$
C\coloneqq Q^TBQ
$$
is positive semidefinite and
$$
c_{ii}\geq0
$$
for every $i$.

::: pf-proof
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

:::

::: {.pf-step #trace-nonneg-forward}
If $A$ and $B$ are positive semidefinite, then
$$
\operatorname{tr}(AB)\geq0.
$$

::: pf-proof
By cyclic invariance of trace and steps [](#A-diagonalization){.pf-ref} and [](#C-psd-nonneg-diagonal){.pf-ref},
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
Every term is nonnegative by steps [](#A-diagonalization){.pf-ref} and [](#C-psd-nonneg-diagonal){.pf-ref}.
:::

:::

::: {.pf-step #Bx-psd}
Conversely, suppose
$$
\operatorname{tr}(AB)\geq0
$$
for every real symmetric positive semidefinite matrix $B$. For each
$x\in\RR^n$, the matrix
$$
B_x\coloneqq xx^T
$$
is positive semidefinite.

::: pf-proof
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

:::

::: {.pf-step #trace-ABx-equals-quadratic}
For every $x\in\RR^n$,
$$
\operatorname{tr}(AB_x)
=
x^TAx.
$$

::: pf-proof
Using cyclic invariance of trace,
$$
\operatorname{tr}(Axx^T)
=
\operatorname{tr}(x^TAx).
$$
The quantity $x^TAx$ is a $1\times1$ matrix, whose trace is itself.
:::

:::

::: {.pf-step #A-psd-converse}
The matrix $A$ is positive semidefinite.

::: pf-proof
By the hypothesis and step [](#Bx-psd){.pf-ref},
$$
\operatorname{tr}(AB_x)\geq0
$$
for every $x$. Step [](#trace-ABx-equals-quadratic){.pf-ref} therefore gives
$$
x^TAx\geq0
$$
for every $x\in\RR^n$, which is the definition of positive
semidefiniteness.
:::

:::

::: pf-qed
Step [](#trace-nonneg-forward){.pf-ref} proves the forward implication and step [](#A-psd-converse){.pf-ref} proves the converse.
:::

:::

:::
