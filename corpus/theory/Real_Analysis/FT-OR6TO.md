---
schema: qual/card@1
id: FT-OR6TO
kind: theorem
title: Riesz representation theorem for the dual of $L^p$
prompts:
- State the Riesz representation theorem for $L^p(X)\dual$.
classification:
  areas:
  - real-analysis
  topics:
  - Riesz Representation
  - Lp Spaces
  - Dual Spaces
relations: []
review: draft
---

::: {.theorem}
Let $1\leq p <\infty$, let $q\in(1,\infty]$ be the conjugate exponent, $\frac1p+\frac1q=1$, and let $X \subseteq \RR^n$ be [[D-MDJII|Lebesgue measurable]].
For every bounded linear functional $\Lambda \in L^p(X)\dual$ there exists a unique $g\in L^q(X)$ such that
$$
\begin{aligned}
\Lambda(f) &= \int_X fg \quad \text{for all } f\in L^p(X), \\
\norm{\Lambda}_{L^p(X)\dual} &= \norm{g}_{L^q(X)} .
\end{aligned}
$$
:::
