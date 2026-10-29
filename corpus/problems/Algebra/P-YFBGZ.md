---
schema: qual/card@1
id: P-YFBGZ
kind: problem
title: Radical ideals in $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Nilpotence
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Classify all **radical ideals** in the ring of integers $\ZZ$.
:::

::: {.solution}
Every ideal of $\ZZ$ is $(n)$ for a unique $n\ge0$.
For $n=p_1^{a_1}\cdots p_r^{a_r}\ge1$ with distinct primes $p_i$, write $\operatorname{rad}(n)=p_1\cdots p_r$, with $\operatorname{rad}(1)=1$.

::: pf

::: pf-step
$(0)$ is radical.

::: pf-proof
$\ZZ$ is a domain, so $x^m=0$ forces $x=0$.
:::

:::

::: {.pf-step #rad}
For $n\ge1$, $\sqrt{(n)}=(\operatorname{rad}(n))$.

::: pf-proof
If $x^m\in(n)$, then each $p_i$ divides $x^m$, hence divides $x$, so $\operatorname{rad}(n)\mid x$.
Conversely, if $\operatorname{rad}(n)\mid x$ and $N\ge\max_ia_i$, then $n\mid x^N$.
:::

:::

::: pf-step
The radical ideals of $\ZZ$ are $\boxed{(0)\text{ and }(n)\text{ for squarefree }n\ge1}$, that is, $(0)$, $\ZZ=(1)$, and $(p_1\cdots p_r)$ with the $p_i$ distinct primes.

::: pf-proof
By step [](#rad){.pf-ref}, for $n\ge1$ the ideal $(n)$ is radical exactly when $(n)=(\operatorname{rad}(n))$, that is, when $n=\operatorname{rad}(n)$, which means $n$ is squarefree.
:::

:::

:::

:::
