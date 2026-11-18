---
schema: qual/card@1
id: P-BKS04-1A
kind: problem
title: Locally uniform convergence on $[a,b]$ is uniform
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Consider a sequence of functions $f_n\colon[a,b]\to\RR$ with the property that for each $x\in[a,b]$ there is an open interval $I_x$ containing $x$ such that $(f_n)_{n\geq1}$ converges uniformly in $I_x\cap[a,b]$. Show that $(f_n)_{n\geq1}$ converges uniformly in $[a,b]$.
:::

::: {.solution}

The argument is the card's own: local uniform convergence gives a pointwise limit, and compactness turns the local estimates into one global estimate.

::: pf

::: {.pf-step #pointwise}

$(f_{n})$ has a pointwise limit $f:[a,b]\to\RR$.

::: pf-proof

For each $x\in[a,b]$ the sequence converges uniformly on $I_{x}\cap[a,b]$, a set containing $x$, and uniform convergence on a set implies pointwise convergence at each of its points. So $(f_{n}(x))$ is a convergent sequence of reals for each $x$, and $f(x)=\lim_{n}f_{n}(x)$ defines the limit function.

:::

:::

::: {.pf-step #subcover}

Finitely many of the intervals $I_{x}$ cover $[a,b]$.

::: pf-proof

$[a,b]$ is closed and bounded, hence compact. The family $\{I_{x}:x\in[a,b]\}$ is an open cover of $[a,b]$ because each $I_{x}$ is an open interval containing $x$. So there are $x_{1},\dots,x_{m}$ with $[a,b]\subset I_{x_{1}}\cup\cdots\cup I_{x_{m}}$.

:::

:::

::: {.pf-step #estimate}

For every $\varepsilon>0$ there is $N$ with $\abs{f_{n}(x)-f(x)}\le\varepsilon$ for all $n\ge N$ and all $x\in[a,b]$.

::: pf-proof

Fix $\varepsilon>0$. On each $I_{x_{k}}$ the sequence converges uniformly to $f$ (the limit of a uniformly convergent sequence on a set agrees there with the pointwise limit), so there is $N_{k}$ with $\abs{f_{n}(y)-f(y)}\le\varepsilon$ for all $n\ge N_{k}$ and all $y\in I_{x_{k}}\cap[a,b]$. Let $N=\max(N_{1},\dots,N_{m})$. Given $x\in[a,b]$, step [](#subcover){.pf-ref} provides $k$ with $x\in I_{x_{k}}$, and for $n\ge N\ge N_{k}$ the estimate holds at $x$.

:::

:::

::: {.pf-step #conclusion}

$(f_{n})$ converges uniformly to $f$ on $[a,b]$.

::: pf-proof

Step [](#estimate){.pf-ref} is exactly the definition of uniform convergence of $(f_{n})$ to $f$ on $[a,b]$: one index $N$ works simultaneously for every point of the set.
$$
\boxed{f_{n}\to f\ \text{uniformly on } [a,b].}
$$

:::

:::

:::

:::
