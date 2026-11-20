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

These are the addition formulas of [@Ahl73, ch. 2, §3.2, The Trigonometric Functions] taken at $a=b=t$ — the section's $\cos(a+b)=\cos a\cos b-\sin a\sin b$ and $\sin(a+b)=\cos a\sin b+\sin a\cos b$, which it derives from the addition theorem for the exponential — together with the section's definition of $\tan z$ as the quotient of $\sin$ and $\cos$: dividing $\sin 2t=2\sin t\cos t$ and $\cos 2t=\cos^2t-\sin^2t$ by $\cos^2t$ gives the two displays, and the hypothesis $\cos t\neq0$ is what that division needs.
:::
