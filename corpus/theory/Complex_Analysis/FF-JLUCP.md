---
schema: qual/card@1
id: FF-JLUCP
kind: fact
title: Double-angle formulas in terms of $\tan t$
slogan: 'Double angles become rational functions of $\tan t$: sine gets $2u/(1+u^2)$ and cosine gets $(1-u^2)/(1+u^2)$.'
prompts:
- How are $\sin(2t)$ and $\cos(2t)$ written in terms of $\tan(t)$?
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
relations: []
review: draft
---

::: {.fact}
For every $t\in\RR$ with $\cos t\neq0$,
$$
\begin{aligned}
\sin(2t) &= {2\tan(t) \over 1+\tan^2(t)}, \\
\cos(2t) &= {1-\tan^2(t) \over 1+\tan^2(t)}.
\end{aligned}
$$
:::
