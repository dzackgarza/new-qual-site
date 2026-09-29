---
schema: qual/card@1
id: P-BKS11-4B
kind: problem
title: Convergence of the matrix series $\sum x^nA^n$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2011 solution PDF and independently reviewed the eigenvalue criterion.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked diagonalizability, sufficiency of the two scalar geometric series, and divergence on and outside the spectral-radius boundary.
---

::: {.problem}
For which real numbers x does the matrix-valued series $\sum _ { n = 0 } ^ { \infty } x ^ { n } A ^ { n }$ converge, where A is the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$?
:::

::: {.solution}
Write
$$
A=
\begin{pmatrix}
0&1\\
1&1
\end{pmatrix}.
$$

::: pf

::: {.pf-step #eigenvalues}
The eigenvalues of $A$ are
$$
\lambda_+
\coloneqq
\frac{1+\sqrt5}{2}
$$
and
$$
\lambda_-
\coloneqq
\frac{1-\sqrt5}{2}.
$$

::: pf-proof
The characteristic polynomial is
$$
\det(tI-A)
=
t^2-t-1.
$$
Its two roots are the displayed numbers.
:::

:::

::: {.pf-step #diagonalizable}
The matrix $A$ is diagonalizable over $\RR$.

::: pf-proof
The two eigenvalues in step [](#eigenvalues){.pf-ref} are distinct and real. Therefore $A$ has
a basis of real eigenvectors.
:::

:::

::: {.pf-step #convergence-region}
If
$$
\abs{x}
<
\frac{\sqrt5-1}{2},
$$
then
$$
\sum_{n=0}^{\infty}x^nA^n
$$
converges.

::: pf-proof
By step [](#diagonalizable){.pf-ref}, choose an invertible real matrix $P$ such that
$$
P^{-1}AP
=
\begin{pmatrix}
\lambda_+&0\\
0&\lambda_-
\end{pmatrix}.
$$
Then
$$
x^nA^n
=
P
\begin{pmatrix}
(x\lambda_+)^n&0\\
0&(x\lambda_-)^n
\end{pmatrix}
P^{-1}.
$$
Now
$$
\frac{1}{\lambda_+}
=
\frac{\sqrt5-1}{2},
$$
and
$$
\abs{\lambda_-}
=
\frac{\sqrt5-1}{2}
<
\lambda_+.
$$
Thus the displayed hypothesis implies
$$
\abs{x\lambda_+}<1
\qquad\text{and}\qquad
\abs{x\lambda_-}<1.
$$
Both diagonal scalar geometric series converge, so conjugating their
sum by the fixed matrices $P$ and $P^{-1}$ gives convergence of the
matrix series.
:::

:::

::: {.pf-step #divergence-region}
If
$$
\abs{x}
\geq
\frac{\sqrt5-1}{2},
$$
then the matrix series diverges.

::: pf-proof
Let $v\neq0$ be an eigenvector for $\lambda_+$. If the matrix series
converged, its terms would tend to the zero matrix, and therefore
$$
x^nA^nv
=
(x\lambda_+)^n v
\longrightarrow0.
$$
This is impossible when
$$
\abs{x\lambda_+}\geq1.
$$
Since
$$
\frac1{\lambda_+}
=
\frac{\sqrt5-1}{2},
$$
the stated lower bound on $\abs{x}$ is exactly this divergent regime.
:::

:::

::: {.pf-step #exact-interval}
The series converges exactly for
$$
\boxed{
-\frac{\sqrt5-1}{2}
<
x
<
\frac{\sqrt5-1}{2}
}.
$$

::: pf-proof
Step [](#convergence-region){.pf-ref} proves convergence throughout the displayed interval, and step
[](#divergence-region){.pf-ref} proves divergence at every real point outside it, including both
endpoints.
:::

:::

::: pf-qed
Step [](#exact-interval){.pf-ref} gives precisely the requested set of real numbers.
:::

:::

:::
