---
schema: qual/card@1
id: FR-EDJWQ
kind: proof
title: Relationship between continuity and differentiability
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
Let $I\subseteq\RR$ be an open interval, let $f\colon I\to\RR$, and let $x_0\in I$.
If $f$ is differentiable at $x_0$, then $f$ is [[D-HHVPT|continuous]] at $x_0$.
:::

::: {.proof}
For $x\in I$ with $x\neq x_0$,
$$
f(x)-f(x_0)=(x-x_0)\,\frac{f(x)-f(x_0)}{x-x_0}.
$$
As $x\to x_0$, the first factor tends to $0$ and the second tends to $f'(x_0)$ by differentiability.
Hence $f(x)-f(x_0)\to0$, so $f$ is continuous at $x_0$.
:::

::: {.example}
The converse fails.
The function $f\colon\RR\to\RR$, $f(x)=\abs{x}$, is continuous at $0$.
Its difference quotient $\frac{f(h)-f(0)}{h}=\frac{\abs{h}}{h}$ equals $1$ for $h>0$ and $-1$ for $h<0$, so it has no limit as $h\to0$, and $f$ is not differentiable at $0$.
:::
