---
schema: qual/card@1
id: P-XQ4R6
kind: problem
title: Invariant factors from the elementary divisors $(x-1)^3$, $(x-1)$, $(x^2+1)^4$,
  $(x^2+1)^2$, $(x^2+1)^2$, and $(x+2)$
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Canonical Forms
  - Modules
relations: []
review: draft
---

::: {.problem}
Suppose the elementary divisors of a finitely generated torsion $F[x]$-module are
\[
(x-1)^3,\quad (x-1),\quad (x^2+1)^4,\quad (x^2+1)^2,\quad (x^2+1)^2,\quad (x+2).
\]
Determine the invariant factors.
:::

::: {.solution}
Group the elementary divisors by irreducible polynomial and order the powers increasingly:
\[
\begin{array}{c|ccc}
 x-1 & 1 & (x-1) & (x-1)^3\\
 x^2+1 & (x^2+1)^2 & (x^2+1)^2 & (x^2+1)^4\\
 x+2 & 1 & 1 & (x+2).
\end{array}
\]
There are three invariant factors because the largest number of elementary divisors belonging to a single irreducible is three.

Multiplying down the columns gives
\[
d_1=(x^2+1)^2,
\]
\[
d_2=(x-1)(x^2+1)^2,
\]
and
\[
d_3=(x-1)^3(x^2+1)^4(x+2).
\]
They satisfy
\[
d_1\mid d_2\mid d_3,
\]
as required.

Thus the invariant-factor decomposition is
\[
F[x]/(d_1)\oplus F[x]/(d_2)\oplus F[x]/(d_3).
\]
:::
