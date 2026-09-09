---
schema: qual/card@1
id: P-RASP25A
kind: problem
title: "L^2 membership characterized by integral inequality with absolutely continuous function"
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
  note: Checked against Problem 1 of the official UCSD Spring 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f \in L^1([0,1])$.
Prove that the following are equivalent:

(1) $f \in L^2([0,1])$.

(2) There exists $g$ absolutely continuous on $[0,1]$ such that for every $x, y \in [0,1]$ it holds
$$
\left|\int_x^y f(t)\,dt\right|^2 \leq (g(y) - g(x))(y - x).
$$
:::

::: solution
<1>1. Prove $(1)\Rightarrow(2)$.
::: proof
Assume $f\in L^2([0,1])$ and define
\[
g(x):=\int_0^x|f(t)|^2\,dt.
\]
Then $g$ is absolutely continuous. If $x<y$, Cauchy--Schwarz gives
\[
\begin{aligned}
\left|\int_x^y f(t)\,dt\right|^2
&\le (y-x)\int_x^y|f(t)|^2\,dt\\
&=(y-x)(g(y)-g(x)).
\end{aligned}
\]
For $y<x$ the same estimate follows after interchanging the endpoints, and for $x=y$ both sides vanish. Thus (2) holds.
:::

<1>2. Show that the function $g$ in (2) is nondecreasing.
::: proof
Assume (2). If $x<y$, then
\[
0\le
\left|\int_x^y f(t)\,dt\right|^2
\le (g(y)-g(x))(y-x).
\]
Since $y-x>0$, it follows that
\[
g(y)\ge g(x).
\]
Thus $g$ is nondecreasing. Because $g$ is absolutely continuous,
\[
g'\ge0
\]
almost everywhere and
\[
g(y)-g(x)=\int_x^y g'(t)\,dt.
\]
:::

<1>3. Differentiate the interval inequality almost everywhere.
::: proof
For $x<y$, divide the assumed inequality by $(y-x)^2$ to obtain
\[
\left|
\frac1{y-x}\int_x^y f(t)\,dt
\right|^2
\le
\frac1{y-x}\int_x^y g'(t)\,dt.
\]
Almost every $x\in(0,1)$ is simultaneously a Lebesgue point of $f$ and of $g'$. Fix such an $x$ and let $y\downarrow x$. By the Lebesgue Differentiation Theorem,
\[
\frac1{y-x}\int_x^y f(t)\,dt\longrightarrow f(x),
\]
and
\[
\frac1{y-x}\int_x^y g'(t)\,dt\longrightarrow g'(x).
\]
Hence
\[
|f(x)|^2\le g'(x)
\]
for almost every $x$.
:::

<1>4. Conclude that $f\in L^2$.
::: proof
Integrating the a.e. inequality from Step 3 gives
\[
\int_0^1|f(x)|^2\,dx
\le \int_0^1g'(x)\,dx
=g(1)-g(0)<\infty.
\]
Therefore
\[
\boxed{f\in L^2([0,1]).}
\]
This proves $(2)\Rightarrow(1)$ and completes the equivalence.
:::
:::
