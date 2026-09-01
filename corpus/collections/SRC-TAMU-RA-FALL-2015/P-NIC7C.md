---
schema: qual/card@1
id: P-NIC7C
kind: problem
title: Every functional on $X$ factors through an injective closed-range operator
  $T:X\to Y$
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Functional Analysis
  - Norms
relations: []
review: draft
---

::: {.problem}
Let $X,Y$ be Banach spaces and $T:X\to Y$ be a one-to-one, bounded and linear operator for which the range $T(X)$ is closed in $Y$.
Show that for each continuous linear functional $\phi$ on $X$ there is a continuous linear functional $\psi$ on $Y$, so that $\phi=\psi\circ T$.
:::

:::{.solution}
By open mapping theorem, $\phi\circ T^{-1}$ is a well-defined linear bounded functional on $T(X)$. Then, by Hahn-Banach Thm, it can be extent to some $\psi$ on $Y$, say, $y\in T(X)$ implies that $\phi\circ T^{-1}(y)=\psi(y)$. It implies that $\psi(T(x))=\phi(x)$ for all $x\in X$.
:::
