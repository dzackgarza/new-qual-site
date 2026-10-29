---
schema: qual/card@1
id: P-F2KNT
kind: problem
title: $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$ are isomorphic subfields of $\CC$ that are not equal
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Show that $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$ are isomorphic fields but are not identical as subfields of $\CC$.
:::

::: {.solution}
Let $\alpha=2^{1/3}$ be the real cube root and $\beta=\zeta_3\alpha$.

::: pf

::: pf-step
$\QQ(\alpha)\cong\QQ(\beta)$.

::: pf-proof
Both $\alpha$ and $\beta$ are roots of $x^3-2$, which is irreducible over $\QQ$ by Eisenstein at $2$.
Hence $\QQ(\alpha)\cong\QQ[x]/(x^3-2)\cong\QQ(\beta)$.
:::

:::

::: pf-step
$\QQ(\alpha)\ne\QQ(\beta)$ as subfields of $\CC$.

::: pf-proof
$\QQ(\alpha)\subset\RR$, while $\beta$ is not real, so $\beta\notin\QQ(\alpha)$.
:::

:::

:::

:::