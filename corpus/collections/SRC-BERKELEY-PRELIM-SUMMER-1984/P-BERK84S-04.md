---
schema: qual/card@1
id: P-BERK84S-04
kind: problem
title: Positive eigenvector of a positive 2-by-2 matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 4 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the larger eigenvalue formula and the explicit positive eigenvector (b, lambda_+-a).
---

::: {.problem}
Let

$$
A = { \binom { a b } { c d } }
$$

be a real matrix with $a , b , c , d > 0$ . Show that A has an eigenvector

$$
{ \binom { x } { y } } \in \mathbb { R } ^ { 2 }
$$

with x, $y > 0$
:::


::: {.solution}
Write
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad a,b,c,d>0.
\]
Its characteristic polynomial is
\[
p(\lambda)=\lambda^2-(a+d)\lambda+(ad-bc),
\]
so the larger eigenvalue is
\[
\lambda_+=\frac{a+d+\sqrt{(a-d)^2+4bc}}2.
\]

<1>1. One has $\lambda_+>a$.
::: {.proof}
Since $bc>0$,
\[
\sqrt{(a-d)^2+4bc}>|a-d|\ge a-d.
\]
Therefore
\[
\lambda_+-a
=\frac{d-a+\sqrt{(a-d)^2+4bc}}2>0.
\]
:::

<1>2. The vector $v=(b,\lambda_+-a)^T$ is a strictly positive eigenvector.
::: {.proof}
By hypothesis $b>0$, and by <1>1 also $\lambda_+-a>0$. Hence both coordinates of $v$ are strictly positive.

Moreover, since $\lambda_+$ is an eigenvalue,
\[
(a-\lambda_+)(d-\lambda_+)-bc=0,
\]
which is equivalent to
\[
c b+(d-\lambda_+)(\lambda_+-a)=0.
\]
Thus
\[
(A-\lambda_+I)
\begin{pmatrix}b\\ \lambda_+-a\end{pmatrix}
=
\begin{pmatrix}
(a-\lambda_+)b+b(\lambda_+-a)\\
cb+(d-\lambda_+)(\lambda_+-a)
\end{pmatrix}
=
\begin{pmatrix}0\\0\end{pmatrix}.
\]
Therefore
\[
A v=\lambda_+ v,
\]
with both coordinates of $v$ positive, as required.
:::
:::
