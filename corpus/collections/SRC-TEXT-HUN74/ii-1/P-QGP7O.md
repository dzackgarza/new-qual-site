---
schema: qual/card@1
id: P-QGP7O
kind: problem
title: Finitely generated torsion-free abelian groups are free
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Abelian Groups
  - Torsion
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the Hungerford II.1 exercise statement reproduced in a Hungerford solutions-manual transcription.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a finitely generated abelian group in which no element (except 0) has finite order.
Show that $G$ is a free abelian group.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There are integers $r\ge0$ and $d_1,\ldots,d_t>1$ such that
\[
G\cong \ZZ^r\oplus \ZZ/d_1\ZZ\oplus\cdots\oplus\ZZ/d_t\ZZ.
\]

::: pf-proof

This is the structure theorem for finitely generated abelian groups, applied
to the finitely generated abelian group $G$.

:::

:::

::: {.pf-step #s2}

One must have $t=0$.

::: pf-proof

If $t>0$, then the element corresponding to
\[
(0,\ldots,0,1\bmod d_1,0,\ldots,0)
\]
is nonzero and has finite order $d_1$. This contradicts the hypothesis that no
nonzero element of $G$ has finite order.

:::

:::

::: pf-step

Hence $G\cong\ZZ^r$, so $G$ is free abelian.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref} the finite cyclic summands are absent, leaving precisely the
free abelian group $\ZZ^r$.

:::

:::

:::

:::
