---
schema: qual/card@1
id: E-JAPBK
kind: problem
title: Quotient by nilradical is reduced
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
Show $\nilrad{R} \normal R$ is an ideal and $A/\nilrad{R}$ is reduced.
:::

::: {.solution}
Let $R$ be a commutative ring with identity.

::: pf

::: {.pf-step #r-times-nilrad-subset-nilrad}
$R\,\nilrad{R}\subseteq\nilrad{R}$.

::: pf-proof
If $r^n=0$ and $x\in R$, then $(xr)^n=x^nr^n=0$.
:::

:::

::: {.pf-step #nilrad-plus-nilrad-subset-nilrad}
$\nilrad{R}+\nilrad{R}\subseteq\nilrad{R}$.

::: pf-proof
Let $r^n=s^m=0$ and $N=n+m-1$.
In $(r+s)^N=\sum_{k=0}^N\binom Nk r^ks^{N-k}$, each term has $k\ge n$ or $N-k\ge m$, so each term is $0$.
Together with $0\in\nilrad{R}$ and $-r\in\nilrad{R}$, steps [](#r-times-nilrad-subset-nilrad){.pf-ref} and [](#nilrad-plus-nilrad-subset-nilrad){.pf-ref} show that $\nilrad{R}$ is an ideal.
:::

:::

::: pf-step
$R/\nilrad{R}$ is reduced.

::: pf-proof
Let $\bar r=r+\nilrad{R}$ with $\bar r^n=0$.
Then $r^n\in\nilrad{R}$, so $(r^n)^m=0$ for some $m$, hence $r^{nm}=0$ and $r\in\nilrad{R}$, that is, $\bar r=0$.
:::

:::

:::

:::
