---
schema: qual/card@1
id: P-FOP4D
kind: problem
title: A square matrix is similar to its transpose
classification:
  areas:
  - algebra
  topics:
  - Canonical Forms
  - Matrices
  - Rational Canonical Form
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
Is a square matrix always similar to its transpose?
:::

::: {.solution}
Yes. Let $A\in M_n(F)$.

::: pf

::: {.pf-step #s1}

The polynomial matrices
\[
tI-A
\qquad\text{and}\qquad
tI-A^t=(tI-A)^t
\]
have the same Smith normal form over the PID $F[t]$.

::: pf-proof

If
\[
U(tI-A)V=D
\]
is a Smith normal form with $U,V$ unimodular, then transposing gives
\[
V^t(tI-A)^tU^t=D^t=D.
\]
Thus the invariant factors are unchanged by transpose.

:::

:::

::: pf-step

Therefore $A$ and $A^t$ have the same rational canonical form.

::: pf-proof

The invariant factors of $tI-A$ are exactly the invariant factors of the $F[t]$-module associated to $A$, and these determine the rational canonical form. By step [](#s1){.pf-ref} the invariant factors for $A$ and $A^t$ agree.

:::

:::

::: pf-step

Hence $A$ is similar to $A^t$.

::: pf-proof

Two matrices over a field are similar iff they have the same rational canonical form.

:::

:::

:::

:::
