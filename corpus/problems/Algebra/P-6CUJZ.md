---
schema: qual/card@1
id: P-6CUJZ
kind: problem
title: $Z(A_n)=1$ for $n\geq 4$
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
Prove that the center of the alternating group $A_n$ is trivial for all $n \ge 4$:
$$Z(A_n) = \{e\} \quad \text{for all } n \ge 4.$$
:::

::: {.solution}
Let $n\ge4$ and $\sigma\in Z(A_n)$.

::: pf

::: {.pf-step #preserves-triples}
$\sigma$ maps every $3$-subset $\{i,j,k\}$ of $\{1,\ldots,n\}$ onto itself.

::: pf-proof
The $3$-cycle $(i\,j\,k)$ lies in $A_n$, so centrality gives $\sigma(i\,j\,k)\sigma^{-1}=(i\,j\,k)$. Conjugation applies $\sigma$ to the entries of a cycle, so $(\sigma(i)\,\sigma(j)\,\sigma(k))=(i\,j\,k)$, and the two cycles move the same set of points.
:::

:::

::: pf-step
$\sigma=e$, so $Z(A_n)=\{e\}$.

::: pf-proof
Fix $i$. By step [](#preserves-triples){.pf-ref}, $\sigma(i)$ lies in every $3$-subset that contains $i$. Since $n\ge4$, the intersection of these $3$-subsets is $\{i\}$, so $\sigma(i)=i$. This holds for every $i$.
:::

:::

:::

:::
