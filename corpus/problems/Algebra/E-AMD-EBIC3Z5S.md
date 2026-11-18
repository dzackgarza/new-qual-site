---
schema: qual/card@1
id: E-AMD-EBIC3Z5S
kind: problem
title: An integral domain in which every prime ideal is maximal is a field, hence a UFD
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. Checked the statement against the collection: the card sits
    in SRC-UNSORTED-ALGEBRA, a compilation with no source text or page, so there is nothing
    printed to compare it with, and no retained solution set covers it; the exercise is read as
    stated in the card. The argument is the card's own. Each step was checked: the zero ideal of
    an integral domain is prime; the hypothesis places it among the maximal ideals; $R/(0)\cong R$
    is a field exactly when $(0)$ is maximal; and a field is a UFD with no irreducible elements.
    Not claimed: the converse, or any factorisation statement for a domain that is not a field.
---

::: {.exercise}
Show that if $\Spec(R) \subseteq \mspec(R)$ and $R$ is an integral domain, then $R$ is a UFD.
:::

::: {.solution}
The argument is the card's own: the collection $SRC-UNSORTED-ALGEBRA$ is a compilation with no source and no retained solution set, and the exercise is an immediate consequence of the definitions. Two conventions are used: an ideal is prime when $ab\in I$ forces $a\in I$ or $b\in I$, and maximal when it is proper and not contained in a proper ideal.

::: pf

::: {.pf-step #prime}
$(0)$ is a prime ideal of $R$.

::: pf-proof
$R$ is an integral domain, so it is commutative with $1\neq 0$ and has no zero divisors. If $ab\in(0)$ then $ab=0$, so $a=0$ or $b=0$, that is, $a\in(0)$ or $b\in(0)$. Hence $(0)$ is prime.
:::

:::

::: {.pf-step #maximal}
$(0)$ is a maximal ideal of $R$.

::: pf-proof
Step [](#prime){.pf-ref} gives $(0)\in\Spec(R)$, and the hypothesis is $\Spec(R)\subseteq\mspec(R)$.
:::

:::

::: {.pf-step #field}
$R$ is a field.

::: pf-proof
For a commutative ring with $1$, an ideal $I$ is maximal if and only if $R/I$ is a field. By step [](#maximal){.pf-ref} this applies to $I=(0)$, and $R/(0)\cong R$ by the first isomorphism theorem, so $R$ is a field.
:::

:::

::: {.pf-step #ufd}
Every field is a UFD.

::: pf-proof
In a field every nonzero element is a unit, so there are no irreducible elements and no nonzero nonunits: the assertion "every nonzero nonunit is a product of irreducibles" is vacuous, and its product is unique because there is nothing to factor. Explicitly, the irreducible factorisation of a nonzero nonunit is the empty product, assigned to each of them by the empty uniqueness.
:::

:::

::: {.pf-step}
$R$ is a UFD, as claimed.

::: pf-proof
Step [](#field){.pf-ref} gives that $R$ is a field and step [](#ufd){.pf-ref} that a field is a UFD, so
$$
\boxed{R\text{ is a UFD}.}
$$
:::

:::

:::
:::
