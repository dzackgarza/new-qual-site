---
schema: qual/card@1
id: P-UCLAB10S-04
kind: problem
title: Trace-zero negative semidefinite matrices vanish; operators with $TT^*=4T-3I$
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
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 4. (i) Let $A=(a_{ij})$ be a real symmetric $n\times n$ matrix such that
$$
\sum_{i,j}a_{ij}x_ix_j\le0
$$
for every $x\in\RR^n$.
Prove that if $\operatorname{tr}(A)=0$, then $A=0$.

(ii) Let $T$ be a linear operator on a finite-dimensional complex inner-product space.
Suppose
$$
TT^*=4T-3I.
$$
Prove that $T$ is positive-definite Hermitian and find all possible eigenvalues of $T$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In part (i), every eigenvalue of $A$ is nonpositive.


::: pf-proof

Because $A$ is real symmetric, the spectral theorem gives a real eigenvector
$$
v\ne0
$$
for each eigenvalue $\lambda$.
Substituting $x=v$ into the hypothesis gives
$$
v^TAv\le0.
$$
Since
$$
Av=\lambda v,
$$
one has
$$
v^TAv
=
\lambda\norm{v}_2^2.
$$
Because
$$
\norm{v}_2^2>0,
$$
it follows that
$$
\lambda\le0.
$$

:::

:::

::: {.pf-step #s1-2}

The trace of $A$ is the sum of its eigenvalues.


::: pf-proof

By the spectral theorem, there exists an orthogonal matrix $Q$ such that
$$
Q^TAQ
=
\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
$$
Trace is invariant under similarity, so
$$
\operatorname{tr}(A)
=
\lambda_1+\cdots+\lambda_n.
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
\operatorname{tr}(A)=0,
$$
then every eigenvalue of $A$ is zero.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\lambda_i\le0
$$
for every $i$.
By step [](#s1-2){.pf-ref} and the trace hypothesis,
$$
\sum_{i=1}^n\lambda_i=0.
$$
A finite sum of nonpositive real numbers can equal zero only if every summand is zero.
Thus
$$
\lambda_i=0
$$
for all $i$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{A=0}.
$$


::: pf-proof

The symmetric matrix $A$ is orthogonally diagonalizable.
By step [](#s1-3){.pf-ref}, its diagonal form has only zero entries.
Hence the diagonal form is the zero matrix, and therefore so is $A$.
This proves part (i).

:::

:::

::: {.pf-step #s1-5}

For part (ii), the operator
$$
TT^*
$$
is Hermitian.


::: pf-proof

Taking adjoints gives
$$
(TT^*)^*
=
T^{**}T^*
=
TT^*.
$$
Thus $TT^*$ is self-adjoint.

:::

:::

::: {.pf-step #s1-6}

The identity
$$
TT^*=4T-3I
$$
forces $T$ to be Hermitian.


::: pf-proof

By step [](#s1-5){.pf-ref}, the left-hand side is Hermitian.
Hence the right-hand side is Hermitian:
$$
(4T-3I)^*
=
4T-3I.
$$
But
$$
(4T-3I)^*
=
4T^*-3I.
$$
Therefore
$$
4T^*-3I
=
4T-3I,
$$
so
$$
\boxed{T^*=T}.
$$

:::

:::

::: {.pf-step #s1-7}

Consequently,
$$
\boxed{(T-I)(T-3I)=0}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
T^*=T.
$$
The given identity becomes
$$
T^2
=
4T-3I.
$$
Rearranging,
$$
T^2-4T+3I=0.
$$
Factor the polynomial:
$$
T^2-4T+3I
=
(T-I)(T-3I).
$$

:::

:::

::: {.pf-step #s1-8}

Every eigenvalue $\lambda$ of $T$ belongs to
$$
\boxed{\{1,3\}}.
$$


::: pf-proof

Let
$$
Tv=\lambda v
$$
with
$$
v\ne0.
$$
Applying the polynomial identity from step [](#s1-7){.pf-ref} gives
$$
(\lambda-1)(\lambda-3)v=0.
$$
Since
$$
v\ne0,
$$
one has
$$
(\lambda-1)(\lambda-3)=0.
$$
Thus
$$
\lambda=1
\quad\text{or}\quad
\lambda=3.
$$

:::

:::

::: {.pf-step #s1-9}

The operator $T$ is positive definite.


::: pf-proof

By step [](#s1-6){.pf-ref}, $T$ is Hermitian.
Hence the spectral theorem gives an orthonormal basis of eigenvectors.
By step [](#s1-8){.pf-ref}, every eigenvalue is either $1$ or $3$, and therefore positive.

For any nonzero
$$
v=\sum_j c_je_j
$$
in an orthonormal eigenbasis,
$$
\langle Tv,v\rangle
=
\sum_j\lambda_j\abs{c_j}^2.
$$
Every $\lambda_j$ is positive and at least one $c_j$ is nonzero.
Therefore
$$
\langle Tv,v\rangle>0.
$$
Thus
$$
\boxed{T\text{ is positive-definite Hermitian}.}
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (i).
Steps [](#s1-6){.pf-ref} and [](#s1-8){.pf-ref}, and [](#s1-9){.pf-ref} prove part (ii): $T$ is Hermitian, its only possible eigenvalues are $1$ and $3$, and it is positive definite.

:::

:::

:::
