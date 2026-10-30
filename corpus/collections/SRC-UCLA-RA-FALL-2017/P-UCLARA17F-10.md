---
schema: qual/card@1
id: P-UCLARA17F-10
kind: problem
title: Subharmonicity of $\sum\abs{f_n}^2$ for holomorphic $f_n$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 10. Let $\{f_n\}$ be a sequence of holomorphic functions on $\DD$ with the property that
$$
F(z):=\sum_{n=1}^{\infty}\abs{f_n(z)}^2\le1
$$
for all $z\in\DD$. Show that the series defining $F(z)$ converges uniformly on compact subsets of $\DD$ and that $F$ is subharmonic.
:::

::: {.solution}

For $N\ge1$, set
$$
g_N(z)\coloneqq\sum_{n=1}^N\abs{f_n(z)}^2.
$$

::: pf

::: {.pf-step #s1}

Each $g_N$ is continuous and subharmonic on $\DD$, and
$$
0\le g_N(z)\uparrow F(z)\le1
\qquad (z\in\DD).
$$


::: pf-proof

If $f$ is holomorphic, then
$$
\Delta \abs{f}^2=4\abs{f'}^2\ge0,
$$
so $\abs{f}^2$ is subharmonic. Finite sums of subharmonic functions are subharmonic, hence each $g_N$ is subharmonic; continuity is immediate from holomorphy of the $f_n$. The monotone convergence to $F$ is exactly the definition of the series, whose terms are nonnegative.

:::

:::

::: {.pf-step #s2}

The sequence $(g_N)$ is uniformly Cauchy on every compact subset of $\DD$.


::: pf-proof

::: pf-step

Fix a compact set $K\subset\DD$. There exist $\rho>0$ and points $w_1,\dots,w_m\in K$ such that
$$
K\subset\bigcup_{j=1}^m B(w_j,\rho)
\quad\text{and}\quad
\overline{B(w_j,2\rho)}\subset\DD
\ \text{for every }j.
$$


::: pf-proof

Since $K$ is compact and $\DD$ is open,
$$
d\coloneqq\operatorname{dist}(K,\partial\DD)>0.
$$
Choose $0<\rho<d/2$. The balls $B(w,\rho)$ with $w\in K$ cover $K$, so compactness gives a finite subcover with centers $w_1,\dots,w_m\in K$. The choice $2\rho<d$ gives the second assertion.

:::

:::

::: {.pf-step #s2-2}

If $M>N$ and $z\in B(w_j,\rho)$, then
$$
0\le g_M(z)-g_N(z)
\le
\frac{3}{2\pi}\int_0^{2\pi}
\bigl(F-g_N\bigr)(w_j+2\rho e^{i\theta})\,d\theta.
$$


::: pf-proof

The function
$$
v_{N,M}\coloneqq g_M-g_N
=
\sum_{n=N+1}^M\abs{f_n}^2
$$
is nonnegative and subharmonic. Applying the subharmonic Poisson inequality on the disk $B(w_j,2\rho)$ gives
$$
v_{N,M}(z)
\le
\frac1{2\pi}\int_0^{2\pi}
\frac{4\rho^2-\abs{z-w_j}^2}
{\abs{2\rho e^{i\theta}-(z-w_j)}^2}
v_{N,M}(w_j+2\rho e^{i\theta})\,d\theta.
$$
For $\abs{z-w_j}<\rho$, the Poisson kernel is bounded by
$$
\frac{2\rho+\abs{z-w_j}}{2\rho-\abs{z-w_j}}
\le3.
$$
Also $0\le v_{N,M}\le F-g_N$. Substituting these two bounds yields the stated estimate.

:::

:::

::: {.pf-step #s2-3}

For each $j$,
$$
\frac1{2\pi}\int_0^{2\pi}
\bigl(F-g_N\bigr)(w_j+2\rho e^{i\theta})\,d\theta
\longrightarrow0
\qquad (N\to\infty).
$$


::: pf-proof

By step [](#s1){.pf-ref}, $F-g_N\downarrow0$ pointwise and
$$
0\le F-g_N\le1.
$$
The constant function $1$ is integrable on $[0,2\pi]$, so dominated convergence gives the result.

:::

:::

::: {.pf-step #s2-4}

The sequence $(g_N)$ is uniformly Cauchy on $K$.


::: pf-proof

Fix $\varepsilon>0$. Since there are only finitely many centers $w_j$, step [](#s2-3){.pf-ref} gives an index $N_0$ such that for every $N\ge N_0$ and every $j$,
$$
\frac1{2\pi}\int_0^{2\pi}
\bigl(F-g_N\bigr)(w_j+2\rho e^{i\theta})\,d\theta
<\frac{\varepsilon}{3}.
$$
If $M>N\ge N_0$ and $z\in K$, choose $j$ with $z\in B(w_j,\rho)$. Step [](#s2-2){.pf-ref} then gives
$$
0\le g_M(z)-g_N(z)<\varepsilon.
$$
This bound is independent of $z\in K$.

:::

:::

::: pf-qed

Step [](#s2-4){.pf-ref} proves the claim of step [](#s2){.pf-ref} for an arbitrary compact set $K\subset\DD$.

:::

:::

:::

::: {.pf-step #s3}

The series
$$
\sum_{n=1}^{\infty}\abs{f_n(z)}^2
$$
converges uniformly on every compact subset of $\DD$ to $F$.


::: pf-proof

By step [](#s2){.pf-ref}, the partial sums $(g_N)$ are uniformly Cauchy on each compact set $K$. Since the pointwise limit is $F$ by step [](#s1){.pf-ref}, the uniform limit on $K$ is necessarily $F$.

:::

:::

::: {.pf-step #s4}

The function $F$ is subharmonic on $\DD$.


::: pf-proof

By step [](#s3){.pf-ref}, $F$ is a locally uniform limit of the continuous functions $g_N$, so $F$ is continuous. Let $\overline{B(z_0,r)}\subset\DD$. Since $g_N$ is subharmonic,
$$
g_N(z_0)
\le
\frac1{2\pi}\int_0^{2\pi}g_N(z_0+re^{i\theta})\,d\theta.
$$
The circle $\{z_0+re^{i\theta}:0\le\theta\le2\pi\}$ is compact, so step [](#s3){.pf-ref} gives uniform convergence of $g_N$ to $F$ on that circle. Passing to the limit yields
$$
F(z_0)
\le
\frac1{2\pi}\int_0^{2\pi}F(z_0+re^{i\theta})\,d\theta.
$$
Thus the continuous function $F$ satisfies the sub-mean-value inequality on every closed disk compactly contained in $\DD$, which is the defining criterion for subharmonicity.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves compact-uniform convergence of the series, and step [](#s4){.pf-ref} proves that its sum $F$ is subharmonic.

:::

:::

:::
