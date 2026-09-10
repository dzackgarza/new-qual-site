---
schema: qual/card@1
id: P-ZUESF
kind: problem
title: $n_p=1$ when $n_p\mid q<p$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
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
Let $G$ be a finite group of order $|G| = p^k m$, where $p$ is a prime. Let $n_p$ denote the number of Sylow $p$-subgroups of $G$.
Suppose that $n_p$ divides an integer $q < p$.
Prove that $n_p = 1$, and consequently every Sylow $p$-subgroup is normal in $G$.
:::

::: {.solution}
By Sylow's theorem,
\[
n_p\equiv1\pmod p.
\]
The hypothesis $n_p\mid q$ with $0<q<p$ gives
\[
1\le n_p\le q<p.
\]
The only positive integer less than $p$ that is congruent to $1$ modulo $p$ is $1$. Hence
\[
\boxed{n_p=1}.
\]
Therefore the Sylow $p$-subgroup is unique, and hence normal in $G$.
:::
