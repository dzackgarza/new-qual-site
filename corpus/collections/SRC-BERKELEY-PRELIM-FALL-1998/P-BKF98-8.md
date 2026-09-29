---
schema: qual/card@1
id: P-BKF98-8
kind: problem
title: A non-zero-divisor in a finite unital ring is invertible
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Left and right multiplication by a are injective because a is not a zero
    divisor; finiteness makes both maps surjective, producing left and right
    inverses which necessarily coincide.
---

::: {.problem}
Let $R$ be a finite ring with identity, and let $a\in R$ be an element which is not a zero divisor. Show that $a$ is invertible.
:::

::: {.solution}

::: pf

::: {.pf-step #La-injective}
The map
$$
L_a:R\longrightarrow R,
\qquad
L_a(x)=ax
$$
is injective.

::: pf-proof
If
$$
L_a(x)=L_a(y),
$$
then
$$
a(x-y)=0.
$$
Since $a$ is not a zero divisor, this forces
$$
x-y=0,
$$
so $x=y$.
:::

:::

::: {.pf-step #ab-equals-one}
There is an element $b\in R$ such that
$$
ab=1.
$$

::: pf-proof
The set $R$ is finite, so every injective self-map of $R$ is surjective.
By step [](#La-injective){.pf-ref}, $L_a$ is surjective. Hence the identity element lies in its
image:
$$
L_a(b)=ab=1
$$
for some $b\in R$.
:::

:::

::: {.pf-step #Ra-injective-surjective}
The map
$$
R_a:R\longrightarrow R,
\qquad
R_a(x)=xa
$$
is injective and therefore surjective.

::: pf-proof
If
$$
xa=ya,
$$
then
$$
(x-y)a=0.
$$
Since $a$ is not a zero divisor, $x=y$. Thus $R_a$ is injective, and
finiteness of $R$ makes it surjective.
:::

:::

::: {.pf-step #ca-equals-one}
There is an element $c\in R$ such that
$$
ca=1.
$$

::: pf-proof
By surjectivity of $R_a$ from step [](#Ra-injective-surjective){.pf-ref}, the identity element lies in its
image.
:::

:::

::: {.pf-step #b-equals-c}
The elements $b$ and $c$ from steps [](#ab-equals-one){.pf-ref} and [](#ca-equals-one){.pf-ref} are equal.

::: pf-proof
Using associativity,
$$
c
=
c(ab)
=
(ca)b
=
b.
$$
:::

:::

::: {.pf-step #a-invertible}
The element $a$ is invertible.

::: pf-proof
By steps [](#ab-equals-one){.pf-ref}, [](#ca-equals-one){.pf-ref}, and [](#b-equals-c){.pf-ref}, the single element
$$
b=c
$$
satisfies
$$
ab=ba=1.
$$
Thus it is the inverse of $a$.
:::

:::

::: pf-qed
Step [](#a-invertible){.pf-ref} proves the claim.
:::

:::

:::
