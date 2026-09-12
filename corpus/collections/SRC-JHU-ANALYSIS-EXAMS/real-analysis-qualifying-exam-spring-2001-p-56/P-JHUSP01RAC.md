---
schema: qual/card@1
id: P-JHUSP01RAC
kind: problem
title: "Lower semicontinuous functions and lower Riemann sums"
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
  - Lower Semicontinuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the JHU Real Analysis Qualifying Exam, Spring 2001, in the preserved exam collection. The source says |P| is the smallest subinterval length; that cannot control refinement. The corrected statement uses the standard mesh, the largest subinterval length.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f:[0,1]\to[0,\infty)$ be lower semicontinuous. For a partition
\[
P:0=t_0<t_1<\cdots<t_N=1,
\]
define the lower Riemann sum
\[
S_+(f,P)=\sum_{j=1}^N\left(\inf_{x\in[t_{j-1},t_j)}f(x)\right)(t_j-t_{j-1}).
\]
Let the mesh be
\[
|P|=\max_j(t_j-t_{j-1}).
\]
Prove that
\[
S_+(f,P)\longrightarrow\int_0^1 f(x)\,dx
\]
as $|P|\to0$, where the integral is the Lebesgue integral.
:::

::: {.solution}
For a partition $P$, define the lower-step function
\[
s_P(x)=\inf_{y\in[t_{j-1},t_j)}f(y)
\qquad\text{when }x\in[t_{j-1},t_j).
\]
Then
\[
S_+(f,P)=\int_0^1 s_P(x)\,dx
\]
and
\[
0\le s_P(x)\le f(x)
\]
for $x<1$.

Now let $(P_k)$ be any sequence of partitions with $|P_k|\to0$. Fix $x\in[0,1)$. Since $f$ is lower semicontinuous, for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
|y-x|<\delta\implies f(y)>f(x)-\varepsilon.
\]
For all sufficiently large $k$, the subinterval of $P_k$ containing $x$ has length less than $\delta$, hence is contained in $(x-\delta,x+\delta)$. Therefore
\[
f(x)-\varepsilon\le s_{P_k}(x)\le f(x).
\]
Thus
\[
s_{P_k}(x)\longrightarrow f(x)
\]
for every $x\in[0,1)$.

By Fatou's lemma,
\[
\int_0^1f\le\liminf_{k\to\infty}\int_0^1s_{P_k}.
\]
On the other hand, $s_{P_k}\le f$, so
\[
\limsup_{k\to\infty}\int_0^1s_{P_k}\le\int_0^1f.
\]
Hence
\[
S_+(f,P_k)=\int_0^1s_{P_k}\longrightarrow\int_0^1f.
\]
Since this holds for every sequence with mesh tending to zero, the desired limit follows.
:::
