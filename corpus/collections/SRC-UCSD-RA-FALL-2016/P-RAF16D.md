---
schema: qual/card@1
id: P-RAF16D
kind: problem
title: "Conditional expectation via Radon-Nikodym"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing Radon-Nikodym proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) = 1$, $\mathcal{M}_0$ a sub-$\sigma$-algebra of $\mathcal{M}$, and $\nu = \mu|_{\mathcal{M}_0}$ (the restriction of $\mu$ onto $\mathcal{M}_0$). Let $f \in L^1(\mathcal{M}, \mu)$ be real-valued.
Use the Radon-Nikodym Theorem to prove that there exists a unique $g \in L^1(\mathcal{M}_0, \nu)$ such that
$$
\int_E f\,d\mu = \int_E g\,d\nu \qquad \forall E \in \mathcal{M}_0.
$$
(Note that $g$ is, but $f$ may not be, measurable with respect to $\mathcal{M}_0$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Define a signed measure $\lambda$ on $\mathcal M_0$ by $\lambda(E) = \int_E f\, d\mu$ for $E \in \mathcal M_0$.

::: pf-proof

definition.

:::

:::

::: {.pf-step #s2}

$\lambda$ is a finite signed measure on $\mathcal M_0$.

::: pf-proof

$f \in L^1(\mu)$ and $\mu(X) = 1$, so $|\lambda(E)| \le \int |f|\, d\mu < \infty$; countable additivity follows from the dominated convergence theorem.

:::

:::

::: {.pf-step #s3}

$\lambda$ is absolutely continuous with respect to $\nu$.

::: pf-proof

if $\nu(E) = \mu(E) = 0$ for $E \in \mathcal M_0$, then $\lambda(E) = \int_E f\, d\mu = 0$ (the integral over a null set is $0$).

:::

:::

::: {.pf-step #s4}

By the Radon–Nikodym theorem, there is a unique $g \in L^1(\mathcal M_0, \nu)$ with $\lambda(E) = \int_E g\, d\nu$ for all $E \in \mathcal M_0$.

::: pf-proof

Radon–Nikodym theorem applied to steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Hence $\int_E f\, d\mu = \int_E g\, d\nu$ for all $E \in \mathcal M_0$.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref}.

:::

:::

:::
