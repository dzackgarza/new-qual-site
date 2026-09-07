---
schema: qual/card@1
id: P-ALGF21E
kind: problem
title: Jordan form of a $7\times 7$ matrix with $A^5 = 2A^4 + A^3$, rank $5$, trace $4$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 5 of the official UCSD Algebra Qualifying Exam, Fall 2021 source; the polynomial identity, rank, and trace hypotheses agree with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the eigenvalue multiplicities from the trace, the two zero Jordan blocks from nullity, and semisimplicity of the nonzero eigenspaces from the squarefree nonzero factor of the annihilating polynomial.
---

::: problem
Suppose that $A$ is a complex $7 \times 7$ matrix such that $A^5 = 2A^4 + A^3$.
Suppose that $\mathrm{rk}\, A = 5$ and $\mathrm{tr}\, A = 4$, where $\mathrm{rk}$ indicates the rank and $\mathrm{tr}$ indicates the trace of a matrix.
Find the Jordan canonical form of $A$.
:::

::: {.solution}
<1>1. The matrix $A$ is annihilated by
\[
p(x)=x^3(x^2-2x-1)
=x^3(x-(1+\sqrt2))(x-(1-\sqrt2)).
\]
::: {.proof}
Rearranging the given identity gives
\[
A^5-2A^4-A^3
=A^3(A^2-2A-I)
=0.
\]
:::

<1>2. Every eigenvalue of $A$ belongs to
\[
\{0,1+\sqrt2,1-\sqrt2\}.
\]
Moreover, every Jordan block for either nonzero eigenvalue has size $1$.
::: {.proof}
The minimal polynomial of $A$ divides the polynomial $p$ from <1>1, so every eigenvalue is a root of $p$.
The factors
\[
x-(1+\sqrt2)
\quad\text{and}\quad
x-(1-\sqrt2)
\]
occur only to the first power in $p$.
Hence they occur to exponent at most $1$ in the minimal polynomial, which means that the Jordan blocks for those eigenvalues all have size $1$.
:::

<1>3. The eigenvalue $0$ has exactly two Jordan blocks.
::: {.proof}
Since
\[
\operatorname{rank}A=5,
\]
rank-nullity gives
\[
\dim\ker A=7-5=2.
\]
The dimension of $\ker A$ equals the geometric multiplicity of the eigenvalue $0$, which is exactly the number of Jordan blocks for $0$.
:::

<1>4. The eigenvalues $1+\sqrt2$ and $1-\sqrt2$ each have algebraic multiplicity $2$.
::: {.proof}
Let $r$ and $s$ be the algebraic multiplicities of $1+\sqrt2$ and $1-\sqrt2$, respectively.
The trace is the sum of the eigenvalues with algebraic multiplicity, so
\[
4=r(1+\sqrt2)+s(1-\sqrt2).
\]
Equating rational and irrational parts gives
\[
r-s=0
\]
and
\[
r+s=4.
\]
Therefore
\[
r=s=2.
\]
:::

<1>5. The eigenvalue $0$ has algebraic multiplicity $3$.
::: {.proof}
The total algebraic multiplicity is $7$.
By <1>4, the two nonzero eigenvalues contribute
\[
2+2=4.
\]
Hence the remaining algebraic multiplicity is
\[
7-4=3.
\]
:::

<1>6. The Jordan blocks for $0$ have sizes $2$ and $1$.
::: {.proof}
By <1>3, there are exactly two Jordan blocks for $0$.
By <1>5, their sizes sum to $3$.
The only two positive integers summing to $3$ are $2$ and $1$.
:::

<1>7. The Jordan canonical form of $A$ is
\[
J_2(0)
\oplus J_1(0)
\oplus J_1(1+\sqrt2)^{\oplus2}
\oplus J_1(1-\sqrt2)^{\oplus2}.
\]
::: {.proof}
The zero blocks are determined by <1>6.
By <1>4, each nonzero eigenvalue has algebraic multiplicity $2$, and by <1>2 all of its Jordan blocks have size $1$.
These blocks account for all seven dimensions.
:::
:::
