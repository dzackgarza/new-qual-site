---
schema: qual/card@1
id: E-7YQU4
kind: problem
title: Finite fields are not algebraically closed
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Checked against standard finite-field references for the no-root polynomial argument.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
11. Prove that a finite field cannot be algebraically closed.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let \(F\) be a finite field and define
\[
g(T)=1+\prod_{a\in F}(T-a)\in F[T].
\]
Then \(g\) is nonconstant.

::: pf-proof

If \(|F|=q\), the product has degree \(q\), so \(g\) also has degree \(q\ge1\).

:::

:::

::: {.pf-step #s2}

The polynomial \(g\) has no root in \(F\).

::: pf-proof

For any \(b\in F\), one factor in the product is \(b-b=0\). Hence
\[
g(b)=1+0=1\neq0.
\]
Thus no element of \(F\) is a zero of \(g\).

:::

:::

::: pf-step

Therefore \(F\) is not algebraically closed.

::: pf-proof

An algebraically closed field has a root for every nonconstant polynomial in one variable. By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, \(g\in F[T]\) is nonconstant and has no root in \(F\). Hence \(F\) is not algebraically closed.

:::

:::

:::

:::
