---
schema: qual/card@1
id: P-RASP11B
kind: problem
title: "Dyadic averaging operators converge to the identity in L^1"
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

::: problem
For each integer $k > 0$ denote by $\Delta_k(j) = [j 2^{-k}, (j+1) 2^{-k})]$ where $j \in \mathbb{Z}$, the dyadic rational interval of length $2^{-k}$ starting at $j 2^{-k}$.
Let $f \in L^1(\mathbb{R})$, and define
$$
A_k(f)(x) = \sum_j a_k(j) \mathbf{1}_{\Delta_k(j)}(x), \quad a_k(j) = \frac{1}{|\Delta_k(j)|} \int_{\Delta_k(j)} f(y) \, dy.
$$

(a) Prove that $\|A_k f\|_{L^1(\mathbb{R})} \leq \|f\|_{L^1(\mathbb{R})}$ for all $k > 0$, $f \in L^1(\mathbb{R})$.

(b) Show that if $f \in L^1(\mathbb{R})$ then $A_k(f) \to f$ in $L^1(\mathbb{R})$ as $k \to \infty$.
:::

::: solution
<1>1. Prove the $L^1$ contraction estimate.
::: proof
On each dyadic interval $\Delta_k(j)$, the function $A_kf$ is constant with value
\[
a_k(j)=2^k\int_{\Delta_k(j)}f(y)\,dy.
\]
Therefore
\[
\begin{aligned}
\|A_kf\|_1
&=\sum_j |a_k(j)|\,|\Delta_k(j)|\\
&=\sum_j\left|\int_{\Delta_k(j)}f(y)\,dy\right|\\
&\le\sum_j\int_{\Delta_k(j)}|f(y)|\,dy\\
&=\|f\|_1.
\end{aligned}
\]
Hence
\[
\boxed{\|A_kf\|_1\le\|f\|_1.}
\]
:::

<1>2. Prove convergence for continuous compactly supported functions.
::: proof
Let $g\in C_c(\mathbb R)$. Since $g$ is uniformly continuous, let
\[
\omega_g(\delta)
:=\sup\{|g(x)-g(y)|:|x-y|\le\delta\}.
\]
Then $\omega_g(\delta)\to0$ as $\delta\downarrow0$.

If $x\in\Delta_k(j)$, then every $y\in\Delta_k(j)$ satisfies $|x-y|\le2^{-k}$, so
\[
\begin{aligned}
|A_kg(x)-g(x)|
&=\left|2^k\int_{\Delta_k(j)}(g(y)-g(x))\,dy\right|\\
&\le \omega_g(2^{-k}).
\end{aligned}
\]
Moreover, if $\operatorname{supp}g\subset[-R,R]$, then both $g$ and $A_kg$ vanish outside a fixed bounded interval such as $[-R-1,R+1]$ for all $k\ge1$. Thus
\[
\|A_kg-g\|_1
\le (2R+2)\,\omega_g(2^{-k})\longrightarrow0.
\]
:::

<1>3. Pass to arbitrary $L^1$ functions by density.
::: proof
Fix $f\in L^1(\mathbb R)$ and $\varepsilon>0$. Since $C_c(\mathbb R)$ is dense in $L^1(\mathbb R)$, choose $g\in C_c(\mathbb R)$ such that
\[
\|f-g\|_1<\varepsilon.
\]
By Step 1,
\[
\|A_k(f-g)\|_1\le\|f-g\|_1<\varepsilon.
\]
Hence
\[
\begin{aligned}
\|A_kf-f\|_1
&\le \|A_k(f-g)\|_1+\|A_kg-g\|_1+\|g-f\|_1\\
&<2\varepsilon+\|A_kg-g\|_1.
\end{aligned}
\]
Letting $k\to\infty$ and using Step 2 gives
\[
\limsup_{k\to\infty}\|A_kf-f\|_1\le2\varepsilon.
\]
Since $\varepsilon$ is arbitrary,
\[
\boxed{A_kf\to f\text{ in }L^1(\mathbb R).}
\]
:::
:::
