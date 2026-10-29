---
schema: qual/card@1
id: P-KTQL5
kind: problem
title: Centre of $S_n$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
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
What is the center $Z(S_n)$ of the symmetric group $S_n$? Prove it.
:::

::: {.solution}

::: pf

::: {.pf-step #small-n}
For $n=1,2$, $Z(S_n)=S_n$.

::: pf-proof
$S_1$ is trivial and $S_2$ has order $2$, so both are abelian.
:::

:::

::: {.pf-step #large-n}
For $n\ge3$, $Z(S_n)=\{1\}$.

::: pf-proof
Let $\sigma\in S_n$ be nontrivial. Choose $a$ with $b=\sigma(a)\ne a$, choose $c\notin\{a,b\}$, which exists since $n\ge3$, and let $\tau=(bc)$. Then $\sigma\tau(a)=\sigma(a)=b$ while $\tau\sigma(a)=\tau(b)=c$, so $\sigma\tau\ne\tau\sigma$ and $\sigma\notin Z(S_n)$.
:::

:::

::: pf-step
$$
Z(S_n)=\boxed{\begin{cases}S_n,&n=1,2,\\ \{1\},&n\ge3.\end{cases}}
$$

::: pf-proof
This combines steps [](#small-n){.pf-ref} and [](#large-n){.pf-ref}.
:::

:::

:::

:::
