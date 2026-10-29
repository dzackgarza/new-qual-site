---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W5
kind: problem
title: Equicontinuity upgrades pointwise convergence to uniform convergence
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Uniform Convergence
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Show that if $\{f_n\}$ is an equicontinuous sequence of functions on a compact set $K$ and $f_n\to f$ pointwise on $K$, then $f_n\to f$ uniformly on $K$.
:::

::: {.solution}

If $K$ is empty, uniform convergence is vacuous, so assume $K\ne\varnothing$. Fix $\varepsilon>0$.

::: pf

::: {.pf-step #s2}

For every $z\in K$, there exists $r_z>0$ such that for every $n$ and every $y\in K$ with $d(y,z)<r_z$,
$$
\abs{f_n(y)-f_n(z)}<\varepsilon/3,
\qquad \abs{f(y)-f(z)}\leq\varepsilon/3.
$$

::: pf-proof

Choose $r_z$ by equicontinuity with tolerance $\varepsilon/3$. The first inequality is its defining property. Taking limits in that inequality using pointwise convergence at $y$ and $z$ gives the second.

:::

:::

::: {.pf-step #s3}

There exist $z_1,\ldots,z_m\in K$ and $N\in\NN$ such that
$$
K\subseteq\bigcup_{i=1}^m B(z_i,r_{z_i}),
\qquad \abs{f_n(z_i)-f(z_i)}<\varepsilon/3
\quad(n\geq N,\ 1\leq i\leq m).
$$

::: pf-proof

The balls $B(z,r_z)$ cover $K$. Compactness gives a finite subcover. Pointwise convergence at each of its finitely many centers gives indices $N_i$ after which the displayed inequality holds; choose $N=\max_iN_i$.

:::

:::

::: pf-step

$\abs{f_n(x)-f(x)}<\varepsilon$ for every $x\in K$ and $n\geq N$; hence $f_n\to f$ uniformly on $K$.

::: pf-proof

Given $x\in K$, select $i$ with $d(x,z_i)<r_{z_i}$. For $n\geq N$, the triangle inequality gives
$$
\begin{aligned}
\abs{f_n(x)-f(x)}
&\leq \abs{f_n(x)-f_n(z_i)}+\abs{f_n(z_i)-f(z_i)}+\abs{f(z_i)-f(x)}\\
&<\varepsilon/3+\varepsilon/3+\varepsilon/3=\varepsilon.
\end{aligned}
$$
The first and third terms are bounded by step [](#s2){.pf-ref}, and the middle term by step [](#s3){.pf-ref}. Since $\varepsilon>0$ was arbitrary and $N$ does not depend on $x$, this is uniform convergence.

:::

:::

:::

:::
