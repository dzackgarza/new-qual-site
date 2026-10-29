---
schema: qual/card@1
id: E-AMD-4SSSVQJY
kind: problem
title: Every element of a finite ring is a unit or a zero-divisor
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Invertibility
relations: []
review: draft
---

::: {.exercise}
Show that every element of a finite ring is either a unit or a zero divisor.
:::

::: {.solution}
Let $R$ be a finite ring with $1$, and call $a\in R$ a zero divisor if $ab=0$ for some nonzero $b\in R$.

::: pf

::: {.pf-step #right-inverse}

If $a\in R$ is not a zero divisor, then $ax=1$ for some $x\in R$.

::: pf-proof

The map $\phi\colon R\to R$, $\phi(y)=ay$, is additive with kernel $\{y: ay=0\}=0$, so it is injective.
An injective map from a finite set to itself is surjective, so $1=\phi(x)=ax$ for some $x\in R$.

:::

:::

::: {.pf-step #unit}

If $ax=1$ in $R$, then $xa=1$, so $a$ is a unit.

::: pf-proof

If $xy=0$, then $y=(ax)y=a(xy)=0$, so left multiplication by $x$ is injective, hence surjective by finiteness of $R$.
Choose $z$ with $xz=1$.
Then $a=a(xz)=(ax)z=z$, so $xa=xz=1$.
Together with $ax=1$ this shows that $a$ is a unit with inverse $x$.

:::

:::

::: pf-qed

Every $a\in R$ is either a zero divisor or, by steps [](#right-inverse){.pf-ref} and [](#unit){.pf-ref}, a unit.

:::

:::

:::
