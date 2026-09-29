---
schema: qual/card@1
id: E-AMD-564ETBH5
kind: problem
title: $a+\nilrad{R}$ nilpotent implies $a\in\nilrad{R}$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
  - Rings
relations: []
review: draft
---

::: {.exercise}
Let $R$ be a commutative ring and let $\operatorname{Nil}(R)$ denote its nilradical.
Show that if $a + \operatorname{Nil}(R)$ is nilpotent in the quotient ring $R/\operatorname{Nil}(R)$, then $a \in \operatorname{Nil}(R)$.
:::

::: {.solution}

::: pf

::: {.pf-step #a-power-in-nilradical}
There is $n\ge1$ with $a^n\in\operatorname{Nil}(R)$.

::: pf-proof
Multiplication of cosets gives $(a+\operatorname{Nil}(R))^n=a^n+\operatorname{Nil}(R)$ for every $n\ge1$.
Since $a+\operatorname{Nil}(R)$ is nilpotent, $a^n+\operatorname{Nil}(R)=\operatorname{Nil}(R)$ for some $n\ge1$, that is, $a^n\in\operatorname{Nil}(R)$.
:::

:::

::: {.pf-step #a-power-nm-zero}
$a^{nm}=0$ for some $m\ge1$.

::: pf-proof
By step [](#a-power-in-nilradical){.pf-ref}, $a^n$ is nilpotent, so $(a^n)^m=0$ for some $m\ge1$, and $a^{nm}=(a^n)^m$.
:::

:::

::: pf-qed
By step [](#a-power-nm-zero){.pf-ref}, $a$ is nilpotent, so $a\in\operatorname{Nil}(R)$.
Equivalently, $R/\operatorname{Nil}(R)$ has no nonzero nilpotent elements.
:::

:::

:::
