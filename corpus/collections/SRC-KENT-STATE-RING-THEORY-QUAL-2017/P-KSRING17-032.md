---
schema: qual/card@1
id: P-KSRING17-032
kind: problem
title: The Vandermonde determinant
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 32 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be an integral domain and let $D [ x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ]$ be the polynomial ring over D in the n indeterminates $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ . Let

$$
V = \left[ \begin{array} { c c c c c } { x _ { 1 } ^ { n - 1 } } & { \cdot \cdot \cdot } & { x _ { 1 } ^ { 2 } } & { x _ { 1 } } & { 1 } \\ { x _ { 2 } ^ { n - 1 } } & { \cdot \cdot \cdot } & { x _ { 2 } ^ { 2 } } & { x _ { 2 } } & { 1 } \\ { \vdots } & { } & { \vdots } & { \vdots } & { \vdots } \\ { x _ { n } ^ { n - 1 } } & { \cdot \cdot \cdot } & { x _ { n } ^ { 2 } } & { x _ { n } } & { 1 } \end{array} \right] .
$$

Prove that the determinant of V is $\prod _ { 1 \leqslant i < j \leqslant n } ( x _ { i } - x _ { j } )$
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

<1>1. The formula holds for $n=1$.

::: {.proof}
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

<1>2. Assume the formula holds for size $n-1$.
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

::: {.proof}
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

<1>3. For every
$$
j\in\{2,\ldots,n\},
$$
the polynomial $\det V$ vanishes when
$$
x_1=x_j.
$$

::: {.proof}
After substituting
$$
x_1=x_j,
$$
the first row of $V$ becomes identical to the $j$th row. A determinant with two equal rows is zero.
:::

<1>4. The product
$$
\prod_{j=2}^{n}(x_1-x_j)
$$
divides $\det V$ in
$$
A[x_1].
$$

::: {.proof}
By step <1>3 and the polynomial remainder theorem,
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
By step <1>3,
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

<1>5. There exists
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

::: {.proof}
The divisor from step <1>4 has degree exactly
$$
n-1
$$
in $x_1$, while step <1>2 gives
$$
\deg_{x_1}\det V\le n-1.
$$
Therefore the quotient is independent of $x_1$ and lies in $A$.
:::

<1>6. The coefficient $C$ from step <1>5 is
$$
\det V_{n-1}(x_2,\ldots,x_n),
$$
the determinant of the same reversed-column Vandermonde matrix of size $n-1$.

::: {.proof}
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

<1>7. By the induction hypothesis,
$$
C
=
\prod_{2\le i<j\le n}(x_i-x_j).
$$

::: {.proof}
Apply the induction hypothesis to the matrix in step <1>6.
:::

<1>8. Therefore
$$
\det V
=
\prod_{1\le i<j\le n}(x_i-x_j).
$$

::: {.proof}
Substitute step <1>7 into step <1>5:
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

<1>9. Q.E.D.

::: {.proof}
Step <1>1 gives the base case, and steps <1>2--<1>8 prove the induction step.
:::
:::
