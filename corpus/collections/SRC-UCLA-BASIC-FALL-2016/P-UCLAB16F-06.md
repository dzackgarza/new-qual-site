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
Let $A$ be an invertible $n \times n$ matrix whose entries belong to $\QQ$, the set of rational numbers.
Suppose that $Av = 3v$ for a vector $v \in \RR^n$.

(i) Give an example in which no non-zero scalar multiple $\lambda v$ for $\lambda \in \RR$ is in $\QQ^n$.

(ii) Show that there is always a non-zero $w \in \QQ^n$ such that $Aw = 3w$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (i), take
$$
n=2,
\qquad
A=3I_2,
\qquad
v=
\begin{pmatrix}
1\\
\sqrt2
\end{pmatrix}.
$$
Then
$$
Av=3v.
$$


::: pf-proof

Since
$$
A=3I_2,
$$
one has
$$
Av=3v
$$
for every vector $v\in\RR^2$.
The matrix $A$ is invertible and has rational entries.

:::

:::

::: {.pf-step #s1-2}

For the vector in step [](#s1-1){.pf-ref}, no nonzero real scalar multiple belongs to
$$
\QQ^2.
$$


::: pf-proof

Suppose
$$
\lambda
\begin{pmatrix}
1\\
\sqrt2
\end{pmatrix}
\in
\QQ^2.
$$
Then the first coordinate gives
$$
\lambda\in\QQ.
$$
If $\lambda\ne0$, the second coordinate
$$
\lambda\sqrt2
$$
would be rational.
Dividing by the nonzero rational number $\lambda$ would imply
$$
\sqrt2\in\QQ,
$$
a contradiction.
Thus only $\lambda=0$ gives a rational vector.

:::

:::

::: {.pf-step #s1-3}

For part (ii), the equation
$$
Aw=3w
$$
is equivalent to
$$
(A-3I)w=0.
$$


::: pf-proof

Rearrange the eigenvalue equation:
$$
Aw-3w=0.
$$

:::

:::

::: {.pf-step #s1-4}

The matrix
$$
A-3I
$$
 has rational entries.


::: pf-proof

The entries of $A$ are rational by hypothesis, and the diagonal entries of $3I$ are rational.
Their difference therefore has rational entries.

:::

:::

::: {.pf-step #s1-5}

The real nullspace
$$
\ker_{\RR}(A-3I)
$$
is nonzero.


::: pf-proof

The given vector $v$ satisfies
$$
(A-3I)v=0.
$$
Since $v$ is an eigenvector, it is nonzero.
Thus the real nullspace is nontrivial.

:::

:::

::: {.pf-step #s1-6}

A rational matrix with nontrivial real nullspace has a nonzero rational null vector.


::: pf-proof

Let $M$ be a matrix with rational entries and suppose
$$
\ker_{\RR}M\ne\{0\}.
$$
Perform Gaussian elimination on $M$ using rational row operations.
The resulting reduced row-echelon matrix still has rational entries.

Since the real nullspace is nonzero, the homogeneous system has at least one free variable.
Set one free variable equal to $1$, all other free variables equal to $0$, and solve for the pivot variables.
Because all coefficients in the reduced system are rational, every pivot variable obtained in this way is rational.
Thus the resulting vector is a nonzero element of
$$
\QQ^n
$$
lying in the nullspace.

:::

:::

::: {.pf-step #s1-7}

There exists
$$
0\ne w\in\QQ^n
$$
such that
$$
Aw=3w.
$$


::: pf-proof

Apply step [](#s1-6){.pf-ref} to
$$
M=A-3I.
$$
Step [](#s1-4){.pf-ref} gives rational entries and step [](#s1-5){.pf-ref} gives nontrivial real nullspace.
Hence there is
$$
0\ne w\in\QQ^n
$$
with
$$
(A-3I)w=0.
$$
By step [](#s1-3){.pf-ref}, this is equivalent to
$$
Aw=3w.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give the example required in part (i), and steps [](#s1-3){.pf-ref} through [](#s1-7){.pf-ref} prove part (ii).

:::

:::

:::
