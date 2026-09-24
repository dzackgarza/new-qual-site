---
schema: qual/card@1
id: P-BKF07-7B
kind: problem
title: A continuous function with a finite limit at infinity is uniformly continuous
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the compact-interval uniform continuity argument and
    the tail estimate from the finite limit against the vendored solution.
---

::: {.problem}
Let \(f:[0,\infty)\to\mathbb R\) be continuous and suppose
\[
\lim_{x\to\infty}f(x)
\]
exists and is finite.
Must \(f\) be uniformly continuous?
Give a proof or a counterexample.
:::

::: {.solution}
Let
$$
L\coloneqq\lim_{x\to\infty}f(x).
$$

<1>1. For every $\varepsilon>0$, there is $M\ge0$ such that
$$
x\ge M
\quad\Longrightarrow\quad
\abs{f(x)-L}<\frac{\varepsilon}{3}.
$$

::: {.proof}
This is the definition of the finite limit $L$ at infinity.
:::

<1>2. For the $M$ from step <1>1, there is
$\delta\in(0,1]$ such that whenever
$x,y\in[0,M+1]$ and $\abs{x-y}<\delta$, one has
$$
\abs{f(x)-f(y)}<\varepsilon.
$$

::: {.proof}
The function $f$ is continuous on the compact interval $[0,M+1]$.
Hence it is uniformly continuous there. Choose a corresponding
positive modulus and decrease it if necessary so that $\delta\le1$.
:::

<1>3. If $x,y\ge0$ and $\abs{x-y}<\delta$, then
$$
\abs{f(x)-f(y)}<\varepsilon.
$$

::: {.proof}
Interchange $x$ and $y$ if necessary so that $x\le y$.

If $x\ge M$, then also $y\ge M$, and step <1>1 gives
$$
\begin{aligned}
\abs{f(x)-f(y)}
&\le \abs{f(x)-L}+\abs{L-f(y)}\\
&<\frac{2\varepsilon}{3}
<\varepsilon.
\end{aligned}
$$

If $x<M$, then
$$
y<x+\delta\le M+1.
$$
Thus $x,y\in[0,M+1]$, and step <1>2 gives
$\abs{f(x)-f(y)}<\varepsilon$.
:::

<1>4. The answer is $\boxed{\text{yes}}$: the function $f$ is
uniformly continuous on $[0,\infty)$.

::: {.proof}
Given any $\varepsilon>0$, steps <1>1--<1>3 produce a single
$\delta>0$ that works for every $x,y\ge0$. This is uniform
continuity.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required answer and proof.
:::
:::
