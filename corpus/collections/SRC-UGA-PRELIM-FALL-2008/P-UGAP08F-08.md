---
schema: qual/card@1
id: P-UGAP08F-08
kind: problem
title: Five examples involving power series, differentiability, separate continuity, series, and line integrals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction prints the singleton in part (a) as “f5g”; context identifies this as the set {5}.
---

::: {.problem}
Give examples of the following. No proofs are required.

(a) A real power series whose domain of convergence is the singleton $\{5\}$.

(b) Functions $f,g:\RR\to\RR$, both differentiable at $0$, such that $f\circ g$ is not differentiable at $0$.

(c) A function $f:\RR^2\to\RR$ that is continuous in each variable separately but is not continuous at $(0,0)$.

(d) A sequence $(a_n)$ converging to $0$ such that the partial sums of $\sum a_n$ are bounded but the series diverges.

(e) A continuously differentiable vector field $F=(M,N)$ on $\RR^2$ such that
$$
\int_C M(x,y)\,dx+N(x,y)\,dy=4,
$$
where $C$ is the unit circle oriented counterclockwise.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a), one example is
$$
\boxed{\sum_{n=0}^{\infty} n!(x-5)^n}.
$$


::: pf-proof

At $x=5$ every term except the constant term is $0$, so the series converges. If $x\ne5$, then
$$
\abs{\frac{(n+1)!(x-5)^{n+1}}{n!(x-5)^n}}
=(n+1)\abs{x-5}\to\infty,
$$
so the terms do not tend to $0$. Hence the series diverges for every $x\ne5$.

:::

:::

::: {.pf-step #s1-2}

For part (b), take
$$
\boxed{f(t)=\abs{t-1},
\qquad
g(t)=1+t.}
$$


::: pf-proof

The function $f$ is differentiable at $0$ because near $0$ one has $f(t)=1-t$, and $g$ is differentiable everywhere. But
$$
(f\circ g)(t)=\abs{t},
$$
which is not differentiable at $0$.

:::

:::

::: {.pf-step #s1-3}

For part (c), take
$$
\boxed{
f(x,y)=
\begin{cases}
\dfrac{xy}{x^2+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}}
$$


::: pf-proof

For each fixed $y$, the resulting function of $x$ is continuous, including at $x=0$; similarly for each fixed $x$. However,
$$
f(t,t)=\frac12
$$
for every $t\ne0$, so $f(t,t)$ does not tend to $f(0,0)=0$ as $t\to0$. Thus $f$ is not continuous at $(0,0)$.

:::

:::

::: {.pf-step #s1-4}

For part (d), define the sequence in successive blocks: for each $k\ge1$, take $k$ consecutive terms equal to $1/k$, followed by $k$ consecutive terms equal to $-1/k$.


::: pf-proof

The terms tend to $0$ because the absolute value of every term in the $k$th block is $1/k$. At the start of every block the partial sum is $0$; during the first half of the block it increases from $0$ to $1$, and during the second half it decreases from $1$ back to $0$. Hence all partial sums lie in $[0,1]$, but the subsequence of block-end partial sums is constantly $0$ while the subsequence of midpoint partial sums is constantly $1$. Therefore the series diverges although its partial sums are bounded.

:::

:::

::: {.pf-step #s1-5}

For part (e), take
$$
\boxed{
F(x,y)=\left(-\frac{2}{\pi}y,\frac{2}{\pi}x\right).}
$$


::: pf-proof

This vector field is continuously differentiable on $\RR^2$. Parametrize the counterclockwise unit circle by
$$
x=\cos t,
\qquad
y=\sin t,
\qquad
0\le t\le2\pi.
$$
Then
$$
dx=-\sin t\,dt,
\qquad
dy=\cos t\,dt,
$$
and therefore
$$
\begin{aligned}
\int_C M\,dx+N\,dy
&=\int_0^{2\pi}
\left[
\left(-\frac{2}{\pi}\sin t\right)(-\sin t)
+\left(\frac{2}{\pi}\cos t\right)(\cos t)
\right]dt\\
&=\frac{2}{\pi}\int_0^{2\pi}1\,dt\\
&=4.
\end{aligned}
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} give examples satisfying parts (a)--(e), respectively.

:::

:::

:::
