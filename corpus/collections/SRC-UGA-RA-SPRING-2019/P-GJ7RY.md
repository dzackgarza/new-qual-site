---
schema: qual/card@1
id: P-GJ7RY
kind: problem
title: $C([0,1])$ is complete in the uniform norm but not in the $L^1$ norm
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Completeness
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2019 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2019.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: problem
Let $C([0,1])$ be the space of continuous real-valued functions on $[0,1]$.

1. Prove that $C([0,1])$ is complete under the uniform norm
\[
\|f\|_\infty:=\sup_{x\in[0,1]}|f(x)|.
\]

2. Prove that $C([0,1])$ is not complete under the $L^1$ norm
\[
\|f\|_1:=\int_0^1|f(x)|\,dx.
\]
:::

::: solution
<1>1. Completeness in the uniform norm.
::: proof
Let $(f_n)$ be Cauchy in $\|\cdot\|_\infty$. For each $x\in[0,1]$, the real sequence $(f_n(x))$ is Cauchy, so define
\[
f(x):=\lim_{n\to\infty}f_n(x).
\]
Given $\varepsilon>0$, choose $N$ such that
\[
\|f_n-f_m\|_\infty<\varepsilon
\qquad(n,m\ge N).
\]
Fix $n\ge N$ and let $m\to\infty$. Then
\[
|f_n(x)-f(x)|\le\varepsilon
\]
for every $x$, hence
\[
\|f_n-f\|_\infty\le\varepsilon.
\]
Thus $f_n\to f$ uniformly. A uniform limit of continuous functions is continuous, so $f\in C([0,1])$ and the space is complete.
:::

<1>2. Failure of completeness in the $L^1$ norm.
::: proof
Let
\[
g=\mathbf1_{[1/2,1]}.
\]
For $n\ge2$, define $f_n\in C([0,1])$ by
\[
f_n(x)=
\begin{cases}
0,&x\le \frac12-\frac1n,\\
\frac n2\left(x-\frac12+\frac1n\right),&\frac12-\frac1n<x<\frac12+\frac1n,\\
1,&x\ge \frac12+\frac1n.
\end{cases}
\]
Then $0\le f_n\le1$ and $f_n=g$ outside an interval of length $2/n$. Therefore
\[
\|f_n-g\|_1\le\frac2n\to0.
\]
Hence $(f_n)$ is Cauchy in the $L^1$ norm.

If $C([0,1])$ were complete in that norm, there would exist $h\in C([0,1])$ with
\[
\|f_n-h\|_1\to0.
\]
But limits in $L^1$ are unique up to almost-everywhere equality, so $h=g$ almost everywhere. A continuous function equal almost everywhere to $g$ must be $0$ on $[0,1/2)$ and $1$ on $(1/2,1]$, contradicting continuity at $1/2$. Thus no such $h$ exists.

Therefore $C([0,1])$ is not complete under $\|\cdot\|_1$.
:::
:::
