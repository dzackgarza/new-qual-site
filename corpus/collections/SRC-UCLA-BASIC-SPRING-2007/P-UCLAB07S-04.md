---
schema: qual/card@1
id: P-UCLAB07S-04
kind: problem
title: Limits of even powers of a symmetric matrix quadratic form
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
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Let $A$ be a real symmetric $n\times n$ matrix with distinct eigenvalues $\lambda_1,\ldots,\lambda_\ell$, where $\ell\le n$.
Determine
$$
X=\left\{x\in\RR^n:\lim_{k\to\infty}(x^TA^{2k}x)^{1/k}\text{ exists}\right\}
$$
and
$$
L=\left\{\lim_{k\to\infty}(x^TA^{2k}x)^{1/k}:x\in X\right\}.
$$
:::

::: {.solution}

For each distinct eigenvalue $\lambda_j$, let
$$
E_j=\ker(A-\lambda_jI).
$$

::: pf

::: {.pf-step #s1-1}

Since $A$ is real symmetric,
$$
\RR^n
=
\bigoplus_{j=1}^{\ell}E_j
$$
orthogonally.


::: pf-proof

By the spectral theorem for real symmetric matrices, $\RR^n$ has an orthonormal basis of eigenvectors of $A$.
Grouping basis vectors with the same eigenvalue yields the stated orthogonal direct sum of eigenspaces.

:::

:::

::: {.pf-step #s1-2}

Every
$$
x\in\RR^n
$$
has a unique decomposition
$$
x=x_1+\cdots+x_\ell,
\qquad
x_j\in E_j,
$$
and
$$
\boxed{
x^TA^{2k}x
=
\sum_{j=1}^{\ell}
\norm{x_j}_2^2\,\lambda_j^{2k}
}.
$$


::: pf-proof

The decomposition is given by step [](#s1-1){.pf-ref}.
Since
$$
Ax_j=\lambda_jx_j,
$$
one has
$$
A^{2k}x_j
=
\lambda_j^{2k}x_j.
$$
Therefore
$$
A^{2k}x
=
\sum_{j=1}^{\ell}
\lambda_j^{2k}x_j.
$$
Using orthogonality of the eigenspaces,
$$
\begin{aligned}
x^TA^{2k}x
&=
\left\langle
\sum_i x_i,
\sum_j\lambda_j^{2k}x_j
\right\rangle\\
&=
\sum_{j=1}^{\ell}
\lambda_j^{2k}\norm{x_j}_2^2.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

For
$$
x\ne0,
$$
define
$$
M(x)
=
\max\left\{
\abs{\lambda_j}^2:
x_j\ne0
\right\}.
$$
Then
$$
\lim_{k\to\infty}
\left(
x^TA^{2k}x
\right)^{1/k}
=
M(x).
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
x^TA^{2k}x
=
\sum_{j:x_j\ne0}
\norm{x_j}_2^2
\left(
\abs{\lambda_j}^2
\right)^k.
$$
Let
$$
M=M(x).
$$
Choose an index $j_0$ with
$$
x_{j_0}\ne0
\qquad\text{and}\qquad
\abs{\lambda_{j_0}}^2=M.
$$
Then
$$
\norm{x_{j_0}}_2^2 M^k
\le
x^TA^{2k}x.
$$
Also,
$$
x^TA^{2k}x
\le
\left(
\sum_j\norm{x_j}_2^2
\right)
M^k
=
\norm{x}_2^2M^k.
$$
Taking $k$th roots gives
$$
\norm{x_{j_0}}_2^{2/k}M
\le
\left(
x^TA^{2k}x
\right)^{1/k}
\le
\norm{x}_2^{2/k}M.
$$
Both scalar factors tend to $1$ as $k\to\infty$.
Hence the squeeze theorem gives the stated limit.

:::

:::

::: {.pf-step #s1-4}

For
$$
x=0,
$$
the limit exists and equals $0$.


::: pf-proof

For every $k$,
$$
x^TA^{2k}x=0.
$$
Thus
$$
\left(
x^TA^{2k}x
\right)^{1/k}
=0.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{X=\RR^n}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} proves existence of the limit for every nonzero $x$, and step [](#s1-4){.pf-ref} handles $x=0$.
Thus every vector belongs to $X$.

:::

:::

::: {.pf-step #s1-6}

Every nonzero limit value is one of the numbers
$$
\lambda_1^2,\ldots,\lambda_\ell^2.
$$


::: pf-proof

For $x\ne0$, step [](#s1-3){.pf-ref} says that the limit equals
$$
\max\left\{
\abs{\lambda_j}^2:x_j\ne0
\right\}.
$$
Since the eigenvalues are real,
$$
\abs{\lambda_j}^2=\lambda_j^2.
$$
The maximum of a finite nonempty subset of the numbers $\lambda_j^2$ is one of those numbers.

:::

:::

::: {.pf-step #s1-7}

Every number
$$
\lambda_j^2
$$
occurs as a limit.


::: pf-proof

Choose a nonzero eigenvector
$$
v\in E_j.
$$
Then
$$
A^{2k}v
=
\lambda_j^{2k}v.
$$
Hence
$$
\begin{aligned}
\left(
v^TA^{2k}v
\right)^{1/k}
&=
\left(
\norm{v}_2^2\lambda_j^{2k}
\right)^{1/k}\\
&=
\norm{v}_2^{2/k}\lambda_j^2
\longrightarrow
\lambda_j^2.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
L
=
\{0\}
\cup
\{\lambda_1^2,\ldots,\lambda_\ell^2\}
}.
$$


::: pf-proof

The value $0$ occurs at $x=0$ by step [](#s1-4){.pf-ref}.
Step [](#s1-6){.pf-ref} shows that no other values can occur.
Step [](#s1-7){.pf-ref} shows that every listed square does occur.
Repeated squares, such as those coming from eigenvalues $\lambda$ and $-\lambda$, appear only once because $L$ is a set.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} determines $X$, and step [](#s1-8){.pf-ref} determines $L$.

:::

:::

:::
