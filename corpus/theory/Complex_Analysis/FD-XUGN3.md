---
schema: qual/card@1
id: FD-XUGN3
kind: definition
title: Exponential definitions of $\cosh$ and $\sinh$
prompts:
- How are $\cosh$ and $\sinh$ written as exponentials?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Functions
relations: []
review: draft
---

::: {.definition}
For $z\in\CC$, the \dfn{hyperbolic cosine} and \dfn{hyperbolic sine} are
$$
\begin{aligned}
\cosh(z)&\coloneqq\frac{e^{z}+e^{-z}}{2},\\
\sinh(z)&\coloneqq\frac{e^{z}-e^{-z}}{2}.
\end{aligned}
$$
:::

::: {.remark}
With $iz$ in place of $z$, the same expressions give the trigonometric functions: $\cos(z)=\frac{e^{iz}+e^{-iz}}{2}=\cosh(iz)$ and $\sin(z)=\frac{e^{iz}-e^{-iz}}{2i}=-i\sinh(iz)$.
:::
