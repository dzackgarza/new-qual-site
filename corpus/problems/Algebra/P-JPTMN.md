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

::: problem
Prove that the center of the symmetric group $S_n$ is trivial for all $n \ge 3$:
$$Z(S_n) = \{e\} \quad \text{for all } n \ge 3.$$
:::

::: solution
Let $\sigma\in Z(S_n)$ with $n\ge3$. Suppose $\sigma\ne1$. Then for some $i$,
\[
\sigma(i)=j\ne i.
\]
Choose $k$ distinct from both $i$ and $j$, and let $\tau=(jk)$. Since $\tau$ fixes $i$,
\[
(\sigma\tau)(i)=\sigma(i)=j,
\]
whereas
\[
(\tau\sigma)(i)=\tau(j)=k.
\]
Thus $\sigma\tau\ne\tau\sigma$, contradicting centrality. Therefore $\sigma=1$, so
\[
Z(S_n)=\{1\}
\]
for every $n\ge3$.
:::
