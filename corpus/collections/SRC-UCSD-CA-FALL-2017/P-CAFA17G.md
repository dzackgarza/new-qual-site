---
schema: qual/card@1
id: P-CAFA17G
kind: problem
title: "Bezout-type identity for entire functions without common zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Assume that $f$ and $g$ are entire functions without common zeros.
Show that there exist entire functions $A$, $B$ such that $Af + Bg = 1$.

Hint: Ensure that $A = (1 - Bg)/f$ is entire by matching the principal parts of $1/f$ and $Bg/f$.
:::

::: {.solution}
Let $\{a_j\}$ be the zeros of $f$, repeated through their multiplicities only in the local data below. Because $f$ and $g$ have no common zero, $g(a_j)\ne0$.

Consider the meromorphic function
\[
\frac1{f(z)g(z)}.
\]
At each zero $a_j$ of $f$, record its principal part. By the Mittag--Leffler theorem, there exists a meromorphic function $h$ on $\mathbb C$ whose only poles are among the $a_j$ and whose principal part at every $a_j$ agrees with that of $1/(fg)$.

Define
\[
B=fh.
\]
The poles of $h$ are canceled by the corresponding zeros of $f$, so $B$ is entire. Now set
\[
A=\frac{1-Bg}{f}=\frac1f-hg.
\]
Near a zero $a_j$ of $f$,
\[
h-\frac1{fg}
\]
is holomorphic by construction, and therefore
\[
A=-g\left(h-\frac1{fg}\right)
\]
is holomorphic there. Away from the zeros of $f$, it is plainly holomorphic. Hence $A$ is entire.

Finally,
\[
Af+Bg=1
\]
by definition.
:::
