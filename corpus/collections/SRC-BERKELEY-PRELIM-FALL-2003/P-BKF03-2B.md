---
schema: qual/card@1
id: P-BKF03-2B
kind: problem
title: Berkeley Fall 2003 prelim problem 2B
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
---

::: {.problem}
Let $u _ { m , n }$ be an array of numbers for $1 \leq m \leq N$ and $1 \leq n \leq N$ . Suppose that $u _ { m , n } = 0$ when m is 1 or $N _ { ; }$ or when n is 1 or N. Suppose also that

$$
u _ { m , n } = { \frac { 1 } { 4 } } \left( u _ { m - 1 , n } + u _ { m + 1 , n } + u _ { m , n - 1 } + u _ { m , n + 1 } \right)
$$

whenever $1 < m < N$ and $1 < n < N$ . Show that all the $u _ { m , n }$ are zero.
:::
\n\n::: {.solution}\nSuppose, for contradiction, that the array is not identically zero.\n\n<1>1. After replacing every $u_{m,n}$ by $-u_{m,n}$ if necessary, we may assume that the maximum value\n\[\nM:=\max_{1\le m,n\le N}u_{m,n}\n\]\nis strictly positive.\n::: {.proof}\nIf some entry is positive, then the maximum is positive already. If no entry is positive but the array is nonzero, then some entry is negative; replacing the entire array by its negative preserves both the zero boundary conditions and the averaging equations, and produces a positive entry.\n:::\n\n<1>2. Every point at which the value $M$ is attained lies in the interior.\n::: {.proof}\nEvery boundary value is $0$ by hypothesis, whereas $M>0$. Hence no maximizing point can have $m\in\{1,N\}$ or $n\in\{1,N\}$.\n:::\n\n<1>3. Choose a maximizing point $(m,n)$ with $m$ minimal. Then\n\[\nu_{m-1,n}<M,\n\]\nwhile each of the other three neighboring values is at most $M$.\n::: {.proof}\nBy <1>2, $1<m<N$ and $1<n<N$, so all four neighbors are defined. Since $M$ is the global maximum, every neighbor is at most $M$. If $u_{m-1,n}=M$, then $(m-1,n)$ would also be a maximizing point with smaller first coordinate, contradicting the choice of $m$. Thus $u_{m-1,n}<M$.\n:::\n\n<1>4. The averaging identity now contradicts $u_{m,n}=M$.\n::: {.proof}\nUsing <1>3,\n\[\n\begin{aligned}\nu_{m,n}\n&=\frac14\bigl(u_{m-1,n}+u_{m+1,n}+u_{m,n-1}+u_{m,n+1}\bigr)\\\n&<\frac14(M+M+M+M)=M.\n\end{aligned}\n\]\nBut $(m,n)$ was chosen so that $u_{m,n}=M$. This contradiction shows that the assumption of a nonzero array is impossible. Therefore\n\[\n\boxed{u_{m,n}=0\text{ for all }1\le m,n\le N}.\n\]\n:::\n:::\n