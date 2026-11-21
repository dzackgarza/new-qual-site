---
schema: qual/card@1
id: E-AMD-5UFPG7F5
kind: problem
title: An ideal is maximal iff the quotient is a field
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source states the claim for an ideal I of an unspecified ring R; it is false for noncommutative rings (the zero ideal of a matrix ring over a field is maximal with non-field quotient). The statement now assumes R commutative with identity.'
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured the prose solution into a structured proof under #2 and re-checked it: the
    correspondence theorem gives the inclusion-preserving bijection $J\mapsto J/I$ between the
    ideals of $R$ containing $I$ and those of $R/I$; maximality turns it into "the only ideals of
    $R/I$ are $(0)$ and the whole ring", and a commutative ring with identity having only those
    ideals is a field, and conversely. Two points the prose left implicit are now steps: $R/I$ is
    not the zero ring on either side of the equivalence, which is what makes $(0)\ne R/I$, and
    $R/I$ commutative with identity follows from $R$ being so. Both hypotheses are used, in
    $R/I$ inheriting commutativity and in the correspondence theorem; the noncommutative failure
    recorded above is unaffected. No defect found in the statement or proof. The card carries no
    collection and no retained solution set covers this exercise, so the argument is the card's
    own. Not claimed: a citation to a publication.
---

::: {.exercise}
Let $R$ be a commutative ring with identity. Show that $I\normal R$ is maximal iff $R/I$ is a field.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and it is the standard correspondence-theorem argument. Let $R$ be a commutative ring with identity and $I\normal R$ an ideal, with $\pi\colon R\to R/I$ the quotient map.

::: pf

::: {.pf-step #correspondence}
The ideals of $R/I$ are exactly the images $\pi(J)=J/I$ of the ideals $J$ of $R$ with $I\subseteq J\subseteq R$, and $J\mapsto J/I$ is an inclusion-preserving bijection.

::: pf-proof
This is the correspondence theorem for quotients of a ring by an ideal, which applies because $I$ is an ideal of the commutative ring $R$: an ideal $J$ of $R$ containing $I$ has $J/I$ an ideal of $R/I$, and conversely the preimage under $\pi$ of an ideal of $R/I$ is an ideal of $R$ containing $I=\pi^{-1}(0)$. The two assignments are mutually inverse and preserve inclusions, since $\pi$ is surjective and preserves sums and products.
:::

:::

::: {.pf-step #maximal-implies-field}
If $I$ is maximal, then $R/I$ is a field.

::: pf-proof
Maximality says the only ideals $J$ of $R$ with $I\subseteq J\subseteq R$ are $I$ and $R$, so by step [](#correspondence){.pf-ref} the only ideals of $R/I$ are $(0)$ and $R/I$. A commutative ring with identity whose only ideals are $(0)$ and the whole ring is a field: for $0\ne a\in R/I$ the principal ideal $(a)$ is nonzero, hence equals $R/I$, so $ab=1$ for some $b$, that is $a$ is a unit. Also $R/I$ is not the zero ring, since $I\ne R$ by maximality.
:::

:::

::: {.pf-step #field-implies-maximal}
If $R/I$ is a field, then $I$ is maximal.

::: pf-proof
In a field the only ideals are $(0)$ and the whole ring, so the ideals of $R/I$ are $\pi(I)=0$ and $R/I$; by step [](#correspondence){.pf-ref} the only ideals of $R$ containing $I$ are $I$ and $R$. Hence no proper ideal of $R$ strictly contains $I$, and since $I\ne R$ (as $R/I$ is a field, not the zero ring) the ideal $I$ is maximal.
:::

:::

::: {.pf-step}
$\boxed{I\text{ maximal}\iff R/I\text{ is a field}}$.

::: pf-proof
The two implications are steps [](#maximal-implies-field){.pf-ref} and [](#field-implies-maximal){.pf-ref}.
:::

:::

:::
:::
