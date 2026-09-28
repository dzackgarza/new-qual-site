---
schema: qual/card@1
id: P-BKS83-6
kind: problem
title: Extrema, uniform continuity, and a point with $f(x_0+\pi)=f(x_0)$ for a continuous $1$-periodic function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the compact-period reduction for Parts (1) and (2) and the one-period integral argument for Part (3).
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and $1$-periodic.

1. Prove that $f$ is bounded above and below and attains its maximum and minimum.
2. Prove that $f$ is uniformly continuous on $\mathbb R$.
3. Prove that there is $x_0\in\mathbb R$ such that
   \[
   f(x_0+\pi)=f(x_0).
   \]
:::

::: {.solution}
<1>1. Part (1): $f$ is bounded above and below on $\mathbb R$ and attains
both a global maximum and a global minimum.

::: {.proof}
The restriction of $f$ to the compact interval $[0,1]$ is continuous, so
the extreme value theorem gives points $x_{\min},x_{\max}\in[0,1]$ such
that
$$
f(x_{\min})
\le
f(t)
\le
f(x_{\max})
\qquad
(0\le t\le1).
$$
For every $x\in\mathbb R$, choose an integer $n$ such that
$x-n\in[0,1)$. Periodicity gives
$$
f(x)=f(x-n).
$$
Hence the same two inequalities hold for every $x\in\mathbb R$, and the
bounding values are attained at $x_{\min}$ and $x_{\max}$.
:::

<1>2. Part (2): $f$ is uniformly continuous on $\mathbb R$.

::: {.proof}
Fix $\varepsilon>0$. By the Heine--Cantor theorem, the restriction of $f$
to the compact interval $[-1,2]$ is uniformly continuous. Hence there is
$\eta>0$ such that
$$
u,v\in[-1,2],
\qquad
\abs{u-v}<\eta
\quad\Longrightarrow\quad
\abs{f(u)-f(v)}<\varepsilon.
$$
Set
$$
\delta\coloneqq\min\{\eta,1/2\}.
$$
Suppose $x,y\in\mathbb R$ and $\abs{x-y}<\delta$. Choose an integer $n$
with $x-n\in[0,1)$. Then
$$
x-n\in[-1,2],
\qquad
y-n\in(-1/2,3/2)\subset[-1,2],
$$
and
$$
\abs{(x-n)-(y-n)}=\abs{x-y}<\eta.
$$
Since $n$ is an integer, periodicity gives
$$
f(x)=f(x-n),
\qquad
f(y)=f(y-n).
$$
Therefore
$$
\abs{f(x)-f(y)}
=
\abs{f(x-n)-f(y-n)}
<
\varepsilon.
$$
The same $\delta$ works for all $x,y\in\mathbb R$.
:::

<1>3. Part (3): there exists $x_0\in\mathbb R$ such that
$$
f(x_0+\pi)=f(x_0).
$$

::: {.proof}
Define
$$
g(x)\coloneqq f(x+\pi)-f(x).
$$
The function $g$ is continuous. Also, the integral of a continuous
$1$-periodic function over any interval of length $1$ is independent of
the interval. Indeed, after translating the interval by an integer, it is
enough to consider $[r,r+1]$ with $0\le r<1$, and then
$$
\begin{aligned}
\int_r^{r+1}f(t)\,dt
&=\int_r^1f(t)\,dt+\int_1^{r+1}f(t)\,dt\\
&=\int_r^1f(t)\,dt+\int_0^rf(s)\,ds\\
&=\int_0^1f(t)\,dt.
\end{aligned}
$$
Consequently
$$
\begin{aligned}
\int_0^1g(x)\,dx
&=\int_0^1f(x+\pi)\,dx-\int_0^1f(x)\,dx\\
&=\int_\pi^{\pi+1}f(t)\,dt-\int_0^1f(t)\,dt\\
&=0.
\end{aligned}
$$
If $g$ had no zero on $[0,1]$, continuity and the intermediate value
theorem would force $g$ to have one strict sign throughout that interval,
which would make its integral strictly positive or strictly negative.
This contradicts the displayed equality. Hence some $x_0\in[0,1]$
satisfies $g(x_0)=0$, which is exactly
$$
f(x_0+\pi)=f(x_0).
$$
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 establish Parts (1), (2), and (3),
respectively.
:::
:::
