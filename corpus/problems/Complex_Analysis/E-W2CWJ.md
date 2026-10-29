---
schema: qual/card@1
id: E-W2CWJ
kind: problem
title: Removable singularity at infinity iff constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Removable Singularities
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Let $f$ be entire.
Show that $f$ has a removable singularity at $z_0 = \infty$ iff $f$ is constant.
:::

::: {.solution}
::: pf

::: pf-step
If $f$ has a removable singularity at $\infty$, then $f$ is constant.

::: pf-proof
Removability at $\infty$ means $f$ is bounded on $\abs{z} > R$ for some $R$, say by $M_1$.
The closed disk $\abs{z}\le R$ is compact and $f$ is continuous, so $f$ is bounded there, say by $M_2$.
Then $f$ is a bounded entire function, with $\abs{f}\le\max(M_1, M_2)$, and Liouville's theorem shows that $f$ is constant.
:::

:::

::: pf-step
If $f$ is constant, then $f$ has a removable singularity at $\infty$.

::: pf-proof
$f(1/w)$ is constant on $w\neq0$, hence bounded near $w=0$, so $0$ is a removable singularity of $f(1/w)$ by Riemann's theorem.
:::

:::

:::

:::
