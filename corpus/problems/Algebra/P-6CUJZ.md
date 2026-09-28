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
Let $\sigma\in Z(A_n)$ with $n\ge4$. For every $3$-cycle $(i\,j\,k)\in A_n$, centrality gives
\[
\sigma(i\,j\,k)\sigma^{-1}=(i\,j\,k).
\]
But conjugation acts on a cycle by applying $\sigma$ to its entries, so
\[
(\sigma(i)\,\sigma(j)\,\sigma(k))=(i\,j\,k).
\]
In particular, $\sigma$ preserves the underlying set $\{i,j,k\}$ of every $3$-subset of $\{1,\dots,n\}$.

Fix $i$. The intersection of all $3$-subsets containing $i$ is exactly $\{i\}$ when $n\ge4$. Since $\sigma$ preserves each such $3$-subset, it preserves their intersection, so $\sigma(i)=i$. This holds for every $i$, hence $\sigma=e$.

Therefore
\[
Z(A_n)=\{e\}\qquad(n\ge4).
\]
:::
