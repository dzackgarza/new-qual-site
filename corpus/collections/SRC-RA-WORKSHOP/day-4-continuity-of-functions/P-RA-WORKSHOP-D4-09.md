---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-09
kind: problem
title: Continuity of a running supremum
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Suppose that $f:[a,b]\to\RR$ is continuous and define $M:[a,b]\to\RR$ by $$M(x)=\sup\{f(y):a\le y\le x\}.$$ Show that $M$ is continuous on $[a,b]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $M$ is nondecreasing.

::: pf-proof

If $a\leq x\leq y\leq b$, the inclusion $[a,x]\subseteq[a,y]$ implies
$$
M(x)=\sup_{t\in[a,x]}f(t)\leq\sup_{t\in[a,y]}f(t)=M(y).
$$

:::

:::

::: {.pf-step #s2}

The function $M$ is uniformly continuous on $[a,b]$.

::: pf-proof

Fix $\varepsilon>0$. Since $f$ is continuous on the compact interval $[a,b]$, it is uniformly continuous. Choose $\delta>0$ such that $\abs{f(u)-f(v)}<\varepsilon/2$ whenever $u,v\in[a,b]$ and $\abs{u-v}<\delta$. Given $x,y\in[a,b]$ with $\abs{x-y}<\delta$, assume $x\leq y$. Every $t\in[x,y]$ satisfies $f(t)<f(x)+\varepsilon/2$, so
$$
M(y)=\max\left\{M(x),\sup_{t\in[x,y]}f(t)\right\}
\leq\max\left\{M(x),f(x)+\varepsilon/2\right\}
\leq M(x)+\varepsilon/2.
$$
By step [](#s1){.pf-ref}, $0\leq M(y)-M(x)\leq\varepsilon/2<\varepsilon$. Interchanging $x$ and $y$ gives the same bound in the other order. Hence $\abs{M(x)-M(y)}<\varepsilon$.

:::

:::

::: pf-qed

Uniform continuity in step [](#s2){.pf-ref} implies continuity at every point of $[a,b]$.

:::

:::

:::
