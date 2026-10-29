---
schema: qual/card@1
id: P-PRACT20-W3-13
kind: problem
title: Octants met by the graph of $e^{x+y}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
In how many of the standard octants of xyz-space does the graph of $f ( x , y ) = e ^ { x + y }$ appear?
:::

::: {.solution}
The graph is the surface $\{(x,y,e^{x+y}) : (x,y)\in\RR^2\}$.
A standard octant is a set on which each of $x$, $y$, $z$ has a fixed nonzero sign.

::: pf

::: {.pf-step #z-positive}
No point of the graph lies in an octant with $z<0$.

::: pf-proof
The exponential function is positive on $\RR$, so every point of the graph has $z=e^{x+y}>0$.
:::

:::

::: {.pf-step #xy-signs}
For each pair of signs $(s,t)$ with $s,t\in\{1,-1\}$, some point of the graph has $x$ of sign $s$ and $y$ of sign $t$.

::: pf-proof
The point $(s,t,e^{s+t})$ lies on the graph, and its first two coordinates are $s$ and $t$.
:::

:::

::: pf-step
The graph appears in exactly $\boxed{4}$ octants.

::: pf-proof
By steps [](#xy-signs){.pf-ref} and [](#z-positive){.pf-ref}, the graph meets each of the four octants with $z>0$.
By step [](#z-positive){.pf-ref}, it meets none of the four octants with $z<0$.
:::

:::

:::

:::
