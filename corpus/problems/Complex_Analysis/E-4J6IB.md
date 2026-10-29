---
schema: qual/card@1
id: E-4J6IB
kind: problem
title: An isolated singularity with $\abs{f(z)}\le\abs z^{-1/2}$ is removable
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The statement block carried a warning that Riemann's theorem does not apply to z^{1/2} f(z) because z^{1/2} is "highly singular" at 0; that guidance moved to a hint, which says that z^{1/2} has no single-valued branch near 0.
---

::: {.exercise}
Suppose $f$ is holomorphic with $z_0 = 0$ an isolated singularity, and suppose there is some neighborhood of $0$ on which
$$
\abs{f(z)} \leq \abs{z}^{-1/2}.
$$
Show that $z_0$ is removable.

:::

::: {.hint}
Riemann's removable singularity theorem does not apply to $z^{1/2}f(z)$, because $z^{1/2}$ has no single-valued holomorphic branch on a punctured neighbourhood of $0$. Apply it to $zf(z)$.
:::

::: {.solution}

::: pf

::: pf-step
$0$ is a removable singularity of $f$.

::: pf-proof
On the punctured neighbourhood, $\abs{zf(z)} \leq \abs{z}^{1/2}\to0$ as $z\to0$.
By Riemann's removable singularity theorem in the form "$\lim_{z\to0}zf(z)=0$ implies removable", $0$ is removable.
:::

:::

:::

:::
