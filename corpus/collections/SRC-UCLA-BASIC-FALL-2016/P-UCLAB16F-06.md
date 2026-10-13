---
schema: qual/card@1
id: P-UCLAB16F-06
kind: problem
title: Rational eigenvectors for a rational eigenvalue
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Let A be an invertible $n \times n$ matrix whose entries belong to $\mathbb { Q }$ the set of rational numbers.
Suppose that $A v = 3 v$ for a vector $v \in \mathbb { R } ^ { n }$ (i) Give an example in which no non-zero scalar multiple λv for $\lambda \in \mathbb { R }$ is in $\mathbb { Q } ^ { n }$ (ii) Show that there is always a non-zero $w \in \mathbb { Q } ^ { n }$ such that $A w = 3 w$
:::

::: {.solution}
<1>1. For part (i), take
\[
n=2,
\qquad
A=3I_2,
\qquad
v=
\begin{pmatrix}
1\\
\sqrt2
\end{pmatrix}.
\]
Then
\[
Av=3v.
\]

::: {.proof}
Since
\[
A=3I_2,
\]
one has
\[
Av=3v
\]
for every vector $v\in\mathbb R^2$.
The matrix $A$ is invertible and has rational entries.
:::

<1>2. For the vector in step <1>1, no nonzero real scalar multiple belongs to
\[
\mathbb Q^2.
\]

::: {.proof}
Suppose
\[
\lambda
\begin{pmatrix}
1\\
\sqrt2
\end{pmatrix}
\in
\mathbb Q^2.
\]
Then the first coordinate gives
\[
\lambda\in\mathbb Q.
\]
If $\lambda\ne0$, the second coordinate
\[
\lambda\sqrt2
\]
would be rational.
Dividing by the nonzero rational number $\lambda$ would imply
\[
\sqrt2\in\mathbb Q,
\]
a contradiction.
Thus only $\lambda=0$ gives a rational vector.
:::

<1>3. For part (ii), the equation
\[
Aw=3w
\]
is equivalent to
\[
(A-3I)w=0.
\]

::: {.proof}
Rearrange the eigenvalue equation:
\[
Aw-3w=0.
\]
:::

<1>4. The matrix
\[
A-3I
\]
 has rational entries.

::: {.proof}
The entries of $A$ are rational by hypothesis, and the diagonal entries of $3I$ are rational.
Their difference therefore has rational entries.
:::

<1>5. The real nullspace
\[
\ker_{\mathbb R}(A-3I)
\]
is nonzero.

::: {.proof}
The given vector $v$ satisfies
\[
(A-3I)v=0.
\]
Since $v$ is an eigenvector, it is nonzero.
Thus the real nullspace is nontrivial.
:::

<1>6. A rational matrix with nontrivial real nullspace has a nonzero rational null vector.

::: {.proof}
Let $M$ be a matrix with rational entries and suppose
\[
\ker_{\mathbb R}M\ne\{0\}.
\]
Perform Gaussian elimination on $M$ using rational row operations.
The resulting reduced row-echelon matrix still has rational entries.

Since the real nullspace is nonzero, the homogeneous system has at least one free variable.
Set one free variable equal to $1$, all other free variables equal to $0$, and solve for the pivot variables.
Because all coefficients in the reduced system are rational, every pivot variable obtained in this way is rational.
Thus the resulting vector is a nonzero element of
\[
\mathbb Q^n
\]
lying in the nullspace.
:::

<1>7. There exists
\[
0\ne w\in\mathbb Q^n
\]
such that
\[
Aw=3w.
\]

::: {.proof}
Apply step <1>6 to
\[
M=A-3I.
\]
Step <1>4 gives rational entries and step <1>5 gives nontrivial real nullspace.
Hence there is
\[
0\ne w\in\mathbb Q^n
\]
with
\[
(A-3I)w=0.
\]
By step <1>3, this is equivalent to
\[
Aw=3w.
\]
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 give the example required in part (i), and steps <1>3--<1>7 prove part (ii).
:::
:::
