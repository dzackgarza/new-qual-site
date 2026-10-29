---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW4
kind: problem
title: The parallelogram law for inner-product norms
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Show that an inner product space satisfies the parallelogram law with its induced norm:
$$
\norm{x+y}^2+\norm{x-y}^2=2\norm{x}^2+2\norm{y}^2.
$$
(For simplicity, you may assume that this is an inner product space over $\RR$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For all $x,y$ in a real inner product space,
$$
\norm{x+y}^2=\norm{x}^2+2\inner{x}{y}+\norm{y}^2,
\qquad
\norm{x-y}^2=\norm{x}^2-2\inner{x}{y}+\norm{y}^2.
$$

::: pf-proof

Expand $\inner{x+y}{x+y}$ and $\inner{x-y}{x-y}$ by bilinearity. The equality $\inner{y}{x}=\inner{x}{y}$ combines the two cross terms in each expression, and $\inner{v}{v}=\norm{v}^2$ identifies the diagonal terms.

:::

:::

::: pf-step

For all $x,y$ the parallelogram identity holds:
$$
\norm{x+y}^2+\norm{x-y}^2=2\norm{x}^2+2\norm{y}^2.
$$

::: pf-proof

Add the two equalities in step [](#s1){.pf-ref}. The terms $2\inner{x}{y}$ and $-2\inner{x}{y}$ cancel.

:::

:::

:::

:::
