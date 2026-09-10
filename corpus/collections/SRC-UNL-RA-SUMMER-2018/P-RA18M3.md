---
schema: qual/card@1
id: P-RA18M3
kind: problem
title: Riemann-Stieltjes integration against a step integrator on $[-2,2]$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 3 of the preserved UNL May 31, 2018 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Replaced the mesh-limit discussion by the correct refinement criterion for a discontinuous Riemann--Stieltjes integrator.
---

::: {.problem}
Define $f,\alpha\in\mathcal B([-2,2])$ by
$$
f(x):=\begin{cases}
-1,&x\in[-2,0),\\
3,&x\in[0,2],
\end{cases}
\qquad
\alpha(x):=\begin{cases}
-2,&x\in[-2,0],\\
1,&x\in(0,2].
\end{cases}
$$
Determine whether $f$ is Riemann--Stieltjes integrable with respect to $\alpha$ over $[-1,1]$.
If it is, evaluate $$\int_{-1}^{1}f(x)\,d\alpha(x).$$
:::

:::: {.solution}
**Goal:** Determine whether $f$ is Riemann–Stieltjes integrable w.r.t. $\alpha$ on $[-1,1]$, where $f = -1$ on $[-2,0)$, $3$ on $[0,2]$; $\alpha = -2$ on $[-2,0]$, $1$ on $(0,2]$.
If so, evaluate $\int_{-1}^1 f\,d\alpha$.

<1>1. The restriction to $[-1,1]$: $f(x) = -1$ on $[-1,0)$, $f(x) = 3$ on $[0,1]$; $\alpha(x) = -2$ on $[-1,0]$, $\alpha(x) = 1$ on $(0,1]$.
Proof: restrict the given definitions to $[-1,1]$.

<1>2. $f \in \mathcal R(\alpha)$ on $[-1,1]$ and the integral equals $9$.
<2>1. Use a partition that contains the jump point.
Proof: take the partition $P=\{-1,0,1\}$. If $Q$ is any refinement of $P$, then $\alpha$ is constant on every subinterval of $Q$ except the first subinterval $[0,q]$ immediately to the right of $0$. On that interval
\[
\alpha(q)-\alpha(0)=1-(-2)=3.
\]
<2>2. Every tagged Riemann--Stieltjes sum for every refinement of $P$ equals $9$.
Proof: on the exceptional interval $[0,q]$ one has $f\equiv3$, including at $0$. Hence its contribution is
\[
3\,[\alpha(q)-\alpha(0)]=3\cdot3=9,
\]
while every other interval contributes $0$ because its $\alpha$-increment is $0$. Thus the sum is independent of both the refinement and the tags.
<2>3. Apply the Riemann--Stieltjes refinement criterion.
Proof: given any $\varepsilon>0$, the partition $P$ above has the property that every tagged sum over every refinement of $P$ equals $9$, hence differs from $9$ by less than $\varepsilon$. Therefore
\[
\boxed{f\in\mathcal R(\alpha),\qquad \int_{-1}^1 f\,d\alpha=9.}
\]
:::
