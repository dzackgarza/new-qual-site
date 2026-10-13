---
schema: qual/card@1
id: P-UCLAB04F-09
kind: problem
title: Eigenvalues of an operator annihilated by a polynomial
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Exam Fall 2004 PDF.
---

::: {.problem}
Let $T:\mathbb C^n\to\mathbb C^n$ be a linear transformation and let $P(X)$ be a polynomial such that
\[
P(T)=0.
\]
Prove that every eigenvalue of $T$ is a root of $P(X)$.
:::

::: {.solution}
Let $\lambda$ be an eigenvalue of $T$, and choose a nonzero eigenvector $v$ such that
\[
Tv=\lambda v.
\]

<1>1. For every nonnegative integer $k$,
\[
T^kv=\lambda^k v.
\]

::: {.proof}
The case $k=0$ is immediate. If the statement holds for $k$, then
\[
T^{k+1}v
=
T(T^kv)
=
T(\lambda^k v)
=
\lambda^k Tv
=
\lambda^{k+1}v.
\]
Thus the result follows by induction.
:::

<1>2. If
\[
P(X)=\sum_{k=0}^m c_kX^k,
\]
then
\[
P(T)v=P(\lambda)v.
\]

::: {.proof}
Using step <1>1,
\[
\begin{aligned}
P(T)v
&=
\sum_{k=0}^m c_kT^kv\\
&=
\sum_{k=0}^m c_k\lambda^kv\\
&=
P(\lambda)v.
\end{aligned}
\]
:::

<1>3. One has
\[
P(\lambda)=0.
\]

::: {.proof}
By hypothesis,
\[
P(T)=0.
\]
Therefore
\[
0=P(T)v=P(\lambda)v
\]
by step <1>2. Since $v\ne0$, the scalar multiplying it must be zero. Hence
\[
\boxed{P(\lambda)=0}.
\]
:::

<1>4. Every eigenvalue of $T$ is a root of $P$.

::: {.proof}
The eigenvalue $\lambda$ was arbitrary, and step <1>3 shows that $P(\lambda)=0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
