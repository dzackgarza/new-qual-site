---
schema: qual/card@1
id: P-BERK84S-03
kind: problem
title: Alternative theorem for strict linear inequalities
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
  note: Checked against Problem 3 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Restored the extraction-lost map arrow and the forced inequality range i=1,...,n from the surrounding source notation f=(f_1,...,f_n).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the hyperplane-annihilator argument and the explicit positive vector when the annihilating relation has both signs.
---

::: {.problem}
Let $f : \mathbb { R } ^ { m } \to \mathbb { R } ^ { n } , n \geqslant 2$ , be a linear transformation of rank $n - 1$ . Let $f ( v ) = ( f _ { 1 } ( v ) , f _ { 2 } ( v ) , \ldots , f _ { n } ( v ) )$ for $v \in \mathbb { R } ^ { m }$ . Show that a necessary and sufficient condition for the system of inequalities $f _ { i } ( v ) > 0 , i = 1 , \ldots , n$ , to have no solution is that there exist real numbers $\lambda _ { i } \geqslant 0$ , not all zero, such that

$$
\sum _ { i = 1 } ^ { n } \lambda _ { i } f _ { i } = 0 .
$$
:::


::: {.solution}
Let
\[
L=\operatorname{im}f\subseteq\mathbb R^n.
\]
Since $\operatorname{rank}f=n-1$, the subspace $L$ is a hyperplane.

<1>1. A nonzero linear relation among $f_1,\ldots,f_n$ is the same thing as a nonzero vector orthogonal to $L$.
::: {.proof}
For $\lambda=(\lambda_1,\ldots,\lambda_n)\in\mathbb R^n$,
\[
\sum_{i=1}^n\lambda_i f_i=0
\]
means that for every $v\in\mathbb R^m$,
\[
0=\sum_{i=1}^n\lambda_i f_i(v)
=\lambda\cdot f(v).
\]
Thus the relation holds exactly when $\lambda\in L^\perp$.
Because $\dim L=n-1$, the space $L^\perp$ is one-dimensional and contains a nonzero vector.
:::

<1>2. If there is a relation with $\lambda_i\ge0$ and not all $\lambda_i=0$, then the strict inequalities have no solution.
::: {.proof}
Suppose, toward a contradiction, that some $v$ satisfies
\[
f_i(v)>0\qquad(i=1,\ldots,n).
\]
Then
\[
\sum_{i=1}^n\lambda_i f_i(v)>0,
\]
because every summand is nonnegative and at least one coefficient $\lambda_i$ is positive. But the assumed relation gives
\[
\sum_{i=1}^n\lambda_i f_i(v)=0,
\]
a contradiction.
:::

<1>3. If the strict inequalities have no solution, then some nonzero vector in $L^\perp$ has all coordinates of one sign.
::: {.proof}
Choose $0\ne\lambda=(\lambda_1,\ldots,\lambda_n)\in L^\perp$.
Suppose that $\lambda$ has at least one positive coordinate and at least one negative coordinate. Put
\[
P=\{i:\lambda_i>0\},
\qquad
N=\{i:\lambda_i<0\},
\]
and define
\[
A=\sum_{i\in P}\lambda_i>0,
\qquad
B=-\sum_{i\in N}\lambda_i>0.
\]
Now define $y\in\mathbb R^n$ by
\[
y_i=
\begin{cases}
B,&i\in P,\\
A,&i\in N,\\
1,&\lambda_i=0.
\end{cases}
\]
Every coordinate of $y$ is strictly positive, and
\[
\lambda\cdot y
=B\sum_{i\in P}\lambda_i
+A\sum_{i\in N}\lambda_i
=BA-AB=0.
\]
Hence $y\in\lambda^\perp=L$, because both $L$ and $\lambda^\perp$ are hyperplanes and $L\subseteq\lambda^\perp$.
Therefore $y=f(v)$ for some $v\in\mathbb R^m$, and then every $f_i(v)=y_i$ is positive, contradicting the assumed infeasibility.

Thus $\lambda$ cannot have both positive and negative coordinates. Multiplying $\lambda$ by $-1$ if necessary, we may assume
\[
\lambda_i\ge0\qquad(i=1,\ldots,n).
\]
Since $\lambda\ne0$, the coefficients are not all zero.
:::

<1>4. The two conditions are equivalent.
::: {.proof}
By <1>1 and <1>3, infeasibility produces real numbers $\lambda_i\ge0$, not all zero, with
\[
\sum_{i=1}^n\lambda_i f_i=0.
\]
By <1>2, any such relation makes the strict system infeasible. Hence the stated condition is both necessary and sufficient.
:::
:::
