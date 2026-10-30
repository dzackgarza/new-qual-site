---
schema: qual/card@1
id: P-WESCA06-I1
kind: problem
title: "Define the winding number of a path about a point"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Theorems and Definitions, item 1 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Define the winding number of a path $\gamma$ about a point $z\in\CC$.
:::

::: {.solution}

Assume
$$
\gamma:[a,b]\to\CC
$$
is a closed piecewise $C^1$ path and
$$
z\notin\gamma([a,b]).
$$

::: pf

::: {.pf-step #s1-1}

The winding number, or index, of $\gamma$ about $z$ is
$$
\boxed{
\operatorname{Ind}(\gamma,z)
\coloneqq
\frac1{2\pi i}
\int_\gamma
\frac{dw}{w-z}.
}
$$


::: pf-proof

This is the standard analytic definition of the winding number.
The denominator never vanishes because
$$
z\notin\gamma([a,b]).
$$

:::

:::

::: {.pf-step #s1-2}

Equivalently,
$$
\operatorname{Ind}(\gamma,z)
$$
is the total change of a continuous argument of
$$
\gamma(t)-z
$$
divided by
$$
2\pi.
$$


::: pf-proof

Because
$$
\gamma(t)-z\ne0,
$$
one can choose a continuous lifted argument
$$
\theta:[a,b]\to\RR
$$
such that
$$
\gamma(t)-z
=
\abs{\gamma(t)-z}e^{i\theta(t)}.
$$
Then
$$
\frac{d}{dt}
\log(\gamma(t)-z)
=
\frac{\gamma'(t)}{\gamma(t)-z}
$$
along each smooth piece, so integrating gives
$$
\frac1{2\pi i}
\int_\gamma
\frac{dw}{w-z}
=
\frac{\theta(b)-\theta(a)}{2\pi}.
$$
Since $\gamma$ is closed,
$$
e^{i\theta(b)}
=
e^{i\theta(a)},
$$
so
$$
\theta(b)-\theta(a)
\in
2\pi\ZZ.
$$
Thus the winding number is an integer.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give the requested definition and its geometric
interpretation.

:::

:::

:::
