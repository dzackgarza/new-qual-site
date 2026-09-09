---
schema: qual/card@1
id: P-RAF24E
kind: problem
title: Infinite Radon measure integrates some $C_0$ function to infinity; positive functionals on $C_0$ are bounded
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X$ be an LCH space.
\begin{enumerate}
\item[(a)] If $\mu$ is a Radon measure on $X$ satisfying $\mu(X) = \infty$, prove that there is a non-negative function $f \in C_0(X)$ satisfying $\int f\, d\mu = \infty$.
\item[(b)] Prove that every positive linear functional on $C_0(X)$ is bounded.
\end{enumerate}
:::

::: solution
<1>1. Construct a nonnegative $C_0$ function with infinite integral when $\mu(X)=\infty$.
::: proof
Because $\mu$ is Radon and $\mu(X)=\infty$, inner regularity implies that for every $n\ge1$ there is a compact set $K_n\subset X$ such that
\[
\mu(K_n)\ge 4^n.
\]
Since $X$ is locally compact Hausdorff, for each $K_n$ there exists a function
\[
u_n\in C_c(X),
\qquad
0\le u_n\le1,
\qquad
u_n=1\text{ on }K_n.
\]

Define
\[
f:=\sum_{n=1}^\infty 2^{-n}u_n.
\]
The series converges uniformly because
\[
\sum_{n=1}^\infty\|2^{-n}u_n\|_\infty
\le\sum_{n=1}^\infty2^{-n}<\infty.
\]
Each $u_n\in C_0(X)$, and $C_0(X)$ is closed in the uniform norm, so
\[
f\in C_0(X),
\qquad f\ge0.
\]

By Tonelli's theorem,
\[
\begin{aligned}
\int_X f\,d\mu
&=\sum_{n=1}^\infty2^{-n}\int_Xu_n\,d\mu\\
&\ge\sum_{n=1}^\infty2^{-n}\mu(K_n)\\
&\ge\sum_{n=1}^\infty2^n
=\infty.
\end{aligned}
\]
Thus the required function exists.
:::

<1>2. Reduce unboundedness of a positive functional to positive test functions.
::: proof
Let $L:C_0(X)\to\mathbb C$ be positive. On real-valued functions, positivity implies monotonicity:
\[
g\le h\quad\Longrightarrow\quad L(g)\le L(h).
\]
Hence for real $g$,
\[
-|g|\le g\le |g|
\]
implies
\[
|L(g)|\le L(|g|).
\]
Consequently, if $L$ were unbounded, then its values on the positive part of the unit ball would also be unbounded. Thus for every $n$ we could choose
\[
g_n\in C_0(X),
\qquad
0\le g_n\le1,
\]
such that
\[
L(g_n)\ge2^n.
\]
For a complex-valued $C_0(X)$, apply the same argument to real and imaginary parts; unboundedness would again force unboundedness on positive real-valued functions.
:::

<1>3. Derive a contradiction from a uniformly convergent positive series.
::: proof
Set
\[
h_n:=2^{-n}g_n.
\]
Then
\[
\|h_n\|_\infty\le2^{-n},
\qquad
L(h_n)\ge1.
\]
The series
\[
h:=\sum_{n=1}^\infty h_n
\]
converges uniformly, hence $h\in C_0(X)$, and $h\ge0$.

For every $N$,
\[
h\ge\sum_{n=1}^N h_n.
\]
Positivity therefore gives
\[
L(h)
\ge\sum_{n=1}^N L(h_n)
\ge N.
\]
Since $L(h)$ is a finite scalar, this is impossible as $N\to\infty$.

Therefore $L$ must be bounded.
:::
:::
