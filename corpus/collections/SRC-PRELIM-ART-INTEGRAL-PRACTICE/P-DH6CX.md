---
schema: qual/card@1
id: P-DH6CX
kind: problem
title: The substitution $u=1/x$ (integrand missing)
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: The collection has no preserved provenance and explicitly records that the original drill sheet was not found. Repository history contains no earlier version with the missing integrand, so the original problem statement cannot be recovered from available sources.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
The original integral is missing from the surviving drill-sheet data. The only mathematical information preserved is the suggested substitution
\[
u=\frac1x,
\qquad
du=-\frac1{x^2}\,dx.
\]

- **Used 2018**
:::

::: solution
<1>1. The original integral cannot be reconstructed from the surviving data.
::: proof
The substitution
\[
u=\frac1x,
\qquad
du=-\frac1{x^2}\,dx
\]
does not determine a unique integrand. For example, every integral of the form
\[
\int \frac{\Phi(1/x)}{x^2}\,dx
\]
for a suitable function $\Phi$ is transformed by this substitution into
\[
-\int \Phi(u)\,du.
\]
Different choices of $\Phi$ give different original problems while producing exactly the same recorded substitution rule.

The collection metadata has no provenance and states that the original drill sheet was not found. Repository history likewise contains no earlier version of this card with the missing integrand. Therefore the available evidence is insufficient to recover a unique integral, and supplying one would require fabrication.
:::

<1>2. Record the only valid mathematical conclusion supplied by the surviving fragment.
::: proof
If an integral contains a factor $x^{-2}\,dx$ together with an expression depending on $1/x$, then the substitution $u=1/x$ converts that factor according to
\[
\frac{dx}{x^2}=-du.
\]
No more specific evaluation is determined by the surviving statement.
:::
:::
