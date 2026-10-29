---
schema: qual/card@1
id: P-JWYGQ
kind: problem
title: The degree of $\QQ(2^{3/2})$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Compute
$$
[\QQ(2^{3/2}):\QQ].
$$
:::

::: {.solution}

::: pf

::: {.pf-step #same-field}

$\QQ(2^{3/2})=\QQ(\sqrt2)$.

::: pf-proof

$2^{3/2}=2\sqrt2$ and $2\in\QQ^\times$.

:::

:::

::: pf-step

$[\QQ(2^{3/2}):\QQ]=\boxed{2}$.

::: pf-proof

The polynomial $x^2-2$ is irreducible over $\QQ$ by Eisenstein's criterion at $2$, so $[\QQ(\sqrt2):\QQ]=2$. Apply step [](#same-field){.pf-ref}.

:::

:::

:::

:::
