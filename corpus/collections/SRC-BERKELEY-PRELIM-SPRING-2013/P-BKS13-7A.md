---
schema: qual/card@1
id: P-BKS13-7A
kind: problem
title: Complex matrices of finite order are diagonalizable
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
  note: Compared the authored statement with page 3 of the retained Spring 2013 solution PDF and independently reviewed both the characteristic-zero argument and the positive-characteristic counterexample.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked squarefreeness of x^m-1 over C and finite order p of the nontrivial Jordan block over an algebraic closure of F_p.
---

::: {.problem}
Let A be a matrix over the field of complex numbers. Suppose A has finite order, in other words $A ^ { m } = I$ for some positive integer m. Prove that A is diagonalizable. Give an example of a matrix of finite order over an algebraically closed field that is not diagonalizable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The minimal polynomial $\mu_A(x)$ of $A$ divides
$$
x^m-1.
$$

::: pf-proof

The relation
$$
A^m=I
$$
is equivalent to
$$
(A^m-I)=0.
$$
Thus the polynomial $x^m-1$ annihilates $A$. By the defining property of
the minimal polynomial, $\mu_A$ divides every polynomial that annihilates
$A$.

:::

:::

::: pf-step

The polynomial
$$
x^m-1
$$
has no repeated roots over $\CC$.

::: pf-proof

Its derivative is
$$
mx^{m-1}.
$$
A repeated root would be a common root of $x^m-1$ and $mx^{m-1}$. But a
root of $x^m-1$ is nonzero, whereas the only root of $mx^{m-1}$ is $0$
because the characteristic is $0$. Thus the two polynomials have no common
root.

:::

:::

::: {.pf-step #s3}

The matrix $A$ is diagonalizable over $\CC$.

::: pf-proof

By step [](#s1){.pf-ref}, the minimal polynomial $\mu_A$ divides the squarefree
polynomial $x^m-1$. Hence $\mu_A$ also has no repeated root. Since
$x^m-1$ splits completely over $\CC$, so does $\mu_A$. A linear operator
is diagonalizable exactly when its minimal polynomial splits into distinct
linear factors. Therefore $A$ is diagonalizable.

:::

:::

::: {.pf-step #s4}

Let $K=\overline{\FF_p}$ for a prime $p$, and let
$$
B
\coloneqq
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
$$
Then $B$ has finite order.

::: pf-proof

Write
$$
B=I+N,
\qquad
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$
Since
$$
N^2=0,
$$
the binomial theorem gives
$$
B^p
=
(I+N)^p
=
I+pN
=
I
$$
in characteristic $p$. Since $B\neq I$, it is a nontrivial matrix of
finite order.

:::

:::

::: {.pf-step #s5}

The matrix $B$ from step [](#s4){.pf-ref} is not diagonalizable.

::: pf-proof

The characteristic polynomial of $B$ is
$$
(x-1)^2,
$$
so its only eigenvalue is $1$. If $B$ were diagonalizable, it would be
similar to
$$
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
=
I,
$$
and hence would itself equal $I$. But $B\neq I$.

:::

:::

::: {.pf-step #s6}

Thus an algebraically closed field of positive characteristic admits
a finite-order matrix that is not diagonalizable.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give the explicit example over
$\overline{\FF_p}$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the complex statement, and step [](#s6){.pf-ref} supplies the
requested counterexample.

:::

:::

:::
