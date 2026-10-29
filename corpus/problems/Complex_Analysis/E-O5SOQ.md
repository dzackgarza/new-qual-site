---
schema: qual/card@1
id: E-O5SOQ
kind: problem
title: Entire functions with $|f(z)|\le|\sin z|$ are $c\sin z$ with $|c|\le 1$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Removable Singularities
  - Entire Functions
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ is entire and for every $z$,
$$
\abs{f(z)}\leq \abs{\sin(z)}.
$$
Characterize all possibilities for $f$.
:::

::: {.solution}

::: pf

::: {.pf-step #constant}
$g(z) \coloneqq f(z)/\sin(z)$ extends to a constant $c$ with $\abs{c}\leq 1$.

::: pf-proof
$g$ is holomorphic off the zeros $\pi\ZZ$ of $\sin$, which are isolated, and $\abs{g}\leq 1$ there.
By Riemann's removable singularity theorem, $g$ extends to a bounded entire function, which is constant by Liouville's theorem.
:::

:::

::: pf-step
The possibilities are exactly $\boxed{f(z) = c\sin(z) \text{ with } c\in\CC,\ \abs{c}\leq 1}$.

::: pf-proof
By step [](#constant){.pf-ref}, $f = c\sin$ off $\pi\ZZ$, hence everywhere by continuity.
Conversely, $\abs{c\sin(z)}\leq\abs{\sin(z)}$ when $\abs{c}\leq1$.
:::

:::

:::

:::
