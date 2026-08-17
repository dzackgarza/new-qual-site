---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-BV3
kind: problem
title: 'Determine whether x sin(1/x) has bounded variation'
classification:
  areas:
  - real-analysis
  topics:
  - variation
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2017, 2a) Define $f:[0,1]\to[-1,1]$ by
$$
f(x):=
\begin{cases}
x\sin\left(\frac1x\right),&0<x\le1,\\
0,&x=0.
\end{cases}
$$
Determine, with justification, whether $f$ is of bounded variation on the interval $[0,1]$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Determine whether $f(x) = x\sin(1/x)$ for $x > 0$, $f(0) = 0$, is of bounded variation on $[0,1]$.

<1>1. $f$ is NOT of bounded variation on $[0,1]$.
<2>1. For each $k \ge 1$, set $x_k = \frac{2}{(2k+1)\pi} \in (0,1]$; then $|f(x_k)| = x_k$.
Proof: $1/x_k = (2k+1)\pi/2$ and $\sin((2k+1)\pi/2) = \pm 1$, so $|f(x_k)| = x_k|\sin(1/x_k)| = x_k$.
<2>2. Consecutive values have opposite signs, so $|f(x_k) - f(x_{k+1})| = x_k + x_{k+1}$.
Proof: $\sin((2k+1)\pi/2)$ and $\sin((2k+3)\pi/2)$ have opposite signs (odd multiples of $\pi/2$ alternate between $+1$ and $-1$), so $f(x_k)$ and $f(x_{k+1})$ have opposite signs; hence $|f(x_k) - f(x_{k+1})| = |f(x_k)| + |f(x_{k+1})| = x_k + x_{k+1}$ by <2>1. <2>3. $\sum_{k} x_k = \frac{2}{\pi}\sum_k \frac{1}{2k+1} = \infty$.
Proof: the odd harmonic series diverges (comparison with the harmonic series: $\frac{1}{2k+1} \ge \frac{1}{2(k+1)}$). <2>4. $V_0^1 f = \infty$.
Proof: for the partition $\{x_1 > x_2 > \cdots > x_N, 0, 1\}$ (ordered decreasingly), the variation is at least $\sum_{k=1}^{N-1}|f(x_k) - f(x_{k+1})| = \sum_{k=1}^{N-1}(x_k + x_{k+1}) \ge \sum_{k=2}^{N-1} x_k$, which diverges as $N \to \infty$ by <2>3 (note $x_k \to 0$ and the variation from $x_N$ down to $0$ is $|f(x_N) - f(0)| = x_N$, another divergent tail).
<2>5. Q.E.D. Proof: <2>4 contradicts finiteness of total variation, so $f \notin BV[0,1]$.
:::
