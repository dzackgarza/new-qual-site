---
schema: qual/card@1
id: P-UCLAB07S-03
kind: problem
title: Solution space of a second-order linear recurrence
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Let $\mathcal S$ be the vector space of real sequences $(a_0,a_1,a_2,\ldots)$.
For fixed $A,B\in\mathbb R$, prove that the set of sequences satisfying
\[
x_{n+2}=Ax_{n+1}+Bx_n\qquad(n\ge0)
\]
is a two-dimensional linear subspace of $\mathcal S$.
:::

::: {.solution}
Let
\[
W
\subseteq
\mathcal S
\]
be the set of sequences satisfying the recurrence
\[
x_{n+2}
=
Ax_{n+1}
+
Bx_n
\]
for every
\[
n\ge0.
\]

<1>1. The zero sequence belongs to $W$.

::: {.proof}
For the zero sequence,
\[
x_n=0
\]
for every $n$, and hence
\[
x_{n+2}
=0
=
A\cdot0+B\cdot0
=
Ax_{n+1}+Bx_n.
\]
:::

<1>2. The set $W$ is closed under addition.

::: {.proof}
Let
\[
x=(x_n)
\quad\text{and}\quad
y=(y_n)
\]
belong to $W$.
Then for every $n$,
\[
x_{n+2}
=
Ax_{n+1}+Bx_n
\]
and
\[
y_{n+2}
=
Ay_{n+1}+By_n.
\]
Adding gives
\[
\begin{aligned}
(x+y)_{n+2}
&=
x_{n+2}+y_{n+2}\\
&=
A(x_{n+1}+y_{n+1})
+
B(x_n+y_n)\\
&=
A(x+y)_{n+1}
+
B(x+y)_n.
\end{aligned}
\]
Thus
\[
x+y\in W.
\]
:::

<1>3. The set $W$ is closed under scalar multiplication.

::: {.proof}
Let
\[
x=(x_n)\in W
\]
and
\[
c\in\mathbb R.
\]
Then
\[
\begin{aligned}
(cx)_{n+2}
&=
cx_{n+2}\\
&=
c(Ax_{n+1}+Bx_n)\\
&=
A(cx_{n+1})
+
B(cx_n)\\
&=
A(cx)_{n+1}
+
B(cx)_n.
\end{aligned}
\]
Hence
\[
cx\in W.
\]
:::

<1>4. Therefore $W$ is a linear subspace of $\mathcal S$.

::: {.proof}
Steps <1>1--<1>3 verify that $W$ contains zero and is closed under addition and scalar multiplication.
:::

<1>5. Define
\[
\Phi:W\to\mathbb R^2
\]
by
\[
\Phi(x)
=
(x_0,x_1).
\]
Then $\Phi$ is linear.

::: {.proof}
Taking the first two coordinates is linear:
\[
\Phi(cx+dy)
=
(cx_0+dy_0,cx_1+dy_1)
=
c\Phi(x)+d\Phi(y).
\]
:::

<1>6. The map $\Phi$ is injective.

::: {.proof}
Suppose
\[
\Phi(x)=\Phi(y).
\]
Then
\[
x_0=y_0,
\qquad
x_1=y_1.
\]
The recurrence determines every later term from the preceding two.
Indeed, if
\[
x_n=y_n
\qquad\text{and}\qquad
x_{n+1}=y_{n+1},
\]
then
\[
\begin{aligned}
x_{n+2}
&=
Ax_{n+1}+Bx_n\\
&=
Ay_{n+1}+By_n\\
&=
y_{n+2}.
\end{aligned}
\]
By induction,
\[
x_n=y_n
\]
for every $n$.
Thus
\[
x=y.
\]
:::

<1>7. The map $\Phi$ is surjective.

::: {.proof}
Let
\[
(u,v)\in\mathbb R^2.
\]
Define a sequence recursively by
\[
x_0=u,
\qquad
x_1=v,
\]
and
\[
x_{n+2}
=
Ax_{n+1}+Bx_n
\]
for
\[
n\ge0.
\]
This defines a real sequence
\[
x=(x_n)
\]
belonging to $W$ and satisfying
\[
\Phi(x)=(u,v).
\]
Hence every element of $\mathbb R^2$ lies in the image.
:::

<1>8. Therefore
\[
W\cong\mathbb R^2.
\]

::: {.proof}
By steps <1>5--<1>7, $\Phi$ is a linear bijection.
Hence it is a vector-space isomorphism.
:::

<1>9. Consequently
\[
\boxed{\dim W=2}.
\]

::: {.proof}
Isomorphic finite-dimensional vector spaces have the same dimension.
Since
\[
\dim\mathbb R^2=2,
\]
step <1>8 gives
\[
\dim W=2.
\]
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>4 proves that the recurrence solutions form a linear subspace of $\mathcal S$, and step <1>9 proves that this subspace is two-dimensional.
:::
:::
