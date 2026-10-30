---
schema: qual/card@1
id: P-UCLAB08F-09
kind: problem
title: Existence of complex eigenvectors and the real case
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
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2008.
---
::: {.problem}
(a) Prove that every linear transformation $T\colon\CC^n\to\CC^n$ has a nonzero eigenvector.

(b) Is (a) true for every linear transformation $T\colon\RR^n\to\RR^n$?

Prove your assertion.
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Every linear transformation
$$
T:\CC^n\to\CC^n
$$
has a nonzero eigenvector.

::: pf-proof

Let
$$
p_T(\lambda)=\det(\lambda I-T)
$$
be the characteristic polynomial. It has degree $n$. By the fundamental theorem of algebra, there exists
$$
\lambda\in\CC
$$
such that
$$
p_T(\lambda)=0.
$$
Thus
$$
\det(\lambda I-T)=0,
$$
so $\lambda I-T$ is singular. Hence its kernel contains a nonzero vector $v$, and
$$
(\lambda I-T)v=0.
$$
Therefore
$$
Tv=\lambda v,
$$
so $v$ is a nonzero eigenvector.

:::

:::

::: {.pf-step #p2-s2}

The corresponding assertion over $\RR$ is false in general.

::: pf-proof

Consider the real-linear transformation
$$
T:\RR^2\to\RR^2
$$
with matrix
$$
A=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
$$
the rotation through $90^\circ$.

:::

:::

::: {.pf-step #p2-s3}

The transformation in step [](#p2-s2){.pf-ref} has no nonzero real eigenvector.

::: pf-proof

If
$$
Av=\lambda v
$$
for some nonzero $v\in\RR^2$ and $\lambda\in\RR$, then $\lambda$ would be a real root of the characteristic polynomial
$$
\det(\lambda I-A)
=
\det
\begin{pmatrix}
\lambda&1\\
-1&\lambda
\end{pmatrix}
=
\lambda^2+1.
$$
But
$$
\lambda^2+1>0
$$
for every real $\lambda$. Thus no such eigenvector exists.

:::

:::

::: {.pf-step #p2-s4}

Therefore
$$
\boxed{
\text{every complex linear map has an eigenvector, but a real linear map need not}
}.
$$

::: pf-proof

Step [](#p2-s1){.pf-ref} proves part (a), and steps [](#p2-s2){.pf-ref} and [](#p2-s3){.pf-ref} give a counterexample to part (b).

:::

:::

::: pf-qed

Step [](#p2-s4){.pf-ref} gives both requested conclusions.

:::

:::

:::
