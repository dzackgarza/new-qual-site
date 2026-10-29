---
schema: qual/card@1
id: P-2V6GL
kind: problem
title: Connected versus locally connected spaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Find a space that is connected but not locally connected.
Can there be a space that is locally connected but not connected?
:::

::: {.solution}

Let $X = \theset{(x, \sin(1/x)) : x > 0} \cup \theset{(0, y) : -1 \le y \le 1}\subseteq\RR^2$ be the topologist's sine curve, and $p=(0,0)$.

::: pf

::: pf-step

$X$ is connected.

::: pf-proof

The graph $\theset{(x, \sin(1/x)) : x > 0}$ is connected as a continuous image of $(0,\infty)$, and $X$ is its closure in $\RR^2$. The closure of a connected set is connected.

:::

:::

::: pf-step

$X$ is not locally connected at $p$.

::: pf-proof

::: {.pf-step #component}

The component of $p$ in $U\coloneqq X\cap\bigl(\RR\times(-1/2,1/2)\bigr)$ is $C=\{0\}\times(-1/2,1/2)$.

::: pf-proof

$C$ is connected and contains $p$. Let $q=(x_q,\sin(1/x_q))\in U$ with $x_q>0$, and choose $m$ with $c=1/(\pi/2+2\pi m)<x_q$. Since $\sin(1/c)=1$, $U$ has no point with first coordinate $c$, so $U\cap\{x<c\}$ and $U\cap\{x>c\}$ are disjoint, relatively open, and cover $U$. They separate $p$ from $q$, so $q$ is not in the component of $p$.

:::

:::

::: pf-step

No connected open $W\subseteq X$ satisfies $p\in W\subseteq U$.

::: pf-proof

Such a $W$ lies in $C$ by step [](#component){.pf-ref}. But every neighborhood of $p$ in $X$ contains graph points $(x,\sin(1/x))$ with $x>0$ small and $\sin(1/x)=0$, which are not in $C$.

:::

:::

:::

:::

::: pf-step

$(0,1) \cup (2,3)\subseteq\RR$ is locally connected but not connected. So the answer to the second question is $\boxed{\text{yes}}$.

::: pf-proof

Each point has arbitrarily small open interval neighborhoods, which are connected. The two intervals are disjoint nonempty open sets that cover the space.

:::

:::

:::

:::
