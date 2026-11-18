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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The step function's measurability and the identity of its integral with S_+ are now stated and proved (including that the point 1 is omitted, a null set), the one-sided control of the interval containing x is written out (0 <= y - x < delta, so lower semicontinuity applies), and Fatou's lemma is applied to a nonnegative sequence with the liminf identified with f almost everywhere. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Let $f:[0,1]\to[0,\infty)$ be lower semicontinuous. For a partition
$$
P:0=t_0<t_1<\cdots<t_N=1,
$$
define the lower Riemann sum
$$
S_+(f,P)=\sum_{j=1}^N\left(\inf_{x\in[t_{j-1},t_j)}f(x)\right)(t_j-t_{j-1}).
$$
Let the mesh be
$$
\partitionmesh{P}=\max_j(t_j-t_{j-1}).
$$
Prove that
$$
S_+(f,P)\longrightarrow\int_0^1 f(x)\,dx
$$
as $\partitionmesh{P}\to0$, where the integral is the Lebesgue integral.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the JHU examination papers and the card records only the statement. The argument is the card's own.

For a partition $P:0=t_0<\cdots<t_N=1$ let $s_P$ be the step function with $s_P(x)=\inf_{y\in[t_{j-1},t_j)}f(y)$ for $x\in[t_{j-1},t_j)$.

::: pf

::: {.pf-step #step}
$S_+(f,P)=\int_0^1s_P(x)\,dx$ and $0\le s_P\le f$ almost everywhere.

::: pf-proof
$s_P$ is constant, equal to $m_j=\inf_{[t_{j-1},t_j)}f$, on each $[t_{j-1},t_j)$, and these intervals are disjoint and cover $[0,1)$; the single point $1$ is omitted and has measure $0$. So $s_P$ is measurable and $\int_0^1s_P=\sum_jm_j(t_j-t_{j-1})=S_+(f,P)$. For $x\in[t_{j-1},t_j)$ the value $m_j$ is an infimum over a set containing $x$, so $m_j\le f(x)$; and $m_j\ge0$ because $f\ge0$.
:::

:::

::: {.pf-step #pointwise}
For every $x\in[0,1)$, $s_{P_k}(x)\to f(x)$ whenever $\partitionmesh{P_k}\to0$.

::: pf-proof
Fix $x<1$ and $\varepsilon>0$. Lower semicontinuity gives $\delta>0$ with $f(y)>f(x)-\varepsilon$ for all $y$ with $\abs{y-x}<\delta$. For large $k$ let $[t_{j-1},t_j)$ be the interval of $P_k$ containing $x$; then $t_j-t_{j-1}\le\partitionmesh{P_k}<\delta$, and every $y$ in that interval satisfies $0\le y-x<\delta$, so $f(y)>f(x)-\varepsilon$ there and hence $s_{P_k}(x)\ge f(x)-\varepsilon$. With $s_{P_k}(x)\le f(x)$ from step [](#step){.pf-ref}, this gives the convergence. Only $x<1$ is needed, and $\{1\}$ is a null set.
:::

:::

::: {.pf-step #fatou}
$\displaystyle\int_0^1f\le\liminf_kS_+(f,P_k)$.

::: pf-proof
$s_{P_k}\ge0$ are measurable with $s_{P_k}\to f$ almost everywhere by step [](#pointwise){.pf-ref}, so Fatou's lemma gives $\int_0^1f=\int_0^1\liminf_ks_{P_k}\le\liminf_k\int_0^1s_{P_k}=\liminf_kS_+(f,P_k)$, using step [](#step){.pf-ref}.
:::

:::

::: {.pf-step #limsup}
$\displaystyle\limsup_kS_+(f,P_k)\le\int_0^1f$.

::: pf-proof
$s_{P_k}\le f$ by step [](#step){.pf-ref}, so $\int_0^1s_{P_k}\le\int_0^1f$ for every $k$ and hence so is the limsup.
:::

:::

::: {.pf-step}
$S_+(f,P)\to\int_0^1f$ as $\partitionmesh{P}\to0$.

::: pf-proof
For any sequence of partitions with mesh tending to $0$, steps [](#fatou){.pf-ref} and [](#limsup){.pf-ref} squeeze the liminf and limsup together, so $S_+(f,P_k)\to\int_0^1f$. As this holds for every such sequence, the net convergence as the mesh tends to $0$ follows.
:::

:::

:::
:::
