---
schema: qual/card@1
id: P-ALGF18B
kind: problem
title: 'Matrices of $p$-power order in characteristic $p$: unipotence and failure of $g^p=I$'
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: 'Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2018 source. Part (b) is false as printed: p=2, n=3 admits a unipotent Jordan block of order 4.'
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Frobenius-power nilpotence argument and the explicit GL_3(F_2) counterexample to part (b).
---

::: problem
Suppose $p$ is a prime which is at most $n$, and $F$ is a field of characteristic $p$.
Suppose $g \in \mathrm{GL}_n(F)$ and $g^{p^m} = I$ for some positive integer $m$.

(a) Prove that $g - I$ is a nilpotent matrix.

(b) Prove that $g^p = I$.
:::

::: {.remark}
Part (b) is false as stated. A counterexample satisfying all printed hypotheses is given in the solution below.
:::

::: {.solution}
<1>1. The matrix $g-I$ is nilpotent.
::: {.proof}
In characteristic $p$, commuting elements satisfy
\[
(X-Y)^p=X^p-Y^p.
\]
Since $g$ commutes with $I$, iterating this identity $m$ times gives
\[
(g-I)^{p^m}=g^{p^m}-I.
\]
The hypothesis $g^{p^m}=I$ therefore yields
\[
(g-I)^{p^m}=0.
\]
Hence $g-I$ is nilpotent, proving part (a).
:::

<1>2. The conclusion $g^p=I$ in part (b) does not follow from the stated hypotheses.
::: {.proof}
Take
\[
p=2,
\qquad
n=3,
\qquad
F=\mathbb F_2,
\]
and set
\[
N=
\begin{pmatrix}
0&1&0\\
0&0&1\\
0&0&0
\end{pmatrix},
\qquad
g=I+N.
\]
The matrix $g$ is upper triangular with diagonal entries $1$, so
\[
g\in\operatorname{GL}_3(\mathbb F_2).
\]
Moreover,
\[
N^2=
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0
\end{pmatrix}
\neq0,
\qquad
N^3=0.
\]
Because the characteristic is $2$,
\[
g^2=(I+N)^2=I+N^2\neq I.
\]
On the other hand,
\[
g^4=(g^2)^2=(I+N^2)^2=I+N^4=I.
\]
Thus $g^{2^2}=I$ while $g^2\neq I$, and the hypotheses hold because
\[
p=2\le3=n.
\]
This disproves part (b) as printed.
:::
:::
