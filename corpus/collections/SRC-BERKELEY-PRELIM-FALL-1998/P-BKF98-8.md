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
<1>1. The map
$$
L_a:R\longrightarrow R,
\qquad
L_a(x)=ax
$$
is injective.

::: {.proof}
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

<1>2. There is an element $b\in R$ such that
$$
ab=1.
$$

::: {.proof}
The set $R$ is finite, so every injective self-map of $R$ is surjective.
By step <1>1, $L_a$ is surjective. Hence the identity element lies in its
image:
$$
L_a(b)=ab=1
$$
for some $b\in R$.
:::

<1>3. The map
$$
R_a:R\longrightarrow R,
\qquad
R_a(x)=xa
$$
is injective and therefore surjective.

::: {.proof}
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

<1>4. There is an element $c\in R$ such that
$$
ca=1.
$$

::: {.proof}
By surjectivity of $R_a$ from step <1>3, the identity element lies in its
image.
:::

<1>5. The elements $b$ and $c$ from steps <1>2 and <1>4 are equal.

::: {.proof}
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

<1>6. The element $a$ is invertible.

::: {.proof}
By steps <1>2, <1>4, and <1>5, the single element
$$
b=c
$$
satisfies
$$
ab=ba=1.
$$
Thus it is the inverse of $a$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves the claim.
:::
:::
