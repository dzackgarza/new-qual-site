---
schema: qual/card@1
id: E-AMD-5QO44RPA
kind: problem
title: No simple group of order $p^2 q^2$ for primes $p<q$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that no group of order $p^2 q^2$ is simple for $p<q$ primes.
:::

::: {.solution}
Let $\abs G=p^2q^2$ with primes $p<q$, and let $n_q$ be the number of Sylow $q$-subgroups.

::: pf

::: {.pf-step #nq-values}
$n_q=1$ or $n_q=p^2$.

::: pf-proof
Sylow's theorems give $n_q\mid p^2$ and $n_q\equiv1\pmod q$. The value $n_q=p$ would give $q\mid p-1$, impossible since $0<p-1<q$.
:::

:::

::: pf-step
If $n_q=1$, then $G$ is not simple.

::: pf-proof
The unique Sylow $q$-subgroup is normal, nontrivial and proper.
:::

:::

::: {.pf-step #order-36}
If $n_q=p^2$, then $(p,q)=(2,3)$, $\abs G=36$ and $n_3=4$.

::: pf-proof
$p^2\equiv1\pmod q$ gives $q\mid(p-1)(p+1)$. Since $1\le p-1<q$, $q\nmid p-1$, so $q\mid p+1$. As $q>p$, this forces $q=p+1$, so $(p,q)=(2,3)$.
:::

:::

::: pf-step
If $n_q=p^2$, then $G$ is not simple.

::: pf-proof
By step [](#order-36){.pf-ref}, $G$ acts by conjugation on its four Sylow $3$-subgroups, giving a homomorphism $\varphi\colon G\to S_4$. The action is transitive on four points, so $\ker\varphi\ne G$, and $\abs G=36>24=\abs{S_4}$, so $\ker\varphi\ne1$. Thus $\ker\varphi$ is a proper nontrivial normal subgroup.
:::

:::

:::

:::
