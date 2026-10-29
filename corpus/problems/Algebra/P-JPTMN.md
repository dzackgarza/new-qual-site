---
schema: qual/card@1
id: P-JPTMN
kind: problem
title: The center of $S_n$ is trivial for $n \geq 3$
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
Prove that the center of the symmetric group $S_n$ is trivial for all $n \ge 3$:
$$Z(S_n) = \{e\} \quad \text{for all } n \ge 3.$$
:::

::: {.solution}

::: pf

::: pf-step

If $n\ge3$ and $\sigma\in S_n$ is not the identity, then $\sigma$ is not central.

::: pf-proof

Choose $i$ with $j=\sigma(i)\ne i$, choose $k\notin\{i,j\}$, which exists because $n\ge3$, and let $\tau=(j\ k)$. Since $\tau$ fixes $i$,
$$
(\sigma\tau)(i)=\sigma(i)=j,
\qquad
(\tau\sigma)(i)=\tau(j)=k\ne j.
$$
So $\sigma\tau\ne\tau\sigma$.

:::

:::

:::

:::
