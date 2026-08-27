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

<1>2. $f$ has a single jump (from $-1$ to $3$) at $0$; $\alpha$ has a single jump (from $-2$ to $1$) at $0$.
Proof: both functions are constant on each side of $0$.

<1>3. $f \in \mathcal R(\alpha)$ on $[-1,1]$.
<2>1. The Stieltjes sum for a partition containing $0$ as a partition point: only the interval straddling $0$ contributes.
Proof: $\Delta\alpha_i = 0$ except across $0$ where $\Delta\alpha = 1 - (-2) = 3$.
<2>2. With $0 = x_j$ a partition point, the terms at $j$ and $j+1$: $f(x_j^*)\Delta\alpha_j + f(x_{j+1}^*)\Delta\alpha_{j+1}$ with $\Delta\alpha_j = \alpha(0) - \alpha(x_{j-1}) = -2 - (-2) = 0$ and $\Delta\alpha_{j+1} = \alpha(x_{j+1}) - \alpha(0) = 1 - (-2) = 3$.
Proof: direct computation using <1>1: $\alpha(0) = -2$ (since $0 \in [-1,0]$), so the jump is between $0$ and the next point, with size $3$.
<2>3. The sum is $3 f(t_{j+1})$ with $t_{j+1} \in [0, x_{j+1}]$; as mesh $\to 0$, $t_{j+1} \to 0^+$, so $f(t_{j+1}) \to f(0^+) = 3$?
$f(0) = 3$ (as $0 \in [0,2]$), and by right-continuity of $f$ at $0$: $f(t) = 3$ for all $t \in (0, 1]$, so $f(t_{j+1}) = 3$ exactly.
Proof: for $t_{j+1} > 0$, $f(t_{j+1}) = 3$ by definition of $f$ on $(0, 2]$; so the sum is exactly $9$.
<2>4. Q.E.D. Proof: <2>1–<2>3 show the Stieltjes sums converge to $9$: $f \in \mathcal R(\alpha)$ and $\int_{-1}^1 f\,d\alpha = 9$.
<2>5. Sanity check via the general jump formula: $\int f\,d\alpha = f(0)\cdot(\alpha(0^+) - \alpha(0)) + f(0)(\alpha(0) - \alpha(0^-))$-style; with our convention the integral equals $f(0^+)(\alpha(0^+) - \alpha(0)) = 3 \cdot (1 - (-2)) = 9$.
Proof: for step functions the Stieltjes integral is $\sum f(c_i)\Delta\alpha(c_i)$ summed over jump points, with $\Delta\alpha(0) = \alpha(0^+) - \alpha(0) = 3$ and $f$ evaluated to the right of the jump (value $3$); matches <2>4.
:::
