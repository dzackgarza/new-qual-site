---
schema: qual/card@1
id: P-IEZIG
kind: problem
title: Algebraic and transcendental elements
classification:
  areas:
  - algebra
  topics:
  - Transcendence
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
What does it mean for an element to be algebraic or transcendental?
Which is $x\in \CC(x)$?
What is an example of a clearly non-algebraic element of a field?
:::

::: {.solution}
Let $K\subseteq F$ be a field extension. An element $\alpha\in F$ is algebraic over $K$ if $f(\alpha)=0$ for some nonzero $f\in K[t]$, and transcendental over $K$ otherwise.

::: pf

::: pf-step

The element $x\in\CC(x)$ is $\boxed{\text{transcendental over }\CC}$.

::: pf-proof

If $f=\sum_{i=0}^n c_it^i\in\CC[t]$ satisfies $f(x)=0$ in $\CC(x)$, then $\sum_i c_ix^i$ is the zero polynomial in $\CC[x]\subseteq\CC(x)$, so every $c_i=0$ and $f=0$.

:::

:::

::: pf-step

The number $\pi\in\RR$ is transcendental over $\QQ$, while $i\in\CC$ is algebraic over $\QQ$.

::: pf-proof

The first statement is the Lindemann theorem. The second holds because $i$ is a root of $t^2+1\in\QQ[t]$.

:::

:::

:::

:::
