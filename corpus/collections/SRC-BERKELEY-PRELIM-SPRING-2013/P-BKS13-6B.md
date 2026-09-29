---
schema: qual/card@1
id: P-BKS13-6B
kind: problem
title: Cauchy determinant
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2013 solution PDF and independently completed its polynomial divisibility argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked denominator clearing, separate alternation, Vandermonde divisibility, degree equality, and the specialization fixing the constant.
---

::: {.problem}
Show that the $n \times n$ (Cauchy) matrix with entries $1 / ( x _ { i } - y _ { j } )$ has determinant

$$
\frac { \prod _ { 1 \leq j < i \leq n } ( x _ { i } - x _ { j } ) ( y _ { j } - y _ { i } ) } { \prod _ { 1 \leq i , j \leq n } ( x _ { i } - y _ { j } ) }
$$
:::

::: {.solution}
Let
$$
D(x,y)
\coloneqq
\det\left(\frac{1}{x_i-y_j}\right)_{1\leq i,j\leq n}
$$
and define
$$
Q(x,y)
\coloneqq
\left(
\prod_{i,j=1}^n(x_i-y_j)
\right)
D(x,y).
$$

::: pf

::: {.pf-step #s1}

The expression $Q(x,y)$ is a polynomial in the $2n$ variables
$x_1,\ldots,x_n,y_1,\ldots,y_n$.

::: pf-proof

Expanding the determinant,
$$
D(x,y)
=
\sum_{\sigma\in S_n}
\operatorname{sgn}(\sigma)
\prod_{i=1}^n
\frac{1}{x_i-y_{\sigma(i)}}.
$$
Multiplication by the full denominator gives
$$
Q(x,y)
=
\sum_{\sigma\in S_n}
\operatorname{sgn}(\sigma)
\prod_{i=1}^n
\prod_{\substack{1\leq j\leq n\\j\neq\sigma(i)}}
(x_i-y_j),
$$
which is visibly a polynomial.

:::

:::

::: pf-step

The polynomial $Q$ is alternating in the variables
$x_1,\ldots,x_n$ and also alternating in the variables
$y_1,\ldots,y_n$.

::: pf-proof

Interchanging two $x$-variables interchanges the corresponding two rows
of the determinant $D$, so it changes the sign of $D$. The factor
$$
\prod_{i,j}(x_i-y_j)
$$
is symmetric under permutations of the $x_i$. Hence $Q$ changes sign.

Similarly, interchanging two $y$-variables interchanges two columns of
$D$, while the full denominator product is symmetric in the $y_j$.
Thus $Q$ is alternating in the $y$-variables as well.

:::

:::

::: {.pf-step #s3}

The polynomial $Q$ is divisible by
$$
\Delta_x
\coloneqq
\prod_{1\leq j<i\leq n}(x_i-x_j)
$$
and by
$$
\Delta_y
\coloneqq
\prod_{1\leq j<i\leq n}(y_j-y_i).
$$

::: pf-proof

Because $Q$ is alternating in the $x$-variables, setting
$$
x_i=x_j
$$
for $i\neq j$ gives
$$
Q=-Q,
$$
and hence $Q=0$. Therefore each linear factor $x_i-x_j$ divides $Q$.
The distinct factors are pairwise relatively prime in the polynomial ring,
so their product $\Delta_x$ divides $Q$.

The same argument in the $y$-variables shows divisibility by every
$y_j-y_i$, and hence by $\Delta_y$.

:::

:::

::: {.pf-step #s4}

The polynomial $Q$ has total degree
$$
n(n-1),
$$
which is also the total degree of $\Delta_x\Delta_y$.

::: pf-proof

In the explicit expansion from step [](#s1){.pf-ref}, each summand is a product of
$n(n-1)$ linear factors, so it is homogeneous of that degree. Hence $Q$
is homogeneous of degree at most $n(n-1)$. The evaluation at $x=y$ in
step [](#s5){.pf-ref} shows that $Q\neq0$, so this is its degree.

Each Vandermonde factor has degree
$$
\frac{n(n-1)}2.
$$
Thus their product has degree $n(n-1)$.

:::

:::

::: {.pf-step #s5}

There is a constant $c$ such that
$$
Q=c\,\Delta_x\Delta_y,
$$
and in fact
$$
c=1.
$$

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, the quotient of $Q$ by
$\Delta_x\Delta_y$ has degree $0$, so it is a constant $c$.

To determine $c$, evaluate the polynomial identity at
$$
x_i=y_i
$$
for pairwise distinct values $y_1,\ldots,y_n$. In the polynomial expansion
of step [](#s1){.pf-ref}, every term corresponding to a nonidentity permutation
$\sigma$ contains a factor
$$
x_i-y_i
$$
for some $i$ with $\sigma(i)\neq i$, and therefore vanishes. The identity
term remains:
$$
Q(y,y)
=
\prod_{i=1}^n
\prod_{j\neq i}
(y_i-y_j).
$$
For each pair $j<i$, the two factors contributed are
$$
(y_i-y_j)(y_j-y_i).
$$
Hence
$$
Q(y,y)
=
\prod_{j<i}
(y_i-y_j)(y_j-y_i)
=
\Delta_x(y)\Delta_y(y).
$$
Because the $y_i$ are pairwise distinct, this quantity is nonzero.
Therefore $c=1$.

:::

:::

::: {.pf-step #s6}

Whenever all denominators $x_i-y_j$ are nonzero,
$$
\boxed{
\det\left(\frac{1}{x_i-y_j}\right)
=
\frac{
\prod_{1\leq j<i\leq n}
(x_i-x_j)(y_j-y_i)
}{
\prod_{1\leq i,j\leq n}
(x_i-y_j)
}
}.
$$

::: pf-proof

By step [](#s5){.pf-ref},
$$
\left(
\prod_{i,j}(x_i-y_j)
\right)D(x,y)
=
\Delta_x\Delta_y.
$$
Divide by the nonzero denominator product.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is exactly the Cauchy determinant formula in the problem.

:::

:::

:::
