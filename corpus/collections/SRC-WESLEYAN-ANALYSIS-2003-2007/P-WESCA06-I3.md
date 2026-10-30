---
schema: qual/card@1
id: P-WESCA06-I3
kind: problem
title: "State the Maximum Principle"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Theorems and Definitions, item 3 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State the Maximum Principle.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Maximum Principle.** Let $\Omega\subseteq\CC$ be a domain and let $f:\Omega\to\CC$ be holomorphic. If $\abs{f}$ attains a local maximum at a point of $\Omega$, then $f$ is constant on $\Omega$.


::: pf-proof

This is the maximum-modulus principle for holomorphic functions.

:::

:::

::: {.pf-step #s1-2}

Equivalently, if $f$ is nonconstant and holomorphic on a domain $\Omega$, then
$$
\abs{f(z)}
$$
has no local maximum at any interior point $z\in\Omega$.


::: pf-proof

This is the contrapositive of step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

In particular, if $\Omega$ is bounded, $f$ is continuous on $\overline\Omega$, and $f$ is holomorphic on $\Omega$, then
$$
\boxed{
\max_{z\in\overline\Omega}\abs{f(z)}
=
\max_{z\in\partial\Omega}\abs{f(z)}}
$$
unless $f$ is constant.


::: pf-proof

Continuity on the compact set $\overline\Omega$ guarantees existence of a maximum. If a nonconstant $f$ attained that maximum at an interior point, step [](#s1-1){.pf-ref} would force $f$ to be constant. Hence every maximum occurs on the boundary.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested theorem statement; steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} record its standard equivalent and boundary forms.

:::

:::

:::
