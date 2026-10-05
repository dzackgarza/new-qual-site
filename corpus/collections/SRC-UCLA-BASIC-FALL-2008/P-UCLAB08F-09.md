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
<1>1. Prove that every linear transformation $T\colon\mathbb C^n\to\mathbb C^n$ has a nonzero eigenvector.

<1>2. Is <1>1 true for every real-linear transformation $T\colon\mathbb R^n\to\mathbb R^n$?
Prove your assertion.
:::

::: {.solution}
<1>1. Every linear transformation
\[
T:\mathbb C^n\to\mathbb C^n
\]
has a nonzero eigenvector.

::: {.proof}
Let
\[
p_T(\lambda)=\det(\lambda I-T)
\]
be the characteristic polynomial. It has degree $n$. By the fundamental theorem of algebra, there exists
\[
\lambda\in\mathbb C
\]
such that
\[
p_T(\lambda)=0.
\]
Thus
\[
\det(\lambda I-T)=0,
\]
so $\lambda I-T$ is singular. Hence its kernel contains a nonzero vector $v$, and
\[
(\lambda I-T)v=0.
\]
Therefore
\[
Tv=\lambda v,
\]
so $v$ is a nonzero eigenvector.
:::

<1>2. The corresponding assertion over $\mathbb R$ is false in general.

::: {.proof}
Consider the real-linear transformation
\[
T:\mathbb R^2\to\mathbb R^2
\]
with matrix
\[
A=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\]
the rotation through $90^\circ$.
:::

<1>3. The transformation in step <1>2 has no nonzero real eigenvector.

::: {.proof}
If
\[
Av=\lambda v
\]
for some nonzero $v\in\mathbb R^2$ and $\lambda\in\mathbb R$, then $\lambda$ would be a real root of the characteristic polynomial
\[
\det(\lambda I-A)
=
\det
\begin{pmatrix}
\lambda&1\\
-1&\lambda
\end{pmatrix}
=
\lambda^2+1.
\]
But
\[
\lambda^2+1>0
\]
for every real $\lambda$. Thus no such eigenvector exists.
:::

<1>4. Therefore
\[
\boxed{
\text{every complex linear map has an eigenvector, but a real linear map need not}
}.
\]

::: {.proof}
Step <1>1 proves part <1>1, and steps <1>2--<1>3 give a counterexample to part <1>2.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives both requested conclusions.
:::
:::
