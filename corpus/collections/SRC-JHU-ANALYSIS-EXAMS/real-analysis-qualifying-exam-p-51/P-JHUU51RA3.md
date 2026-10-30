---
schema: qual/card@1
id: P-JHUU51RA3
kind: problem
title: "The $1/5$-Hölder norm $\\abs{f(0)}+[f]_{1/5}$ is complete on $[0,1]$"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 3 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $X$ be the set of functions $f:[0,1]\to\RR$ for which
$$
\norm{f}:=\abs{f(0)}+\sup_{x\ne y}\frac{\abs{f(x)-f(y)}}{\abs{x-y}^{1/5}}<\infty.
$$
Prove that $(X,\norm{\cdot})$ is a Banach space.
:::

::: {.solution}
Write
$$
[f]_{1/5}:=\sup_{x\ne y}\frac{\abs{f(x)-f(y)}}{\abs{x-y}^{1/5}}.
$$
Then
$$
\norm{f}=\abs{f(0)}+[f]_{1/5}.
$$

::: pf

::: pf-step

$X$ is a vector space and $\norm{\cdot}$ is a norm.

::: pf-proof

If $f,g\in X$ and $a,b\in\RR$, then
$$
[af+bg]_{1/5}\le \abs{a}[f]_{1/5}+\abs{b}[g]_{1/5}<\infty,
$$
so $af+bg\in X$. The seminorm $[\cdot]_{1/5}$ is homogeneous and subadditive, hence so is $\norm{\cdot}$.

If $\norm{f}=0$, then $f(0)=0$ and $[f]_{1/5}=0$, so $f(x)=f(y)$ for all $x,y$. Thus $f$ is constant, and since $f(0)=0$, one has $f\equiv0$. Therefore $\norm{\cdot}$ is a norm.

:::

:::

::: {.pf-step #s2}

The norm controls uniform convergence.

::: pf-proof

For every $f\in X$ and $x\in[0,1]$,
$$
\abs{f(x)}\le \abs{f(0)}+\abs{f(x)-f(0)}
\le \abs{f(0)}+[f]_{1/5}\abs{x}^{1/5}
\le \norm{f}.
$$
Hence
$$
\norm{f}_\infty\le\norm{f}.
$$

:::

:::

::: pf-step

$X$ is complete.

::: pf-proof

Let $(f_n)$ be Cauchy in $\norm{\cdot}$. By step [](#s2){.pf-ref}, it is uniformly Cauchy, so there is a function $f:[0,1]\to\RR$ such that
$$
f_n\to f
$$
uniformly.

Fix $\varepsilon>0$. Since $(f_n)$ is Cauchy in $\norm{\cdot}$, there exists $N$ such that for all $m,n\ge N$,
$$
\abs{f_n(0)-f_m(0)}+[f_n-f_m]_{1/5}<\varepsilon.
$$
Fix $n\ge N$ and let $m\to\infty$. Uniform convergence gives
$$
\abs{f_n(0)-f(0)}\le\varepsilon,
$$
and for every $x\ne y$,
$$
\abs{(f_n-f)(x)-(f_n-f)(y)}
=\lim_{m\to\infty}\abs{(f_n-f_m)(x)-(f_n-f_m)(y)}
\le\varepsilon \abs{x-y}^{1/5}.
$$
Therefore
$$
[f_n-f]_{1/5}\le\varepsilon,
$$
so
$$
\norm{f_n-f}\le2\varepsilon.
$$
In particular $f_n\to f$ in $\norm{\cdot}$. Since $f=f_n-(f_n-f)$ and both terms have finite Hölder seminorm, $f\in X$. Thus every Cauchy sequence converges in $X$, and $X$ is Banach.

:::

:::

:::

:::
