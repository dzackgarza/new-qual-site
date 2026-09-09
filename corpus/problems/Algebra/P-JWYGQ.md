---
schema: qual/card@1
id: P-JWYGQ
kind: problem
title: $[\QQ(2^{3/2}):\QQ]$
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

::: problem
Compute
\[
[\QQ(2^{3/2}):\QQ].
\]
:::

::: {.solution}
Since
\[
2^{3/2}=2\sqrt2,
\]
and $2\in\QQ^\times$, we have
\[
\QQ(2^{3/2})=\QQ(2\sqrt2)=\QQ(\sqrt2).
\]
The polynomial $x^2-2$ is irreducible over $\QQ$ by the rational-root test (or Eisenstein at $2$), so
\[
[\QQ(\sqrt2):\QQ]=2.
\]
Therefore
\[
[\QQ(2^{3/2}):\QQ]=2.
\]
:::
