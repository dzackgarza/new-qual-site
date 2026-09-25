---
schema: qual/card@1
id: P-BKS82-5
kind: problem
title: Compactness of a family with uniformly bounded second derivatives and fixed initial jet
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained PDF; the extracted markdown contains a different Problem 5.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the derivative bounds, uniform Lipschitz estimate, and the Arzelà--Ascoli compactness argument.
---

::: {.problem}
Let $(g_n)$ be twice differentiable functions on $[0,1]$ such that
\[
g_n(0)=g_n'(0)=0
\]
for every $n$, and suppose
\[
|g_n''(x)|\le1
\]
for every $n$ and every $x\in[0,1]$. Prove that $(g_n)$ has a subsequence converging uniformly on $[0,1]$.
:::

::: {.solution}
<1>1. For every $n$ and every $x\in[0,1]$,
$$
\abs{g_n'(x)}\le x\le1.
$$

::: {.proof}
Fix $n$ and $x\in(0,1]$. By the mean value theorem applied to $g_n'$ on
$[0,x]$, there is $\xi\in(0,x)$ such that
$$
g_n'(x)-g_n'(0)=g_n''(\xi)x.
$$
Since $g_n'(0)=0$ and $\abs{g_n''(\xi)}\le1$,
$$
\abs{g_n'(x)}\le x.
$$
The same estimate holds at $x=0$ because $g_n'(0)=0$.
:::

<1>2. The family $(g_n)$ is uniformly bounded and uniformly
equicontinuous on $[0,1]$.

::: {.proof}
For $x\in[0,1]$, the mean value theorem, $g_n(0)=0$, and step <1>1 give
$$
\abs{g_n(x)}
=
\abs{g_n(x)-g_n(0)}
\le x
\le1.
$$
Thus the family is uniformly bounded.

For $x,y\in[0,1]$, another application of the mean value theorem and step
<1>1 gives
$$
\abs{g_n(x)-g_n(y)}
\le
\abs{x-y}.
$$
Hence every $g_n$ is $1$-Lipschitz, uniformly in $n$, so the family is
equicontinuous.
:::

<1>3. Let
$$
\mathcal F\coloneqq\{g_n:n\ge1\}
\subset C([0,1],\RR).
$$
Its closure in the uniform norm is compact.

::: {.proof}
Every uniform limit of functions bounded in absolute value by $1$ is again
bounded in absolute value by $1$. Likewise, a uniform limit of
$1$-Lipschitz functions is $1$-Lipschitz. Therefore the uniform closure
$\overline{\mathcal F}$ is closed, bounded, and equicontinuous in
$C([0,1],\RR)$. Since $[0,1]$ is compact, the Arzelà--Ascoli theorem
implies that $\overline{\mathcal F}$ is compact in the uniform norm.
:::

<1>4. The sequence $(g_n)$ has a subsequence converging uniformly on
$[0,1]$.

::: {.proof}
The sequence $(g_n)$ lies in the compact metric space
$\overline{\mathcal F}$ from step <1>3. Every sequence in a compact
metric space has a convergent subsequence. Convergence in the metric of
$C([0,1],\RR)$ is uniform convergence, so some subsequence
$(g_{n_k})$ converges uniformly on $[0,1]$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
