---
schema: qual/card@1
id: FE-U5AQQ
kind: example
title: The function $xy/(x^2+y^2)$ is separately continuous but not jointly continuous
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Counterexamples
  - Euclidean Spaces
relations: []
review: draft
---

::: {.example title="Give an example of a function $f: \RR^n \to \RR$ that is continuous in each variable but not continuous."}
Take limit along $y=x$ and compare to $y=0$:
$$
f(x, y) =
\begin{cases}
{xy \over x^2 +y^2} & (x, y) \neq \vector 0 \\
0 & \text{else}
\end{cases}
.$$
:::
