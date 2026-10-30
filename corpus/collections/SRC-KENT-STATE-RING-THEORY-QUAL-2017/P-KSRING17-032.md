---
schema: qual/card@1
id: P-KSRING17-032
kind: problem
title: The Vandermonde determinant
classification:
  areas: [algebra]
  topics:
  - Vandermonde Determinant
  - Polynomial Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 32 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $D$ be an integral domain and let $D[x_{1}, x_{2}, \ldots, x_{n}]$ be the polynomial ring over $D$ in the $n$ indeterminates $x_{1}, x_{2}, \ldots, x_{n}$. Let
$$
V = \begin{bmatrix} x_{1}^{n-1} & \cdots & x_{1}^{2} & x_{1} & 1 \\ x_{2}^{n-1} & \cdots & x_{2}^{2} & x_{2} & 1 \\ \vdots & & \vdots & \vdots & \vdots \\ x_{n}^{n-1} & \cdots & x_{n}^{2} & x_{n} & 1 \end{bmatrix}.
$$
Prove that the determinant of $V$ is $\prod_{1 \leqslant i < j \leqslant n} (x_{i} - x_{j})$.
:::

::: {.solution}

We prove by induction on $n$ that
$$
\boxed{
\det V
=
\prod_{1\le i<j\le n}(x_i-x_j).
}
$$

::: pf

::: {.pf-step #s1-1}

The formula holds for $n=1$.


::: pf-proof

For $n=1$,
$$
V=[1],
$$
so
$$
\det V=1.
$$
The product over
$$
1\le i<j\le1
$$
is empty and therefore equals $1$.

:::

:::

::: {.pf-step #s1-2}

Assume the formula holds for size $n-1$.
Regard
$$
\det V
$$
as a polynomial in $x_1$ with coefficients in
$$
A
\coloneqq
D[x_2,\ldots,x_n].
$$
Then
$$
\deg_{x_1}(\det V)\le n-1.
$$


::: pf-proof

Only the first row of $V$ contains $x_1$, and its entries are
$$
x_1^{n-1},
x_1^{n-2},
\ldots,
x_1,
1.
$$
Expanding the determinant along the first row shows that the highest possible power of $x_1$ is
$$
x_1^{n-1}.
$$

:::

:::

::: {.pf-step #s1-3}

For every
$$
j\in\{2,\ldots,n\},
$$
the polynomial $\det V$ vanishes when
$$
x_1=x_j.
$$


::: pf-proof

After substituting
$$
x_1=x_j,
$$
the first row of $V$ becomes identical to the $j$th row. A determinant with two equal rows is zero.

:::

:::

::: {.pf-step #s1-4}

The product
$$
\prod_{j=2}^{n}(x_1-x_j)
$$
divides $\det V$ in
$$
A[x_1].
$$


::: pf-proof

By step [](#s1-3){.pf-ref} and the polynomial remainder theorem,
$$
x_1-x_2
$$
divides $\det V$. Write
$$
\det V
=
(x_1-x_2)Q_2(x_1).
$$

Now substitute
$$
x_1=x_3.
$$
By step [](#s1-3){.pf-ref},
$$
0
=
(x_3-x_2)Q_2(x_3).
$$
The coefficient ring
$$
A=D[x_2,\ldots,x_n]
$$
is an integral domain because $D$ is an integral domain, and
$$
x_3-x_2\ne0.
$$
Hence
$$
Q_2(x_3)=0.
$$
Thus
$$
x_1-x_3
$$
divides $Q_2$.

Repeating this argument successively for
$$
x_4,\ldots,x_n
$$
gives
$$
\prod_{j=2}^{n}(x_1-x_j)
\mid
\det V.
$$

:::

:::

::: {.pf-step #s1-5}

There exists
$$
C\in A
$$
such that
$$
\det V
=
C
\prod_{j=2}^{n}(x_1-x_j).
$$


::: pf-proof

The divisor from step [](#s1-4){.pf-ref} has degree exactly
$$
n-1
$$
in $x_1$, while step [](#s1-2){.pf-ref} gives
$$
\deg_{x_1}\det V\le n-1.
$$
Therefore the quotient is independent of $x_1$ and lies in $A$.

:::

:::

::: {.pf-step #s1-6}

The coefficient $C$ from step [](#s1-5){.pf-ref} is
$$
\det V_{n-1}(x_2,\ldots,x_n),
$$
the determinant of the same reversed-column Vandermonde matrix of size $n-1$.


::: pf-proof

The product
$$
\prod_{j=2}^{n}(x_1-x_j)
$$
is monic in $x_1$ of degree $n-1$. Hence $C$ is the coefficient of
$$
x_1^{n-1}
$$
in $\det V$.

Expanding $\det V$ along the first row, the only term contributing
$$
x_1^{n-1}
$$
comes from the first entry of that row. Its cofactor sign is
$$
(-1)^{1+1}=1,
$$
and its minor is
$$
\begin{pmatrix}
x_2^{n-2}&\cdots&x_2&1\\
\vdots&&\vdots&\vdots\\
x_n^{n-2}&\cdots&x_n&1
\end{pmatrix}.
$$
Thus $C$ is exactly the determinant of the size-$(n-1)$ matrix of the same form.

:::

:::

::: {.pf-step #s1-7}

By the induction hypothesis,
$$
C
=
\prod_{2\le i<j\le n}(x_i-x_j).
$$


::: pf-proof

Apply the induction hypothesis to the matrix in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\det V
=
\prod_{1\le i<j\le n}(x_i-x_j).
$$


::: pf-proof

Substitute step [](#s1-7){.pf-ref} into step [](#s1-5){.pf-ref}:
$$
\begin{aligned}
\det V
&=
\left(
\prod_{2\le i<j\le n}(x_i-x_j)
\right)
\left(
\prod_{j=2}^{n}(x_1-x_j)
\right)\\
&=
\prod_{1\le i<j\le n}(x_i-x_j).
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the base case, and steps [](#s1-2){.pf-ref} through [](#s1-8){.pf-ref} prove the induction step.

:::

:::

:::
