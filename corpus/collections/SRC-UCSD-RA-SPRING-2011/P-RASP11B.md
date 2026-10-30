---
schema: qual/card@1
id: P-RASP11B
kind: problem
title: 'Dyadic averaging operators converge to the identity in $L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - Approximate Identity
  - Lebesgue Points
  - Maximal Function
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Spring 2011 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
For each integer $k > 0$ denote by $\Delta_k(j) = [j 2^{-k}, (j+1) 2^{-k})]$ where $j \in \ZZ$, the dyadic rational interval of length $2^{-k}$ starting at $j 2^{-k}$.
Let $f \in L^1(\RR)$, and define
$$
A_k(f)(x) = \sum_j a_k(j) \mathbf{1}_{\Delta_k(j)}(x), \quad a_k(j) = \frac{1}{\setmeasure{\Delta_k(j)}} \int_{\Delta_k(j)} f(y) \, dy.
$$

(a) Prove that $\norm{A_k f}_{L^1(\RR)} \leq \norm{f}_{L^1(\RR)}$ for all $k > 0$, $f \in L^1(\RR)$.

(b) Show that if $f \in L^1(\RR)$ then $A_k(f) \to f$ in $L^1(\RR)$ as $k \to \infty$.
:::

::: {.solution}

::: pf

::: pf-step

Prove the $L^1$ contraction estimate.

::: pf-proof

On each dyadic interval $\Delta_k(j)$, the function $A_kf$ is constant with value
$$
a_k(j)=2^k\int_{\Delta_k(j)}f(y)\,dy.
$$
Therefore
$$
\begin{aligned}
\norm{A_kf}_1
&=\sum_j \abs{a_k(j)}\,\setmeasure{\Delta_k(j)}\\
&=\sum_j\abs{\int_{\Delta_k(j)}f(y)\,dy}\\
&\le\sum_j\int_{\Delta_k(j)}\abs{f(y)}\,dy\\
&=\norm{f}_1.
\end{aligned}
$$
Hence
$$
\boxed{\norm{A_kf}_1\le\norm{f}_1.}
$$

:::

:::

::: pf-step

Prove convergence for continuous compactly supported functions.

::: pf-proof

Let $g\in C_c(\RR)$. Since $g$ is uniformly continuous, let
$$
\omega_g(\delta)
:=\sup\{\abs{g(x)-g(y)}:\abs{x-y}\le\delta\}.
$$
Then $\omega_g(\delta)\to0$ as $\delta\downarrow0$.

If $x\in\Delta_k(j)$, then every $y\in\Delta_k(j)$ satisfies $\abs{x-y}\le2^{-k}$, so
$$
\begin{aligned}
\abs{A_kg(x)-g(x)}
&=\abs{2^k\int_{\Delta_k(j)}(g(y)-g(x))\,dy}\\
&\le \omega_g(2^{-k}).
\end{aligned}
$$
Moreover, if $\operatorname{supp}g\subset[-R,R]$, then both $g$ and $A_kg$ vanish outside a fixed bounded interval such as $[-R-1,R+1]$ for all $k\ge1$. Thus
$$
\norm{A_kg-g}_1
\le (2R+2)\,\omega_g(2^{-k})\longrightarrow0.
$$

:::

:::

::: pf-step

Pass to arbitrary $L^1$ functions by density.

::: pf-proof

Fix $f\in L^1(\RR)$ and $\varepsilon>0$. Since $C_c(\RR)$ is dense in $L^1(\RR)$, choose $g\in C_c(\RR)$ such that
$$
\norm{f-g}_1<\varepsilon.
$$
By Step 1,
$$
\norm{A_k(f-g)}_1\le\norm{f-g}_1<\varepsilon.
$$
Hence
$$
\begin{aligned}
\norm{A_kf-f}_1
&\le \norm{A_k(f-g)}_1+\norm{A_kg-g}_1+\norm{g-f}_1\\
&<2\varepsilon+\norm{A_kg-g}_1.
\end{aligned}
$$
Letting $k\to\infty$ and using Step 2 gives
$$
\limsup_{k\to\infty}\norm{A_kf-f}_1\le2\varepsilon.
$$
Since $\varepsilon$ is arbitrary,
$$
\boxed{A_kf\to f\text{ in }L^1(\RR).}
$$

:::

:::

:::

:::
