---
schema: qual/card@1
id: P-ALGS15G
kind: problem
title: Jordan and rational forms of the all-ones $3\times 3$ matrix
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
  - Rational Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let
\[
M = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \in M_3(F),
\]
where $F$ is an algebraically closed field.

Find both the Jordan canonical form and rational canonical form of $M$.
(The answer may depend on the characteristic of $F$).
:::

::: {.solution}
<1>1. $M$ has rank $1$, so its nullity is $2$; the eigenvalues are $0$ (with multiplicity $2$) and $3$ (with multiplicity $1$).
::: {.proof}
$M$ has rank $1$ (all rows equal), so $\dim \ker M = 2$; the trace is $3$, so the third eigenvalue is $3$.
:::

<1>2. Case 1: $\operatorname{char} F \neq 3$.
<2>1. The eigenvalues are $0, 0, 3$, all distinct from each other (since $3 \neq 0$).
::: {.proof}
<1>1 and $\operatorname{char} F \neq 3$.
:::
<2>2. $M$ is diagonalizable.
::: {.proof}
$M$ is symmetric (self-adjoint), hence diagonalizable; equivalently, the eigenspace for $0$ has dimension $2$ and for $3$ has dimension $1$, summing to $3$.
:::
<2>3. Jordan form: $\operatorname{diag}(0, 0, 3)$.
::: {.proof}
<2>2.
:::
<2>4. Rational form: $\operatorname{diag}(x, x(x-3))$... more precisely, the invariant factors are $x$ and $x(x-3)$, so the rational form is the block-diagonal of companion matrices of $x$ and $x(x-3)$.
::: {.proof}
the minimal polynomial is $x(x-3)$ and the characteristic polynomial is $x^2(x-3)$, so the invariant factors are $x$ and $x(x-3)$.
:::

<1>3. Case 2: $\operatorname{char} F = 3$.
<2>1. Then $3 = 0$ in $F$, so the eigenvalues are all $0$ (with multiplicity $3$).
::: {.proof}
the trace is $3 = 0$, and the only eigenvalue is $0$.
:::
<2>2. $M$ is nilpotent (since $M^2 = 3M = 0$).
::: {.proof}
$M^2 = 3M = 0$ in characteristic $3$.
:::
<2>3. $M$ has rank $1$, so its Jordan form is a single Jordan block of size $2$ plus a block of size $1$: $J_2(0) \oplus J_1(0)$.
::: {.proof}
a nilpotent matrix of rank $1$ on a $3$-dimensional space has Jordan blocks of sizes $2$ and $1$.
:::
<2>4. Rational form: the companion matrix of $x^2$ (for the block of size $2$) and of $x$ (for the block of size $1$).
::: {.proof}
the invariant factors are $x$ and $x^2$.
:::

<1>4. Q.E.D.
::: {.proof}
<1>2 (char $\neq 3$) and <1>3 (char $= 3$).
:::
:::
