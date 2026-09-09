---
schema: qual/card@1
id: P-SUU6D
kind: problem
title: Number of elements of order $4$ in $\Aut(\ZZ/20)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Cyclic Groups
  - Number Theory
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
How many elements in the automorphism group $\operatorname{Aut}(\mathbb{Z}/20\mathbb{Z})$ have order 4?
:::

::: solution
Since $\mathbb Z/20\mathbb Z$ is cyclic,
\[
\operatorname{Aut}(\mathbb Z/20\mathbb Z)\cong(\mathbb Z/20\mathbb Z)^\times.
\]
By the Chinese remainder theorem,
\[
(\mathbb Z/20\mathbb Z)^\times
\cong(\mathbb Z/4\mathbb Z)^\times\times(\mathbb Z/5\mathbb Z)^\times
\cong C_2\times C_4.
\]
An element $(a,b)\in C_2\times C_4$ has order $4$ exactly when $b$ has order $4$. There are two choices for $a$ and two elements of order $4$ in $C_4$, hence
\[
2\cdot2=4
\]
such elements.

Explicitly, they correspond to
\[
3,7,13,17\pmod{20}.
\]
Therefore the answer is
\[
\boxed{4}.
\]
:::
