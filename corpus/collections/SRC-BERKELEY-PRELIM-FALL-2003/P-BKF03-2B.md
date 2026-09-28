---
schema: qual/card@1
id: P-BKF03-2B
kind: problem
title: Discrete harmonic arrays vanishing on the boundary are zero
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
  note: Checked against Problem 2B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the discrete maximum-principle contradiction at a maximizing point of minimal first coordinate.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed the stray N subscript residue in the boundary condition against f03.pdf page 2 problem 2B, and restored two solution formulas where a line break had become the symbol nu.
---

::: {.problem}
Let $u_{m,n}$ be an array of numbers for $1 \leq m \leq N$ and $1 \leq n \leq N$. Suppose that $u_{m,n} = 0$ when $m$ is $1$ or $N$, or when $n$ is $1$ or $N$. Suppose also that

$$
u_{m,n} = \frac{1}{4} \left( u_{m-1,n} + u_{m+1,n} + u_{m,n-1} + u_{m,n+1} \right)
$$

whenever $1 < m < N$ and $1 < n < N$. Show that all the $u_{m,n}$ are zero.
:::


::: {.solution}
Suppose, for contradiction, that the array is not identically zero.

<1>1. After replacing every $u_{m,n}$ by $-u_{m,n}$ if necessary, we may assume that the maximum value
\[
M:=\max_{1\le m,n\le N}u_{m,n}
\]
is strictly positive.
::: {.proof}
If some entry is positive, then the maximum is positive already.
If no entry is positive but the array is nonzero, then some entry is negative; replacing the entire array by its negative preserves both the zero boundary conditions and the averaging equations, and produces a positive entry.
:::

<1>2. Every point at which the value $M$ is attained lies in the interior.
::: {.proof}
Every boundary value is $0$ by hypothesis, whereas $M>0$.
Hence no maximizing point can have $m\in\{1,N\}$ or $n\in\{1,N\}$.
:::

<1>3. Choose a maximizing point $(m,n)$ with $m$ minimal.
Then
\[
u_{m-1,n}<M,
\]
while each of the other three neighboring values is at most $M$.
::: {.proof}
By <1>2, $1<m<N$ and $1<n<N$, so all four neighbors are defined.
Since $M$ is the global maximum, every neighbor is at most $M$.
If $u_{m-1,n}=M$, then $(m-1,n)$ would also be a maximizing point with smaller first coordinate, contradicting the choice of $m$.
Thus $u_{m-1,n}<M$.
:::

<1>4. The averaging identity now contradicts $u_{m,n}=M$.
::: {.proof}
Using <1>3,
\[
\begin{aligned}
u_{m,n}
&=\frac14\bigl(u_{m-1,n}+u_{m+1,n}+u_{m,n-1}+u_{m,n+1}\bigr)\\
&<\frac14(M+M+M+M)=M.
\end{aligned}
\]
But $(m,n)$ was chosen so that $u_{m,n}=M$.
This contradiction shows that the assumption of a nonzero array is impossible.
Therefore
\[
\boxed{u_{m,n}=0\text{ for all }1\le m,n\le N}.
\]
:::
:::

