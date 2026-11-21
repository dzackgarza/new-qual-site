---
schema: qual/card@1
id: E-AMD-SD3PTZ4O
kind: problem
title: The union of two ideals need not be an ideal
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Kept the minimal counterexample in Z and removed redundant scaffolding.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. The card carries no source (it is listed in
    SRC-UNSORTED-ALGEBRA, a compilation with no text or page) and no retained solution set covers
    it, so the argument is the card's own; only the example is checked, by arithmetic: $2$ and $3$
    lie in the union of the principal ideals they generate, and $5$ lies in neither because
    neither $2$ nor $3$ divides it. Nothing beyond the example is claimed: in particular the card
    does not assert the general criterion that a union of two ideals is an ideal exactly when one
    contains the other.
---

::: {.exercise}
Show that the union of two ideals need not be an ideal.
:::

::: {.solution}
The argument is the card's own: the card sits in $SRC-UNSORTED-ALGEBRA$, a compilation with no source text or page, and no retained solution set covers it. The exercise asks only for an example, so one counterexample in $\ZZ$ settles it.

::: pf

::: {.pf-step #ideals}
$2\ZZ$ and $3\ZZ$ are ideals of $\ZZ$.

::: pf-proof
For $n\neq 0$ the set $n\ZZ$ is the kernel of reduction modulo $n$, hence an additive subgroup closed under multiplication by arbitrary elements of $\ZZ$: if $nk\in n\ZZ$ and $r\in\ZZ$ then $r(nk)=n(rk)\in n\ZZ$. So each is an ideal.
:::

:::

::: {.pf-step #witness}
$2\in2\ZZ\cup3\ZZ$ and $3\in2\ZZ\cup3\ZZ$, but $2+3=5\notin2\ZZ\cup3\ZZ$.

::: pf-proof
$2=2\cdot1\in2\ZZ$ and $3=3\cdot1\in3\ZZ$, so both lie in the union. If $5\in2\ZZ$ then $2$ divides $5$, which is false; if $5\in3\ZZ$ then $3$ divides $5$, which is false. Hence $5$ lies in neither ideal.
:::

:::

::: {.pf-step}
$2\ZZ\cup3\ZZ$ is not an ideal of $\ZZ$.

::: pf-proof
Every ideal is in particular an additive subgroup, so it is closed under addition. By step [](#witness){.pf-ref} the set $2\ZZ\cup3\ZZ$ contains $2$ and $3$ but not their sum, so it is not closed under addition, hence not an ideal. Since $2\ZZ$ and $3\ZZ$ are ideals by step [](#ideals){.pf-ref}, this is an example of two ideals whose union is not an ideal, which is the assertion of the exercise.
:::

:::

:::
:::
