---
schema: qual/card@1
id: P-Q3LW9
kind: problem
title: Polynomials cannot approximate $\bar z$ uniformly on $\partial\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomials
  - Power Series
relations: []
review: draft
---

::: {.problem}
Prove or disprove: there is a sequence of analytic polynomials $p_n$ such
that $p_n(z)\to\bar z$ uniformly for $z\in\partial\DD$.
:::

::: {.solution}

::: pf

::: {.pf-step #reduce}

If $p_n\to\bar z$ uniformly on $\partial\DD$, then $\varepsilon_n\coloneqq\max_{\abs z=1}\abs{zp_n(z)-1}\to0$.

::: pf-proof

On $\abs z=1$ we have $\bar z=1/z$, so $\abs{zp_n(z)-1}=\abs{p_n(z)-\bar z}$.

:::

:::

::: pf-step

No such sequence $p_n$ exists.

::: pf-proof

Each $zp_n(z)-1$ is a polynomial, so by the maximum modulus principle
$$
1=\abs{0\cdot p_n(0)-1}\le\varepsilon_n.
$$
This contradicts step [](#reduce){.pf-ref}.

:::

:::

:::

:::
