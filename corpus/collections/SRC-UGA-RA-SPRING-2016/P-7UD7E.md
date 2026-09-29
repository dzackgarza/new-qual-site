---
schema: qual/card@1
id: P-7UD7E
kind: problem
title: Borel measurability of distribution functions and $\int|f|=\int_0^\infty(\phi+\psi)\,d\lambda$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Spring 2016 Problem 5 in the preserved UGA source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $(X, \mathcal M, \mu)$ be a measure space.
For $f\in L^1(\mu)$ and $\lambda > 0$, define
$$
\phi(\lambda)=\mu(\{x \in X | f(x)>\lambda\}) 
\quad \text { and } \quad 
\psi(\lambda)=\mu(\{x \in X | f(x)<-\lambda\})
$$

Show that $\phi, \psi$ are Borel measurable and
$$
\int_{X}|f| ~d \mu=\int_{0}^{\infty}[\phi(\lambda)+\psi(\lambda)] ~d \lambda
$$
:::

::: {.solution}

::: pf

::: pf-step

$\phi$ and $\psi$ are Borel measurable functions of $\lambda \in (0, \infty)$.

::: pf-proof

$\lambda \mapsto \mu\{f > \lambda\}$ is decreasing (if $\lambda_1 < \lambda_2$ then $\{f > \lambda_1\} \supseteq \{f > \lambda_2\}$); decreasing (indeed monotone) functions are Borel measurable; likewise $\psi$ is decreasing.

:::

:::

::: {.pf-step #s2}

$\int_0^\infty \mu\{|f| > \lambda\}\,d\lambda = \int_X |f|\,d\mu$.

::: pf-proof

::: pf-step

Write $\mu\{|f| > \lambda\} = \int_X \chi_{\{|f(x)| > \lambda\}}\,d\mu(x)$.

::: pf-proof

definition of the measure of a set.

:::

:::

::: {.pf-step #s2-2}

Interchange: $\int_0^\infty\int_X \chi_{\{|f| > \lambda\}}\,d\mu(x)\,d\lambda = \int_X \int_0^\infty \chi_{\{|f(x)| > \lambda\}}\,d\lambda\,d\mu(x)$.

::: pf-proof

Tonelli — the integrand is non-negative and measurable.

:::

:::

::: {.pf-step #s2-3}

$\int_0^\infty \chi_{\{|f(x)| > \lambda\}}\,d\lambda = |f(x)|$ for every $x$.

::: pf-proof

the inner integral is the length of $\{\lambda > 0 : \lambda < |f(x)|\} = (0, |f(x)|)$.

:::

:::

::: pf-qed

Steps [](#s2-2){.pf-ref} and [](#s2-3){.pf-ref} give $\int_0^\infty\mu\{|f|>\lambda\}d\lambda = \int_X|f|d\mu$.

:::

:::

:::

::: {.pf-step #s3}

$\{|f| > \lambda\} = \{f > \lambda\} \cup \{f < -\lambda\}$, a disjoint union, so $\mu\{|f| > \lambda\} = \phi(\lambda) + \psi(\lambda)$.

::: pf-proof

$|f(x)| > \lambda \iff f(x) > \lambda$ or $f(x) < -\lambda$, and the two sets are disjoint.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give $\int_X|f|\,d\mu = \int_0^\infty[\phi(\lambda) + \psi(\lambda)]\,d\lambda$.

:::

:::

:::
