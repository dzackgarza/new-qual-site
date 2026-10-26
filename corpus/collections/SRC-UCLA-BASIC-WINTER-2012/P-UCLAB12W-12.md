---
schema: qual/card@1
id: P-UCLAB12W-12
kind: problem
title: Equivalence of two binary quadratic forms over the real and complex numbers
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Recall that quadratic forms $Q_1(x,y)$ and $Q_2(x',y')$ are equivalent if they are related by a nonsingular change of coordinates $(x,y)\mapsto(x',y')$.

Decide whether
\[
Q_1=xy,
\qquad
Q_2=x^2+y^2
\]
are equivalent over $\mathbb C$ and whether they are equivalent over $\mathbb R$.
If not, prove that they are not.
If yes, find the matrix of a change of coordinates.
:::

::: pf

::: pf-step

Over $\CC$, define the change of coordinates
$$
\binom{x'}{y'}
=
\begin{pmatrix}
1&i\\
1&-i
\end{pmatrix}
\binom{x}{y},
$$
so that
$$
x'=x+iy,
\qquad
y'=x-iy.
$$
This change of coordinates is nonsingular.


::: pf-proof

The determinant of the change-of-coordinates matrix is
$$
\det
\begin{pmatrix}
1&i\\
1&-i
\end{pmatrix}
=-i-i=-2i\ne0.
$$
Hence the matrix is invertible over $\CC$.

:::

:::

::: pf-step

Under the change of coordinates in step <1>1,
$$
Q_1(x',y')=Q_2(x,y).
$$


::: pf-proof

Directly,
$$
Q_1(x',y')
=x'y'
=(x+iy)(x-iy)
=x^2+y^2
=Q_2(x,y).
$$
Thus the two forms are equivalent over $\CC$.

:::

:::

::: pf-step

The real quadratic form $Q_1(x,y)=xy$ has a nonzero isotropic vector.


::: pf-proof

For example,
$$
Q_1(1,0)=0,
$$
while $(1,0)\ne(0,0)$.

:::

:::

::: pf-step

The real quadratic form $Q_2(x,y)=x^2+y^2$ has no nonzero isotropic vector.


::: pf-proof

If
$$
x^2+y^2=0
$$
with $x,y\in\RR$, then both nonnegative summands must vanish. Hence $x=y=0$.

:::

:::

::: pf-step

An invertible real change of coordinates preserves whether a quadratic form has a nonzero isotropic vector.


::: pf-proof

Suppose quadratic forms $Q$ and $Q'$ satisfy
$$
Q'(v)=Q(Mv)
$$
for an invertible real matrix $M$. If $v\ne0$ and $Q'(v)=0$, then $Mv\ne0$ because $M$ is invertible, and
$$
Q(Mv)=0.
$$
Conversely, applying the same argument to $M^{-1}$ shows that a nonzero zero of $Q$ produces a nonzero zero of $Q'$. Thus the property is invariant under nonsingular coordinate changes.

:::

:::

::: pf-step

The forms $Q_1$ and $Q_2$ are not equivalent over $\RR$.


::: pf-proof

By step <1>3, $Q_1$ has a nonzero isotropic vector, while by step <1>4, $Q_2$ does not. Step <1>5 shows that equivalent real quadratic forms must agree on this property. Therefore no nonsingular real change of coordinates can relate them.

:::

:::

::: pf-step

Hence
$$
\boxed{
Q_1\sim Q_2\text{ over }\CC,
\qquad
Q_1\not\sim Q_2\text{ over }\RR.
}
$$


::: pf-proof

Complex equivalence is established in steps <1>1--<1>2, with explicit matrix
$$
\begin{pmatrix}
1&i\\
1&-i
\end{pmatrix}.
$$
Real inequivalence is step <1>6.

:::

:::

::: pf-qed

Step <1>7 gives both requested decisions and the required complex change-of-coordinates matrix.

:::

:::
