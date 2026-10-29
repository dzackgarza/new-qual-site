---
schema: qual/card@1
id: P-DDUA3
kind: problem
title: Every map $S^2\to S^1$ has $f(x)=f(-x)$
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Show that for every map $f: S^2 \to S^1$, there is a point $x\in S^2$ such that $f(x) = f(-x)$.
:::

::: {.solution}
Regard $S^1 \subseteq \CC$, and let $e\colon \RR \to S^1$, $t \mapsto e^{2\pi i t}$, be the universal covering map.

::: pf

::: {.pf-step #lift}
There is a map $F\colon S^2 \to \RR$ with $f = e \circ F$.

::: pf-proof
$S^2$ is simply connected and locally path connected, so the lifting criterion gives a lift of $f$ through the covering $e$.
:::

:::

::: {.pf-step #zero}
The map $h\colon S^2 \to \RR$, $h(x) = F(x) - F(-x)$, has a zero.

::: pf-proof
$h$ is continuous and $h(-x) = -h(x)$.
Pick any $x_0 \in S^2$.
If $h(x_0) = 0$, we are done.
Otherwise $h(x_0)$ and $h(-x_0)$ have opposite signs, and $S^2$ is connected, so the intermediate value theorem, applied along a path from $x_0$ to $-x_0$, gives a zero of $h$.
:::

:::

::: pf-step
Some $x \in S^2$ has $f(x) = f(-x)$.

::: pf-proof
By step [](#zero){.pf-ref}, some $x$ has $F(x) = F(-x)$.
By step [](#lift){.pf-ref}, $f(x) = e(F(x)) = e(F(-x)) = f(-x)$.
:::

:::

:::
:::
