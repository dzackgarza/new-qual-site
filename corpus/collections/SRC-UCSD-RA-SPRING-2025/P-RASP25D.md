---
schema: qual/card@1
id: P-RASP25D
kind: problem
title: "Closed convex set in L^1 with no best approximation"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $E$ be the Banach space $L^1([0,1])$ and
$$
C := \left\{u \in E : u(x) \geq 0 \text{ a.e. } x \in [0,1],\; \int_0^1 x u(x)\,dx \geq 1\right\}.
$$

Show that

(1) $C$ is nonempty, closed and convex in $E$.

(2) $d(0, C) := \inf\{\|u\| : u \in C\} = 1$.

Hint: try piecewise constant functions.

(3) There is no $u \in C$ such that $\|u\| = d(0, C) = 1$.
:::


::: solution
<1>1. Prove that $C$ is nonempty, closed, and convex.
::: proof
The constant function $u\equiv2$ lies in $C$ because
\[
\int_0^1 2x\,dx=1.
\]

Convexity is immediate: if $u,v\in C$ and $0\le t\le1$, then $tu+(1-t)v\ge0$ a.e. and
\[
\int_0^1 x\bigl(tu+(1-t)v\bigr)\,dx
=t\int_0^1xu\,dx+(1-t)\int_0^1xv\,dx\ge1.
\]

For closedness, suppose $u_n\in C$ and $u_n\to u$ in $L^1$. Since $u_n\ge0$ a.e., the negative part $u^-:=\max(-u,0)$ satisfies
\[
u^-(x)\le |u(x)-u_n(x)|
\]
for a.e. $x$. Hence
\[
\|u^-\|_1\le\|u-u_n\|_1\to0,
\]
so $u\ge0$ a.e. Also $x\in L^\infty([0,1])$, so
\[
\left|\int_0^1x(u_n-u)\,dx\right|\le\|u_n-u\|_1\to0.
\]
Thus
\[
\int_0^1xu\,dx=\lim_n\int_0^1xu_n\,dx\ge1,
\]
and $u\in C$. Therefore $C$ is closed.
:::

<1>2. Compute the distance from $0$ to $C$.
::: proof
If $u\in C$, then $u\ge0$ a.e. and $0\le x\le1$, so
\[
\|u\|_1=\int_0^1u\,dx\ge\int_0^1xu\,dx\ge1.
\]
Hence $d(0,C)\ge1$.

For $0<\varepsilon<1$, define
\[
v_\varepsilon(x)=\frac{1}{\varepsilon(1-\varepsilon/2)}\mathbf1_{[1-\varepsilon,1]}(x).
\]
Then
\[
\int_0^1xv_\varepsilon(x)\,dx
=\frac{1}{\varepsilon(1-\varepsilon/2)}\int_{1-\varepsilon}^1x\,dx=1,
\]
so $v_\varepsilon\in C$. Moreover,
\[
\|v_\varepsilon\|_1=\frac{1}{1-\varepsilon/2}\longrightarrow1.
\]
Thus $d(0,C)\le1$, and therefore
\[
\boxed{d(0,C)=1.}
\]
:::

<1>3. Show that the distance is not attained.
::: proof
Suppose $u\in C$ and $\|u\|_1=1$. Since $u\ge0$ a.e.,
\[
1=\int_0^1u\,dx\ge\int_0^1xu\,dx\ge1.
\]
Hence equality holds throughout, so
\[
\int_0^1(1-x)u(x)\,dx=0.
\]
The integrand is nonnegative. Therefore
\[
(1-x)u(x)=0
\]
a.e., which implies $u=0$ a.e. on $[0,1)$. Since the point $1$ has measure zero, $u=0$ in $L^1$, contradicting
\[
\int_0^1xu\,dx\ge1.
\]
Thus no element of $C$ attains the distance $1$ from the origin.
:::
:::
