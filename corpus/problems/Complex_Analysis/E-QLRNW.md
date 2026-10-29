---
schema: qual/card@1
id: E-QLRNW
kind: problem
title: Uniform limits of derivatives, term-by-term differentiation
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Cauchy Integral Formula
  - Power Series
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "differentiable functions" on Omega; for real-differentiable functions the conclusions fail, so the statement says complex differentiable on an open set. The source also reads "\sum{k\geq 0}", corrected to a subscripted sum.'
---

::: {.exercise}
Suppose $\Omega\subseteq\CC$ is open and $f_k: \Omega\to \CC$ is a sequence of complex differentiable functions converging locally uniformly to $f:\Omega\to \CC$.
Show that

(a) $f$ is continuous,

(b) $f$ is differentiable,

(c) $\theset{f_k'}\to f'$ locally uniformly.

Thus if $f(z) = \sum_{k\geq 0} c_k (z-z_0)^k$ is a power series, since $S_N\to f$ locally uniformly, $f$ can be differentiated term-by-term within its radius of convergence.
:::

::: {.solution}

All circles are positively oriented.

::: pf

::: {.pf-step #part-a}
(a) $f$ is continuous.

::: pf-proof
Each $f_k$ is continuous, and continuity is local; on each closed disc in $\Omega$, $f$ is a uniform limit of the continuous $f_k$.
:::

:::

::: {.pf-step #part-b}
(b) $f$ is holomorphic, and for $\overline{D_r(w)}\subseteq\Omega$ and $\abs{z-w}<r$, $f(z) = \frac{1}{2\pi i}\oint_{\abs{\xi-w}=r}\frac{f(\xi)}{\xi-z}\,d\xi$.

::: pf-proof
By the Cauchy integral formula, $f_k(z) = \frac{1}{2\pi i}\oint_{\abs{\xi-w}=r}\frac{f_k(\xi)}{\xi-z}\,d\xi$.
On the circle, $\frac{1}{\abs{\xi-z}}$ is bounded and $f_k\to f$ uniformly, so letting $k\to\infty$ gives the formula for $f$.
The right side is holomorphic in $z$ on $D_r(w)$, by differentiation under the integral sign, since $f$ is continuous by step [](#part-a){.pf-ref}.
:::

:::

::: {.pf-step #estimate}
If $\overline{D_{2r}(w)}\subseteq\Omega$, then $\sup_{\overline{D_r(w)}}\abs{f_k'-f'}\leq\frac1r\sup_{\overline{D_{2r}(w)}}\abs{f_k-f}$.

::: pf-proof
For $z\in\overline{D_r(w)}$, $\overline{D_r(z)}\subseteq\overline{D_{2r}(w)}$; by step [](#part-b){.pf-ref}, $f_k-f$ is holomorphic, and the Cauchy integral formula for the derivative gives
$$
\abs{f_k'(z)-f'(z)} = \abs{\frac{1}{2\pi i}\oint_{\abs{\xi-z}=r}\frac{f_k(\xi)-f(\xi)}{(\xi-z)^2}\,d\xi}\leq\frac{1}{2\pi}\cdot2\pi r\cdot\frac{1}{r^2}\sup_{\overline{D_{2r}(w)}}\abs{f_k-f}.
$$
:::

:::

::: {.pf-step #part-c}
(c) $f_k'\to f'$ locally uniformly.

::: pf-proof
Let $K\subseteq\Omega$ be compact.
Each $w\in K$ has $r_w>0$ with $\overline{D_{2r_w}(w)}\subseteq\Omega$; finitely many discs $D_{r_{w_j}}(w_j)$, $1\leq j\leq N$, cover $K$.
By step [](#estimate){.pf-ref},
$$
\sup_K\abs{f_k'-f'}\leq\max_{j}\frac{1}{r_{w_j}}\sup_{\overline{D_{2r_{w_j}}(w_j)}}\abs{f_k-f},
$$
which tends to $0$ since $f_k\to f$ uniformly on the compact union of the closed discs.
:::

:::

::: pf-step
A power series may be differentiated term by term inside its disc of convergence.

::: pf-proof
The partial sums $S_N$ are polynomials converging locally uniformly to $f$ on the disc of convergence, so by steps [](#part-b){.pf-ref} and [](#part-c){.pf-ref}, $f$ is holomorphic and $f' = \lim_N S_N' = \sum_{k\geq1}kc_k(z-z_0)^{k-1}$.
:::

:::

:::

:::

::: {.remark title="Holomorphy of the limit by Morera"}
Part (b) also follows from Morera's theorem: for a closed triangle $T$ in a disc in $\Omega$, $\int_{\partial T}f=\lim_k\int_{\partial T}f_k=0$ by uniform convergence on $\partial T$ and Goursat's theorem.
:::
