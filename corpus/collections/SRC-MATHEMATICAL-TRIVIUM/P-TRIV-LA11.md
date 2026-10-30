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
V(x_1, \ldots, x_n) = \begin{bmatrix} 1 & 1 & 1 & \cdots & 1 \\ x_1 & x_2 & x_3 & \cdots & x_n \\ x_1^2 & x_2^2 & x_3^2 & \cdots & x_n^2 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ x_1^{n-1} & x_2^{n-1} & x_3^{n-1} & \cdots & x_n^{n-1} \end{bmatrix}. \tag{4}
$$

(a) Calculate $\det V(x_1, \ldots, x_n)$.

(b) Show that $\det V(x_1, \ldots, x_n) = 0$ if and only if $x_i = x_j$ for some $i \neq j$.
:::

::: {.solution}

Let
$$
D_n(x_1,\ldots,x_n)
=
\det V(x_1,\ldots,x_n).
$$

::: pf

::: {.pf-step #s1-1}

For $n=1$,
$$
D_1(x_1)=1.
$$


::: pf-proof

The $1\times1$ Vandermonde matrix is $(1)$.

:::

:::

::: {.pf-step #s1-2}

Regard $D_n$ as a polynomial in $x_n$. Its degree is at most $n-1$.


::: pf-proof

Only the last column depends on $x_n$, and its entries are
$$
1,x_n,x_n^2,\ldots,x_n^{n-1}.
$$
The determinant is linear in that column, so its degree in $x_n$ is at most
$n-1$.

:::

:::

::: {.pf-step #s1-3}

For every $j<n$,
$$
D_n(x_1,\ldots,x_{n-1},x_j)=0.
$$


::: pf-proof

If $x_n=x_j$, then columns $n$ and $j$ of the Vandermonde matrix are equal.
A determinant with two equal columns is zero.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
D_n(x_1,\ldots,x_n)
=
C(x_1,\ldots,x_{n-1})
\prod_{j=1}^{n-1}(x_n-x_j)
$$
for some polynomial $C$ independent of $x_n$.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, the polynomial in $x_n$ has the $n-1$ distinct roots
$$
x_1,\ldots,x_{n-1}
$$
and degree at most $n-1$. Therefore it is a scalar multiple, with scalar
independent of $x_n$, of the displayed product.

:::

:::

::: {.pf-step #s1-5}

The coefficient of $x_n^{n-1}$ in $D_n$ is
$$
D_{n-1}(x_1,\ldots,x_{n-1}).
$$


::: pf-proof

In the last column, the only term containing $x_n^{n-1}$ occurs in the last
row. Expanding the determinant along that entry leaves the upper-left
$(n-1)\times(n-1)$ Vandermonde matrix. The cofactor sign is
$$
(-1)^{n+n}=1.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
C(x_1,\ldots,x_{n-1})
=
D_{n-1}(x_1,\ldots,x_{n-1}).
$$


::: pf-proof

The product in step [](#s1-4){.pf-ref} is monic of degree $n-1$ in $x_n$. Hence its
coefficient of $x_n^{n-1}$ is $C$. Compare with step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Inductively,
$$
\boxed{
D_n(x_1,\ldots,x_n)
=
\prod_{1\le i<j\le n}(x_j-x_i).
}
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} and [](#s1-6){.pf-ref},
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
and combine the factors. The base case is step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Part (a) follows.


::: pf-proof

This is step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

One has
$$
D_n(x_1,\ldots,x_n)=0
$$
if and only if
$$
x_i=x_j
$$
for some $i\neq j$.


::: pf-proof

By step [](#s1-7){.pf-ref}, the determinant is a product of the factors
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

:::

::: {.pf-step #s1-10}

Part (b) follows.


::: pf-proof

This is step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-8){.pf-ref} and [](#s1-10){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
