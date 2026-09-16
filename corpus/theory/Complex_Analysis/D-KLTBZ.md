---
schema: qual/card@1
id: D-KLTBZ
kind: definition
title: Real differentiability of maps $\RR^n\to\RR^m$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Cauchy-Riemann
relations: []
review: draft
---

::: {.definition}
Let $U\subseteq\RR^n$ be open, let $F\colon U\to\RR^m$, and let $\vector p\in U$.
The map $F$ is \dfn{real-differentiable} at $\vector p$ if there exists a linear map $A\colon\RR^n\to\RR^m$ such that
$$
\lim_{\vector h\to0}\frac{\norm{F(\vector p+\vector h)-F(\vector p)-A(\vector h)}}{\norm{\vector h}}=0.
$$
:::

::: {.remark}
Equivalently, there is a function $R$, defined for $\vector h$ with $\vector p+\vector h\in U$, such that $\norm{R(\vector h)}\to0$ as $\vector h\to0$ and
$$
F(\vector p+\vector h)=F(\vector p)+A(\vector h)+\norm{\vector h}\,R(\vector h).
$$
In little-$o$ notation, $F(\vector p+\vector h)=F(\vector p)+A(\vector h)+o(\norm{\vector h})$ as $\vector h\to0$.
:::
