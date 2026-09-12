---
schema: qual/card@1
id: P-LJURM
kind: problem
title: A polynomial with Galois group $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
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
Give a polynomial with $S_3$ as its Galois group over $\mathbb{Q}$, and prove it.
:::

::: solution
Take
\[
f(x)=x^3-2.
\]
It is irreducible over $\mathbb Q$ by Eisenstein at $2$. Let $\alpha=\sqrt[3]{2}$ and let $\omega$ be a primitive cube root of unity. The roots are
\[
\alpha,\quad \alpha\omega,\quad \alpha\omega^2,
\]
so the splitting field is
\[
K=\mathbb Q(\alpha,\omega).
\]
Now
\[
[\mathbb Q(\alpha):\mathbb Q]=3,
\]
and $\mathbb Q(\alpha)\subset\mathbb R$ while $\omega\notin\mathbb R$, so
\[
[K:\mathbb Q(\alpha)]=2.
\]
Hence
\[
[K:\mathbb Q]=6.
\]
Since $K/\mathbb Q$ is the splitting field of a separable cubic, its Galois group embeds in $S_3$, and its order is $6$. Therefore
\[
\operatorname{Gal}(K/\mathbb Q)\cong S_3.
\]
:::
