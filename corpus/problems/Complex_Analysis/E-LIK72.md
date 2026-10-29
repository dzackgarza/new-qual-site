---
schema: qual/card@1
id: E-LIK72
kind: problem
title: A meromorphic function on $\CP^1$ has finitely many poles
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Essential Singularities
  - Meromorphic Functions
  - Riemann Surfaces
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source says the poles "must accumulate on an essential singularity at z=infinity". An accumulation point of poles is not an isolated singularity, so it is not an essential singularity in the usual sense; the statement says the poles accumulate at infinity, so that f does not extend to a meromorphic function on CP^1.
---

::: {.exercise}
Show that a meromorphic function on $\CP^1$ can have only finitely many poles.
Show that moreover if $f$ is meromorphic on $\CC$ with infinitely many poles, then the poles must accumulate at $z=\infty$, so that $\infty$ is a non-isolated singularity of $f$ and $f$ does not extend to a meromorphic function on $\CP^1$.
:::

::: {.solution}
::: pf

::: {.pf-step #closed-discrete}
The set $P_f$ of poles of a meromorphic function $f$ on a Riemann surface $X$ is closed and discrete in $X$.

::: pf-proof
Each pole has a punctured neighborhood on which $f$ is holomorphic, so $P_f$ is discrete. At a point not in $P_f$, $f$ is holomorphic, hence holomorphic on a neighborhood of that point, so $X\setminus P_f$ is open.
:::

:::

::: {.pf-step #finite}
A meromorphic function on $\CP^1$ has finitely many poles.

::: pf-proof
By step [](#closed-discrete){.pf-ref}, $P_f$ is a closed discrete subset of the compact space $\CP^1$, hence compact and discrete, hence finite.
:::

:::

::: pf-step
If $f$ is meromorphic on $\CC$ with infinitely many poles, then the poles accumulate at $\infty$, and $f$ does not extend to a meromorphic function on $\CP^1$.

::: pf-proof
By step [](#closed-discrete){.pf-ref} applied to $X=\CC$, each closed disk $\abs z\le R$ contains finitely many poles, so there are poles $p_k$ with $\abs{p_k}\to\infty$. Every neighborhood of $\infty$ in $\CP^1$ then contains poles, so $\infty$ is not an isolated singularity, and a meromorphic extension to $\CP^1$ would contradict step [](#finite){.pf-ref}.
:::

:::

:::

:::
