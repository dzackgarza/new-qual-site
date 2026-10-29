---
schema: qual/card@1
id: E-XXUNZ
kind: problem
title: Uniform convergence $f_n\to f$ implies $\int_\gamma f_n\to\int_\gamma f$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Contour Integration
  - Sequences of Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source printed "Show that if f_n -> f uniformly then int_gamma f_n -> int_gamma f" without hypotheses on gamma or the f_n; the statement now takes gamma piecewise C^1 and the f_n continuous on gamma, so that the integrals are defined and gamma has finite length.'
---

::: {.exercise}
Let $\gamma$ be a piecewise $C^1$ curve and let $f_n$ be continuous on $\gamma$.
Show that if $f_n\to f$ uniformly on $\gamma$ then $\int_\gamma f_n\to \int_\gamma f$.
:::

::: {.solution}
Write $L(\gamma)$ for the length of $\gamma$ and $\norm{h}_\gamma \coloneqq \sup_{z\in\gamma}\abs{h(z)}$.

::: pf

::: pf-step
$\int_\gamma f_n\to\int_\gamma f$.

::: pf-proof
$f$ is continuous on $\gamma$ as a uniform limit of continuous functions, so $\int_\gamma f$ is defined.
By the standard estimate for contour integrals,
$$
\abs{\int_\gamma f_n\,dz - \int_\gamma f\,dz} = \abs{\int_\gamma (f_n - f)\,dz} \le \norm{f_n - f}_\gamma\, L(\gamma),
$$
and the right-hand side tends to $0$ because $L(\gamma)<\infty$ and $\norm{f_n-f}_\gamma\to0$.
:::

:::

:::

:::
