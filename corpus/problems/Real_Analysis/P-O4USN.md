---
schema: qual/card@1
id: P-O4USN
kind: problem
title: $\nu\perp\mu$ and $\nu\ll\totalvariation{\mu}$ implies $\nu=0$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Radon-Nikodym
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $\nu, \mu$ be signed measures, and show that
$$
\nu \perp \mu \text{ and } \nu \ll \abs{ \mu} \implies \nu = 0
.$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is a measurable $A$ with $\totalvariation{\mu}(A) = 0$ and $\totalvariation{\nu}(A^c) = 0$.

::: pf-proof

This is the definition of $\nu \perp \mu$: there is a partition $X = A \sqcup A^c$ with $A$ null for $\mu$ and $A^c$ null for $\nu$, and a set is null for a signed measure exactly when it has total variation measure $0$.

:::

:::

::: {.pf-step #s2}

$\totalvariation{\nu}(A) = 0$.

::: pf-proof

$\nu \ll \totalvariation{\mu}$ means $\totalvariation{\nu}(E) = 0$ whenever $\totalvariation{\mu}(E) = 0$, equivalently $\nu(E) = 0$ for every measurable $E$ with $\totalvariation{\mu}(E) = 0$. Apply it to $E = A$ from step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\totalvariation{\nu}(X) = \totalvariation{\nu}(A) + \totalvariation{\nu}(A^c) = 0$. Since $\abs{\nu(E)} \le \totalvariation{\nu}(E)$ for every $E$, $\nu = 0$.

:::

:::

:::
