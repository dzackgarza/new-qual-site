---
schema: qual/card@1
id: P-TRIV-LA11
kind: problem
title: Vandermonde determinant
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the Vandermonde matrix

$$
V ( x _ { 1 } , . . . , x _ { n } ) = \left[ \begin{array} { c c c c c } { { 1 } } & { { 1 } } & { { 1 } } & { { . . . } } & { { 1 } } \\ { { x _ { 1 } } } & { { x _ { 2 } } } & { { x _ { 3 } } } & { { . . . } } & { { x _ { n } } } \\ { { x _ { 1 } ^ { 2 } } } & { { x _ { 2 } ^ { 2 } } } & { { x _ { 3 } ^ { 2 } } } & { { . . . } } & { { x _ { n } ^ { 2 } } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { x _ { 1 } ^ { n - 1 } } } & { { x _ { 2 } ^ { n - 1 } } } & { { x _ { 3 } ^ { n - 1 } } } & { { . . . } } & { { x _ { n } ^ { n - 1 } } } \end{array} \right] .\tag{4}
$$

(a) Calculate det $V ( x _ { 1 } , . . . , x _ { n } )$

(b) Show that det $V ( x _ { 1 } , . . . , x _ { n } ) = 0$ if and only if $x _ { i } = x _ { j }$ for some $i \neq j$
:::

::: {.solution}
Let
$$
D_n(x_1,\ldots,x_n)
=
\det V(x_1,\ldots,x_n).
$$

<1>1. For $n=1$,
$$
D_1(x_1)=1.
$$

::: {.proof}
The $1\times1$ Vandermonde matrix is $(1)$.
:::

<1>2. Regard $D_n$ as a polynomial in $x_n$. Its degree is at most $n-1$.

::: {.proof}
Only the last column depends on $x_n$, and its entries are
$$
1,x_n,x_n^2,\ldots,x_n^{n-1}.
$$
The determinant is linear in that column, so its degree in $x_n$ is at most
$n-1$.
:::

<1>3. For every $j<n$,
$$
D_n(x_1,\ldots,x_{n-1},x_j)=0.
$$

::: {.proof}
If $x_n=x_j$, then columns $n$ and $j$ of the Vandermonde matrix are equal.
A determinant with two equal columns is zero.
:::

<1>4. Hence
$$
D_n(x_1,\ldots,x_n)
=
C(x_1,\ldots,x_{n-1})
\prod_{j=1}^{n-1}(x_n-x_j)
$$
for some polynomial $C$ independent of $x_n$.

::: {.proof}
By steps <1>2--<1>3, the polynomial in $x_n$ has the $n-1$ distinct roots
$$
x_1,\ldots,x_{n-1}
$$
and degree at most $n-1$. Therefore it is a scalar multiple, with scalar
independent of $x_n$, of the displayed product.
:::

<1>5. The coefficient of $x_n^{n-1}$ in $D_n$ is
$$
D_{n-1}(x_1,\ldots,x_{n-1}).
$$

::: {.proof}
In the last column, the only term containing $x_n^{n-1}$ occurs in the last
row. Expanding the determinant along that entry leaves the upper-left
$(n-1)\times(n-1)$ Vandermonde matrix. The cofactor sign is
$$
(-1)^{n+n}=1.
$$
:::

<1>6. Therefore
$$
C(x_1,\ldots,x_{n-1})
=
D_{n-1}(x_1,\ldots,x_{n-1}).
$$

::: {.proof}
The product in step <1>4 is monic of degree $n-1$ in $x_n$. Hence its
coefficient of $x_n^{n-1}$ is $C$. Compare with step <1>5.
:::

<1>7. Inductively,
$$
\boxed{
D_n(x_1,\ldots,x_n)
=
\prod_{1\le i<j\le n}(x_j-x_i).
}
$$

::: {.proof}
By steps <1>4 and <1>6,
$$
D_n
=
D_{n-1}
\prod_{j=1}^{n-1}(x_n-x_j).
$$
Apply the induction hypothesis
$$
D_{n-1}
=
\prod_{1\le i<j\le n-1}(x_j-x_i),
$$
and combine the factors. The base case is step <1>1.
:::

<1>8. Part (a) follows.

::: {.proof}
This is step <1>7.
:::

<1>9. One has
$$
D_n(x_1,\ldots,x_n)=0
$$
if and only if
$$
x_i=x_j
$$
for some $i\neq j$.

::: {.proof}
By step <1>7, the determinant is a product of the factors
$$
x_j-x_i,
\qquad
i<j.
$$
Over a field, a finite product is zero exactly when one factor is zero. Thus
$$
D_n=0
\iff
x_j-x_i=0
$$
for some $i<j$.
:::

<1>10. Part (b) follows.

::: {.proof}
This is step <1>9.
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>8 and <1>10 establish parts (a) and (b), respectively.
:::
:::
