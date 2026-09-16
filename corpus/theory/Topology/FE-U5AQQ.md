---
schema: qual/card@1
id: FE-U5AQQ
kind: example
title: The function $xy/(x^2+y^2)$ is separately continuous but not jointly continuous
prompts:
- 'Give an example of a function $f: \RR^n \to \RR$ that is continuous in each variable but not continuous.'
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Counterexamples
  - Euclidean Spaces
relations:
- kind: variant-of
  target: FE-BGEZL
review: draft
---

::: {.example}
A function $\RR^2\to\RR$ can be continuous in each variable separately without being continuous.
Define $f\colon\RR^2\to\RR$ by
$$
f(x, y) =
\begin{cases}
\dfrac{xy}{x^2 + y^2}, & (x, y) \neq (0, 0), \\
0, & (x, y) = (0, 0).
\end{cases}
$$
For each $b\in\RR$ the map $x\mapsto f(x, b)$ is continuous on $\RR$, and for each $a\in\RR$ the map $y\mapsto f(a, y)$ is continuous on $\RR$; on the line $y = 0$ the function vanishes identically.
Along the line $y = x$, $f(t, t) = 1/2$ for $t\neq 0$, so $f(t,t)\to 1/2\neq f(0,0)$ as $t\to 0$, and $f$ is not continuous at the origin.
:::
