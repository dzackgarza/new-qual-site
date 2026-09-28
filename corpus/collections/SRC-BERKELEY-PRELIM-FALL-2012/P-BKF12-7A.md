---
schema: qual/card@1
id: P-BKF12-7A
kind: problem
title: Invertibility and inverse of $I_n+aJ_n$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 7A in the retained Fall 2012 Berkeley prelim exam
    and its retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the eigenspace decomposition of J_n and the explicit inverse
    using J_n^2=nJ_n.
---

::: {.problem}
Let $I_n$ denote the $n\times n$ identity matrix, and let $J_n$ be
the $n\times n$ matrix with all entries equal to $1$. Determine for
which real numbers $a$ the matrix $I_n+aJ_n$ is invertible, and find
its inverse.
:::

::: {.solution}
Let
$$
\mathbf 1=(1,\ldots,1)^T\in\RR^n
$$
and
$$
W\coloneqq
\left\{x=(x_1,\ldots,x_n)^T\in\RR^n:
\sum_{j=1}^n x_j=0\right\}.
$$

<1>1. One has
$$
J_n\mathbf1=n\mathbf1,
\qquad
J_nx=0
\quad(x\in W),
$$
and
$$
\RR^n=\operatorname{span}(\mathbf1)\oplus W.
$$

::: {.proof}
Every row of $J_n$ has $n$ entries equal to $1$, so
$J_n\mathbf1=n\mathbf1$. For arbitrary $x\in\RR^n$, every coordinate
of $J_nx$ equals $\sum_jx_j$; hence $J_nx=0$ for $x\in W$.

The functional $x\mapsto\sum_jx_j$ is nonzero, so $W$ has dimension
$n-1$. Since $\mathbf1\notin W$, the displayed sum is direct and has
dimension $n$.
:::

<1>2. The matrix $I_n+aJ_n$ acts by the scalar $1+an$ on
$\operatorname{span}(\mathbf1)$ and by the scalar $1$ on $W$.

::: {.proof}
Step <1>1 gives
$$
(I_n+aJ_n)\mathbf1=(1+an)\mathbf1.
$$
If $x\in W$, then step <1>1 gives
$$
(I_n+aJ_n)x=x.
$$
:::

<1>3. The matrix $I_n+aJ_n$ is invertible exactly when
$$
a\ne-\frac1n.
$$

::: {.proof}
By step <1>2 and the direct-sum decomposition in step <1>1, the only
two eigenvalues are $1+an$ on the all-ones line and $1$ on $W$.
Thus the map is invertible exactly when $1+an\ne0$.
:::

<1>4. One has
$$
J_n^2=nJ_n.
$$

::: {.proof}
Every entry of $J_n^2$ is the sum of $n$ products $1\cdot1$, and
therefore equals $n$. This is exactly the matrix $nJ_n$.
:::

<1>5. If $a\ne-1/n$, then
$$
\boxed{
(I_n+aJ_n)^{-1}
=I_n-\frac{a}{1+na}J_n
}.
$$

::: {.proof}
Put
$$
b=-\frac{a}{1+na}.
$$
Using step <1>4,
$$
\begin{aligned}
(I_n+aJ_n)(I_n+bJ_n)
&=I_n+(a+b)J_n+abJ_n^2\\
&=I_n+(a+b+nab)J_n.
\end{aligned}
$$
The chosen $b$ satisfies
$$
a+b+nab=0,
$$
so the product is $I_n$. The two matrices commute, so the reverse
product is also $I_n$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>3 gives the complete invertibility condition, and step <1>5
gives the inverse whenever it exists.
:::
:::
