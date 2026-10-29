---
schema: qual/card@1
id: P-UCLAB08S-09
kind: problem
title: Real eigenvectors in odd and even dimensions
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
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Spring 2008.
---
::: {.problem}

::: pf

::: pf-step

Let $V$ be an odd-dimensional real vector space and $T\colon V\to V$ a real-linear transformation.
Prove that $T$ has a nonzero real eigenvector.

:::

::: pf-step

For every positive even integer $n$, give an $n$-dimensional real vector space $V$ and a real-linear transformation $T\colon V\to V$ having no nonzero real eigenvector.

:::

:::

:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Suppose
\[
\dim_{\RR}V=2m+1
\]
is odd.
Then the characteristic polynomial
\[
\chi_T(\lambda)
=
\det(\lambda I-T)
\]
has a real root.

::: pf-proof

The polynomial
\[
\chi_T(\lambda)
\]
has real coefficients because $T$ is real-linear, and its degree is
\[
2m+1,
\]
which is odd.
Its leading coefficient is $1$.
Therefore
\[
\chi_T(\lambda)\to+\infty
\]
as
\[
\lambda\to+\infty,
\]
while
\[
\chi_T(\lambda)\to-\infty
\]
as
\[
\lambda\to-\infty.
\]
By the intermediate value theorem, there exists
\[
\lambda_0\in\RR
\]
such that
\[
\chi_T(\lambda_0)=0.
\]

:::

:::

::: {.pf-step #p2-s2}

There exists a nonzero real vector
\[
v\in V
\]
such that
\[
\boxed{Tv=\lambda_0v}.
\]

::: pf-proof

The equality
\[
\chi_T(\lambda_0)=0
\]
means
\[
\det(\lambda_0I-T)=0.
\]
Thus
\[
\lambda_0I-T
\]
is singular.
Hence its kernel contains a nonzero vector
\[
v\in V.
\]
For such $v$,
\[
(\lambda_0I-T)v=0,
\]
so
\[
Tv=\lambda_0v.
\]
Thus every real-linear operator on an odd-dimensional real vector space has a nonzero real eigenvector.

:::

:::

::: {.pf-step #p2-s3}

Now let
\[
n=2m
\]
be positive and even.
Take
\[
V=\RR^{2m}
\]
and let $T$ be block diagonal with $m$ copies of
\[
R=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

::: pf-proof

This defines a real-linear endomorphism of the $2m$-dimensional real vector space
\[
\RR^{2m}.
\]

:::

:::

::: {.pf-step #p2-s4}

The $2\times2$ matrix $R$ has no nonzero real eigenvector.

::: pf-proof

Suppose
\[
Rw=\lambda w
\]
for some nonzero
\[
w\in\RR^2
\]
and real number $\lambda$.
Since
\[
R^2=-I,
\]
applying $R$ once more gives
\[
-w
=
R^2w
=
\lambda^2w.
\]
Thus
\[
(\lambda^2+1)w=0.
\]
Because $w\ne0$,
\[
\lambda^2+1=0,
\]
which has no real solution.
Therefore $R$ has no nonzero real eigenvector.

:::

:::

::: {.pf-step #p2-s5}

The block-diagonal transformation $T$ from step [](#p2-s3){.pf-ref} has no nonzero real eigenvector.

::: pf-proof

Suppose
\[
Tv=\lambda v
\]
for some real $\lambda$ and nonzero
\[
v=(v_1,\ldots,v_m),
\qquad
v_j\in\RR^2.
\]
At least one block coordinate
\[
v_j
\]
is nonzero.
The eigenvalue equation holds blockwise:
\[
Rv_j=\lambda v_j.
\]
This contradicts step [](#p2-s4){.pf-ref}.
Hence no such nonzero $v$ exists.

:::

:::

::: {.pf-step #p2-s6}

Therefore:
\[
\boxed{
\begin{aligned}
&\text{every odd-dimensional real-linear operator has a real eigenvector,}\\
&\text{whereas in every positive even dimension there is an operator with none.}
\end{aligned}
}
\]

::: pf-proof

Steps [](#p2-s1){.pf-ref} and [](#p2-s2){.pf-ref} prove part step [](#p2-s1){.pf-ref}.
Steps [](#p2-s3){.pf-ref}, [](#p2-s4){.pf-ref} and [](#p2-s5){.pf-ref} give the required example for every positive even dimension in part step [](#p2-s2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#p2-s6){.pf-ref} contains both requested conclusions.

:::

:::

:::
