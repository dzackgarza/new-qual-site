---
schema: qual/card@1
id: FF-5EBCJ
kind: fact
title: Discontinuity sets of real-valued functions
prompts:
- Characterize the set $D_f$ of discontinuities of a function.
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Countability
  - Measure Theory
relations: []
review: draft
---

::: {.fact}
Let $(X, d)$ be a metric space, let $f\colon X\to\RR$, and let $D_f\subseteq X$ be the set of points at which $f$ is not continuous.
For $x\in X$, the oscillation of $f$ at $x$ is
$$
\omega_f(x)\coloneqq\inf_{\delta>0}\,\sup\theset{\abs{f(y) - f(z)} \suchthat y, z\in B_\delta(x)}\in[0,\infty].
$$
Then $f$ is continuous at $x$ if and only if $\omega_f(x) = 0$, each set $\theset{x\in X\suchthat \omega_f(x)\geq 1/k}$ is closed, and
$$
D_f = \bigcup_{k\geq 1}\theset{x\in X\suchthat \omega_f(x)\geq 1/k}.
$$
In particular, $D_f$ is an [[D-RPOGQ|$F_\sigma$ set]].
:::

::: {.proof}
If $f$ is continuous at $x$ and $\varepsilon>0$, choose $\delta>0$ with $\abs{f(y)-f(x)}<\varepsilon$ for $y\in B_\delta(x)$; then $\abs{f(y)-f(z)}<2\varepsilon$ for $y,z\in B_\delta(x)$, so $\omega_f(x)\leq 2\varepsilon$.
Conversely, if $\omega_f(x) = 0$ and $\varepsilon>0$, some $\delta>0$ has $\abs{f(y)-f(x)}<\varepsilon$ for all $y\in B_\delta(x)$.
This proves the characterization of continuity, and hence the formula for $D_f$.

For closedness, suppose $\omega_f(x)<1/k$, and choose $\delta>0$ with $s\coloneqq\sup\theset{\abs{f(y)-f(z)}\suchthat y,z\in B_\delta(x)}<1/k$.
For $x'\in B_\delta(x)$, the ball $B_{\delta - d(x,x')}(x')$ is contained in $B_\delta(x)$, so $\omega_f(x')\leq s<1/k$.
Hence $\theset{\omega_f<1/k}$ is open.
:::

::: {.fact}
Let $X$ be a metric space, and let $f_n\colon X\to\RR$ be continuous functions converging [[D-IYDZU|pointwise]] to $f\colon X\to\RR$.
Then $D_f$ is [[D-5NODS|meager]] in $X$.
:::

::: {.fact title="Lebesgue criterion"}
Let $a<b$ and let $f\colon[a,b]\to\RR$ be bounded.
Then $f$ is Riemann integrable on $[a,b]$ if and only if $D_f$ has Lebesgue measure $0$.
:::

::: {.fact}
Let $I\subseteq\RR$ be an interval and let $f\colon I\to\RR$ be monotone.
Then $D_f$ is countable, and $f$ is differentiable at almost every point of $I$.
:::

::: {.proof}
We prove countability; differentiability almost everywhere is Lebesgue's differentiation theorem for monotone functions.
Assume $f$ is nondecreasing.
At each interior point $x$ of $I$ the one-sided limits $f(x^-)\leq f(x)\leq f(x^+)$ exist, and $f$ is discontinuous at $x$ if and only if $f(x^-)<f(x^+)$.
For interior points $x<x'$ of $D_f$, $f(x^+)\leq f(x'^-)$, so the open intervals $(f(x^-), f(x^+))$ for interior $x\in D_f$ are pairwise disjoint.
Choosing a rational number in each gives an injection of the interior points of $D_f$ into $\QQ$, and $I$ has at most two endpoints.
:::
