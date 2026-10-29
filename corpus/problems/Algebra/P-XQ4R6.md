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
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source leaves F undeclared; the statement declares F as a field.
---

::: {.problem}
Let $F$ be a field. Suppose the elementary divisors of a finitely generated torsion $F[x]$-module are
$$
(x-1)^3,\quad (x-1),\quad (x^2+1)^4,\quad (x^2+1)^2,\quad (x^2+1)^2,\quad (x+2).
$$
Determine the invariant factors.
:::

::: {.solution}

::: pf

::: {.pf-step #table}
Grouping the elementary divisors by irreducible factor, padded with $1$ and ordered by increasing power, gives
$$
\begin{array}{c|ccc}
 x-1 & 1 & (x-1) & (x-1)^3\\
 x^2+1 & (x^2+1)^2 & (x^2+1)^2 & (x^2+1)^4\\
 x+2 & 1 & 1 & (x+2).
\end{array}
$$

::: pf-proof
The irreducible $x^2+1$ has the most elementary divisors, three, so there are three invariant factors, and each row is padded to length three.
:::

:::

::: pf-step
The invariant factors are $\boxed{d_1=(x^2+1)^2,\ d_2=(x-1)(x^2+1)^2,\ d_3=(x-1)^3(x^2+1)^4(x+2)}$, and the module is $F[x]/(d_1)\oplus F[x]/(d_2)\oplus F[x]/(d_3)$.

::: pf-proof
The $j$-th invariant factor is the product of the $j$-th column of the table in step [](#table){.pf-ref}.
Since the powers increase along each row, $d_1\mid d_2\mid d_3$.
:::

:::

:::

:::
