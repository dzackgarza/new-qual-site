---
schema: qual/card@1
id: P-ALGS12E
kind: problem
title: Polynomials that force diagonalizability over an algebraically closed field
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Diagonalization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared against the official UCSD Spring 2012 Algebra qualifying exam; statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Characterized forcing polynomials by squarefreeness and treated A^m=I via separability of x^m-1.
---

::: problem
Consider a polynomial $f \in K[x]$, where $K$ is an algebraically closed field.
Suppose that $f$ has the property that for all matrices $A \in M_n(K)$ of any size $n$, if $f(A) = 0$, then $A$ is a diagonalizable matrix; then we say that the polynomial $f$ forces diagonalizability.

(a) Characterize by a simple rule exactly which polynomials in $K[x]$ force diagonalizability.
Prove your answer.

(b) Fix $m \geq 1$.
Is every square matrix $A$ with entries in $K$ satisfying $A^m = I$ diagonalizable?
(The answer depends on $K$.)
:::

::: {.solution}
<1>1. A polynomial $f\in K[x]$ forces diagonalizability if and only if $f$ is squarefree.
::: {.proof}
Because $K$ is algebraically closed, write
\[
f(x)=c\prod_{i=1}^r (x-\lambda_i)^{e_i}
\]
with distinct $\lambda_i\in K$.

Suppose first that $f$ is squarefree, so every $e_i=1$.
If $f(A)=0$, then the minimal polynomial $m_A$ divides $f$.
Hence $m_A$ is also a product of distinct linear factors.
A matrix over an algebraically closed field is diagonalizable exactly when its minimal polynomial is a product of distinct linear factors.
Thus $A$ is diagonalizable.

Conversely, suppose $f$ is not squarefree.
Then some root $\lambda$ occurs with multiplicity at least $2$, so $(x-\lambda)^2\mid f$.
Let
\[
J=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}.
\]
Its minimal polynomial is $(x-\lambda)^2$, so $f(J)=0$, but $J$ is not diagonalizable.
Therefore $f$ does not force diagonalizability.
:::

<1>2. Fix $m\ge 1$.
Every matrix $A$ satisfying $A^m=I$ is diagonalizable if and only if $\operatorname{char}K$ does not divide $m$.
::: {.proof}
The condition $A^m=I$ is equivalent to $(x^m-1)(A)=0$.
By <1>1, every such $A$ is diagonalizable exactly when $x^m-1$ is squarefree.

Its derivative is $mx^{m-1}$.
If $\operatorname{char}K\nmid m$, then $m\neq0$ in $K$, and any common root of $x^m-1$ and $mx^{m-1}$ would have to be both nonzero and zero, impossible.
Hence $x^m-1$ is squarefree.

If $\operatorname{char}K=p$ divides $m$, write $m=pr$.
Then
\[
x^m-1=(x^r)^p-1=(x^r-1)^p
\]
in characteristic $p$, so the polynomial has repeated roots.
By <1>1 there is a non-diagonalizable matrix annihilated by $x^m-1$; explicitly, for any $m$th root $\lambda$ one may take the $2\times2$ Jordan block $J_2(\lambda)$ whenever $(x-\lambda)^2\mid x^m-1$.
:::
:::
