---
schema: qual/card@1
id: FE-BGEZL
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
  target: FE-U5AQQ
review: draft
---

::: {.example}
Take limit along $y=x$ and compare to $y=0$:
\begin{align*}
f(x, y) = 
\begin{dcases}
{xy \over x^2 +y^2} & (x, y) \neq \vector 0 \\
0 & \text{else}
\end{dcases}
.\end{align*}
:::
