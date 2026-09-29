---
schema: qual/card@1
id: E-SMI-8000E-NR1
kind: problem
title: In a Noetherian ring every proper ideal sits in a maximal ideal, without Zorn
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
If $R$ is a Noetherian ring, prove every ideal $I$ of $R$ is contained in a maximal ideal without using Zorn's lemma.
:::

::: {.solution}
The ideal $I=R$ lies in no maximal ideal, so we assume $I$ is proper.

::: pf

::: {.pf-step #s1}

If $I$ lies in no maximal ideal, there is a strictly increasing chain of proper ideals $I = I_0 \subsetneq I_1 \subsetneq I_2 \subsetneq \cdots$.

::: pf-proof

Put $I_0 = I$. Given a proper ideal $I_n \supseteq I$, the ideal $I_n$ is not maximal, since otherwise $I$ would lie in the maximal ideal $I_n$. Hence there is a proper ideal $I_{n+1} \supsetneq I_n$, and $I_{n+1} \supseteq I$.

:::

:::

::: pf-qed

A Noetherian ring satisfies the ascending chain condition on ideals, so no chain as in step [](#s1){.pf-ref} exists. Hence $I$ lies in a maximal ideal.

:::

:::

:::
