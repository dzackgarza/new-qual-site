---
schema: qual/card@1
id: P-BKCZH
kind: problem
title: $|f'|\le k|f|$ and $f(0)=0$ imply $f\equiv 0$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the preserved UNL January 23, 2019 qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---


::: problem
Suppose that $f:[0,1]\to\mathbb R$ is differentiable, $f(0)=0$, and there is $k>0$ such that
\[
|f'(x)|\le k|f(x)|
\qquad(x\in[0,1]).
\]
Prove that $f(x)=0$ for all $x\in[0,1]$.
:::

::: solution
<1>1. Obtain an integral inequality.
::: proof
Since $f$ is continuous on $[0,1]$, let
\[
M:=\max_{[0,1]}|f|<\infty.
\]
The derivative bound gives $|f'|\le kM$, so $f$ is Lipschitz and hence absolutely continuous. Therefore, using $f(0)=0$,
\[
|f(x)|
=\left|\int_0^x f'(t)\,dt\right|
\le k\int_0^x |f(t)|\,dt
\qquad(0\le x\le1).
\]
:::

<1>2. Iterate the inequality.
::: proof
We claim that for every integer $n\ge1$,
\[
|f(x)|\le M\frac{(kx)^n}{n!}
\qquad(0\le x\le1).
\]
For $n=1$, Step 1 and $|f(t)|\le M$ give
\[
|f(x)|\le kMx.
\]
If the estimate holds for $n$, then Step 1 gives
\[
|f(x)|
\le k\int_0^x M\frac{(kt)^n}{n!}\,dt
=M\frac{(kx)^{n+1}}{(n+1)!}.
\]
Thus the claim follows by induction.
:::

<1>3. Let the iteration order tend to infinity.
::: proof
For each fixed $x\in[0,1]$,
\[
0\le |f(x)|\le M\frac{(kx)^n}{n!}\longrightarrow0
\qquad(n\to\infty).
\]
Hence $f(x)=0$. Since $x$ was arbitrary,
\[
\boxed{f\equiv0\text{ on }[0,1].}
\]
:::
:::
