---
schema: qual/card@1
id: P-W8CJF
kind: problem
title: An integral domain in which every prime ideal is maximal is a field, hence a UFD
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured: the card's one-step proof was correct, and is now split into the primality of
    the zero ideal from the domain hypothesis, the passage to a field through the hypothesis and
    the isomorphism R/(0) = R, and the verification that a field satisfies the two UFD
    conditions vacuously. Added at the end the observation that the converse fails — Z is a UFD
    whose zero ideal is prime and not maximal — so the statement is not an equivalence and the
    hypothesis is doing real work. No statement was changed.
---

::: {.problem}
If $R$ is an integral domain and $\Spec R\subseteq\mspec R$, show that $R$ is a UFD.
:::

::: {.solution}
Throughout $R$ is an integral domain, $\Spec R$ is the set of prime ideals and $\mspec R$ the set of maximal ideals of $R$, so the hypothesis $\Spec R \subseteq \mspec R$ says that every prime ideal of $R$ is maximal.

::: pf

::: {.pf-step #zero-prime}
$(0)$ is a prime ideal of $R$.

::: pf-proof
$R$ is a domain, so $(0)$ is proper and $xy \in (0)$, that is $xy = 0$, forces $x = 0$ or $y = 0$; that is exactly primality of $(0)$.

:::

:::

::: {.pf-step #zero-maximal}
$(0)$ is a maximal ideal, so $R$ is a field.

::: pf-proof
By step [](#zero-prime){.pf-ref} $(0) \in \Spec R$, and the hypothesis puts it in $\mspec R$. A commutative ring modulo a maximal ideal is a field, and $R/(0) \cong R$ under $x \mapsto x$.

:::

:::

::: {.pf-step #field-ufd}
A field is a unique factorization domain.

::: pf-proof
In a field every nonzero element is a unit. A nonzero nonunit would be reducible into irreducibles; there are none, so every nonzero element admits the empty factorization into irreducibles and it is unique because any two factorizations of a unit consist of units, and a unit is not irreducible. Formally the two conditions of unique factorization — existence and uniqueness of a decomposition into irreducibles up to order and associates — hold vacuously.

:::

:::

::: pf-step
$R$ is a UFD.

::: pf-proof
Step [](#zero-maximal){.pf-ref} makes $R$ a field and step [](#field-ufd){.pf-ref} makes a field a UFD; hence $R$ is a UFD. The converse is false, so the hypothesis is genuinely stronger than the conclusion: $\ZZ$ is a UFD and its prime ideal $(0)$ is not maximal.

:::

:::

:::
:::
