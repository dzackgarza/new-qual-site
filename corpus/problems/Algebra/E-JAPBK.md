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
audit:
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source wrote A/nilrad(R); the ring is R throughout, so the statement now reads R/nilrad(R).'
---

::: {.exercise}
Show $\nilrad{R} \normal R$ is an ideal and $R/\nilrad{R}$ is reduced.
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
:::

:::

::: pf-step
$\nilrad{R}$ is an ideal of $R$.

::: pf-proof
It contains $0$, and $-r=(-1)r\in\nilrad{R}$ for $r\in\nilrad{R}$ by step [](#r-times-nilrad-subset-nilrad){.pf-ref}. Steps [](#r-times-nilrad-subset-nilrad){.pf-ref} and [](#nilrad-plus-nilrad-subset-nilrad){.pf-ref} give closure under multiplication by $R$ and under addition.
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
