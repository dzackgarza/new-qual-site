---
schema: qual/card@1
id: E-SMI-8000E-NR1
kind: problem
title: In a Noetherian ring every ideal sits in a maximal ideal, without Zorn
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
<1>1. Suppose for contradiction that $I$ is not contained in any maximal ideal.
::: {.proof}
assume the conclusion fails.
:::

<1>2. Then $I$ is not maximal, so there is a proper ideal $I_1 \supsetneq I$.
::: {.proof}
<1>1 (if $I$ were maximal it would contain itself).
:::

<1>3. Inductively, given a proper ideal $I_n$ that is not maximal, choose a proper ideal $I_{n+1} \supsetneq I_n$.
::: {.proof}
<1>2, iterated (each $I_n$ is not maximal, so it is properly contained in a proper ideal).
:::

<1>4. This gives a strictly increasing chain $I \subsetneq I_1 \subsetneq I_2 \subsetneq \cdots$ of ideals.
::: {.proof}
<1>3.
:::

<1>5. But $R$ is Noetherian, so it satisfies the ascending chain condition: no strictly increasing infinite chain of ideals exists.
::: {.proof}
definition of Noetherian.
:::

<1>6. Contradiction, so $I$ is contained in some maximal ideal.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
