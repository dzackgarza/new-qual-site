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

::: pf

::: {.pf-step #finite-limit-tail-bound}
For every $\varepsilon>0$, there is $M\ge0$ such that
$$
x\ge M
\quad\Longrightarrow\quad
\abs{f(x)-L}<\frac{\varepsilon}{3}.
$$

::: pf-proof
This is the definition of the finite limit $L$ at infinity.
:::

:::

::: {.pf-step #compact-interval-delta}
For the $M$ from step [](#finite-limit-tail-bound){.pf-ref}, there is
$\delta\in(0,1]$ such that whenever
$x,y\in[0,M+1]$ and $\abs{x-y}<\delta$, one has
$$
\abs{f(x)-f(y)}<\varepsilon.
$$

::: pf-proof
The function $f$ is continuous on the compact interval $[0,M+1]$.
Hence it is uniformly continuous there. Choose a corresponding
positive modulus and decrease it if necessary so that $\delta\le1$.
:::

:::

::: {.pf-step #single-delta-works}
If $x,y\ge0$ and $\abs{x-y}<\delta$, then
$$
\abs{f(x)-f(y)}<\varepsilon.
$$

::: pf-proof
Interchange $x$ and $y$ if necessary so that $x\le y$.

If $x\ge M$, then also $y\ge M$, and step [](#finite-limit-tail-bound){.pf-ref} gives
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
Thus $x,y\in[0,M+1]$, and step [](#compact-interval-delta){.pf-ref} gives
$\abs{f(x)-f(y)}<\varepsilon$.
:::

:::

::: {.pf-step #answer-yes}
The answer is $\boxed{\text{yes}}$: the function $f$ is
uniformly continuous on $[0,\infty)$.

::: pf-proof
Given any $\varepsilon>0$, steps [](#finite-limit-tail-bound){.pf-ref}, [](#compact-interval-delta){.pf-ref} and [](#single-delta-works){.pf-ref} produce a single
$\delta>0$ that works for every $x,y\ge0$. This is uniform
continuity.
:::

:::

::: pf-qed
Step [](#answer-yes){.pf-ref} gives the required answer and proof.
:::

:::

:::
