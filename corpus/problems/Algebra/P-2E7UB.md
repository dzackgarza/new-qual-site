---
schema: qual/card@1
id: P-2E7UB
kind: problem
title: Every non-unit lies in a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Stated the correct one-sided hypothesis and applied Zorn directly to proper left ideals over Rx.
---

::: {.problem}
Let $R$ be a ring with $1\ne0$. Show that any element $x$ having no left inverse is contained in a maximal left ideal. In a commutative ring, this applies to every nonunit.
:::

::: {.solution}

::: pf

::: {.pf-step #proper}

The principal left ideal $Rx$ is proper.

::: pf-proof

If $Rx=R$, then $1\in Rx$, so $rx=1$ for some $r\in R$, and $x$ has a left inverse.

:::

:::

::: {.pf-step #zorn}

The set $\mathcal S$ of proper left ideals containing $Rx$, ordered by inclusion, has a maximal element $M$.

::: pf-proof

By step [](#proper){.pf-ref}, $Rx\in\mathcal S$, so $\mathcal S$ is nonempty. The union of a nonempty chain in $\mathcal S$ is a left ideal containing $Rx$. It is proper: if it contained $1$, some member of the chain would contain $1$ and equal $R$. Thus every chain has an upper bound in $\mathcal S$, and Zorn's lemma gives $M$.

:::

:::

::: {.pf-step #maximal}

$M$ is a maximal left ideal containing $x$.

::: pf-proof

A proper left ideal strictly containing $M$ would contain $Rx$ and so lie in $\mathcal S$, contradicting the maximality of $M$ in step [](#zorn){.pf-ref}. Also $x\in Rx\subseteq M$.

:::

:::

::: pf-step

In a commutative ring, every nonunit lies in a maximal ideal.

::: pf-proof

In a commutative ring an element has a left inverse exactly when it is a unit, and left ideals are ideals. Apply step [](#maximal){.pf-ref}.

:::

:::

:::

:::
