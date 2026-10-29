---
schema: qual/card@1
id: E-SMOHZ
kind: problem
title: Limit point of zeros is an essential singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Essential Singularities
  - Identity Theorem
  - Zeros
  - Singularities
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source does not say that $\Omega$ is a connected open set containing $z_0$ or that the zeros $z_k$ differ from $z_0$. Without connectedness, $f$ can vanish identically near $z_0$ and be nonzero elsewhere; the statement now takes $\Omega$ to be a connected open set containing $z_0$ and $z_k\neq z_0$.'
---

::: {.exercise}
Let $\Omega$ be a connected open set containing $z_0$.
Suppose $f\not\equiv 0$ is holomorphic on $\Omega\smts{z_0}$ with a sequence of zeros $z_k\neq z_0$ limiting to $z_0$.
Show that $z_0$ is an essential singularity of $f$.
:::

::: {.solution}
The zeros $z_k$ accumulate at $z_0$, so $z_0$ is an isolated singularity of $f$; we exclude the other two kinds.

::: pf

::: pf-step
$z_0$ is not a pole of $f$.

::: pf-proof
At a pole, $\abs{f(z)}\to\infty$ as $z\to z_0$, but $f(z_k)=0$ with $z_k\to z_0$.
:::

:::

::: pf-step
$z_0$ is not a removable singularity of $f$.

::: pf-proof
If it were, $f$ would extend to a holomorphic $g$ on $\Omega$. The zeros of $g$ include the $z_k$, which accumulate at $z_0\in\Omega$. Since $\Omega$ is connected, the identity theorem gives $g\equiv 0$ on $\Omega$ and hence $f\equiv 0$, which is excluded.
:::

:::

::: pf-qed
An isolated singularity that is neither removable nor a pole is essential.
:::

:::

:::
