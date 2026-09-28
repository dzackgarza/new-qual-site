---
schema: qual/card@1
id: P-BKF98-5
kind: problem
title: A homogeneous function with bilinear polarization is a quadratic form
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
    Evaluated the bilinear polarization on the diagonal to obtain
    g(x,x)=2f(x), then represented the bilinear form g/2 by a matrix in the
    standard basis.
---

::: {.problem}
Let $f:\mathbb R^n\to\mathbb R$ satisfy:

1. The function
\[
g(x,y)=f(x+y)-f(x)-f(y)
\]
is bilinear.

2. For every $x\in\mathbb R^n$ and $t\in\mathbb R$,
\[
f(tx)=t^2f(x).
\]

Show that there is a linear transformation $A:\mathbb R^n\to\mathbb R^n$ such that
\[
f(x)=\langle x,Ax\rangle
\]
for the usual inner product.
:::

::: {.solution}
Let
$$
e_1,\ldots,e_n
$$
be the standard basis of $\RR^n$.

<1>1. One has
$$
f(0)=0.
$$

::: {.proof}
Apply the homogeneity hypothesis with $t=0$:
$$
f(0)
=
f(0x)
=
0^2f(x)
=0.
$$
:::

<1>2. For every $x\in\RR^n$,
$$
g(x,x)=2f(x).
$$

::: {.proof}
By definition,
$$
g(x,x)
=
f(2x)-2f(x).
$$
The homogeneity hypothesis with $t=2$ gives
$$
f(2x)=4f(x).
$$
Therefore
$$
g(x,x)
=
4f(x)-2f(x)
=
2f(x).
$$
:::

<1>3. Define the real matrix
$$
A=(a_{ij})
$$
by
$$
a_{ij}
\coloneqq
\frac12g(e_i,e_j).
$$
Then $A$ defines a linear transformation
$$
A:\RR^n\longrightarrow\RR^n.
$$

::: {.proof}
Every real $n\times n$ matrix defines a linear endomorphism of $\RR^n$ in
the standard basis.
:::

<1>4. For every $x\in\RR^n$,
$$
\langle x,Ax\rangle
=
\frac12g(x,x).
$$

::: {.proof}
Write
$$
x=\sum_{i=1}^n x_i e_i.
$$
Then
$$
\begin{aligned}
\langle x,Ax\rangle
&=
\sum_{i,j=1}^n x_i a_{ij}x_j\\
&=
\frac12
\sum_{i,j=1}^n
x_ix_jg(e_i,e_j).
\end{aligned}
$$
Since $g$ is bilinear,
$$
\sum_{i,j=1}^n
x_ix_jg(e_i,e_j)
=
g(x,x).
$$
This gives the identity.
:::

<1>5. For every $x\in\RR^n$,
$$
\boxed{
f(x)=\langle x,Ax\rangle
}.
$$

::: {.proof}
Step <1>2 gives
$$
f(x)=\frac12g(x,x),
$$
and step <1>4 identifies the right side with
$\langle x,Ax\rangle$.
:::

<1>6. Q.E.D.

::: {.proof}
The linear transformation constructed in step <1>3 has the required
property by step <1>5.
:::
:::
