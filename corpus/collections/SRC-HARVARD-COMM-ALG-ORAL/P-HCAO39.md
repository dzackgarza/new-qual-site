---
schema: qual/card@1
id: P-HCAO39
kind: problem
title: A matrix congruent to the identity over a local ring is invertible
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Matrices
  - Invertibility
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $(R,\mathfrak m)$ be a local ring, and let $M$ be an $n\times n$ matrix whose entries lie in $\mathfrak m$.
Prove, possibly using Nakayama's lemma, that $I_n+M$ is invertible.
:::

::: {.solution}
Let $T=I_n+M$.

::: pf

::: pf-step
Modulo the maximal ideal, $T$ becomes the identity matrix.

::: pf-proof
Every entry of $M$ lies in $\mathfrak m$, so its image in
$R/\mathfrak m$ is zero. Hence
\[
\overline T=I_n
\]
in $M_n(R/\mathfrak m)$.
:::

:::

::: {.pf-step #det-t-is-unit}
Therefore $\det(T)$ is a unit of $R$.

::: pf-proof
Reducing the determinant modulo $\mathfrak m$ gives
\[
\det(T)\equiv1\pmod{\mathfrak m}.
\]
Thus $\det(T)\notin\mathfrak m$. In a local ring, the nonunits are exactly the
elements of the maximal ideal, so $\det(T)$ is a unit.
:::

:::

::: pf-step
Hence $T=I_n+M$ is invertible.

::: pf-proof
The adjugate identity gives
\[
T\operatorname{adj}(T)=\det(T)I_n.
\]
Since $\det(T)$ is a unit by step [](#det-t-is-unit){.pf-ref},
\[
T^{-1}=\det(T)^{-1}\operatorname{adj}(T).
\]
:::

:::

:::
:::
