---
schema: qual/card@1
id: P-BKF03-8B
kind: problem
title: Conjugacy classes of $5\times5$ complex matrices with $A^3=A^2$
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
  note: Checked against Problem 8B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the allowable Jordan blocks from the annihilating polynomial x^2(x-1) and the count of multiplicity triples.
---

::: {.problem}
The set of $5 \times 5$ complex matrices A satisfying $A ^ { 3 } = A ^ { 2 }$ is a union of conjugacy classes.
How many conjugacy classes?
:::


::: {.solution}
The equation is
\[
A^3=A^2,
\]
equivalently
\[
A^2(A-I)=0.
\]

<1>1. Every Jordan block of $A$ has eigenvalue $0$ or $1$.
::: {.proof}
The polynomial
\[
q(x)=x^2(x-1)
\]
annihilates $A$.
Therefore the minimal polynomial of $A$ divides $q$, so every eigenvalue is a root of $q$, namely $0$ or $1$.
:::

<1>2. The only possible Jordan blocks are
\[
[0],\qquad [1],\qquad J_2(0)=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
::: {.proof}
For eigenvalue $0$, the exponent of $x$ in the minimal polynomial is at most $2$, so Jordan blocks at $0$ have size at most $2$.
Thus the only possibilities are $[0]$ and $J_2(0)$.

For eigenvalue $1$, the factor $x-1$ occurs only to the first power in $q$, so every Jordan block at $1$ has size $1$.
Thus only $[1]$ is allowed.
:::

<1>3. A conjugacy class is uniquely determined by the multiplicities $(a,b,c)$ of these three block types, subject to
\[
a+b+2c=5.
\]
::: {.proof}
Over $\mathbb C$, conjugacy classes are determined uniquely by Jordan normal form.
If $a$ is the number of $[0]$ blocks, $b$ the number of $[1]$ blocks, and $c$ the number of $J_2(0)$ blocks, then the total dimension is exactly $a+b+2c$.
Conversely, every nonnegative triple satisfying the displayed equation gives a valid Jordan form annihilated by $x^2(x-1)$.
:::

<1>4. There are exactly $12$ such triples.
::: {.proof}
The integer $c$ can be $0,1,$ or $2$.
For fixed $c$, the number of nonnegative solutions of
\[
a+b=5-2c
\]
is $6-2c$.
Therefore the total number is
\[
6+4+2=\boxed{12}.
\]
:::
:::

