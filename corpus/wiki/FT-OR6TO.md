---
schema: qual/card@1
id: FT-OR6TO
kind: theorem
title: Riesz Representation Theorem
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
For $1\leq p <\infty$, $X \subset \RR^n$ measurable, $\Lambda \in L^p(X)\dual$, there exists a unique $g\in L^q(X)$ such that
$$\begin{align*}
\forall f\in L^p(X), \quad \Lambda(f) &= \int_X fg \\
\norm{\Lambda}_{L^p(X)\dual} &= \norm{g}_{L^q(X)}
\end{align*}$$
:::
