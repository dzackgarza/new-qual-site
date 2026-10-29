---
schema: qual/card@1
id: E-2BLQW
kind: problem
title: Connectedness versus path-connectedness
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
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}

Show that:

(a) Connected does not imply path connected.

(b) Connected and locally path connected *does* imply path connected.

(c) Path connected implies connected.

:::

::: {.solution}

::: pf

::: pf-step

(a) Connected need not imply path-connected.

::: pf-proof

Consider the closed topologist's sine curve
$$
S=\left\{(x,\sin(1/x)):0<x\le1\right\}\cup(\{0\}\times[-1,1]).
$$
The graph part is connected as the continuous image of $(0,1]$, and $S$ is its closure, so $S$ is connected.
Suppose a path $\gamma(t)=(x(t),y(t))$, $t \in [0,1]$, in $S$ joined a point of the vertical segment to a point of the graph. Let
$$
t_0=\sup\{t:x(t)=0\}.
$$
By continuity $x(t_0)=0$, so $t_0<1$, and $x(t)>0$ for $t>t_0$. For each $\delta>0$ with $t_0 + \delta \le 1$, the intermediate value theorem applied to $x$ on $[t_0, t_0+\delta]$ shows that $x$ takes every value in $(0, x(t_0+\delta)]$, in particular the values
$$
\frac1{\pi/2+2\pi n}
\quad\text{and}\quad
\frac1{3\pi/2+2\pi n}
$$
for all large $n$. At these points $\gamma$ lies on the graph, where $y=1$ and $y=-1$, respectively. Hence $y(t)$ takes both values $\pm 1$ at times arbitrarily close to $t_0$, contradicting continuity of $y$ at $t_0$. Thus $S$ is not path-connected.

:::

:::

::: pf-step

(b) Connected and locally path-connected implies path-connected.

::: pf-proof

Fix $x_0\in X$ and let $P$ be its path component. Local path-connectedness implies every path component is open: a path-connected open neighborhood of any point lies in that point's path component. Hence $P$ is open, and its complement, being the union of the other open path components, is open as well. Thus $P$ is clopen. Since $X$ is connected and $P\ne\varnothing$, we have $P=X$.

:::

:::

::: pf-step

(c) Path-connected spaces are connected.

::: pf-proof

Let $X$ be path-connected and nonempty, and fix $x_0\in X$. For each $x\in X$, choose a path from $x_0$ to $x$. Its image is connected, and all these images contain $x_0$. Their union is $X$, so $X$ is connected.

:::

:::

:::

:::
